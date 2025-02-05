#  ♻️ Plataforma Circular - FrontEnd
---
> Sistema FrontEnd da Plataforma Circular

### 💻 Pré-Requisitos
---
Antes de começar é importante conferir se você possui os seguintes requisitos:
- Possuir `Python 3.13.1` ou acima;
- Possuir `Pip 24.3.1` ou acima;

### 🚀 Instalação
---
Para instalar as dependências do projeto, siga as seguintes etapas:

**Clone o repositório:**
```bash
git clone git@github.com:Gabriel-Cisneiros/plataforma-circular.git

```

**Entre em seu respectivo diretório:**
```bash
cd plataforma-circular
```

**Abra um virtual environment com python:**
```bash
python -m venv .env
source .env/bin/activate
```

**Instale as dependências:**
```python
pip install -r requirements.txt
```

### ☕ Execução
---
Para rodar o projeto, primeiro dê o comando abaixo e depois entre em `http://localhost:8000/` para acessar o site:

```python
python manage.py runserver
```

### 📖 Guia de Fluxo de Trabalho

##### 1. Criando a branch de trabalho (Gitflow)

O Gitflow define um modelo de branches para o projeto:

- `main`: A branch de produção
- `dev`: A branch de desenvolvimento
- `feature`: Branches para o desenvolvimento de novas funcionalidades
- `bugfix`: Branches para a correção de bugs em releases
- `hotfix`: Branches para a correção de bugs críticos encontrados em produção

Usando um exemplo real, uma branch para a criação das telas de autenticação ficaria: `feature/auth`. Todas a branches devem ser criadas a partir da branch `dev` e, sempre que uma feature for encerrada, deve-se dar um merge da branch da feature com a `dev` e a branch deve ser excluida.

Se quiser saber mais [clique aqui](https://medium.com/trainingcenter/utilizando-o-fluxo-git-flow-e63d5e0d5e04)

##### 2. Padrões de Commits (Commits Semânticos)

Os commits devem seguir um padrão semântico para facilitar a leitura e o entendimento do histórico do projeto. Aqui estão alguns exemplos:

- `feat`: Uma nova feature
- `fix`: Uma correção de bug
- `docs`: Mudanças na documentação
- `style`: Mudanças que não afetam o significado do código (espaços em branco, formatação, ponto e vírgula faltando, etc)
- `refactor`: Uma mudança no código que não corrige um bug nem adiciona uma feature
- `perf`: Uma mudança no código que melhora a performance
- `test`: Adicionando testes faltantes ou corrigindo testes existentes
- `chore`: Mudanças no processo de build ou ferramentas auxiliares e bibliotecas

Usando ainda a branch criada no exemplo acima, um commit para a branch `feature/auth`, poderia ficar como: `feat: criação da tela de cadastro`

Para mais detalhes [clique aqui](https://www.conventionalcommits.org/en/v1.0.0/).

##### 3. Estrutura das Pastas (Principais Items)
```bash
    .
    ├── .env                 # Environment Python
    ├── frontend             # aplicação do frontend
    │   ├── ...
    │   ├── migrations       # migrations do banco de dados
    │   ├── static           # arquivos estáticos do sistema
    │   │     ├── css        # estilos css
    │   │     ├── images     # imagens do sistema
    │   │     └── js         # funções javascript
    │   │
    │   ├── templates        # arquivos html das paginas
    │   │      ├── ...
    │   │      ├── base.html # arquivo base
    │   │      └── ...
    │   │
    │   ├── admin.py         # representação dos ORMs no django-admin
    │   ├── apps.py          # gerenciamento de configurações específicas do app
    │   ├── models.py        # definição de estrutura de dados
    │   ├── tests.py         # testes unitários
    │   ├── urls.py          # mapeamento de URLs das views
    │   └── views.py         # processamento de solicitações de usuário
    │
    ├── ...
    ├── asgi.py              # lida com requests HTTP assíncronos            
    ├── settings.py          # configurações do projeto
    ├── urls.py              # mapeia URLs para views
    └── wsgi.py              # conecta a aplicação ao serviço web
```
