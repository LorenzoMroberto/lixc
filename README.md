# lixc
Manipulação da lixeira do windows por cli

![Python](https://img.shields.io/badge/Python-3.7+-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Ativo-brightgreen)
![Versão](https://img.shields.io/badge/Versão-1.0-blue)
![Dependencies](https://img.shields.io/badge/dependencies-2-brightgreen)
![Py+Win](https://img.shields.io/badge/Python%203.11.7%20%7C%20Windows%2011-✔-brightgreen?logo=python&logoColor=white)

<img width="878" height="875" alt="Captura de tela 2025-08-08 120852" src="https://github.com/user-attachments/assets/0fc9ce5d-f02a-4f43-b6df-ff368899930e" />


É isso mesmo, o script é apenas isto, manipular a lixeira por cli


## Como usar o script

| Argumento | Tipo | Descrição |
| ----------- | ----------- | ----------- |
| l     | comando | Lista todos os itens da lixeira |
| e      | Comando | Esvazia completamente a lixeira |
| e <numero: 3> | Comando | Exclui permanentemente o item com o número especificado |
| <arquivo/pasta> | Comando | Move o item para a lixeira |


📌 Resumo: Por que este script é adequado para você?
- ✅ Usa APIs oficiais do Windows ( Ou seja, é totalmente seguro )
- ✅ Sem diálogos indesejados ( afinal, é por interface de linha de comando 'cli' )
- ✅ Código pequeno e funcional
- ✅ Trata erros com mensagens claras
- ✅ Funciona em Windows 10 e 11

## Módulos usados no script

| Módulo | Detalhes |
| -- | -- |
| pywin32 | Terá que baixar |
| os | Interno para python 3x ou 1.4+ |
| sys | Interno para python 3x ou 1.0+ |
| pythoncom | Terá que baixar |
| ctypes | Interno para python 3x ou 2.5+ |

Testado e funcional em python 3.11.7 e Windows 11
