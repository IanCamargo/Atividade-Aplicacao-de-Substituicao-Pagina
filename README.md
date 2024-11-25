# Atividade Aplicação de Substituição Página 

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)

## 💼 Informações sobre o Trabalho
**Faculdade de Tecnologia de Mogi Mirim**

**Curso:** Análise e Desenvolvimento de Sistemas (Noturno)

**Matérias:**

* 🖥️Sistemas Operacionais I
  
**Professores:**

* 👨🏻‍🏫Sandro Roberto Armelin

**Autores:**

- **Fernando Divino** - [@FernaandoJr](https://github.com/FernaandoJr)
- **Gabriel Coelho** - [@GabrielCoelho](https://github.com/GabrielCoelho)
- **Ian Camargo** - [@IanCamargo](https://github.com/IanCamargo)
- **Marcus Fernandes** - [@marcusfrnds](https://github.com/marcusfrnds)

## &#128214; Índice 

* [Tecnologias Utilizadas](#Tecnologias-Utilizadas)
* [Problemas e Soluções](#Problemas-e-Soluções)
* [Guia do Usuário](#Guia-do-Usuário)
* [Conclusão](#conclusão)
* [Agradecimentos](#agradecimentos)

## 🔗 Tecnologias Utilizadas

 - Linguagem Python
 - Visual Studio

## ❓ Problemas e Soluções
A necessidade de gerenciar a alocação de páginas na memória, simulando algoritmos de substituição (LRU e FIFO) para minimizar faltas de página. Frequentemente, os sistemas operacionais enfrentam dificuldades em decidir quais páginas manter ou substituir quando a memória está cheia, o que pode impactar o desempenho.

### Problema
A necessidade de gerenciar a alocação de páginas na memória, simulando algoritmos de substituição (LRU e FIFO) para minimizar faltas de página. Frequentemente, os sistemas operacionais enfrentam dificuldades em decidir quais páginas manter ou substituir quando a memória está cheia, o que pode impactar o desempenho.

### Solução
Implementação de um programa interativo em Python que simula os algoritmos de substituição de páginas LRU e FIFO. Este programa permite:

* Identificar o impacto de diferentes algoritmos na quantidade de faltas de página.
* Avaliar padrões de acesso e eficiência de alocação para um número limitado de quadros.

## **📝 Guia do Usuário**

### 1. Requisitos:
   - Python 3 instalado no sistema.

### 2. Como executar:
   - Salve o código em um arquivo chamado, por exemplo, `simulador_paginas.py`.
   - Abra o terminal ou prompt de comando e execute:
     ```bash
     python simulador_paginas.py
     ```

### 3. Entrada de Dados:
   - Insira a sequência de referência de páginas no formato: `7 0 1 2 0 3 0 4`.
   - Digite o número de quadros de memória disponíveis (ex.: `4`).
   - Escolha o algoritmo de substituição:
     - `1` para LRU.
     - `2` para FIFO.

### 4. Saída Esperada:
   - Estado dos quadros após cada referência de página.
   - Indicação de "ACERTO" ou "FALTA" para cada passo.
   - Resumo final com o total de acertos, faltas e o estado final dos quadros.

Aqui está um exemplo completo de execução do programa com o algoritmo **LRU** e as seguintes entradas:

- **Sequência de páginas:** `7 0 1 2 0 3 0 4`
- **Número de quadros:** `4`

### 5. Execução Completa

**Entrada:**
```plaintext
### Simulação de Algoritmos de Substituição de Páginas ###
Informe a sequência de referência de páginas (ex.: 7 0 1 2 0 3 0 4): 7 0 1 2 0 3 0 4
Informe o número de quadros de memória: 4

Escolha o algoritmo:
1 - LRU (Least Recently Used)
2 - FIFO (First-In, First-Out)
Digite sua escolha: 1
```

**Saída:**
```plaintext
Simulando LRU...
Página Referenciada: 7 | Quadros: [7] | FALTA
Página Referenciada: 0 | Quadros: [7, 0] | FALTA
Página Referenciada: 1 | Quadros: [7, 0, 1] | FALTA
Página Referenciada: 2 | Quadros: [7, 0, 1, 2] | FALTA
Página Referenciada: 0 | Quadros: [7, 0, 1, 2] | ACERTO
Página Referenciada: 3 | Quadros: [3, 0, 1, 2] | FALTA
Página Referenciada: 0 | Quadros: [3, 0, 1, 2] | ACERTO
Página Referenciada: 4 | Quadros: [4, 0, 1, 2] | FALTA

### Resultado LRU ###
Conteúdo final dos quadros: [4, 0, 1, 2]
Total de faltas de página: 6
Total de acertos de página: 2
```

### 6. Explicação do Resultado

- **Faltas de página (6):**
   - Cada nova página adicionada à memória (quando ainda não estava nos quadros) resultou em uma falta de página.
   - Ocorreram nos seguintes passos: `7`, `0`, `1`, `2`, `3`, `4`.

- **Acertos de página (2):**
   - Quando a página `0` foi referenciada novamente nas etapas `5` e `7`, já estava presente na memória.

- **Substituições:**
   - As páginas `7` e `3` foram substituídas pelas páginas mais recentemente usadas, seguindo o algoritmo LRU.

**OBS:** Esse exemplo é da opção 1 - LRU (Menos Recentemente Usado), caso deseje testar a opção 2 - FIFO (Primeiro a Entrar, Primeiro a Sair) será o mesmo procedimento as mudanças serão o resultado e a opção selecionada no início do código.

### 7. Dicas de Uso:
   - Teste diferentes padrões de referência de páginas para observar o impacto nos algoritmos.
   - Compare os resultados de LRU e FIFO para o mesmo conjunto de dados.

Este programa é ideal para aprender sobre substituição de páginas de forma prática!

# ✅ Conclusão
Este código é uma excelente ferramenta didática para entender o comportamento de algoritmos de substituição de páginas. Ele não só demonstra o funcionamento básico de LRU e FIFO, mas também permite experimentar com diferentes padrões de referência e quantidades de quadros para observar como os algoritmos se comportam em cenários distintos.

# 🙏 Agradecimentos
❤️ Obrigado por visitar meu repositório! Esperamos que você ache nosso projeto útil e interessante.
