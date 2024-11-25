import networkx as nx
import matplotlib.pyplot as plt


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

        self.hash_generos.adicionar_jogo(jogo)

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
    
    def add_edges(self, node, graph, pos, x=0, y=0, layer=1):
        if node is not None:
            graph.add_node(node.jogo.titulo, pos=(x, y))
            if node.esquerda:
                graph.add_edge(node.jogo.titulo, node.esquerda.jogo.titulo)
                self.add_edges(node.esquerda, graph, pos, x=x - 1 / layer, y=y - 1, layer=layer + 1)
            if node.direita:
                graph.add_edge(node.jogo.titulo, node.direita.jogo.titulo)
                self.add_edges(node.direita, graph, pos, x=x + 1 / layer, y=y - 1, layer=layer + 1)

    def draw_tree(self):
        if not self.raiz:
            print("A árvore está vazia.")
            return
        
        graph = nx.DiGraph()
        pos = {}
        self.add_edges(self.raiz, graph, pos)
        pos = nx.spring_layout(graph)  # Layout ajustado automaticamente
        labels = {node: node for node in graph.nodes()}
        nx.draw(graph, pos, labels=labels, with_labels=True, arrows=False)
        plt.show()



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
    


def main():
    arvore = ArvoreJogos()
    while True:
        print("\nSteam 2: Electric Boogaloo")
        print("1 - Inserir jogo")
        print("2 - Buscar jogo por preço")
        print("3 - Buscar jogos por faixa de preço")
        print("4 - Buscar jogos por gênero")
        print("5 - Mostrar árvore")
        print("6 - Sair")

        opc = input("Escolha uma opção: ")

        if opc == "1":
            jogo_id = input("ID do jogo: ")
            titulo = input("Título do jogo: ")
            desenvolvedor = input("Desenvolvedor do jogo: ")
            preco = float(input("Preço do jogo: "))
            generos = input("Gêneros do jogo (separados por vírgula): ").split(", ")
            jogo = Jogo(jogo_id, titulo, desenvolvedor, preco, generos)
            arvore.inserir(jogo)
            print(f"Jogo '{titulo}' inserido com sucesso!")
        
        elif opc == "2":
            preco = float(input("Digite o preço para buscar jogos: "))
            resultados = arvore.buscar_por_preco(preco)
            if resultados:
                print("Jogos encontrados:")
                for jogo in resultados:
                    print(f"{jogo.titulo} - R$ {jogo.preco}")
            else:
                print("Nenhum jogo encontrado com esse preço.")
        
        elif opc == "3":
            preco_min = float(input("Digite o preço mínimo: "))
            preco_max = float(input("Digite o preço máximo: "))
            resultados = arvore.buscar_por_faixa_de_preco(preco_min, preco_max)
            if resultados:
                print("Jogos encontrados:")
                for jogo in resultados:
                    print(f"{jogo.titulo} - R$ {jogo.preco}")
            else:
                print("Nenhum jogo encontrado nessa faixa de preço.")
        
        elif opc == "4":
            genero = input("Digite o gênero para buscar jogos: ")
            resultados = arvore.buscar_jogos_por_genero(genero)
            if resultados:
                print("Jogos encontrados:")
                for jogo in resultados:
                    print(f"{jogo.titulo} - Gêneros: {', '.join(jogo.generos)}")
            else:
                print("Nenhum jogo encontrado para esse gênero.")
        
        elif opc == "5":
            arvore.draw_tree()

        elif opc == "6":
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
