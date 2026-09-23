class Rect:
    count=0
    def __init__(self):
        Rect.count+=1
        print(f"Rect{Rect.count} Object Created")
        #self represent the current object of the class
        self.__l=0 # here l and b instance attribute of the class 
        self.__b=0

    #def set_length(self,l):
    #    self.__l=l
    #def get_length(self):
    #    return self.__l
    #length=property(get_length, set_length)

    @property
    def length(self):
        return self__l
    @length.setter
    def length(self,l):
        self.__l=l
        
    #def set_breadth(self,b):
    #    self.__b=b

    #def get_breadth(self):
    #    return self.__b

    #breadth=property(get_breadth,set_breadth)
    @property
    def breadth(self):
        return self.__b
    @breadth.setter
    def breadth(self,b):
        self.__b=b
        
    def area(self):
        return self.__l*self.__b

    def display(self):
        print(f"Rect{Rect.count} Dimension {self.__l}x{self.__b}")
        
