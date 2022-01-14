#Write a function to verify if two strings are anagrams.  
#Strings are anagrams if they contain the same letters and the letters occur with the same frequency.

def is_anagram(string1,string2):
    if len(string1) != len(string2):
        return False
    return sorted(string1) == sorted(string2)

print(is_anagram("a gentleman", "elegant man"))