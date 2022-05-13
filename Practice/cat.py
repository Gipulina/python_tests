
#Exercise : https://replit.com/@aneagoie/OOP-Exercise-Cat


#Given the below class:


class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Joa', 3)
cat2 = Cat('Jil', 2)
cat3 = Cat('Gardfield', 6)
print(cat2.name)
print(cat3.name)
print(cat1.name)

# 2 Create a function that finds the oldest cat
def findOldestCat(*args):
    return max(args)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2       

oldCat = findOldestCat(cat1.age,cat2.age,cat3.age)
print (oldCat)
oldCatName = ''
if oldCat == cat1.age:
    oldCatName = cat1.name
elif oldCat == cat2.age:
    oldCatName = cat2.name
else : oldCatName = cat3.name

print(oldCatName)

print(f'The oldest Cat is {findOldestCat(cat1.age,cat2.age,cat3.age)} years old and was named {oldCatName}.')