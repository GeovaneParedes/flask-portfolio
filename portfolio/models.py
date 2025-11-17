from django.db import models
from django.utils.text import slugify

class ConfiguracaoSite(models.Model):
    """
    Modelo Singleton para armazenar textos estáticos e variáveis globais do site.
    Isso evita 'hardcoding' de conteúdo em templates e views, facilitando a manutenção (Clean Code).
    """
    titulo_header = models.CharField(
        max_length=100,
        default="DevGege - Desenvolvedor Python",
        help_text="Texto principal exibido na animação de digitação."
    )
    descricao_sobre_mim = models.TextField(
        help_text="O parágrafo principal da seção 'Sobre Mim'."
    )
    
    class Meta:
        verbose_name = "Configuração do Site"
        verbose_name_plural = "Configuração do Site"
    
    # Garantia de que haverá apenas uma instância deste modelo (Singleton)
    def save(self, *args, **kwargs):
        if not self.pk and ConfiguracaoSite.objects.exists():
            # Tratamento robusto de erros: previne múltiplos objetos
            raise Exception('Só pode haver uma instância de ConfiguracaoSite.')
        return super(ConfiguracaoSite, self).save(*args, **kwargs)

    def __str__(self):
        return "Configurações Globais"

class Tecnologia(models.Model):
    """
    Modelo para gerenciar as tecnologias exibidas na Stack Técnica.
    """
    nome = models.CharField(max_length=50, unique=True)
    # Ex: 'fa-brands fa-python'. O prefixo 'fa-' é necessário para o Font Awesome.
    classe_icone = models.CharField(
        max_length=50, 
        help_text="Classe CSS completa do ícone Font Awesome (ex: 'fa-brands fa-python')"
    )
    
    class Meta:
        verbose_name = "Tecnologia"
        verbose_name_plural = "Stack Técnica"
        ordering = ['nome'] # Eficiência algorítmica: ordena por nome

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    """
    Modelo para gerenciar os projetos exibidos no portfólio.
    """
    titulo = models.CharField(max_length=100, unique=True)

    # MELHORIA SEO/URL: Adicionar um slug para URLs amigáveis
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    # CORREÇÃO: TextField não deve ter max_length (use CharField para isso)
    descricao = models.TextField()

    url_github = models.URLField(
        max_length=200, help_text="Link completo para o repositório do GitHub."
    )
    ativo = models.BooleanField(
        default=True,
        help_text="Define se o projeto deve ser exibido na página inicial.",
    )
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"
        ordering = ["-data_criacao"]

    # MELHORIA CLEAN CODE: Geração automática do slug antes de salvar
    def save(self, *args, **kwargs):
        if not self.slug:
            # Garante que o slug seja limpo e baseado no título
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo
