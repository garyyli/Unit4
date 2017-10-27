#Gary Li
#10/27/17
#warmup12.py

def GCF(x,y):
    maxNum = max(x,y)
    for i in range(maxNum,1,-1):
        if x%i==0 and y%i==0:
            return i

print(GCF(14,7))
