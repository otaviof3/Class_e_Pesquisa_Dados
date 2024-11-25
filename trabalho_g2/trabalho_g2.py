class Jogo:
    def __init__(self, jogo_id, titulo, desenvolvedor, preco, generos):
        self.jogo_id = jogo_id
        self.titulo = titulo
        self.desenvolvedor = desenvolvedor
        self.preco = preco
        self.generos = generos  

class NoJogo:
    def __init__(self, jogo):
        self.jogo = jogo
        self.esquerda = None
        self.direita = None

class ArvoreJogos:
    def __init__(self):
        self.raiz = None
        self.hash_generos = HashGeneros()

    def inserir(self, jogo):

        # Adicionar o jogo à tabela hash de gêneros
        self.hash_generos.adicionar_jogo(jogo)

        # Inserir na árvore binária
        novo_no = NoJogo(jogo)
        if self.raiz is None:
            self.raiz = novo_no
        else:
            atual = self.raiz
            while True:
                if novo_no.jogo.preco < atual.jogo.preco:
                    if atual.esquerda is None:
                        atual.esquerda = novo_no
                        break
                    atual = atual.esquerda
                else:
                    if atual.direita is None:
                        atual.direita = novo_no
                        break
                    atual = atual.direita

    def buscar_por_preco(self, preco):
        # Busca todos os jogos com preço exato
        resultados = []
        stack = [self.raiz] if self.raiz else []

        while stack:
            atual = stack.pop()
            if atual.jogo.preco == preco:
                resultados.append(atual.jogo)
            if atual.esquerda:
                stack.append(atual.esquerda)
            if atual.direita:
                stack.append(atual.direita)

        return resultados

    def buscar_por_faixa_de_preco(self, preco_min, preco_max):
        # Busca todos os jogos dentro de uma faixa de preço
        resultados = []
        stack = [self.raiz] if self.raiz else []

        while stack:
            atual = stack.pop()
            if preco_min <= atual.jogo.preco <= preco_max:
                resultados.append(atual.jogo)
            if atual.esquerda:
                stack.append(atual.esquerda)
            if atual.direita and atual.jogo.preco <= preco_max:
                stack.append(atual.direita)

        return resultados
    
    def buscar_jogos_por_genero(self, genero):
        return self.hash_generos.obter_jogos(genero)

class HashGeneros:
    def __init__(self):
        self.genero_para_jogos = {}
        self.genero_para_ids = {}

    def adicionar_jogo(self, jogo):
        for genero in jogo.generos:
            if genero not in self.genero_para_jogos:
                self.genero_para_jogos[genero] = []
            self.genero_para_jogos[genero].append(jogo)

    def obter_jogos(self, genero):
        return self.genero_para_jogos.get(genero, [])

arvore = ArvoreJogos()
arvore.inserir(Jogo(1, "RPG Quest", "Dev A", 100, ["RPG", "Aventura"]))
arvore.inserir(Jogo(2, "Action Blast", "Dev B", 50, ["Ação"]))
arvore.inserir(Jogo(3, "Puzzle World", "Dev C", 150, ["Estratégia", "Puzzle"]))
arvore.inserir(Jogo(4, "Indie Gem", "Dev D", 75, ["Indie", "RPG"]))
arvore.inserir(Jogo(5, "Shooter Pro", "Dev E", 200, ["Ação", "Tiro"]))

print("Jogos com preço exato R$ 100:")
for jogo in arvore.buscar_por_preco(100):
    print(f"{jogo.titulo} - R$ {jogo.preco}")

print("\nJogos com faixa de preço entre R$ 50 e R$ 150:")
for jogo in arvore.buscar_por_faixa_de_preco(50, 150):
    print(f"{jogo.titulo} - R$ {jogo.preco}")

jogos_rpg = arvore.buscar_jogos_por_genero("RPG")
print("\nJogos do gênero 'RPG':")
for jogo in jogos_rpg:
    print(f"{jogo.titulo} - R$ {jogo.preco}")