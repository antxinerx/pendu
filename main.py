f = open('truc.txt', 'r')
contenu = f.read()
word = []
for l in contenu:
    word.append(l)
guessword = []
for e in word:
    guessword.append("_")
print(guessword)
f.close()

while guessword.count("_") > 0:
    user_input = input("take a guess")
    index = 0
    while index < len(word):
        if user_input == word[index]:
            guessword[index] = word[index]
        index +=1
    print(guessword)