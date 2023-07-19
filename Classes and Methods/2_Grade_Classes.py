class Students:
    def __init__(self,first,last):
        self.first=first
        self.last=last
    def gradeinput(self,ng):
        self.ng=ng
        self.Grades=[]
        for i in range(0,ng,1):
            gd=float(input("please enter the grade"))
            self.Grades.append(gd)
        return self.Grades
    def printgrades(self):
        for i in range(0,self.ng,1):
            print("\nGrades = ",self.Grades[i])
    def avggrades(self):
        tot=0
        for i in range(0,self.ng,1):
            print(i)
            tot=tot+self.Grades[i]
        return (tot/self.ng)
        
Student1=Students("Gani","GANISHVAR")
Student2=Students("Dharun","Vinayak")
##print(Student1.first,Student1.last)
gradess=Student1.gradeinput(2)
print(gradess)
Student1.printgrades()
##print(Student1.Grades)
print(Student1.avggrades()) 