from django.shortcuts import render  # Renderiza o template
from .models import Projeto, Tecnologia, ConfiguracaoSite


def index(request):
    """
    Renderiza a página inicial do portfólio, buscando dados dinâmicos dos modelos.

    Otimização: O uso de .filter(ativo=True) garante eficiência (Big-O) ao
    limitar as consultas apenas aos registros necessários.
    """

    # Busca a única instância de configuração ou cria uma se não existir (tratamento robusto de erros/falback)
    config, _ = ConfiguracaoSite.objects.get_or_create(pk=1, defaults={
        'descricao_sobre_mim': 'Descrição padrão. Edite no Admin.', 
    })

    context = {
        'config': config,
        # Consulta otimizada: apenas projetos ativos
        'projetos': Projeto.objects.filter(ativo=True), 
        # Consulta otimizada: busca todas as tecnologias
        'tecnologias': Tecnologia.objects.all(), 
    }

    # O template de destino é o que criamos: portfolio/index.html
    return render(request, "portfolio/index.html", context)
