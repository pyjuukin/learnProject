
def reverse(self, x: int) -> int:
    for i in range(len(x)):
        if i == 0:
            del(x[i])
    y = reversed(x)
    return y
    
reverse(1232)