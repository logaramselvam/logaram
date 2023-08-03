class Parent:
    def myfun_p(self):
         print ("Parent Class")
class Child (Parent):
     def myfun_c(self):
          print ("Child Class")


obj = Child()
obj.myfun_p()
obj.myfun_c()