#=========FURRO404=========#
#Bad_Enigma_Machine.py
characters = []
bruh = []
while True:
    oof = int(input("1 for Encoding\n2 for Decoding\nChoice ~ "))
    if oof == 1:
        keys = {
            "j" : "a",    
            "c" : "b",    
            "a" : "c",    
            "i" : "d",    
            "t" : "e",
            "g" : "f",    
            "v" : "g",   
            "p" : "h",    
            "l" : "i",    
            "k" : "j",    
            "s" : "k",    
            "h" : "l",    
            "d" : "m",   
            "e" : "n",    
            "r" : "o",    
            "q" : "p",    
            "z" : "q",    
            "w" : "r",    
            "o" : "s",    
            "u" : "t",    
            "b" : "u",    
            "m" : "v",    
            "n" : "w",    
            "y" : "x",    
            "f" : "y",
            "x" : "z",
            " " : " ",
            "?" : "?",
            "." : ".",
            "," : ","
            }
    elif oof == 2:
        keys = {
            "a" : "j",
            "b" : "c",
            "c" : "a",
            "d" : "i",
            "e" : "t",
            "f" : "g",
            "g" : "v",
            "h" : "p",
            "i" : "l",
            "j" : "k",
            "k" : "s",
            "l" : "h", 
            "m" : "d",
            "n" : "e",
            "o" : "r",
            "p" : "q",
            "q" : "z",
            "r" : "w",
            "s" : "o",
            "t" : "u",
            "u" : "b",
            "v" : "m",
            "w" : "n",
            "x" : "y",
            "y" : "f",
            "z" : "x",
            " " : " ",
            "?" : "?",
            "." : ".",
            "," : ","
            }
#--------------------------------------#

    string = input("\n\n\nEnter String: ")
    length = len(string)

    number = 0
    for i in range (0, length):
        character = string[number]
        characters.append(character)
        number = number + 1
        
    number = 0
    
    for i in range (0, length):
        choose = characters[number]
        a = keys[choose]
        bruh.append(a)
        number = number + 1
        
    def listToString(bruh):  
        str1 = ""  
        for ele in bruh:  
            str1 += ele   
        return str1  
        s = bruh
    
    print(listToString(bruh))
    print("\n\n")
    characters.clear()
    bruh.clear()
#=========FURRO404=========#
