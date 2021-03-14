import Dictionary

print("These are the list of available words to look for: ", Dictionary.d)
print("The dictionary's length is: ", len(Dictionary.d))
translatedphrase = {}
phraseinenglish = []

phraseinspanish = (input("Provide the phrase in Spanish (in lower case): "))
setofwords = phraseinspanish.split(" ")

for c in setofwords:
    phraseinenglish.append(Dictionary.d.get(c))

print("Phrase in Spanish: ", phraseinspanish, "\nPhrase translated to English: ", *phraseinenglish)









