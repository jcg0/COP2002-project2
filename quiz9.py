class SocialMedia:
    def __init__(self, name, profilePicture, background, friends):
        self.name = name
        self.profilePicture = profilePicture
        self.background = background
        self.friends = friends

    def changePicture(self, picture):
        self.profilePicture = picture
        if (picture.endswith(".jpg")):
            print("1")
        elif (picture.endswith(".png")):
            print("2")
        else:
            print("3")

    def changeBackground(self, background):
        self.background = background
        print("Background change.")

    def printInformation(self):
        print(self.name+" " + self.profilePicture+" " + self.background)


# Code to execute (think of it as in the main function, but it could be in any function)
james = SocialMedia("James", "picture.jpg", "Instructor",
                    ["Ryan", "Allison", "Blanca", "Omar"])
james.printInformation()
james.changePicture("Classroom.gif")
james.printInformation()
james.changeBackground("Python Programmer")
james.printInformation()
