# Network Monitoring

Este projeto monitora a conexão de rede de equipamentos e envia notificações por email usando um script Python e um arquivo `.bat`.

## Estrutura do Projeto


## Passos para Configurar e Executar

### 1. Requisitos

- Python 3.6 ou superior
- Biblioteca `psutil`
- Biblioteca `ping3`
- Biblioteca `smtplib`

### 2. Configuração do Script Python

Salve o seguinte script Python em `scripts/monitor.py`:

```python
(import os e outras bibliotecas necessárias)
(coloque o código do script Python aqui)

### 3. Configuração do Arquivo .bat

Crie um arquivo .bat na raiz do projeto com o nome run_script.bat:

bat

(coloque o conteúdo do arquivo .bat aqui)

### 4. Adicionar Python ao PATH

    Encontre o Diretório de Instalação do Python:
        O Python geralmente está instalado em um caminho como C:\Python39 ou C:\Users\SeuUsuario\AppData\Local\Programs\Python\Python39.

    Adicionar ao PATH:
        Abra o Painel de Controle.
        Vá em "Sistema e Segurança" > "Sistema".
        Clique em "Configurações avançadas do sistema" no lado esquerdo.
        Na aba "Avançado", clique em "Variáveis de Ambiente".
        Na seção "Variáveis de sistema", encontre e selecione a variável Path, depois clique em "Editar".
        Clique em "Novo" e adicione o caminho para o diretório de instalação do Python.

### 5. Criar Senha de Aplicativo no Office 365

    Acessar Segurança da Conta:
        Vá para o portal de contas do Microsoft Office 365: Office 365 Account Portal.

    Gerenciar Segurança:
        Clique em "Segurança" no menu.
        Clique em "Mais opções de segurança" ou "Opções de segurança adicionais".

    Configurar Senha de Aplicativo:
        Na seção de "Senhas de aplicativo", clique em "Criar uma nova senha de aplicativo".
        Siga as instruções para gerar uma senha de aplicativo.

    Anotar a Senha de Aplicativo:
        Copie a senha de aplicativo gerada.

### 6. Executar o Script

    Clique duas vezes no arquivo run_script.bat para executar o script e monitorar a rede.

lua


### 8. Adicionar, Commitar e Enviar os Arquivos para o GitHub

1. No Git Bash, adicione os arquivos ao repositório local:
   ```bash
   git add .

    Faça um commit com uma mensagem descritiva:

    bash

git commit -m "Add network monitoring script and batch file"

Envie os arquivos para o repositório no GitHub:

bash

git push origin master