# 📦 Shibakita Tech - Sistema de Gestão

Este é o sistema oficial de gestão da Shibakita Tech, desenvolvido para o Sr. Toshiro Shibakita. O software moderniza a operação da loja com uma interface de alta fidelidade e armazenamento de dados em nuvem.

Este projeto foi construído como parte do laboratório prático de programação no Senac Jaboticabal.

## 🚀 Funcionalidades

* **Autenticação Segura**: Sistema de login integrado ao Azure SQL Database com distinção de perfis (Administrador e Operador).
* **Interface Moderna**: UI construída com `CustomTkinter`, suportando temas Dark e Light.
* **Gestão de Estoque**: Controle em tempo real com gatilhos (triggers) de banco de dados.
* **Painel de Controle**: Menu lateral responsivo para navegação intuitiva.

## 🛠️ Tecnologias Utilizadas

* **Linguagem**: Python 3.x
* **Interface**: CustomTkinter
* **Banco de Dados**: Microsoft Azure SQL Server
* **Drivers**: `pyodbc` para conexão ODBC.
* **Imagens**: `Pillow` (PIL) para processamento de ativos visuais.

## 📋 Instalação e Configuração

1. **Clone o Repositório:**

```bash
git clone https://github.com/seu-usuario/shibakita-tech.git
cd shibakita-tech
```

2. **Crie um Ambiente Virtual (venv):**

```bash
python -m venv venv

# No Windows:
.\venv\Scripts\activate
```

3. **Instale as Dependências:**

```bash
pip install -r requirements.txt
```

4. **Banco de Dados**: Configure as variáveis de servidor e senha no arquivo `database.py` conforme as orientações do administrador.

## 📁 Estrutura de Arquivos

* `main.py`: Tela de entrada e lógica de login.
* `menu.py`: Dashboard principal e navegação.
* `database.py`: Central de conexão com o Azure SQL.
* `logo_shibakita.png`: Logotipo da empresa.

## 👨‍🏫 Equipe

* **Professor**: Denilson Bonatti
* **Guia dos Slides**: Gabriel Maromba
* **Técnico**: Marcelo Cochilante
* **Cliente**: Sr. Toshiro Shibakita

---

**Senac Jaboticabal - 2026**
