from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Hardening/Segurança: Lembre-se de mudar 'admin/' para algo único em produção!
    path("admin/", admin.site.urls),
    # Modularidade: Direciona todas as requisições para as URLs do app 'portfolio'
    path("", include("portfolio.urls")),
]

# Padrão DevOps/Performance: Serve arquivos estáticos APENAS em desenvolvimento (DEBUG=True).
# Em produção, essa responsabilidade é do servidor web (Nginx, Apache).
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
