def outer():
    n=5
    def inner():
        nonlocal n
        n+=1
        print(n)

    return inner

fn=outer()
fn()

def mult(n):
    def inn(x): return n*x

    return inn
fm=mult(5)
print(fm(8))

t=(1,2,[30,40])
t[2].extend([50,60])
print(t)



