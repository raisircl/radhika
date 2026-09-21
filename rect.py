class Rect:
    count=0
    def __init__(self):
        Rect.count+=1
        print(f"Rect{Rect.count} Object Created")
        #self represent the current object of the class
        self.l=0 # here l and b instance attribute of the class 
        self.b=0
    def area(self):
        return self.l*self.b
    def display(self):
        print(f"Rect{Rect.count} Dimension {self.l}x{self.b}")
        
