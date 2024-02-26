class A:
    def class_a_method(self):
        print("This is class A method")
        
    def Hello(self):
        print("Hello from class A")
        
class B:
    def class_b_method(self):
        print("This is class B method")
        
    def Hello(self):
        print("Hello from class A")
        
class C(A,B):
    pass
        
instanceA = A()
instanceA.class_a_method()
# instanceA.class_b_method()

instanceB = B()
# instanceB.class_a_method()
instanceB.class_b_method()

instanceC = C()            #As we have inherited both class A and B methods from both classes run
instanceC.class_a_method()
instanceC.class_b_method()

instanceC.Hello()

# To find method order resolution 
help(instanceC)
C.mro()
C.__mro__


