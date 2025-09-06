
# Method 1
'''
dict = {}

person_1 = input("Enter first person name: ")
lang1 = input("Enter your favourite language: ")

person_2 = input("Enter second person name: ")
lang2 = input("Enter your favourite language: ")

person_3 = input("Enter third person name: ")
lang3 = input("Enter your favourite language: ")

person_4 = input("Enter fourth person name: ")
lang4 = input("Enter your favourite language: ")

dict[person_1] = lang1
dict[person_2] = lang2
dict[person_3] = lang3
dict[person_4] = lang4

print(dict)

'''



# Method 2

dict2 = {}

for x in range(4):
    name = input("Enter your name: ")
    language = input("Enter your favourite language: ")
    dict2[name] = language

print(dict2)
