import Dictionary

print("These are the list of available words to look for: ", Dictionary.d)
print("The dictionary's length is: ", len(Dictionary.d))
translatedphrase = {}
phraseinspanish = []


phraseinenglish = (input("Provide the phrase in English (in lowercase): "))
setofwords = phraseinenglish.split(" ")

for c in setofwords:
    phraseinspanish.append(Dictionary.d.get(c))

print("Phrase in English: ", phraseinenglish, "\nPhrase translated to Spanish: ", *phraseinspanish)









