import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from pathlib import Path

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

env_path = Path(__file__).resolve().parent.parent / 'config' / '.env'
load_dotenv(env_path)


def load_data(table_name: str, df):
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    db = os.getenv("POSTGRES_DB")
    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT")

    logging.info(f"→ Conectando em {host}:{port}/{db}")

    engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}")

    df.to_sql(table_name, engine, if_exists="append", index=False)

    logging.info(f"Dados carregados com sucesso!") 
    
    df_check = pd.read_sql(f'SELECT * FROM {table_name}', con=engine)
    logging.info(f"Total de registros na tabela: {len(df_check)}")