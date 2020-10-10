# Mario
height = int(input("Height: "))

# Mario: Media piramide derecha
print("Media piramide derecha \n")
for i in range(height):
    for j in range(i):
        print("#", end="")
    print()

# Mario 2: Media piramide izquierda
print("Media piramide izquierda \n")
for i in range(height):
    for j in range(height - (i + 1)):
        print("", end=" ")
        

    for j in range(i):
        print("#", end="")
    print()

# Mario 3: Media pirámide doble
print("Media pirámide doble \n")
for i in  range(height):

    for j in range(height - (i + 1)):
        print(" ", end="")

    for j in range(i):
        print("#", end="")
    print("  ", end = "")

    for j in range(i):
        print("#", end = "")

    print()    


print("This CS50")