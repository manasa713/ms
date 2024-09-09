def encrypt(text,s):
    result=""
    for i in range(len(text)):
        char=text[i]
        if(char.isupper()):
           result+=chr((ord(char)+s-65)%27+65)
        else:
            result+=chr((ord(char)+s-97)%27+97)
    return result
text="LIKITH"
s=4
print("text:",text)
print("shift:",str(s))
print("cipher:",encrypt(text,s))
