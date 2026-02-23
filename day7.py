# numrow=int(input("Enter the number:"))
# triangle=[]
# for i in range (numrow):
#     row=[1]*(i+1)
#     for j in range(1,i):
#         row[j]=triangle[i-1][j-1]+triangle[i-1][j]
#     triangle.append(row)
# print(triangle)

# s = input("Enter a string: ").strip()

# words = s.split()
# print(words)

# if words:
#     print("Length of last word:", len(words[-1]))
# else:
#     print("Length of last word: 0")

# def roman_to_int(s: str) -> int:
#     roman_values = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
    
#     total = 0
#     prev_value = 0
    
#     # Traverse from right to left
#     for char in reversed(s):
#         value = roman_values[char]
        
#         if value < prev_value:
#             total -= value
#         else:
#             total += value
        
#         prev_value = value
    
#     return total


# if __name__ == "__main__":
#     roman = input("Enter a Roman numeral: ").upper()
#     print("Integer value:", roman_to_int(roman))
word=input("Enter the word:")

def detect_capital(word):
    if word.isupper():
            return True
        
     
    if word.islower():
            return True
        
    if word[0].isupper() and word[1:].islower():
            return True
        
    return False
print("This word is",detect_capital(word))