#Write a function to verify if two strings are anagrams.  
#Strings are anagrams if they contain the same letters and the letters occur with the same frequency.

def is_anagram(string1,string2):
    letter_count = 0
    for letter in string1:
        for another_letter in string2:
            if letter == another_letter:
                letter_count += 1
                break
    if letter_count == len(string2):
        return True
    else:
        return False

ans = is_anagram("elegant man","a gentleman")
print(ans)