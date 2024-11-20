import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

def fetch_latest_numbers():
    # URL da página
    url = "http://rodrigodevapi.duckdns.org:1030/immersive-roulette"
    
    try:
        # Fazendo a requisição para a URL
        response = requests.get(url)
        response.raise_for_status()  # Levanta exceção para status code >= 400

        # Parseando o HTML com BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Procurando pelo campo "results"
        body_text = soup.body.get_text()
        if "results:" in body_text:
            # Extraindo os números após "results:"
            results_str = body_text.split("results:")[1].strip()
            results = eval(results_str)  # Converte a string para lista
            return results
        else:
            print("Campo 'results' não encontrado.")
            return None
    except Exception as e:
        print(f"Erro ao acessar a URL: {e}")
        return None

def track_numbers():
    seen_numbers = set()  # Para evitar duplicados
    print("Iniciando o rastreamento...")

    while True:
        numbers = fetch_latest_numbers()
        if numbers:
            # O número mais recente está no início da lista
            latest_number = numbers[0]

            if latest_number not in seen_numbers:
                seen_numbers.add(latest_number)
                # Obtendo a hora atual
                current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                # Salvando no arquivo e exibindo no console
                with open("roleta_registro.txt", "a") as file:
                    file.write(f"{latest_number}, {current_time}\n")
                print(f"Número: {latest_number} | Hora: {current_time}")
        
        # Aguarda 5 segundos antes de verificar novamente
        time.sleep(5)

if __name__ == "__main__":
    track_numbers()
