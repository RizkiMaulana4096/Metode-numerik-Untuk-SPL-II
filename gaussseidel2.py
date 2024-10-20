from numpy import array
a = array([[2,1],[1,3]], float)
b = array([5,5], float)
n = 1000
s = 0
x = 0
y = 0
e = 0.05

#perhitungan error
def check(x,y):
    p1 = 5 - a[0,0]*x - a[0,1]*y
    if p1 < 0:
        e1 = -p1
        return e1
    else:
        e1 = p1
        return e1
def check2(x,y):   
    p2 = 5 - a[1,0]*x - a[1,1]*y
    if p2 < 0:
        e2 = -p2
        return e2
    else:
        e2 = p2
        return e2
#koefisien relaksasi 
r = 1
t = 1

#iterasi gauss_seidel
while (check(x,y)> e or check2(x,y)> e) and n >= s:
    c1 = (5-y)/2
    l1 = r*c1+(1-r)*x
    x = l1
    print(x)
    c2 = (5-x)/3
    l2 = t*c2+(1-t)*y
    y = l2
    print(y)
    print("---")
    s += 1

print('')
print(x)
#solusi x
print(check(x,y))
#error dari x yang diperoleh
print(y)
#solusi y
print(check2(x,y))
#error dari y yang diperoleh