import sys
print "Program to find closure of an element in a given set of functional dependencies"
print "Author: kiran19882004@gmail.com"
print "Enter dependencies in following format"
print "A->B,C;D->A;X,Y->Z"
data = raw_input("Data: ")
inputs=data.split(';')
dictonary={}
def issubset(a,b):
    r=a.split(',')
    for i in r:
        if not i in b:
            return False
    return True
def traverse(t):
    px=[]
    px.extend(t)
    for k, v in dictonary.iteritems():
        if issubset(k,t):
            for d in v:
                if not d in px:
                    px.append(d)
    return px

def find_closure(ele):
    arr=[]
    for e in ele.split(','):
        arr.append(e)
        newarr=traverse(arr)
        while not sorted(newarr) == sorted(arr):
            arr=newarr
            newarr=traverse(arr)
        return newarr

for i in inputs:
    if i !='':
        p=[]
        items=i.split('->')
        if len(items)==2:
            for x in items[1].split(','):
                p.append(x)
            if items[0]not in dictonary:
                dictonary[items[0]]=p
            else:
                dictonary[items[0]].extend(p)
        else:
            raise NameError("Invalid input string")
if(len(dictonary)==0):
    raise NameError("Invalid input string")
tracer=raw_input("Enter which elements closure you require (use comma separation if you need combined closure of multiple elements)")


print find_closure(tracer)
