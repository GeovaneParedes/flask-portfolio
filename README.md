# Flask Portfolio — scaffold


Landing page pessoal simples construída com Flask (>=3.0), Jinja2 e TailwindCSS (via CDN).


## Requisitos


- Python 3.11+
- pip


## Instalação


1. Crie e ative um venv:


```bash
python -m venv .venv
source .venv/bin/activate # macOS / Linux
.venv\Scripts\activate # Windows (PowerShell)

```

Instale dependências:

pip install -r requirements.txt

Crie um arquivo .env (opcional) a partir de .env.example e ajuste valores:

cp .env.example .env

Rodar localmente (modo Flask CLI):

export FLASK_APP=app
export FLASK_ENV=development
flask --app app run --reload

No Windows (PowerShell):

$env:FLASK_APP = "app"
$env:FLASK_ENV = "development"
flask --app app run --reload
Testes
pytest -q
Observações de segurança e próximos passos

Troque SECRET_KEY por um valor seguro antes de publicar.

Se desejar compilar Tailwind localmente (sem CDN), adicionar build step com npx tailwindcss.

Para deploy em produção, recomenda-se usar um WSGI server (gunicorn/uvicorn) por trás de um reverse-proxy.



---


## Notas finais


- Siga as diretivas do DevOps Examiner: código modular, testes básicos inclusos, e docstrings em português para interfaces públicas.
- Caso queira, posso também gerar um `Dockerfile` mínimo e um workflow GitHub Actions para rodar os testes em CI.


<!-- End of scaffold -->

Pronto — criei o scaffold completo no canvas chamado Flask-portfolio - Scaffold.
