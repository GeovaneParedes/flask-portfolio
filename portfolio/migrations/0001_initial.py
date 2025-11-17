from django.db import migrations, models


class Migration(migrations.Migration):
    # A dependência deve ser baseada no histórico do seu projeto.
    # Para a primeira migração (initial=True), geralmente é vazio.
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ConfiguracaoSite",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "titulo_header",
                    models.CharField(
                        default="DevGege - Desenvolvedor Python",
                        help_text="Texto principal exibido na animação de digitação.",
                        max_length=100,
                    ),
                ),
                (
                    "descricao_sobre_mim",
                    models.TextField(
                        help_text="O parágrafo principal da seção 'Sobre Mim'."
                    ),
                ),
            ],
            options={
                "verbose_name": "Configuração do Site",
                "verbose_name_plural": "Configuração do Site",
            },
        ),
        migrations.CreateModel(
            name="Projeto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=100, unique=True)),
                # ADIÇÃO SÊNIOR: Campo Slug para URLs amigáveis (SEO)
                ("slug", models.SlugField(max_length=100, unique=True, blank=True)),
                # CORREÇÃO: Removido 'max_length=300' de TextField
                ("descricao", models.TextField()),
                (
                    "url_github",
                    models.URLField(
                        help_text="Link completo para o repositório do GitHub."
                    ),
                ),
                (
                    "ativo",
                    models.BooleanField(
                        default=True,
                        help_text="Define se o projeto deve ser exibido na página inicial.",
                    ),
                ),
                ("data_criacao", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Projeto",
                "verbose_name_plural": "Projetos",
                "ordering": ["-data_criacao"],
            },
        ),
        migrations.CreateModel(
            name="Tecnologia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=50, unique=True)),
                (
                    "classe_icone",
                    models.CharField(
                        help_text="Classe CSS completa do ícone Font Awesome (ex: 'fa-brands fa-python')",
                        max_length=50,
                    ),
                ),
            ],
            options={
                "verbose_name": "Tecnologia",
                "verbose_name_plural": "Stack Técnica",
                "ordering": ["nome"],
            },
        ),
    ]
