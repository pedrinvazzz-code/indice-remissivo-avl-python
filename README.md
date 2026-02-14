Trabalho Avaliativo - Índice Remissivo utilizando Árvore AVL (python)

- Pedro Henrique Ferreira Borges Vaz - 12321GIN017

INTRODUÇÃO:

O problema consiste em desenvolver um índice remissivo para documentos de texto, listando todas as palavras do texto e apontando em qual linha elas aparecem, além disso o sistema descarta palavras que se repetem na mesma linha, para garantir a precisão da busca das palavras.

Para a resolução do problema, a solução adotada foi uma árvore AVL, que armazena cada palavra em seus nós e faz o balanceamento da árvore, garantindo um bom equilibrío e execução dos comandos de procura, inserção e remoção das palavras.

Para desenvolver os códigos, foi utilizado o estudo dos arquivos disponibilizados pela professora no moodle, onde desenvolvi minhas habilidades em ABB e AVL, sendo assim, a partir dos códigos de Árvore AVL, os adaptei para o problema em questão.

DOCUMENTAÇÃO DO CÓDIGO:

-> Classe NO

A classe NO representa um nó da árvore AVL, e com a função __init__ nós definimos o que cada nó armazena, que no nosso caso é:

Atributos:
- info: palavra armazenada no nó
- linhas: conjunto (set) contendo as linhas onde a palavra ocorre
- altura: altura do nó, utilizada para o balanceamento da árvore
- esq: referência para o filho esquerdo
- dir: referência para o filho direito

-> Classe AVL:

A classe AVL implementa a árvore AVL, que armazena todos os nós e implementa as operações desejadas.

Funções:
- Inserção(insere): Insere uma palavra na árvore, se a palavra não existir, é gerado um novo nó, caso já exista, é adicionado no índice a linha onde a palavra foi inserida.

- Busca(busca): Vasculha a árvore até achar a palavra desejada, caso ache, retorna True, caso não ache retorna False.

- Remoção(remove):Remove a palavra escolhida em uma linha específica.
    Se após a remoção a palavra não possuir mais linhas associadas, o nó inteiro é removido da árvore, mantendo o balanceamento AVL.

- Busca por prefixo (busca_prefixo):
Retorna todas as palavras do texto que se iniciam com o prefixo desejado.

- Medidor de Equilíbrio (medidor_equilibrio): Calcula a diferença entre o número de nós da subárvore esquerda e direita de um determinado nó.

- Palavra mais frequente (palavra_mais_frequente): Retorna a palavra que mais aparece no texto.

- Impressão em ordem (em_ordem_arquivo): Faz a impressão da árvore em ordem alfabética e retorna o índice completo em um arquivo.

-> Programa Principal (main.py)

O programa principal (main.py) é responsável por ler o arquivo do texto desejado, formatar o texto com operações de remoção de pontuações e conversão de todas as palavras para minúsculas, e após isso inserir as palavras na árvore. Uma vez que a árvore armazene todas as palavras, é feito a contabilização de palavras totais, distintas e descartadas.

Além disso o programa retorna o tempo de execução do código e gera o arquivo do índice final.


EXEMPLOS DE USO:

- Inserção e Busca:

avl.insere("python", 10)
avl.insere("python", 20)
avl.insere("java", 5)

print(avl.busca("python").linhas)

        Saída esperada: {10, 20}


- Remoção de Linha:
    avl.remove("python", 10)
    print(avl.busca("python").linhas)

        Saída esperada: {20}


- Busca por prefixo: 
    avl.busca_prefixo("ja")

        Saída esperada: ['java']



