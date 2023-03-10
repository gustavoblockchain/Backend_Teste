import boto3
import csv
import os
import psycopg2
from datetime import datetime

# Set up the S3 client
s3 = boto3.client('s3')

# Define the function to handle the Lambda event
def lambda_handler(event, context):
    
    # Get the bucket name and object key from the event data
    bucket_name = event['bucket_name']
    object_key = event['object_key']
    
    # Set up the database connection
    db_host = os.environ['DB_HOST']
    db_port = os.environ['DB_PORT']
    db_name = os.environ['DB_NAME']
    db_user = os.environ['DB_USER']
    db_password = os.environ['DB_PASSWORD']
    table_name = os.environ['TABLE_NAME']
    
    conn = psycopg2.connect(
        host=db_host,
        port=db_port,
        dbname=db_name,
        user=db_user,
        password=db_password
    )
    cursor = conn.cursor()
    
    # Download the CSV file from S3
    response = s3.get_object(Bucket=bucket_name, Key=object_key)
    csv_data = response['Body'].read().decode('utf-8').splitlines()
    
    # Parse the CSV data
    csv_reader = csv.reader(csv_data, delimiter=',')
    headers = next(csv_reader)
    
    for row in csv_reader:
        # Convert dates to the correct format
        for i in range(len(row)):
            if headers[i].lower().startswith('date'):
                row[i] = datetime.strptime(row[i], '%d/%m/%Y').strftime('%Y-%m-%d')
        # Remove mask from CPF and CNPJ columns
        if 'cpf' in headers:
            cpf_index = headers.index('cpf')
            row[cpf_index] = row[cpf_index].replace('.', '').replace('-', '')
        if 'cnpj' in headers:
            cnpj_index = headers.index('cnpj')
            row[cnpj_index] = row[cnpj_index].replace('.', '').replace('/', '').replace('-', '')
            
        # Insert the row into the database
        insert_query = f"INSERT INTO {table_name} ({', '.join(headers)}) VALUES ({', '.join(['%s'] * len(headers))})"
        cursor.execute(insert_query, row)
        
    # Commit the changes and close the connection
    conn.commit()
    cursor.close()
    conn.close()
    
    # Return an HTTP response with a success status
    return {
        'statusCode': 200,
        'body': 'Dados processados e salvos'
    }
