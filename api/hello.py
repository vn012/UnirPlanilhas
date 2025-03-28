import json

def handler(event, context):
    # Simulando dados para fins de exemplo
    dados = {
        "message": "Olá do Netlify!",
        "data": [1, 2, 3, 4, 5]
    }

    return {
        "statusCode": 200,
        "body": json.dumps(dados)
    }
