import string

list_alpha = list(string.ascii_lowercase)
place = 0
indices = []
final_word = []

word = input("Enter your Plain Text: ")
key = int(input("Enter the key: "))
if key < 0 : print("INVALID INPUT")

else:
    for letter in word:
        for Letter in list_alpha:
            if letter == Letter:
                indices.append(list_alpha.index(Letter))


    while place < key:
        list_alpha.append(list_alpha[0])
        list_alpha.remove(list_alpha[0])
        place = place+1

for index in indices:
    final_word.append(list_alpha[index])

final_word = "".join(final_word)

print(f"The encrypted text is: {final_word}")