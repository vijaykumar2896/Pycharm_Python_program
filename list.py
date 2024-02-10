def interchange_first_last(newlist):
    size = len(newlist)
    temp=newlist[0]
    newlist[0]=newlist[-1]
    newlist[-1]=temp
    return newlist


newlist=[1,2,3,4,5,6]
print(interchange_first_last(newlist))