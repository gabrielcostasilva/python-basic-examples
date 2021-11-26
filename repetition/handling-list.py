keepGoing = True
sentences = []

while keepGoing:
    print("Currently, there are {} sentences".format(len(sentences)))
    sentences.append(input("Enter your sentence: ").strip())
    keepGoing = bool(input("Would you like to keep going? (True/False): "))
else:
    print("These are the {} sentences".format(len(sentences)))
    for i in range(len(sentences)):
        print("{} - \'{}\'".format(i, sentences[i]))


