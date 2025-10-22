# wsgi.py
from app import create_app

# A variável 'app' é o ponto de entrada para o Gunicorn/servidor WSGI
app = create_app()

if __name__ == "__main__":
    # Usado apenas para rodar localmente
    # Em produção, o Gunicorn assume
    app.run(debug=True)
