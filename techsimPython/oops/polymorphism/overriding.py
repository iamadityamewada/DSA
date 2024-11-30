class A:
    def method_a(self):
        print("method a from class A")
class B(A):
    def method_a(self):
        print("method a from class B")

obj =  B()

obj.method_a()
