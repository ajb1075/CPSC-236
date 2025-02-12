def abs_value(x):
    if x < 0:
        return -x
    return x

def is_pos(x):
    x = int(x)
    if x > 0:
        return "positive"
    elif x < 0:
        return "negative"
    else:
        return "zero"

print(str(abs_value(10))+'\n'+str(abs_value(-10))'\n\n')

print(is_pos(1)+'\n'+is_pos(-1)+'\n'is_pos(0))
