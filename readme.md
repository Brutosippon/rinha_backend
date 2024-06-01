# Rinha de Backend

# Python  +  Postgres  + Flask

## Endpoints

- `POST /pessoas` - Cria uma nova pessoa.
- `GET /pessoas/:id` - Retorna os detalhes de uma pessoa pelo ID.
- `GET /pessoas?t=termo` - Busca pessoas pelo termo.
- `GET /contagem-pessoas` - Retorna a contagem de pessoas cadastradas.

## Como Executar

1. Clone o repositório:
    ```
    git clone https://github.com/zanfranceschi/rinha-de-backend-2023-q3.git
    cd rinha-de-backend-2023-q3
    ```
2. Configure o arquivo `.env` com as variáveis de ambiente necessárias.
3. Execute:
    ```
    docker-compose up --build
    ```

## Testes de Stress

Os testes de stress podem ser executados usando Gatling. Configure o Gatling para enviar requisições aos endpoints da API através do Nginx.

### Configuração do Nginx

O arquivo `nginx.conf` é utilizado para balancear a carga entre duas instâncias da API.

### Docker Compose

O arquivo `docker-compose.yml` define os serviços da aplicação, incluindo limites de CPU e memória.


## Como Executar os Testes

### Preparação: 

pip freeze > requirements.txt

docker-compose down -v
docker-compose down
docker-compose build
docker-compose up -d
docker-compose logs

docker-compose exec api1 flask db init
docker-compose exec api1 flask db migrate -m "Initial migration"
docker-compose exec api1 flask db upgrade

teste0:
curl -X POST http://localhost:9999/pessoas \
-H "Content-Type: application/json" \
-d '{
    "apelido": "josé",
    "nome": "José Roberto",
    "nascimento": "2000-10-01",
    "stack": ["C#", "Node", "Oracle"]
}'

{"id":"012ccb0c-d10d-424f-9e39-d79c7c1c9ce6"}




#### Passo 1: Instalar Gatling 
Clone o repositório de testes do GitHub para sua máquina local:
git clone https://github.com/zanfranceschi/rinha-de-backend-2023-q3.git

Navegue até o diretório de testes dentro do repositório clonado:
cd rinha-de-backend-2023-q3/teste/gatling

Execute o script de instalação:
./install-gatling

#### Passo 2: Gerar Dados de Teste
Escolha uma das opções abaixo:

1-Usando Faker como Gerador:
npm install # Instale as dependências necessárias
cd ~/Downloads/rinha-de-backend-2023-q3-main/teste/gatling/geradores/faker
./gerar-pessoas > ../../user-files/resources/pessoas-payloads.tsv
./gerar-termos-busca > ../../user-files/resources/termos-busca.tsv

2-Usando o Gerador Personalizado (Strings Aleatórias):
cd ~/Downloads/rinha-de-backend-2023-q3-main/teste/gatling/geradores/customizado
./gerar-pessoas > ../../user-files/resources/pessoas-payloads.tsv
./gerar-termos-busca > ../../user-files/resources/termos-busca.tsv

#### Passo 3: Executar o Teste do Gatling
Navegue até o diretório do Gatling:
Execute o teste do Gatling:

cd ~/Downloads/rinha-de-backend-2023-q3-main/teste/gatling/
./run-test

Este script irá executar os cenários de teste do Gatling usando os dados gerados.