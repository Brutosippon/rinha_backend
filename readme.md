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

### Passo 0: Preparação

Clone o repositório de testes do GitHub para sua máquina local:
```
git clone https://github.com/zanfranceschi/rinha-de-backend-2023-q3.git

Navegue até o diretório de testes dentro do repositório clonado:
cd rinha-de-backend-2023-q3/teste/gatling

Passo 1: Instalar Gatling (Opcional)

Se você ainda não instalou o Gatling, execute o script de instalação:
./install-gatling

Este script irá baixar e configurar o Gatling no seu sistema.
Passo 2: Gerar Dados de Teste
Agora, você precisa gerar dados de teste usando o Faker ou o gerador personalizado. Escolha uma das opções abaixo:
Usando Faker como Gerador:

npm install # Instale as dependências necessárias

cd geradores/faker
./gerar-pessoas > ../../user-files/resources/pessoas-payloads.tsv
./gerar-termos-busca > ../../user-files/resources/termos-busca.tsv

Usando o Gerador Personalizado (Strings Aleatórias):
cd geradores/customizado
./gerar-pessoas > ../../user-files/resources/pessoas-payloads.tsv
./gerar-termos-busca > ../../user-files/resources/termos-busca.tsv

Passo 3: Executar o Teste do Gatling

Navegue até o diretório do Gatling:
Execute o teste do Gatling:

cd ~/Downloads/rinha-de-backend-2023-q3-main/teste/gatling
./run-test



Este script irá executar os cenários de teste do Gatling usando os dados gerados.