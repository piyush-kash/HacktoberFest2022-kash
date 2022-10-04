def getPhoneNumber(s):
    d1={'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    l=list(s.split(" "))
    lres=[]
    for i in range(len(l)):
        if l[i]=='double':
            for j in range(1):
                lres.append(d1[l[i+1]])
        elif l[i]=='triple':
            for j in range(2):
                lres.append(d1[l[i+1]])
        else:
            lres.append(d1[l[i]])            
    strlist=''.join(map(str,lres))
    return strlist

s = input()
result = getPhoneNumber(s)
print(result)