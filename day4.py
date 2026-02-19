# str1 = input("Enter the text: ")
# str2 = input("Enter the string: ")

# if len(str1) == len(str2):
#     if sorted(str1) == sorted(str2):
#         print("It is an anagram")
#     else:
#         print("It is not an anagram")
# else:
#     print("It is not an anagram")


# #length of the last wor
# a="Hello World"
# a.strip()
# a.split
# print(len(a[-1]))

# a = [1, 2, 3, 4]
# b = [1, 7, 8, 3]
# res = []

# for i in a:
#     if i in b and i not in res: 
#         res.append(i)

# print(res)

# #union
# a = [1, 2, 3, 4]
# b = [1, 7, 8, 3]

# res = []
# for i in a:
#     if i not in res:
#         res.append(i)
# for i in b:
#     if i not in res:
#         res.append(i)
#print(res)

# from itertools import combinations
# players=['A','B','C']
# for combo in combinations(players,2):
#     print(combo)

# from itertools import permutations
# players=[1,2,3]
# for perm in permutations(players,2):
#     print(perm)

# from itertools import combinations

# def combine(n, k):
#     numbers = list(range(1, n+1))      
#     comb = combinations(numbers, k)    
#     return [list(c) for c in comb]     

# print(combine(4, 2))

#multiple digits to single digits
num=int(input("Enter the value :"))
print(1+(num-1)%9)



