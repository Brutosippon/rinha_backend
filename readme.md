# Rinha de Backend

## Endpoints

- `POST /pessoas` - Cria uma nova pessoa.
- `GET /pessoas/:id` - Retorna os detalhes de uma pessoa pelo ID.
- `GET /pessoas?t=termo` - Busca pessoas pelo termo.
- `GET /contagem-pessoas` - Retorna a contagem de pessoas cadastradas.

## Como Executar

1. Clone o repositório.
2. Configure o arquivo `.env` com as variáveis de ambiente necessárias.
3. Execute `docker-compose up --build`.

## Testes de Stress

Os testes de stress podem ser executados usando Gatling. Configure o Gatling para enviar requisições aos endpoints da API através do Nginx.

## Configuração do Nginx

O arquivo `nginx.conf` é utilizado para balancear a carga entre duas instâncias da API.

## Docker Compose

O arquivo `docker-compose.yml` define os serviços da aplicação, incluindo limites de CPU e memória.
