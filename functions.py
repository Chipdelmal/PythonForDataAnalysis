############################################################################
# Functions
############################################################################

import re
import itertools
from functools import partial

def myFunction(x,y,z=1.5):
    if z>1:
        return z*(x+y)
    else:
        return z/(x+y)

myFunction(5,6,z=.7)
myFunction(3.14,7,3.5)
myFunction(10,20)
myFunction(x=1,y=2,z=3)

def f():
    a=5
    b=6
    c=7
    return a,b,c
i,j,k=f()
print(i,j,k)
returnValue=f()
print(returnValue)

def fDict():
    a=5
    b=6
    c=7
    return {"a":a,"b":b,"c":c}
dictionaryTemp=fDict()
dictionaryTemp["a"]

def cleanStrings(strings):
    result=[]
    for value in strings:
        value=value.strip()
        value=re.sub("[!#?]","",value)
        value=value.title()
        result.append(value)
    return result

states=[
    "    Alabama","Georgia","Georgia!","georgia",
    "FlOrida","shouth    Carolina###","West Virginia?"
]
cleanStrings(states)

def removePunctuation(string):
    return re.sub("[!#?]","",string)
cleanOperations=[str.strip,removePunctuation,str.title]

def cleanStrings(strings,operations):
    result=[]
    for value in strings:
        for function in operations:
            value=function(value)
        result.append(value)
    return result
cleanStrings(states,cleanOperations)

map(removePunctuation,states)

def cleanStringsMap(cleanStringsOperations,statesList):
    tempCleanStrings=states
    for x in cleanOperations:
        tempCleanStrings=map(x,tempCleanStrings)
    return tempCleanStrings

cleanStringsMap(cleanOperations,states)
def lambdaFunction(x):
    return x*2

shortFunction=lambda x: x*2
shortFunction(2)


map(lambda x: x*2,[4,0,1,5,6])

strings=["foo","card","bar","aaaa","abab"]
strings.sort(key=lambda x:len(set(list(x))))
strings


def addNumbers(x,y):
    return x+y
listOfNumbers=[1,2,3,4,5]
addFive=lambda y:addNumbers(5,y)
map(addFive,listOfNumbers)

def squares(n=10):
    print("Generating squares from 0 to {0}".format(n**2))
    for i in range(0,n):
        yield i ** 2

gen=squares()
gen
for x in gen:
    print(x)

gen = (x ** 2 for x in range(100))
def _make_gen():
    for x in range(100):
        yield x**2
gen = _make_gen()

for i in gen:
    print(i)

dict((i,i**2) for i in range(10))

names=["Alan","Adam","Wes","Will","Albert","Steven"]
firstLetter=lambda x:x[0]
for letter, names in itertools.groupby(names,firstLetter):
    print(letter,list(names))
