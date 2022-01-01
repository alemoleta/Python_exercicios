my_list = []  # Creating an empty list.

#populando lista
for i in range(5):
    my_list.append(i + 1)

print(my_list)

my_list = []  # Creating an empty list.

#populando lista na mesma sequência, mas em ordem inversa
for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)

