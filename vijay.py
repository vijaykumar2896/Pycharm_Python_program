def test(x):
    print(x)
    if x%3==0 : return test (x/3)
    if x%2==2: return x
    return test(2*x+1)

test(2)