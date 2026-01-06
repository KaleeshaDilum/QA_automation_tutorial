# class areaRect:
#     def __init__(self , l,b):
#         self.l = l
#         self.b = b
#
#     def calcArea(self):
#         return self.l * self.b
#
# area1 = areaRect(10,20)
# area2 = areaRect(32,20)
# print(area1.calcArea())
# print(area2.calcArea())


# class employee:
#     def __init__(self,fname,lname,email):
#         self.fname=fname
#         self.lname=lname
#         self.email=email
#
#     def greet_person(self):
#         print("Hello,",self.fname,"!")
#
#     def personalDetails(self):
#         print("Name:",self.fname,"Email:",self.email)
#
# emp1= employee("John","Doe","Kaleeshadilum2gmail.com")
# emp1.greet_person()
# emp1.personalDetails()
#
# emp1.lname
# print(emp1.lname)

# class rateOfIntrest:
#     intrest = 0.3232
#
#     def __init__(self, name ,loanAmount):
#         self.name = name
#         self.loanAmount = loanAmount
#
#
#     def calculateRateOfInterest(self):
#         print("Total Intrest :", self.loanAmount * self.intrest)
#
# class student(rateOfIntrest):
#     intrest = 0.03232
#
# amount = student("Kaleesha",3232)
# amount.calculateRateOfInterest()

# class MoveCharacter:
#     def move_fwd(self):
#         print("\nMoving forward")
#     def move_back(self):
#         print("\nMoving backward")
#
# class JumpOver(MoveCharacter):
#     def jump(self):
#         print("\nJumping over")
#
#     def swim(self):
#         print("\nSwimming")
#
# class NewUnlock(JumpOver):
#     def move_fwd(self):
#         print("\nMoving forward Pokemon")
#
# Create = NewUnlock()
# Create.move_fwd()
# Create.jump()
# print(NewUnlock.mro())














































