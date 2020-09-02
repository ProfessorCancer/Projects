ef
isfloat(x):
try:
    float(x)
    return True
except ValueError:
    return False


class CalUtils:
    names = []
    height = []
    totalStudentHeight = 0
    totalStudentCount = 0

    def filestuff(self):
        file = open("C:\\Users\\Andre\\Desktop\\pa test\\listOfStudentHeight.txt", 'r')
        read = file.readlines()

        for i in read:
            temp = i.rstrip("\n")
            splitlist = temp.split(",")
            self.names.append(splitlist[0])
            self.height.append(float(splitlist[1]))

        file.close()

        nameinput = input("Please Enter your Name: ")
        heightinput = input("Please enter student height (in meters): ")
        while isfloat(heightinput) == False:
            heightinput = input("Please enter student height (in meters): ")
        self.height.append(float(heightinput))
        self.names.append(nameinput)
        self.totalStudentcount = len(self.height)

    def calAvgHeight(self):
        for i in self.height:
            self.totalStudentHeight += i

        avg = self.totalStudentHeight / self.totalStudentcount
        rounded = avg.__round__(2)
        return rounded


start = CalUtils()
start.filestuff()
print(
    f"The average height is {start.calAvgHeight()} for {start.totalStudentcount} students \n\n\n {start.names} \n {start.height} ")
