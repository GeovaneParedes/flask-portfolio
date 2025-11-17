from django.test import TestCase  # CORREÇÃO: Importa do Django
from django.urls import reverse  # CORREÇÃO: Importa do Django


class PortfolioViewTest(TestCase):
    """
    Testes unitários para a View principal (index).
    """

    def test_index_view_status_code(self):
        """Verifica se a URL raiz retorna status 200 (OK)."""
        response = self.client.get(reverse('index'))
        # Garante o tratamento robusto de erros para o status code
        self.assertEqual(response.status_code, 200)

    def test_index_view_uses_correct_template(self):
        """Verifica se a View usa o template index.html."""
        response = self.client.get(reverse("index"))
        # CORREÇÃO: Template correto é portfolio/index.html
        self.assertTemplateUsed(response, "portfolio/index.html")

    # Exemplo de Teste Sênior: Garantir que o contexto está sendo passado
    def test_context_is_passed(self):
        """Verifica se o contexto (projetos e tecnologias) está sendo passado."""
        # Se você tivesse Models criados no DB, este teste validaria o contexto.
        response = self.client.get(reverse("index"))
        self.assertIn("projetos", response.context)
        self.assertIn("tecnologias", response.context)
