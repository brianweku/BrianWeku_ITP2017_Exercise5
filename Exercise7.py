def a(x):
    def b():
        print("what is 5-4")
        x()
        print("Niceeeee!!")
    return b()
@a
def v():
    print(5-4)
