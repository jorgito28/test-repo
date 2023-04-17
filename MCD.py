def mcd(a,b):
    if a < b:
        a, b = b, a
    c = a%b

    if c==0:
        return b
    return mcd(b,c)

print(mcd(4,6))
