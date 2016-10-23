# while loop

l = (1,2,3,4,5)
i = 0
sum = 0
while (i < len(l)):
    sum += l[i]
    i = i+1

print sum

# for loop
sum = 0
i = 0
for i in range(len(l)):
    sum += l[i]
    
print sum