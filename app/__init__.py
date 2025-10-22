"""Inicialização do pacote app.


Documentação em português apenas para a interface pública: a função create_app produz a
aplicação Flask configurada e pronta para uso em desenvolvimento local.
"""
from flask import Flask
from .config import Config
from dotenv import load_dotenv



def create_app(test_config: dict | None = None) -> Flask:
    """Cria e configura a aplicação Flask.



    Args:
    test_config: dicionário de configuração usado em testes.


    Returns:
    app configurada (Flask).
    """
    load_dotenv()
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config.from_object(Config)



    if test_config:

        app.config.update(test_config)


# Segurança básica: cabeçalhos mínimos
    @app.after_request
    def set_security_headers(response):
        response.headers.setdefault("X-Content-Type-Options", "nosniff")
        response.headers.setdefault("X-Frame-Options", "DENY")
        response.headers.setdefault("Referrer-Policy", "no-referrer")
        return response


    # rotas
    from . import routes

    app.register_blueprint(routes.bp)
    
    return app