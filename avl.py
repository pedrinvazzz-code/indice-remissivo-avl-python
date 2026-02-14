class NO:
    def __init__(self, info, linha):
        self.info = info
        self.linhas = set()
        self.linhas.add(linha)
        self.altura = 0
        self.esq = None
        self.dir = None


class AVL:
    def __init__(self):
        self.__raiz = None
        self.rotacoes = 0

    def getRaiz(self):
        return self.__raiz

    def __altura(self, no):
        if no is None:
            return -1
        return no.altura

    def __maior(self, x, y):
        return x if x > y else y

    def __RotacaoLL(self, A):
        self.rotacoes += 1
        B = A.esq
        A.esq = B.dir
        B.dir = A

        A.altura = self.__maior(self.__altura(A.esq), self.__altura(A.dir)) + 1
        B.altura = self.__maior(self.__altura(B.esq), self.__altura(B.dir)) + 1
        return B

    def __RotacaoRR(self, A):
        self.rotacoes += 1
        B = A.dir
        A.dir = B.esq
        B.esq = A

        A.altura = self.__maior(self.__altura(A.esq), self.__altura(A.dir)) + 1
        B.altura = self.__maior(self.__altura(B.esq), self.__altura(B.dir)) + 1
        return B

    def __RotacaoLR(self, A):
        A.esq = self.__RotacaoRR(A.esq)
        return self.__RotacaoLL(A)

    def __RotacaoRL(self, A):
        A.dir = self.__RotacaoLL(A.dir)
        return self.__RotacaoRR(A)

    def __insere(self, atual, valor, linha):

        if atual is None:
            return NO(valor, linha)

        if valor < atual.info:
            atual.esq = self.__insere(atual.esq, valor, linha)

        elif valor > atual.info:
            atual.dir = self.__insere(atual.dir, valor, linha)

        else:
            atual.linhas.add(linha)
            return atual

        atual.altura = 1 + self.__maior(self.__altura(atual.esq),
                                        self.__altura(atual.dir))

        balance = self.__altura(atual.esq) - self.__altura(atual.dir)

        if balance > 1 and valor < atual.esq.info:
            return self.__RotacaoLL(atual)

        if balance < -1 and valor > atual.dir.info:
            return self.__RotacaoRR(atual)

        if balance > 1 and valor > atual.esq.info:
            atual.esq = self.__RotacaoRR(atual.esq)
            return self.__RotacaoLL(atual)

        if balance < -1 and valor < atual.dir.info:
            atual.dir = self.__RotacaoLL(atual.dir)
            return self.__RotacaoRR(atual)

        return atual

    def insere(self, valor, linha):
        self.__raiz = self.__insere(self.__raiz, valor, linha)

    def __fatorBalanceamento(self, no):
        if no is None:
            return 0
        return self.__altura(no.esq) - self.__altura(no.dir)
    
    def __procuraMenor(self, no):
        atual = no
        while atual.esq is not None:
            atual = atual.esq
        return atual



    def remove(self, valor, linha):
        if self.__raiz is None:
            return False

        if not self.busca(valor):
            return False

        self.__raiz = self.__removeValor(self.__raiz, valor, linha)
        return True
    
    def __removeValor(self, atual, valor, linha):
        if atual is None:
            return atual

        if valor < atual.info:
            atual.esq = self.__removeValor(atual.esq, valor, linha)

        elif valor > atual.info:
            atual.dir = self.__removeValor(atual.dir, valor, linha)

        else:
            if linha in atual.linhas:
                atual.linhas.remove(linha)
            if len(atual.linhas) > 0:
                return atual
            if atual.esq is None:
                return atual.dir
            elif atual.dir is None:
                return atual.esq
            temp = self.__procuraMenor(atual.dir)
            atual.info = temp.info
            atual.linhas = temp.linhas.copy()
            atual.dir = self.__removeValor(
                atual.dir,
                temp.info,
                next(iter(temp.linhas))
            )

        atual.altura = 1 + self.__maior(
            self.__altura(atual.esq),
            self.__altura(atual.dir)
        )

        balance = self.__fatorBalanceamento(atual)
        if balance > 1 and self.__fatorBalanceamento(atual.esq) >= 0:
            return self.__RotacaoLL(atual)

        if balance > 1 and self.__fatorBalanceamento(atual.esq) < 0:
            return self.__RotacaoLR(atual)

        if balance < -1 and self.__fatorBalanceamento(atual.dir) <= 0:
            return self.__RotacaoRR(atual)

        if balance < -1 and self.__fatorBalanceamento(atual.dir) > 0:
            return self.__RotacaoRL(atual)

        return atual


    def busca(self, valor):
        atual = self.__raiz
        while atual:
            if valor == atual.info:
                return atual
            if valor < atual.info:
                atual = atual.esq
            else:
                atual = atual.dir
        return None

    def contar_nos(self, raiz):
        if raiz is None:
            return 0
        return 1 + self.contar_nos(raiz.esq) + self.contar_nos(raiz.dir)

    def medidor_equilibrio(self, valor):
        no = self.busca(valor)
        if no is None:
            return -1

        esquerda = self.contar_nos(no.esq)
        direita = self.contar_nos(no.dir)

        ME = esquerda - direita

        if ME == 0:
            return 0
        else:
            print("Medidor de Equilíbrio:", ME)
            return 1

    def busca_prefixo(self, prefixo):
        resultado = []
        self.__prefixo(self.__raiz, prefixo.lower(), resultado)
        return resultado

    def __prefixo(self, raiz, prefixo, resultado):
        if raiz:
            self.__prefixo(raiz.esq, prefixo, resultado)
            if raiz.info.startswith(prefixo):
                resultado.append(raiz.info)
            self.__prefixo(raiz.dir, prefixo, resultado)

    def palavra_mais_frequente(self):
        return self.__mais_frequente(self.__raiz, None)

    def __mais_frequente(self, raiz, atual):
        if raiz:
            atual = self.__mais_frequente(raiz.esq, atual)
            if atual is None or len(raiz.linhas) > len(atual.linhas):
                atual = raiz
            atual = self.__mais_frequente(raiz.dir, atual)
        return atual

    def em_ordem_arquivo(self, raiz, arquivo):
        if raiz:
            self.em_ordem_arquivo(raiz.esq, arquivo)
            linhas = ",".join(str(l) for l in sorted(raiz.linhas))
            arquivo.write(f"{raiz.info} {linhas}\n")
            self.em_ordem_arquivo(raiz.dir, arquivo)
