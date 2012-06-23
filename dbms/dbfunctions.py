class DBError(Exception):
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return repr(self.value)
def issubset(a,b):
    r=a.split(',')
    for i in r:
        if not i in b:
            return False
    return True
def traverse(t,dictonary):
    px=[]
    px.extend(t)
    for k, v in dictonary.iteritems():
        if issubset(k,t):
            for d in v:
                if not d in px:
                    px.append(d)
    return px
def validateelements(ele,dictonary):
    keyElements=ele.split(",")
    for keyElement in keyElements:
        if keyElement not in dictonary.iterkeys():
            isInAnyDependency=False
            for k, v in dictonary.iteritems():
                if keyElement in v:
                    isInAnyDependency=True
                if keyElement in k.split(','):
                    isInAnyDependency=True
            if not isInAnyDependency:
                raise DBError("ouch.. input values incorrect")
    
def find_closure(ele,dictonary):
    validateelements(ele,dictonary)
    arr=[]
    for e in ele.split(','):
        arr.append(e)
        
    newarr=traverse(arr,dictonary)
    while not sorted(newarr) == sorted(arr):
        arr=newarr
        newarr=traverse(arr,dictonary)
    return newarr

def getAllElementsInFunctionalDependencies(fd):
    elements=[]
    for k, v in fd.iteritems():
        if k not in elements:
            for y in k.split(','):
                if y not in elements:
                    elements.append(y)
        for x in v:
            if x not in elements:
                elements.append(x)
    return elements
def checkKeyValidity(fd,key):
    validateelements(key,fd)
    if len(find_closure(key,fd))!=len(getAllElementsInFunctionalDependencies(fd)):
        raise DBError("ouch.. key not valid")
def isTwoNF(fd,key):
    checkKeyValidity(fd,key)
    if len(key.split(','))==1:
        return True
    else:
        for keyElement in key.split(','):
            if len(find_closure(keyElement,fd))>1:
                return False
        return True
def isThreeNF(fd,key,require2NFCheck):
        if require2NFCheck:
                if not isTwoNF(fd,key):
                        return False
        else:
                checkKeyValidity(fd,key)
        immediateDependencies=fd[key]
        for dependency in immediateDependencies:
                if len(find_closure(dependency,fd))>1:
                        return False
        return True
