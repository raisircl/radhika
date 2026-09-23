def add_gracemarks(x):
    grace=0
    if x <=20:
        grace=x+20
    elif x<=50:
        grace=x+10
    elif x<=95:
        grace = x+5
    return grace

marks=[44,22,53,22,11]

gracemarks=map(add_gracemarks,marks)


#gracemarks=[]
#for i in marks:
#    gracemarks.append(i+5)

print(list(gracemarks))


flist=[4,2,6,8,3]
