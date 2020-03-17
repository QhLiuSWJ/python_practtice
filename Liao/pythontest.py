import threading
class TestA:
    def __init__(self):
        pass
    def PA(self):
        print("testA print")

class TestB ( TestA ):
    def __init__(self):
        pass
    def PA(self):
        print("testB print")
class TestC(TestA):
    def __init__(self):
        pass
    def PA(self):
        print("testC print")
class TestD(TestC ,TestB):
    def __init__(self):
        pass


A = TestA()
A.name = ' 1 '
print(A.name)

print(threading.current_thread())

