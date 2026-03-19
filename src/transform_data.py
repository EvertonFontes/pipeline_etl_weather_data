import pandas as pd
import json
from pathlib import Path

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

path_name = Path(__file__).parent.parent / 'data' / 'weather_data.json'


def create_dataframe(path_name:str) -> pd.DataFrame:
    logging.info("Criando DataFrame do arquivo JSON..")
    path = path_name

    if not path:
        raise FileNotFoundError(f"Arquivo não encontrado no caminho: {path}")

    with open(path) as f:
        data = json.load(f)
    
    df = pd.json_normalize(path)
    logging.info(f"\n DataFrame criado com {len(df)} linha(s)")
    return df


def normalize_weather_columns(df: pd.DataFrame) -> pd.DataFrame:
    print()