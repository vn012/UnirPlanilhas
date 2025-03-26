comando para rodar a o projeto numa maquina virtual e instlaar as dependências:
Ambiente
python -m venv venv
venv\Scripts\activate

dependencias
pip install pandas thefuzz openpyxl   

automatizar dependências
pip freeze > requirements.txt (criar)
pip install -r requirements.txt (utilizar quando já criado)

