#cria uma lista com elementos
my_list = [10, 1, 8, 3, 5]

#variável soma de todos os valores armazenados na lista
total = 0

#loop para realizar a soma de cada elemento da lista
for i in range(len(my_list)):
    total += my_list[i]

#apresenta a soma total
print(total)
