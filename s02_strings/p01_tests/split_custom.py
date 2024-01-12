def mysplit(strng):
    split_words = []
    strng = strng.strip()
    strng += ' '
    word = ''
    
    for char in strng:
        if not char.isspace():
            word += char
        
        else:
            if len(word) > 0:
                split_words.append(word)
                word = ''
    
    return split_words
            
            

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
