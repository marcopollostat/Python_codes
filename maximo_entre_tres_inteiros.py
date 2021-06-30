def maximo(a,b,c):
    if (a>b>c) or (a>c>b):
        return a
    if (b>a>c) or (b>c>a):
        return b
    if (c>a>b) or (c>b>a):
        return c
    if (a==b==c):
        return a
    if (a==b>c):
        return a
    if (a==c>b):
        return a
    if (b==c>a):
        return b
    if (a==b<c):
        return c
    if (a==c<b):
        return b
    if (b==c<a):
        return a
        
