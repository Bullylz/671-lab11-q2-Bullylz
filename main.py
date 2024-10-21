# YOUR CODE HERE
n = int(input())
lst1 = []
lst2 = []
summa = []
def values(n):
    for i in range(n):
        val = int(input())
        lst1.append(val)
    for j in range(n):
        val2 = int(input())
        lst2.append(val2)
    return lst1,lst2

def summation(lst1,lst2):
    for k in range(n):
        summat = int(lst1[k])+int(lst2[k])
        summa.append(summat)
    return summa

def find_min_max(summa):
    summasort = sorted(summa)
    a = summa[0]  #น้อยสุด
    b = summa[-1] #มากสุด
    return a,b
    # for i in range(n):
    #     if b>summa[i]:
    #         b = summa[i] #update ถ้าเจอค่าน้อยกว่า
    #     if a<summa[i]:
    #         a = summa[i] #update ถ้าเจอค่าเยอะกว่า
    # return b,a

values(n)
summation(lst1,lst2)
min_val,max_val = find_min_max(summa)
print(summa)
print((min_val,max_val))
