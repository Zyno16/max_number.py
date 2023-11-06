large_so_far = -1
print ("before",large_so_far)
for num in [0,12,1,32,15,85,10]:
    if num > large_so_far:
       large_so_far = num
       print("the big number = " ,large_so_far)
print("aftethe last decision =",large_so_far)
