import requests

def obter_sas_token():
    # 1. Substitua pela URL de Produção ou Certificação fornecida após o login
    # Exemplo comum da B3: "https://api.cert.b3.com.br/api/cip/v1"
    base_url = "https://COLE_A_URL_AQUI/api/cip/v1"
    endpoint = f"{base_url}/sas-tokens"
    
    # 2. Substitua pela sua credencial gerada no portal "Meus Apps" da B3
    meu_token = "COLE_SUA_CHAVE_OU_TOKEN_AQUI"

    # Cabeçalhos da requisição
    headers = {
        "Accept": "application/json",
        
        # O formato abaixo é o mais comum para APIs modernas (Bearer Token).
        # Verifique na documentação logada se a B3 exige "Authorization", "client_id" ou "x-api-key"
        "Authorization": f"Bearer {meu_token}"
    }

    try:
        print(f"Tentando conectar em: {endpoint}...")
        response = requests.get(endpoint, headers=headers)
        
        # Levanta exceção se o status não for 200 (ex: 401 Unauthorized ou 404 Not Found)
        response.raise_for_status()
        
        # Extrai os dados do JSON
        resposta_json = response.json()
        sas_token = resposta_json.get("data", {}).get("sasToken")
        versao_api = response.headers.get("x-v", "Versão não informada")
        
        print("\n--- Sucesso! ---")
        print(f"Versão da API: {versao_api}")
        print(f"SAS Token (URI): {sas_token}")
        
        return sas_token

    except requests.exceptions.HTTPError as http_err:
        print(f"\nFalha na requisição. Código HTTP: {response.status_code}")
        # Imprimir o response.text ajuda a ler a mensagem de erro que a B3 retorna (ex: "Token expirado")
        print(f"Mensagem do servidor: {response.text}")
    except requests.exceptions.ConnectionError:
        print("\nErro de conexão: Não foi possível acessar o servidor. Verifique se a URL base está correta.")
    except Exception as err:
        print(f"\nOcorreu um erro inesperado: {err}")

# Executa a função principal
if __name__ == "__main__":
    token = obter_sas_token()