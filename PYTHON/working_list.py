#4-1. Pizzas:
pizzas=['margerita pizza','chesse corn pizza','panner tandori pizza']
for pizza in pizzas:
    print(f"i like {pizza.title()}.")

print("\n i really love pizza !!")

#4-2. Animals:
pets=['Dog','Cat','fish']
for pet in pets:
    print(f"A {pet.title()} would make a great pet.")

print("\n Any of these animals would make a great pet!")
#4-3. counting to twenty:
number= list(range(1,21))
print("\n 1 to 20 number is here :")
print(number)
#4-4. one million:
num= list(range(1,101))
print("\n 1 to 100 number is here")
print(num)
#4-5.summing a hunderd
print("\n here is min number from 1 to 100")
print(min(num))
print("\n here is max number from 1 to 100")
print(max(num))
print("\n here is max number from 1 to 100")
print(sum(num))
#4-6.odd number
odd=list(range(1,21,2))
print("\n here is odd number from 1 to 20")
print(odd)
#4-7.threes
three=list(range(3,31,3))
print("\n here is multiples of 3")
print(three)
tables = []
for value in range(1,11):
    table = value *3
    print(table)
#4-8.cubes
cubes=[]
print("\n here is cube :")  
for value in range(1,11):
    cube = value **3
    cubes.append(cube)
for cube in cubes:
    print(cube)
#4-10.slices
place=['surat','banglore','dilhi','pune','gokul','aasam']
print("\n the first three place in the list : ")
print(place[:3])
print("\n three place frm the middle if the list are :")
print(place[2:5])
print("\n the last three place in the list :")
print(place[-3:])
#4-11.my pizzas, your pizzas:
my_pizza=['margherita', 'pepperoni', 'farmhouse']
my_friend=my_pizza[:]
my_pizza.append('cheese burst')
my_friend.append('panner tikka')
print("\n My favorite pizza is :")
for pizza in my_pizza:
    print(f"- {pizza}")
print("\n My friend favorite pizza is :")
for pizza in my_friend:
    print(f"- {pizza}")





