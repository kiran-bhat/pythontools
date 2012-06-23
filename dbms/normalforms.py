import dbfunctions
print "Program to find normal form of a database schema given all its functional dependencies"
print "Author: kiran19882004@gmail.com"
print "Enter dependencies in following format"
print "A->B,C;D->A;X,Y->Z"
data = raw_input("Data: ")
inputs=data.split(';')
dictonary={}
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
tracer=raw_input("Enter which candidate key (use comma separation if you need a composite key)")
if dbfunctions.isTwoNF(dictonary,tracer):
    print "2NF!!!"
else:
    print "Not in 2NF"
