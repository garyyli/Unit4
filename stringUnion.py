#Gary Li
#10/20/17
#stringUnion.py

def stringUnion(str1,str2):
    totalStr = ''
    totalStr += str1
        
    totalStr +=str2
    finalStr = ''
    for ch in totalStr:
        if ch in str1:
            if not ch in finalStr:
                finalStr += ch
        if ch in str2:
            if not ch in finalStr:
                finalStr+= ch
            
            
    return finalStr
    
print(stringUnion('mississippi','pennsyvania'))