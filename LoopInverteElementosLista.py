#Lista
my_list = [10, 1, 8, 3, 5]

#atribuímos a variável length com o comprimento da lista atual
length = len(my_list)


#lançamos o loop for para correr através do seu corpo length // 2 vezes 
#(isto funciona bem para listas com comprimentos pares e ímpares, 
#porque quando a lista contém um número ímpar de elementos, o do meio permanece intocado)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)
