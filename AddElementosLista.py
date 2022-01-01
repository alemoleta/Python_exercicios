#Adicionando elementos a uma lista com métodos append e insert

numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###usando o método .append
#Toma o valor do seu argumento e coloca-o no final da lista que possui o método.
#O comprimento da lista aumenta então em um.

numbers.append(4)

print(len(numbers))
print(numbers)

###usando o método .insert
#Pode acrescentar um novo elemento em qualquer lugar da lista

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

#
numbers.insert(1, 333)
print(len(numbers))
print(numbers)
