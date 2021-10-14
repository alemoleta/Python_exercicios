# Programa que lê uma palavra e apresenta os caracteres excetuando as vogais
# Exercício item 3.2.1.10 do curso de Python Fundamentos da Cisco

# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input("Digite uma palavra: ")

user_word = user_word.upper()

for letter in user_word:
    # Complete the body of the for loop.
    if letter == "A" :
        continue
    elif letter == "E" :
        continue
    elif letter == "I" :
        continue
    elif letter == "O" :
        continue
    elif letter == "U" :
        continue
    else :
        print (letter)

print ("Fim do programa")
