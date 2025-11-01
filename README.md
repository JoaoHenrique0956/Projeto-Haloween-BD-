# 🎃 Cofre de Doces Criptografado

## 📘 Descrição
O projeto **Cofre de Doces Criptografado** tem como objetivo armazenar e proteger os tipos de doces coletados no Halloween.  
Cada registro inserido no sistema é **criptografado** utilizando o método **Fernet (AES simétrico)** antes de ser salvo no banco **MongoDB Atlas**.

O sistema foi desenvolvido em **Python**, com **Tkinter** para a interface gráfica, **PyMongo** para integração com o banco de dados em nuvem, e **Cryptography** para a proteção dos dados sensíveis.

O usuário pode:
- Adicionar novos doces.
- Listar todos os doces armazenados.
- Descriptografar as informações usando a chave correta.

---

## ⚙️ Tecnologias Utilizadas
- **Python 3.12+**
- **Tkinter** → Interface gráfica.
- **Cryptography (Fernet)** → Criptografia simétrica dos dados.
- **PyMongo** → Conexão e manipulação do banco MongoDB Atlas.
- **MongoDB Atlas** → Banco de dados em nuvem.
- **Datetime** → Registro automático de timestamp no formato ISO.

---

## 🗂️ Estrutura do Projeto

