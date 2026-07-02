# # Ist Method
list=[23,89,56,90,1000,56789]
list.sort()
print("Second largest number in the list is:",list[-2])
# # Second Method
a=[10,20,67,30,98]
largest=a[0]
second=a[0]
for num in a:
    if num>largest:
        second=largest
        largest=num
    elif num>second and num!=largest:
        second=num
print("Second largest number in the list is:",second)
