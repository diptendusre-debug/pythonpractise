class car:
    def __init__(self,windows,doors,engineType):
        self.windows=windows
        self.doors=doors
        self.engineType=engineType
    def drive(self,speed):
        print(f"{self.engineType} can drive upto {speed}")
class Tesla(car):
    def __init__(self,windows,doors,engineType,selfDriving):
        super().__init__(windows,doors,engineType)
        self.selfDriving=selfDriving
    def selfDrive(self):
        print(f"Tesla can drive Self: {self.selfDriving}")
    
tesla1=Tesla(4,5,"v18",True)
tesla1.selfDrive()
tesla1.drive(180)
