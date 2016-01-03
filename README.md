# SIMPLEMOOC

[![Code Climate](https://codeclimate.com/repos/56889acfc0992f10b1006986/badges/70bbfee7043f1b36483a/gpa.svg)](https://codeclimate.com/repos/56889acfc0992f10b1006986/feed)
[![Build Status](https://travis-ci.org/CharlesHiroshi/simplemooc.svg?branch=master)](https://travis-ci.org/CharlesHiroshi/simplemooc)


Sistema de Cursos MOOC


## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5.
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env.
6. Execute os testes.

```console
git clone git@github.com:CharlesHiroshi/simplemooc.git pnwcd
cd pnwcd
python -m venv .pnwcd
source .pnwcd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```


## Como fazer o Deploy?

1. Crie uma instância no Heroku.
2. Envie as configurações para o Heroku.
3. Defina uma SECRET_KEY segura para a instância.
4. Defina o DEBUG=False.
5. Configure o serviço de e-mail.
6. Envie o código para o Heroku.

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py
heroku config:set DEBUG=False
# configuro o e-mail
git push heroku master --force
```
