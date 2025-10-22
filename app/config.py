import os
from dataclasses import dataclass


@dataclass
class Config:
    """Configuração da aplicação.


    Valores lidos de variáveis de ambiente com fallback seguro para execução local.
    """

    SECRET_KEY: str = os.getenv("SECRET_KEY", "dev-not-secure-change-me")
    FLASK_ENV: str = os.getenv("FLASK_ENV", "development")
    NAME: str = os.getenv("NAME", "@DevGege")
    GITHUB_URL: str = os.getenv("GITHUB_URL", "https://github.com/GeovaneParedes")

