def char_locator(str, ch):
    positions = []
    
    for i in range(len(str)):
        if str[i] == ch:
            positions.append(i)
    
    return positions

print(char_locator("This is javaScript", "i"))