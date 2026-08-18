def count_char(sentence):
    vowels="aeiouAEIOU"
    vowel=0
    consonants=0
    digit=0
    for i in sentence:
        if i in vowels:
            vowel+=1
        elif i.isalpha() and i not in vowels:
            consonants+=1
        elif i.isdigit():
            digit+=1
    return vowel,consonants,digit
sentence=input("Enter sentence: ")
v,c,d=count_char(sentence)
print("Vowels: ",v)
print("Consonants: ",c)
print("Digits: ",d)
