#3-1
name=['samiksha','isha','nidhi','ujala']
print(name[0].upper())
print(name[1].upper())
print(name[2].upper())
print(name[3].upper())
#3-2
message=(f"she is my best friend {name[0]}")
message1=(f"she is chudela {name[1]}")
message2=(f"she is my sister {name[2]}")
message3=(f"she is my old friend {name[3]}")
print(message)
print(message1)
print(message2)
print(message3)
#3-4

print(f"\n Dear {name[0].title()} you are invited to dinner.")
print(f"\n Dear {name[1].title()} you are invited to dinner.")
print(f"\n Dear {name[2].title()} you are invited to dinner.")
print(f"\n Dear {name[3].title()} you are invited to dinner.")
#3-5
name[0]='radha'
print(name)
print(f"\n Dear {name[0].title()} you are invited to dinner.")
#3-6
name.insert(0,'samiksha')
print(f"\n Dear {name[0].title()} you are invited to dinner.")
name.insert(2,'om')
print(f"\n Dear {name[2].title()} you are invited to dinner.")
name.append('ashok')
print(f"\n Dear {name[6].title()} you are invited to dinner.")
print(name)
#3-7
print("sorry i am invited only two personl on dinner")

popped_name=name.pop()
print(f"sorry {popped_name.title()} you are not invited for dinner ")
popped_name=name.pop()
print(f"sorry {popped_name.title()} you are not invited for dinner ")
popped_name=name.pop()
print(f"sorry {popped_name.title()} you are not invited for dinner ")
popped_name=name.pop()
print(f"sorry {popped_name.title()} you are not invited for dinner ")
popped_name=name.pop()
print(f"sorry {popped_name.title()} you are not invited for dinner ")
print(name)



#3-8
location=['banglour','rajkot','USA','japan','turkish']
print("\n here is original list :")
print(location)
print("\n here is sort list :")
location.sort()
print(location)
print("\n here is original list :")
print(location)
print("\n here is sorted list :")
print(sorted(location))
print("\n here is original list :")
print(location)
print("\n here is reverse list :")
location.reverse()
print(location)
print("\n here is reverse list :")
location.reverse()
print(location)
print("\n here is sort list :")
location.sort()
print(location)
print("\n here is sort list :")
location.sort()
print(location)
#3-9
print(len(name))


















