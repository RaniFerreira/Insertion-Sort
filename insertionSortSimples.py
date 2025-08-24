def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i - 1

        print(f"\nIteração {i}: inserindo {chave}")

        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
            print(f"  Troca: {lista}")

        lista[j + 1] = chave
        print(f"Após inserir {chave}: {lista}")

    return lista


vetor = [7, 2, 4, 1, 5, 3]

print("Lista inicial:", vetor)
print("\nLista final ordenada:", insertion_sort(vetor))
