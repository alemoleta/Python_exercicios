my_list = []
swapped = True
num = int(input("How many elements do you want to sort: ")) #interação com usuário que vai dizer quantos elementos terá a lista

# usuário dará entrada nos elementos 
for i in range(num):
    val = float(input("Enter a list element: "))
    my_list.append(val)

# ordenação da lista com algoritmo bubble sort
while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)
