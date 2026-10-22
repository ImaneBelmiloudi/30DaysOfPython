# Iterate 0 to 10 using for loop
for i in range(11):
    print(i)
# do the same using while loop
i=0
while i <= 10:
    print(i)
    i+=1

# Iterate 10 to 0 using for loop
for i in range(10,-1,-1):
    print(i)

i=10
while i >= 0:
    print(i)
    i -=1

i=1
while i <= 7:
    print("#" * i)
    i+=1

for i in range (8):
    for j in range(8):
        print("#",end="")
    print()


liste = ['Python', 'Numpy','Pandas','Django', 'Flask']
for list in liste:
    print(list)