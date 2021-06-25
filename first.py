#!/usr/bin/env python3
print('hellow')
a='ggggg'
b=33
print(a,b, sep=":",end="\n... ... ... ")

dd=input("dont stop learning ")
print(dd);

arr=[1,2,3]
print(arr)
print(arr[2])

# arr.extend(5) cant be ints cant iterate unless and list
arr.extend("abc")
print(arr)

proto2 = [ 22, 80, 443, 53 ]

arr.append(proto2)

print(arr)

arr2 = arr

arr2.extend(proto2)

print(arr2)