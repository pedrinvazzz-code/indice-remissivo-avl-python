import re
import time
from avl import AVL

def main():

    arvore = AVL()

    total_palavras = 0
    descartadas = 0

    inicio = time.time()

    with open("texto_origem.txt", "r", encoding="utf-8") as f:
        for numero_linha, linha in enumerate(f, start=1):
            linha = re.sub(r'[^\w\s]', '', linha)
            linha = linha.lower()
            palavras = linha.split()

            for palavra in palavras:
                total_palavras += 1

                no = arvore.busca(palavra)

                if no:
                    tamanho_antes = len(no.linhas)
                    arvore.insere(palavra, numero_linha)
                    tamanho_depois = len(no.linhas)

                    if tamanho_depois == tamanho_antes:
                        descartadas += 1
                else:
                    arvore.insere(palavra, numero_linha)

    fim = time.time()
    tempo = fim - inicio

    with open("indice_saida.txt", "w", encoding="utf-8") as out:
        arvore.em_ordem_arquivo(arvore.getRaiz(), out)

        out.write("\n")
        out.write(f"Número total de palavras: {total_palavras}\n")
        out.write(f"Número de palavras distintas: {arvore.contar_nos(arvore.getRaiz())}\n")
        out.write(f"Número de palavras descartadas: {descartadas}\n")
        out.write(f"Tempo de construção: {tempo:.4f}s\n")
        out.write(f"Total de rotações executadas: {arvore.rotacoes}\n")

    print("Índice criado com sucesso!")

if __name__ == "__main__":
    main()
