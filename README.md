# 💻 devgege-project | Portfólio Dinâmico Django

Este projeto é um portfólio pessoal dinâmico construído com 
**Django** e **Tailwind CSS**, seguindo as melhores práticas de 
**Clean Code**, **Modularidade** (padrão de apps Django), e 
**Segurança** (uso de variáveis de ambiente).

## 🚀 1. Inicialização do Projeto

Siga estas instruções para configurar e rodar o projeto localmente.

### Pré-requisitos
* Python (versão >= 3.11, preferencialmente).
* Git.

### 1.1. Configuração do Ambiente

1.  **Clone o repositório:**
    ```bash
    git clone [git@github.com:GeovaneParedes/flask-portfolio.git]
    cd flask-portfolio
    ```

2.  **Crie e Ative o Ambiente Virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    # .\venv\Scripts\activate  # Windows PowerShell
    ```

3.  **Instale as Dependências:**
    Instale todas as bibliotecas listadas em `requirements.txt` 
    (Django, python-decouple, Black, Pytest, etc.).
    ```bash
    pip install -r requirements.txt
    ```

### 1.2. Configuração de Variáveis de Ambiente

O projeto usa a biblioteca `python-decouple` para gerenciar as configurações 
sensíveis, seguindo o padrão **OWASP** para segurança.

1.  Crie o arquivo **`.env`** na raiz do projeto (`devgege-project/`).
2.  Preencha-o com as configurações de desenvolvimento:

    ```ini
    # .env
    # Troque a chave secreta abaixo por uma nova chave gerada para produção!
    SECRET_KEY='django-insecure-m+w@y1o!#6s-i1r_7i^p=w!#m2e8j$r$*+*5e(i#q3b6-i1' 
    DEBUG=True
    ALLOWED_HOSTS=127.0.0.1, localhost

    # Configuração Padrão SQLite (Desenvolvimento)
    DB_ENGINE=django.db.backends.sqlite3
    DB_NAME=db.sqlite3
    ```

### 1.3. Banco de Dados e Superusuário

1.  **Aplique as Migrações** (Cria as tabelas no `db.sqlite3`):
    ```bash
    python manage.py migrate
    ```

2.  **Crie o Superusuário** (Para acessar o painel Admin):
    ```bash
    python manage.py createsuperuser
    ```

3.  **Inicie o Servidor:**
    ```bash
    python manage.py runserver
    ```

O site estará acessível em `http://127.0.0.1:8000/`. O painel de administração para gerenciar o conteúdo (Projetos, Stack, Configurações) está em `http://127.0.0.1:8000/admin/`.

---

## 📐 2. Arquitetura do Projeto (Padrão Sênior)

O projeto segue a estrutura padrão de aplicativos do Django, focando na **modularidade** e na **separação de responsabilidades (SOLID)**.

### Estrutura de Diretórios Corrigida

A pasta **`portfolio/`** contém todos os recursos da aplicação (lógica, modelos, estáticos e templates):
devgege-project/ 
├── .env # Variáveis de Ambiente (NÃO versionado) 
├── .gitignore # Exclui .env, venv, staticfiles (DevOps/Segurança) 
├── manage.py # Script de execução do Django 
├── core/ # Configurações Globais (Settings, URLs principais) 
├── portfolio/ # Aplicação Principal 
│ ├── models.py # Estrutura de Dados (Projetos, Tecnologias, Configuração) 
│ ├── views.py # Lógica de Consulta de Dados 
│ ├── templates/ # Templates HTML (base.html, index.html) 
│ ├── static/ # CSS e JS 
│ └── tests.py # Testes de Unidade 
└── venv/ # Ambiente Virtual (Excluído pelo .gitignore)
### 2.1. Funcionalidades Chave

* 
**Conteúdo Dinâmico:
** Os dados do portfólio (Projetos, Stack, Sobre Mim) são gerenciados via Admin, graças aos modelos `Projeto`, `Tecnologia` e ao `ConfiguracaoSite` (Modelo Singleton).
* 
**SEO:
** O modelo `Projeto` inclui um campo 
**`slug`
** para criar URLs amigáveis.
* 
**Segurança:
** A configuração `settings.py` utiliza `python-decouple` para carregar dados sensíveis e hardening básico nas validações de senha.
* 
**Front-end:
** O site é renderizado usando Templates Django e estilizado com 
**Tailwind CSS** (CDN em desenvolvimento). O JavaScript utiliza `IntersectionObserver` para performance.

---

## 🧪 3. Testes e Qualidade de Código

Para garantir a confiabilidade e escalabilidade, este projeto utiliza **pytest** e **flake8**.

1.  **Executar Testes:**
    ```bash
    pytest
    ```

2.  **Verificar Qualidade (Linting):**
    ```bash
    flake8 .
    ```

3.  **Formatar Código (Black):**
    ```bash
    black .
    ```
    (Garante Clean Code e padrões de estilo consistentes).
