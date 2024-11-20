import streamlit as st
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_latest_numbers():
    url = "http://rodrigodevapi.duckdns.org:1030/immersive-roulette"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        body_text = soup.body.get_text()
        if "results:" in body_text:
            results_str = body_text.split("results:")[1].strip()
            results = eval(results_str)
            return results
        else:
            return []
    except Exception as e:
        st.error(f"Erro ao acessar a URL: {e}")
        return []

st.title("Monitor de Resultados da Roleta")
st.write("Rastreamento dos números mais recentes da roleta.")

numbers = fetch_latest_numbers()
if numbers:
    latest_number = numbers[0]
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    st.write(f"Número mais recente: **{latest_number}** às {timestamp}")
else:
    st.write("Nenhum número encontrado no momento.")
