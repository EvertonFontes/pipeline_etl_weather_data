# ETL Pipeline de Dados Meteorológicos

## Descrição

Este projeto implementa um pipeline ETL (Extract, Transform, Load) completo para coleta, processamento e armazenamento de dados meteorológicos de São Paulo. Utilizando Apache Airflow para orquestração, o pipeline extrai dados em tempo real da API OpenWeatherMap, aplica transformações de limpeza e normalização, e persiste os dados em um banco de dados PostgreSQL. Todo o ambiente é containerizado com Docker para facilitar a implantação e execução.

## Funcionalidades

- **Extração**: Coleta dados meteorológicos atuais de São Paulo via API OpenWeatherMap
- **Transformação**: Limpeza, normalização e estruturação dos dados usando Pandas
- **Carga**: Persistência dos dados transformados no PostgreSQL
- **Orquestração**: Agendamento automático com Apache Airflow (execução a cada hora)
- **Containerização**: Ambiente completo com Docker Compose
- **Análise**: Notebook Jupyter para exploração e análise dos dados coletados

## Tecnologias Utilizadas

- **Apache Airflow**: Orquestração e agendamento do pipeline
- **Python**: Linguagem principal para desenvolvimento
- **Pandas**: Manipulação e transformação de dados
- **PostgreSQL**: Banco de dados para armazenamento
- **Docker & Docker Compose**: Containerização e gerenciamento de serviços
- **Redis**: Broker para execução distribuída do Airflow
- **Jupyter Notebook**: Análise exploratória de dados

## Pré-requisitos

- Docker e Docker Compose instalados
- Chave da API OpenWeatherMap (gratuita)

## Instalação e Configuração

1. **Clone o repositório**:
   ```bash
   git clone <url-do-repositorio>
   cd etl-data-weather
   ```

2. **Configure as variáveis de ambiente**:
   - Copie o arquivo `.env.example` para `.env` (se existir) ou crie um arquivo `.env` na pasta `config/`
   - Adicione sua chave da API OpenWeatherMap:
     ```
     API_KEY=sua_chave_aqui
     ```

3. **Inicie os serviços**:
   ```bash
   docker-compose up -d
   ```

4. **Acesse o Airflow**:
   - Abra o navegador em `http://localhost:8080`
   - Usuário: `airflow`
   - Senha: `airflow`

## Uso

### Executando o Pipeline

1. No painel do Airflow, ative o DAG `weather_pipeline`
2. Execute manualmente ou aguarde o agendamento automático (a cada hora)

### Estrutura dos Dados

Os dados coletados incluem:
- Temperatura atual, mínima e máxima
- Umidade e pressão atmosférica
- Velocidade e direção do vento
- Visibilidade e cobertura de nuvens
- Horários de nascer e pôr do sol
- Coordenadas geográficas

### Análise de Dados

Para explorar os dados coletados:
1. Execute o notebook `notebooks/analisys_data.ipynb`
2. Conecte-se ao banco de dados PostgreSQL usando as credenciais do Docker Compose

## Estrutura do Projeto

```
etl-data-weather/
├── dags/                    # DAGs do Airflow
│   └── weather_dag.py
├── src/                     # Código fonte do ETL
│   ├── extract_data.py      # Extração de dados
│   ├── transform_data.py    # Transformações
│   └── load_data_weather.py # Carga no banco
├── data/                    # Dados coletados
├── config/                  # Configurações
│   └── airflow.cfg
├── notebooks/               # Análises
│   └── analisys_data.ipynb
├── logs/                    # Logs do Airflow
├── plugins/                 # Plugins customizados
├── postgres-data/           # Dados do PostgreSQL
├── docker-compose.yml       # Configuração Docker
├── pyproject.toml           # Dependências Python
└── README.md
```

## Desenvolvimento

Para desenvolvimento local:

1. Instale as dependências:
   ```bash
   pip install -e .
   ```

2. Configure um ambiente virtual Python

3. Execute os testes 

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir melhorias
- Enviar pull requests

## Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.