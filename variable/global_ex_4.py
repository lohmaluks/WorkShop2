x = "awsome"

def myfunc():
    global x
    print("[-] Python is" + x)
     x = "fantastic"

    myfunc()
    print("Python is" + x)