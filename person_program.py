from person import person

p1 = person("Radhika",20) # p1 is an instance or object of person clas
p1.display() # calling the display method of p1


p2 = person() # p2 is another instance or object of person class
p2.name="Alice"
p2.age=25

p2.display()

print(f"Total persons created: {person.count}")