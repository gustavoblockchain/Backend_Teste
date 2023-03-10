# Função S3 CSV para banco de dados Lambda

Essa função do AWS Lambda baixa um arquivo CSV de um bucket S3, processa os dados e os salva em um banco de dados PostgreSQL.

## Pré-requisitos

- Conta da AWS
- AWS CLI instalado e configurado
- Python 3.8 ou superior instalado
- Banco de dados PostgreSQL (pode ser hospedado no AWS RDS ou em outro lugar)
- An S3 bucket with a CSV file to process
- Boto3
- CSV
- OS
- Psycopg2

## Instalação

1. Clone o repositório:
   ``` javascript
   git clone https://github.com/gustavoblockchain/Backend_Teste 
   

  2. Execute o comando pip install requeriments.txt para realizar o download das biblitecas:
  ``` javascript
   pip install requeriments.txt
  ```
## Configuração  
  - O código usa uma função lambda do AWS, portanto, é projetado para ser executado como um serviço em nuvem.

 - Para usá-lo, é necessário ter uma conta na AWS e configurar o serviço Lambda e o banco de dados PostgreSQL.

 -  Abaixo estão as etapas gerais para configurar e executar o código:

 -   Crie uma nova função Lambda no console da AWS e configure-a com o código acima.

 -   Adicione as variáveis de ambiente necessárias para a conexão com o banco de dados (DB_HOST, DB_PORT, DB_NAME, DB_USER e DB_PASSWORD) e o nome da tabela a ser preenchida (TABLE_NAME).

  -  Configure uma nova política de segurança para conceder acesso ao serviço Lambda ao bucket S3 que contém o arquivo CSV.

   - Crie um evento que acione a função Lambda quando um arquivo CSV for adicionado ao bucket S3.

  -  Faça o upload do arquivo CSV para o bucket S3 configurado.

  -  Execute a função Lambda e verifique se os dados foram inseridos corretamente no banco de dados PostgreSQL.


