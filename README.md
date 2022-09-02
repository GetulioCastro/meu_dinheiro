# Projeto Meu Dinheiro

<p>Repositório criado para guardar as configurações iniciais de um projeto Python e Django, para pesquisas frequentes.</p>

# Configurações iniciais de um Projeto Django

Criar o diretório do projeto - mkdir <nome do diretório>

Entrar neste diretório - cd <nome do diretório>

<p>Criar um ambiente virtual dentro deste diretório com o comando:</p>
python -m venv .venv (windows)<br>
python3 .m venv .venv (linux)

<p>Ativar o ambiente virtual com o comando:</p>
.venv/Scripts/activate (windows)<br>
source .venv/bin/activate (linux)

Usar o gerenciador de pacotes do Python: PIP
- pip install django

Crie o projeto no Django com o comando:
- django-admin startproject meudinheiro

<p>Crie um diretório "apps" e, ao entrar nesta app, rodar o comando:</p>
python3 ../manage.py startapp geral

Retornar à raiz do projeto e fazer estas duas instalações:
- pip install python-decouple
- pip install psycopg2-binary

## Agora é começar a programar!