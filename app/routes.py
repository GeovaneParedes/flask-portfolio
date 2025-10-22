from flask import Blueprint, current_app, render_template


bp = Blueprint("main", __name__)


@bp.get("/")
def index():
    """Rota principal — renderiza a landing page com dados configuráveis.


    Usa variáveis de ambiente (via current_app.config) para personalizar o conteúdo.
    """
    return render_template(
        "index.html",
        name=current_app.config.get("NAME"),
        github_url=current_app.config.get("GITHUB_URL"),
    )
