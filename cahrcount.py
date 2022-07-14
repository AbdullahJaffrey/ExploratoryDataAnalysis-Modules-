def charcount(para):
    return len([i for i in para if i !=" "])


def spacecount(para):
    #string = 'Hello world, enter a string'
    return len([i for i in para if i ==" "])

def splitcount(para):
    return len([i for i in para.split(',')])

def totalcount1(para):
    return len([i for i in para.split(' ')])

def indexfinder(para):
    return para.find('Hello')