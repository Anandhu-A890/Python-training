s="anagram"
t="nagaram"
def anagram(s,t):
    if len(s)!=len(t):
        return False
    return sorted(s)==sorted(t)

print("Output",anagram(s,t))