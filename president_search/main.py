from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import datetime
from typing import List, Dict

app = FastAPI()

# Adicionando middleware para permitir CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

CSV_FILE_PATH = "/Users/berlanda/Downloads/intuitiveCare/data_base/Relatorio_cadop.csv"

def filter_data() -> List[Dict]:
    try:
        # Tente ler o CSV e processar os dados
        df = pd.read_csv(CSV_FILE_PATH, delimiter=';', dtype=str)
        
        # Verifica se a coluna 'Data_Registro_ANS' existe
        if 'Data_Registro_ANS' not in df.columns:
            raise ValueError("A coluna 'Data_Registro_ANS' não foi encontrada no CSV")
        
        df['Data_Registro_ANS'] = pd.to_datetime(df['Data_Registro_ANS'], errors='coerce')
        
        # Filtrar registros com 'PRESIDENTE' na coluna 'Cargo_Representante'
        df_filtered = df[df['Cargo_Representante'].str.contains("PRESIDENTE", case=False, na=False)]
        
        # Filtrar registros com mais de 10 anos de registro na ANS
        ten_years_ago = datetime.datetime.now() - datetime.timedelta(days=365*10)
        df_filtered = df_filtered[df_filtered['Data_Registro_ANS'] <= ten_years_ago]
        
        # Substituindo NaN por None
        df_filtered = df_filtered.where(pd.notna(df_filtered), None)
        
        # Retornar os dados como dicionário
        return df_filtered.to_dict(orient='records')
    except Exception as e:
        # Retorne o erro específico para ajudar no diagnóstico
        return {"error": str(e)}

@app.get("/buscar_presidente")
def get_presidentes():
    return filter_data()
