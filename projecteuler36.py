a=[]
for i in range(1,1000000):
    if str(i)[::-1]==str(i) and str(bin(i))[2::]==str(bin(i))[:1:-1]:
        a.append(i)
print(sum(a))
