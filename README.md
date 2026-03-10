# 👤 Sistema de Cadastro de Usuários em Python

Um pequeno projeto em **Python** que permite **cadastrar e listar usuários** através de um menu interativo no terminal.

Os dados dos usuários são armazenados em um arquivo **JSON**, garantindo que as informações permaneçam salvas mesmo após o programa ser fechado.

---

## 🚀 Tecnologias utilizadas

* Python 3
* Biblioteca padrão `json`

---

## 🧠 Como funciona

1. O programa apresenta um **menu com opções**

2. O usuário pode escolher entre:

   * ➕ **Cadastrar usuário**
   * 📋 **Mostrar usuários cadastrados**
   * ❌ **Sair do sistema**

3. Ao cadastrar um usuário, o sistema solicita:

   * Nome
   * Idade
   * Email

4. As informações são armazenadas em uma **lista de dicionários**

5. Os dados são salvos automaticamente no arquivo **usuarios.json**

6. Ao iniciar o programa novamente, os usuários já cadastrados continuam disponíveis

---

## ▶️ Como executar o projeto

1. Clone o repositório:

```bash
git clone https://github.com/mbrv-dev/sistema-cadastro-usuarios.git
```

2. Entre na pasta do projeto:

```bash
cd sistema-cadastro-usuarios
```

3. Execute o programa:

```bash
python sistema-cadastro-usuario.py
```

---

## 📌 Exemplo de execução

```
====================
1. Cadastrar usuario
2. Mostrar usuarios
3. Sair
====================

Escolha uma opção: 1

Digite seu nome: Matheus
Digite sua idade: 22
Digite seu email: matheus@email.com

Usuário cadastrado com sucesso!
```

---

## 📚 Objetivo do projeto

Este projeto foi desenvolvido com o objetivo de **praticar conceitos fundamentais de programação em Python**, como:

* Estruturas de repetição (`while`)
* Condicionais (`if / elif / else`)
* Estruturas de dados (`listas` e `dicionários`)
* Manipulação de arquivos
* Persistência de dados com `JSON`
* Tratamento de erros (`try / except`)

---

## 👨‍💻 Autor

Desenvolvido por **Matheus Barcelos**

GitHub:
https://github.com/mbrv-dev
