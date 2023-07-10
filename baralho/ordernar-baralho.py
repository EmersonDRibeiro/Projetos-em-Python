def mostrar_cartas_em_ordem_decrescente(baralho):
    baralho_ordenado = sorted(baralho, reverse=True)  # Ordena o baralho do maior para o menor
    
    for carta in baralho_ordenado:
        print(carta)

# Exemplo de uso
baralho = [5, 2, 9, 1, 7]  # Exemplo de um baralho de cartas
mostrar_cartas_em_ordem_decrescente(baralho)
