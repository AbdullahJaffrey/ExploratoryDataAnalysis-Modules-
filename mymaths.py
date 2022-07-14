def addition(*num):
    '''
    It can take arbitrary arguments.
    
    '''
    if len(num) == 0:
        return 'atleast two parameters required'
    else:
        return sum(num)

def exponent(num,exp):
    return num**exp