def mcd(a,b):
    if b == 0:
        return a
    if a == 0:
        return b
    if a < b:
        a, b = b, a
    c = a%b

    if c==0:
        return b
    return mcd(b,c)

print(mcd(0,5))
