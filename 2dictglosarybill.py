

# or
a={ "milk":32,'sugar':200,"rice":60}
b={"milk":3,'sugar':2,'rice':2}
c={}
p=a.values()
q=b.values()
for p,q in a,b:
    i=b.keys()
    c[i]=(p*q)
print(c)
print(sum(c.values()))


