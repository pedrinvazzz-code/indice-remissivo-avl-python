class NO:
    def __init__(self, info, linha):
        self.info = info
        self.linhas = set()
        self.linhas.add(linha)
        self.altura = 0
        self.esq = None
        self.dir = None
