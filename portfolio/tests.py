from django.test import TestCase
from django.urls import reverse
from django.core import mail
from django.contrib.auth.models import User
from portfolio.models import Projeto, Tecnologia, ConfiguracaoSite
from django.utils.text import slugify


# --- CLASSE BASE PARA CONFIGURAÇÃO DE DADOS MÍNIMOS ---
class TestSetupData(TestCase):
    """
    Classe base para configurar os dados mínimos necessários (Singleton e User)
    para que todos os testes rodem sem falhar por dependência de Modelos.
    """

    def setUp(self):
        """Cria o ConfiguraçõesSite (Singleton) e um Usuário de Teste."""
        # Cria a configuração singleton, pois as Views dependem disso para não falhar
        self.config, created = ConfiguracaoSite.objects.get_or_create(
            pk=1,
            defaults={
                "titulo_header": "DevGege Teste",
                "descricao_sobre_mim": "Teste de descrição da View",
            },
        )

        # Cria um usuário para ser usado no teste de Password Reset
        self.user_email = "teste@devgege.com"
        self.user = User.objects.create_user(
            username="user_teste", email=self.user_email, password="SenhaForteV2025"
        )

        # Cria um objeto Projeto e Tecnologia para o teste de contexto
        Projeto.objects.create(
            titulo="Projeto Ativo Teste",
            descricao="Descrição breve.",
            url_github="https://github.com/teste/1",
            ativo=True,
        )
        Tecnologia.objects.create(nome="Python", classe_icone="fa-brands fa-python")


# --- TESTES DE MODELO (MODEL TEST) ---
class ProjetoModelTest(TestSetupData):
    """
    Testes de unidade para o modelo Projeto (foco na lógica de slugify).
    """

    # O setUp é herdado de TestSetupData

    def test_slug_generation_on_save(self):
        """Verifica se o slug é gerado automaticamente a partir do título."""
        projeto_data = {
            "titulo": "Meu Novo Projeto de Teste Com Caracteres Especiais!",
            "descricao": "Descrição breve.",
            "url_github": "https://github.com/teste/slug",
        }
        projeto = Projeto.objects.create(**projeto_data)
        expected_slug = slugify(projeto_data["titulo"])
        self.assertEqual(projeto.slug, expected_slug)


# --- TESTES DE VIEW (VIEW TEST) ---
class PortfolioViewTest(TestSetupData):
    """
    Testes de unidade para a View principal (index).
    """

    def test_index_view_status_code(self):
        """Verifica se a URL raiz retorna status 200 (OK)."""
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_index_view_uses_correct_template(self):
        """Verifica se a View usa o template index.html."""
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "portfolio/index.html")

    def test_context_is_passed(self):
        """Verifica se o contexto (projetos e tecnologias) está sendo passado."""
        response = self.client.get(reverse("index"))
        self.assertIn("projetos", response.context)
        self.assertIn("tecnologias", response.context)
        self.assertEqual(response.context["projetos"].count(), 1)
        self.assertEqual(response.context["tecnologias"].count(), 1)


# --- TESTES DE FLUXO DE SEGURANÇA (SECURITY FLOW TEST) ---
class PasswordResetTest(TestSetupData):
    """
    Testa o fluxo de redefinição de senha para garantir que o e-mail seja enviado.
    """

    # O setUp é herdado de TestSetupData

    def test_password_reset_sends_email(self):
        """Verifica se um email é adicionado ao outbox após submeter o formulário."""

        self.url = reverse("password_reset")

        response = self.client.post(self.url, {"email": self.user_email})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(mail.outbox), 1)

        email_sent = mail.outbox[0]
        self.assertIn(self.user_email, email_sent.to)
        self.assertIn("Redefinição de senha em testserver", email_sent.subject)
