# PCS3518/3818 - Projeto: Conta de energia "justa"
Este é o repositório do backend do projeto da disciplina de Aplicações e Tecnologias em Automação. Trabalho desenvolvido pelos alunos:
- Fábio Fusimoto Pires N°USP 9853294
- Gabriel Roberti Passini N°USP 9868071
- Gustavo Ziyu Wang NºUSP 8988790

Este projeto visa criar um dashboard de controle para divisão de contas de energia elétrica em ambientes coabitados.

## Principais tecnologias adotadas
- [Python 3.6.9](https://www.python.org/about/)
- [Django 3.0.5](https://www.djangoproject.com/)
- [PostgreSQL 10.12](https://www.postgresql.org/)
- [Django-RQ](https://github.com/rq/django-rq)

## Instalação
Os comandos de instalação foram testados no Ubuntu 18.04 e podem ser ligeiramente diferentes no Windows.
- Instale a versão mais recente do [Python 3.6](https://www.python.org/downloads/)
- Baixe e instale o [Postgres 10](https://www.postgresql.org/download/)
- Baixe e instale o [Redis](https://redis.io/topics/quickstart)
- Faça o setup do banco de dados e usuário do PostgreSQL (comando válidos para Linux)<br/>
`$ sudo su - postgres`<br/>
`$ psql`<br/>
`postgres=# CREATE DATABASE conta_justa;`<br/>
`postgres=# \q`<br/>
`$ createuser --interactive --pwprompt`<br/>
`Enter name of role to add: conta_justa`<br/>
`Enter password for new role: conta_justa`<br/>
`Enter it again: conta_justa`<br/>
`Shall the new role be a superuser? (y/n) y`<br/>
`$ psql`<br/>
`postgres=# GRANT ALL PRIVILEGES ON DATABASE conta_justa TO conta_justa;`<br/>
- Crie um ambiente virtual e ative-o (os comandos no WIndows são diferentes. Consulte [aqui](https://docs.python.org/3/library/venv.html))<br/>
`$ virtualenv -p /usr/bin/python3 virtualenvironment && cd virtualenvironment`<br/>
 `$ source ./bin/activate`<br/>
- Clone o repositório<br/>
`$ git clone git@github.com:FabioFusimoto/conta_justa.git && cd conta_justa`<br/>
- Instale as dependências<br/>
`$ pip3 install -r requirements.txt  #Linux`  ou `$ pip install -r requirements.txt #Windows`<br/>
- Execute as migrações do banco de dados<br/>
`python3 manage.py migrate`<br/>
- Inicie o Redis broker<br/>
`redis-server`
- Inicie o RQ-Worker<br/>
`python3 manage.py rqworker default`
- Inicie o servidor (roda em [localhost:3030](localhost:3030))<br/>
`python3 manage.py runserver 3030`<br/>

## Organização de diretórios
Os diretórios estão dispostos para seguir a arquitetura hexagonal modificada proposta no [vídeo de detalhamento do projeto](https://www.youtube.com/watch?v=7ZmzBEF5uiQ&list=UUH9esjC9hxJvEErKOnuPiXQ). Algumas exceções à disposição da arquitetura existem para atender às restrições de diretório impostas pelo Django. As pastas relevantes estão descritas abaixo

>├── conta_justa/ ------>  Setup do Django<br/>
>├── server/  &nbsp;----------> O backend em si<br/>
> &nbsp; &nbsp; &nbsp; ├── application/ &nbsp;&nbsp;--> Casos de uso<br/>
> &nbsp; &nbsp; &nbsp; ├── connectors/ &nbsp;--> Conexão com o banco de dados/filas do Redis<br/>
> &nbsp; &nbsp; &nbsp; ├── domain/ ------> Regras de negócio e funções de propósito geral<br/>
> &nbsp; &nbsp; &nbsp; ├── tests/ --------> Testes de funcionamento pontuais e ponta-a-ponta<br/>
> &nbsp; &nbsp; &nbsp; ├── models.py ----> Descrição das entidades do banco de dados<br/>
