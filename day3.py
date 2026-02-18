# #fibonacci series
# n=int(input("Enter the limit:"))
# a=0
# b=1

# for i in range (n):
#     print(a, end=" ")
#     temp = a + b
#     a = b
#     b = temp

#List
#list idices
#list slicing
#list method
#list operation
#map,filter and reduce

# #list indices
# list=[1,2,3,4,5,6]
# print(list[4])

# #list slicing
# #syntax  [start index(include):end index(exclide)]
# print(list[1:4])
# print(list[:4])
# print(list[0:])
# print(list[-7:-1])

# #List operators
# # 1)concatenation operator(1)
# a=[1,2,3,4]
# b=[5,6,7]
# print(a+b)

# #realtive usage
# #2)repitation operator
# num=[1,2,3,4]
# print(num*3)

# #3)membership operator 
# fruit=["apple","banana","orange"]
# print("apple"in fruit)
# print("graps"not in fruit)

# #comparition operators
# list1=[1,2,3,4]
# list2=[5,6,7,89,9]
# print(list1==list2)
# print(list1<list2)

# #list methods

# #1)append
# num=[1,2,3,4]
# num.append(4)
# print(num)

# #2) insert
# # syntax(index,item)
# num=[1,2,3,4]
# num.insert(2,5)
# print(num)

# #3)extend
# a=[1,2]
# b=[3,4]
# b.extend(a)
# print(b)
# a.extend(b)
# print(a)

# #remove
# num=[1,2,3,4,5,6]
# num.remove(2)
# num.remove(6)
# print(num)

# #pop-give index value
# num=[10,20,30,40,50]
# num.pop(4)
# print(num)

# #clear
# num=[10,20,30,40]
# num.clear()
# print(num)

# #index
# num=[10,20,30,40,50]
# print(num.index(30))#return  index position
# print(num[2])#return index value

# #count
# num=[10,20,30,40,50]
# print(num.count(50))

# #sort
# num=[10,20,30,40,50,55,45,67,89]
# num.sort()
# print(num)
# num.sort(reverse=True)
# print(num)

# #reverse
# num=[10,20,30,40,50]
# num.reverse()
# print(num)

# #copy
# num=[10,20,30,40,50]
# b=num.copy()
# print(b)

# #should use it on list
# num=[10,20,30,40,50]
# result=list(map(lambda x:x*2,num))
# print(result)

# #without using lambda
# num=[10,20,30,40,50]
# def funct(x):
#     return x*2
# result=list(map(funct,num))
# print(result)

# #filter with lambda
# num=[1,2,3,4,5,6,7,8,9,0,11,12,13,14,15]
# result=list(filter(lambda x:x%2,num))
# print(result)

# #without lambda
# num=[1,2,3,4,5,6,7,8,9,0,11,12,13,14,15]
# def funct(x):
#     return x%2==0
# result=list(filter(funct,num))
# print(result)

# #reduce-->convert into single value-->python functool module
# from functools import reduce
# num=[1,2,3,4,5,6]
# result=reduce(lambda a,b:a+b,num)
# print(result)

# #print even no
# from functools import reduce
# num=[1,2,3,4,5,6,7,8,9,0,11,12,13,14,15]
# result=list(filter(lambda x:x%2==1,num))
# result2=list(filter(lambda x:x%2==0,num))
# result1=reduce(lambda a,b:a+b,result)
# result3=reduce(lambda a,b:a+b,result2)
# print("___________ODD  NUMBER__________")
# print(result)
# print("Sum of Odd numbers",result1)
# print("___________EVEN NUMBER__________")
# print(result2)
# print("Sum of even number:",result3)


# #palindrom
# #list method
# word=input("Enter the text:")
# palindrom=word[::-1]
# if(word==palindrom):
#     print("Its a palindrome")
# else:
#     print("Its not a palindrome")

# #without slice
# word=input("Enter the text:")
# rev=""
# for ch in word :
#     rev=ch+rev
# if(word==rev):
#     print("Its a palindrome")
# else:
#     print("Its not a palindrome")

# #palidrome for numbers
# num=int(input("enter the number:"))
# original=num
# rev=0
# while num>0:
#     digits=num%10
#     rev=rev*10+digits
#     num=num//10
# if(original==rev):
#     print("Its a palindrome")
# else:
#     print("Its not a palindrome")