# Example to show how to define classes

class MyClass:

    # attributes
    attr1 = "value1"
    attr2 = "value2"
 
    # init method or constructor 
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

    # A sample method 
    def getAttr1(self):
        return self.attr1