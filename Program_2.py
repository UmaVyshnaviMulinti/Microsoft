def interleave(str1, str2):
    str = ''.join(A+B for A,B in zip(str1, str2))
    #A1A2A3A4
    if len(str1)>len(str2):
        str+=str1[len(str2):]
        #str1=AAAA=4
        #str2=1234567=7
        #str=str+str1[len(str2):]
    else:
        str+=str2[len(str1):]
    return str