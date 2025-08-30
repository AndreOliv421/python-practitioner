for num in range (1,10):
    print("*")

for nnum in range (1,10):
    print("*")

for num in range(1,10):
    for num2 in range(num):
        print("*", end=" ")
    print("")

"""
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
"""