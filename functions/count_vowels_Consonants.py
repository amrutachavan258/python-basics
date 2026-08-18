def count_vowels(text):
    vowels="aeiouAEIOU"
    count_v=0
    count_c=0
    for i in text:
        if i in vowels:
            count_v+=1
        else:
            count_c+=1
    return count_v,count_c
my_String="Samartha Ashish Chavan"
vowels,consonants=count_vowels(my_String)
print("vowels:",vowels)
print("consonants:",consonants)
