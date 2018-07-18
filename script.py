#namespace example

def outer_function():
    global a
    a = 20
    print("outer")
    def inner_function():
        global a
        a = 30
        print('a =',a)
        print("inner")

    inner_function()
    print('global a =',a)
     
a = 10
outer_function()
print('a =',a)
print("hello world")
