from collections import Counter

def substituicao_lru(sequencia_referencia, num_quadros):
    quadros = []
    ultimo_uso = {}  # Dicionário para rastrear o último uso de cada página
    faltas_pagina = 0
    acertos = 0

    print("\nSimulando LRU...")
    for tempo_atual, pagina in enumerate(sequencia_referencia):
        if pagina in quadros:
            # Página já está nos quadros
            acertos += 1
            ultimo_uso[pagina] = tempo_atual  # Atualiza o tempo de uso da página
            status = "ACERTO"
        else:
            # Ocorrência de falta de página
            faltas_pagina += 1
            if len(quadros) < num_quadros:
                # Ainda há espaço
                quadros.append(pagina)
            else:
                # Substituir a página menos recentemente usada
                pagina_lru = min(ultimo_uso, key=ultimo_uso.get)  # Página com menor tempo de uso
                indice_lru = quadros.index(pagina_lru)  # Índice da página LRU nos quadros
                quadros[indice_lru] = pagina  # Substituir a página no índice encontrado
                del ultimo_uso[pagina_lru]  # Remover a página substituída do rastreamento

            status = "FALTA"
            # Adicionar a nova página ao rastreamento
            ultimo_uso[pagina] = tempo_atual
        print(f"Página Referenciada: {pagina} | Quadros: {quadros} | {status}")

    print("\n### Resultado LRU ###")
    print(f"Conteúdo final dos quadros: {quadros}")
    print(f"Total de faltas de página: {faltas_pagina}")
    print(f"Total de acertos de página: {acertos}\n")

def substituicao_fifo(sequencia_referencia, num_quadros):
    quadros = []
    faltas_pagina = 0
    acertos_pagina = 0 
    indice_mais_antigo = 0

    print("\nSimulando FIFO...")
    for pagina in sequencia_referencia:
        if pagina in quadros:
            # Página já está nos quadros
            acertos_pagina += 1
            status = "ACERTO"
        else:
            # Falta de página
            faltas_pagina += 1
            if len(quadros) < num_quadros:
                # Ainda há espaço
                quadros.append(pagina)
            else:
                # Substituir a página mais antiga
                quadros[indice_mais_antigo] = pagina
                indice_mais_antigo = (indice_mais_antigo + 1) % num_quadros  # Avançar para o próximo
            status = "FALTA"

        print(f"Página Referenciada: {pagina} | Quadros: {quadros} | {status}")

    print("\n### Resultado FIFO ###")
    print(f"Conteúdo final dos quadros: {quadros}")
    print(f"Total de faltas de página: {faltas_pagina}")
    print(f"Total de acertos de página: {acertos_pagina}")

# Exemplo
sequencia_referencia = [7, 0, 1, 2, 0, 3, 0, 4]
num_quadros = 3

def main():
    print("### Simulação de Algoritmos de Substituição de Páginas ###")
    sequencia_referencia = list(map(int, input("Informe a sequência de referência de páginas (ex.: 7 0 1 2 0 3 0 4): ").split()))
    num_quadros = int(input("Informe o número de quadros de memória: "))
    
    print("\nEscolha o algoritmo:")
    print("1 - LRU (Menos Recentemente Usado)")
    print("2 - FIFO (Primeiro a Entrar, Primeiro a Sair)")
    escolha = int(input("Digite sua escolha: "))

    if escolha == 1:
        substituicao_lru(sequencia_referencia, num_quadros)
    elif escolha == 2:
        substituicao_fifo(sequencia_referencia, num_quadros)
    else:
        print("Escolha inválida.")

if __name__ == "__main__":
    main()