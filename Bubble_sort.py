#Bubble_sort
ar=list(map(int,input('Enter The Numbers into the list:').split()))
print(f'Before Sorting:{ar}')
for i in range(len(ar)-1):
    for j in range(len(ar)-1-i):# 'i' is taken beacuse to avoid the iterations for already sorted elements..
        if(ar[j]>ar[j+1]):
            ar[j],ar[j+1]=ar[j+1],ar[j]
print(f'After Sorting:{ar}')