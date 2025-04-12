import random
def ishuzhi(a, b):
    if a > b:
        temp = a
        a = b
        b = temp
    b=b%a
    if b==0:
        return a
    else: return ishuzhi(b,a)
i = random.randint(1, 100)
print(f"{i=}")
j = random.randint(1, 100)
print(f"{j=}")
k=ishuzhi(i,j)
print(f"{k=}")
if(k==1):
    print("互质")
else:
    print("不互质")


