def get_name_and_decades(name, age):
    print(f"My name is {name} and I'm {age / 10:.5f} decades old.")

get_name_and_decades("Leo", 31)


def f(a, *pargs, **kargs): print(a, pargs, kargs)
f(1, 2, 3, x=4, y=5)