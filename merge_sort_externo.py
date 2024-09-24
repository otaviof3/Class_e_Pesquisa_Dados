import random
import os
import heapq

def gerar_arquivo_teste(nome_arquivo, tamanho):
    with open(nome_arquivo, 'w') as f:
        for _ in range(tamanho):
            num = random.randint(1, 10000)
            f.write(f"{num}\n")

def dividir_arquivo(arquivo_fonte, tamanho_bloco, pasta_temporaria):
    """Divida o arquivo grande em blocos menores"""
    with open(arquivo_fonte, 'r') as f:
        contador = 0
        linha = f.readline()
        while linha:
            bloco = []
            for _ in range(tamanho_bloco):
                if not linha:
                    break
                bloco.append(int(linha.strip()))
                linha = f.readline()
            bloco.sort()
            arquivo_temp = os.path.join(pasta_temporaria, f'bloco_{contador}.txt')
            with open(arquivo_temp, 'w') as f_temp:
                for num in bloco:
                    f_temp.write(f"{num}\n")
            contador += 1
    return contador 

def merge_arquivos(arquivos, arquivo_saida):
    """Mescla os arquivos temporários em um arquivo final ordenado"""
    open_files = [open(arquivo, 'r') for arquivo in arquivos]
    min_heap = []
    for i, f in enumerate(open_files):
        linha = f.readline()
        if linha:
            heapq.heappush(min_heap, (int(linha.strip()), i))
    with open(arquivo_saida, 'w') as f_saida:
        while min_heap:
            valor, index = heapq.heappop(min_heap)
            f_saida.write(f"{valor}\n")
            linha = open_files[index].readline()
            if linha:
                heapq.heappush(min_heap, (int(linha.strip()), index))
    for f in open_files:
        f.close()

def merge_sort_externo(arquivo_fonte, arquivo_saida, tamanho_bloco=10000):
    """Função principal que executa o MergeSort Externo"""
    pasta_temporaria = 'temp'
    os.makedirs(pasta_temporaria, exist_ok=True)
    num_blocos = dividir_arquivo(arquivo_fonte, tamanho_bloco, pasta_temporaria)
    arquivos_temporarios = [os.path.join(pasta_temporaria, f'bloco_{i}.txt') for i in range(num_blocos)]
    merge_arquivos(arquivos_temporarios, arquivo_saida)
    for arquivo in arquivos_temporarios:
        os.remove(arquivo)
    os.rmdir(pasta_temporaria)

gerar_arquivo_teste('arquivo_grande.txt', 1000000)
merge_sort_externo('arquivo_grande.txt', 'arquivo_ordenado.txt')