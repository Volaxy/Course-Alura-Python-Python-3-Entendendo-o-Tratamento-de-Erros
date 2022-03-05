# Python 3: Entendendo o Tratamento de Erros

Curso da Alura sobre pilha de erros, Exceções e como tratar diversos erros

## Objetivo Final &#x1F3AF;

Usar o ByteBank como base para aplicar exceções

URL do curso -> [Python 3: Entendendo o Tratamento de Erros](https://cursos.alura.com.br/course/python-exceptions)

![Python 3: Entendendo o Tratamento de Erros](https://www.alura.com.br/assets/api/share/curso-python-exceptions.png)

## Links Úteis &#x1F517;
*

## Siglas &#x1F5FA;
*

## Atalhos &#x2328;
*

## 01 - Primeiros Passos com Exceções &#x1F516;
* Que o Python é uma linguagem dinamicamente tipada para escrita de atributos, porém estaticamente tipada para leitura deles..
* Sobre o *Attribute error*, uma exceção lançada pelo python quanto tentamos ler um atributos inexistente de uma classe.
* Qual importância de preparar nosso código para o tratamento de erros.
* O que são *f strings* e como podemos usar elas em nosso código.
* Como ler o *traceback* dos erros gerados pelo programa.
* A evitar a parada do nossso programa usando o comando `try` e `except`.

### 01 - Attribute Error
* Criação da classe `Client`.

### 02 - Conhecendo Exceções
* Criar uma classe `CheckingAccount`.

### 03 - Fornçando Problemas
* Ver em detalhes as mensagens de **erro** do **Python**.
* Ver o *traceback* de uma **exceção**.
* Colocar `//` para retornar o resultado inteiro de uma divisão.

### 04 - Try e Except
* Usar a palavra reservada **try** para tratar trechos sensíveis a erros.
* Usar a palavra reservada **except** para tratamento dos erros.
* Tratar várias **exceções** específicas.

## 02 - Propagação de Disparo de Exceções &#x1F516;
* Como lançar exceções com o comando `raise`.
* Qual o fluxo de execução quando um erro é disparado.
* Como usar o `except` para capturar diferentes tipos de exceção.

### 01 - Tratamento de Exceções
* Atribuir uma variável à exceção lançada com `as`.
* Usar o `.__class__.__bases__` para saber qual é a exceção pai de uma exceção.
* Tratar erros do menos genérico até o mais genérico.

### 02 - Raise
* Se nenhum retorno for feito para atribuir o valor a uma variável, o valor `None` será o valor que será atribuido por padrão.
* Usar a palavra reservada `raise`.
* Usar a função `isinstance(VARIABLE, TYPE)` para verificar se a instância da variável.