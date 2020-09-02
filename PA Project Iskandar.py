class ageCal:
    names = []
    age = []
    agelist = 0

    def init(self):
        pass

    def readData(self):
        file = open("listOfStudentage.txt",'r')
        read = file.readlines()
        print(read)

        for items in read:
            list1 = items.rstrip('\n')
            list2 = list1.split(',')
            self.names.append(list2[0])
            self.age.append(list2[1])

        userinputName = str(input('Enter new student name: '))
        userinputAge = input('Enter student Age (in years and months): ')

        while userinputAge.isnumeric() == False:
            userinputAge = input('Enter student Age (in years and months): ')

        self.names.append(str(userinputName))
        self.age.append(float(userinputAge))

        print(self.names)
        print(self.age)

    def calAverage(self):
        self.agelist = len(self.age)
        totalAge = 0
        for number in self.age:
            totalAge = int(totalAge) + int(float(number))
        return int(totalAge/self.agelist)


classinstance = ageCal()
classinstance.readData()
print( "Average age is:", classinstance.calAverage(), "for", classinstance.agelist ,'of student')