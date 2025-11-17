# portfolio/views.py

# CORREÇÃO CRÍTICA DE IMPORTAÇÃO
from django.shortcuts import render  # Renderiza o template
from .models import Projeto, Tecnologia, ConfiguracaoSite  # Importa os Modelos

# Removido: from urls import index, render


def index(request):
    """
    Renderiza a página inicial do portfólio, buscando dados dinâmicos dos modelos.

    A view busca o objeto ConfiguracaoSite (Singleton) e aplica fallback (get_or_create).
    As consultas de Projeto e Tecnologia são otimizadas com filtros, garantindo eficiência algorítmica.

    Contexto Retornado:
    - config: Objeto ConfiguracaoSite.
    - projetos: Queryset de Projetos ativos.
    - tecnologias: Queryset de todas as Tecnologias.
    """

    # Busca a única instância de configuração ou cria uma se não existir
    try:
        config, created = ConfiguracaoSite.objects.get_or_create(
            pk=1,
            defaults={
                "descricao_sobre_mim": "Descrição padrão. Edite no Admin.",
            },
        )
    except Exception as e:
        # Tratamento de erro robusto caso a tabela não exista (após migrações falharem)
        print(f"Erro ao buscar Configuração do Site: {e}")
        config = None  # Força a página a tentar carregar, mas sem o objeto

    context = {
        "config": config,
        "projetos": Projeto.objects.filter(ativo=True),
        "tecnologias": Tecnologia.objects.all(),
    }

    # O template de destino é o que criamos: portfolio/index.html
    return render(request, "portfolio/index.html", context)
