class person:
    count=0 # class attribute
    def __init__(self, name="guest", age=20): #constructor - use to create class instances
        person.count += 1 # person id automatically incremented
        self.pid=person.count
        self.name=name
        self.age=age
        
    def display(self):
        print(f"Person{self.pid} Name: {self.name}, Age: {self.age}")
    
