from .models import ConfiguracaoSite, Tecnologia, Projeto
from django.contrib import admin

# O uso de ModelAdmin personalizados é uma prática sênior para melhorar a UX do Admin.

@admin.register(ConfiguracaoSite)
class ConfiguracaoSiteAdmin(admin.ModelAdmin):
    """
    Gerenciamento do modelo Singleton ConfiguracaoSite.
    Garante que só haja uma linha de configuração global.
    """
    list_display = ('titulo_header',)
    # Garante que só haja um item na lista, simplificando a edição.
    def has_add_permission(self, request):
        return not ConfiguracaoSite.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False # Não permite exclusão, apenas edição.


@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    """
    Gerenciamento da Stack Técnica.
    """
    list_display = ('nome', 'classe_icone')
    search_fields = ('nome', 'classe_icone')
    list_filter = ('nome',)


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    """
    Gerenciamento dos projetos do portfólio.
    """
    list_display = ('titulo', 'url_github', 'ativo', 'data_criacao')
    list_filter = ('ativo', 'data_criacao') # Filtros laterais para eficiência
    search_fields = ('titulo', 'descricao')
    # Campos que podem ser editados diretamente na lista
    list_editable = ('ativo',) 
    # Define a ordem de exibição dos campos no formulário de edição
    fieldsets = (
        (None, {
            'fields': ('titulo', 'descricao', 'url_github', 'ativo')
        }),
        ('Informações de Auditoria', {
            # O campo data_criacao é apenas leitura
            'fields': ('data_criacao',),
            'classes': ('collapse',), # Oculta por padrão para manter o formulário limpo
        }),
    )
    readonly_fields = ('data_criacao',) # Garante que data_criacao não seja alterável
