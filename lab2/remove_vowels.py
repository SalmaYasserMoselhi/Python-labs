def remove_vowels(str):
    vowels = "aeiouAEIOU"
    res = ""
    
    for ch in str:
        if ch not in vowels:
            res += ch
    
    return res

print(remove_vowels("mobile"))
print(remove_vowels("PYTHON"))