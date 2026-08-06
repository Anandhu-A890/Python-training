# s=input("Enter your first word:")
# t=input("Enter your second word:")
# print("Let's check if your two words are anagram or not")
# def anagram(s,t):
#     if len(s)!=len(t):
#         return False
#     return sorted(s)==sorted(t)

# print("Output:",anagram(s,t))

from collections import Counter

s = input("Enter your first word: ")
t = input("Enter your second word: ")

def anagram(s, t):
    return Counter(s) == Counter(t)

print("Output:", anagram(s, t))