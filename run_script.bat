@echo off
REM Define as variáveis de ambiente
set EMAIL_USER=seu_email@dominio.com
set EMAIL_PASS=sua_senha_de_aplicativo

REM Caminho completo para o executável Python
set PYTHON_PATH=C:\Users\SeuUsuario\AppData\Local\Programs\Python\Python39\python.exe

REM Navega até o diretório onde está o script Python
cd scripts

REM Executa o script Python
%PYTHON_PATH% monitor.py
