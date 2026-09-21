class Student:
    def __init__(self, name="Guest", age=18):
        self.name = name
        self.age = age
        self.grade="NA"        

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"


# hindi, eng, math, sci , sst  
# gettotal(), getpercetnage()
