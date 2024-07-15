# Converting CSV to JSON
# By James Nichols

import pprint as pp


class CreateJSONString:

    def __init__(self, arrayKeys, arrayValues):
        self.arrayKeys = arrayKeys
        self.arrayValues = arrayValues
        self.jsonString = ""
        self.___________ = 1

    def headerJSON(self):
        """Opening { for JSON """
        self.jsonString += "___"

    def objectJSONLabel(self):
        if (self.counter > 1):
            self.jsonString += ","

        # Opening information for each object (row in CSV file)
        self._________ += "\""+str(self.____________)+"\""+":"
        self.counter += 1

    def footerJSON(self):
        self.jsonString += "_______"

    def createJSON(self):
        # initialization JSON string
        self._______________()

        # Create object string (i.e. CSV row to JSON)
        resultString = "{"

        count = 0

        for key in self._________:
            resultString += "\""+key+"\""
            resultString += ":"

            value = str(self.____________[count])

            if (value.isnumeric()):  # type(value) == int or type(value) == float
                resultString += str(value)
            elif (value == "True" or value == "False"):
                resultString += str(value).lower()
            elif (value == _______):
                resultString += value
            else:
                resultString += _______________

            count += 1

            if (len(self.________) > count):
                resultString += ","

        # Add closing to this object
        resultString += "}\n"

        self.jsonString += resultString

    def toString(self):
        return self.jsonString

    def processHeaderLine(self, line):

        line = line.split(",")

        self.arrayKeys = []

        for item in line:
            item = item.replace("\n", "")
            self.arrayKeys.append(item)

        # print(arrayKeys)

    def processLine(self, line):

        line = line.split(",")

        self.arrayValues = []

        for item in line:
            item = item.replace(______, "")
            self.arrayValues.append(item)

        # print("Array values")
        # print(self.arrayValues)

    def inputStudentFile(self, filename):
        # global arrayValues

        try:
            with open(filename) as file_object:
                # print(filename)
                counter = 0

                self.headerJSON()

                for line in file_object:
                    # print(line)
                    if (counter > 0):
                        # print(line)
                        value = self.processLine(line)
                        self.createJSON()
                    else:
                        self.processHeaderLine(line)
                    counter += 1

                self.footerJSON()

        except FileNotFoundError:
            print(____________________________________)

    def writeToFile(self, filename):

        try:
            with open(filename, "w") as file_object:
                file_object.write(self.________________)
        except FileNotFoundError:
            print(f"Sorry, the file {filename} does not exist.")


def main():
    # arrayKeys=["Last Name", "First Name", "Preferred Name", "Preferred Pronoun", "SF ID#", "Program Code", "Phone", "Email", "Enrolled"]
    # arrayValues=["Nichols", "James", "James", "null", "1234-5678", 3652, "3523955220", "james.nichols@sfcollege.edu", True]

    arrayKeys = []
    arrayValues = []

    filename = (input("Enter the filename:  ")).______
    # print(filename)

    outputFilename = (input("Enter the OUTPUT filename:  ")).strip()
    # print(outputFilename)

    if (outputFilename == ""):
        outputFilename = "Project7Output.txt"

    converted = ________________________________

    converted.____________(filename)

    print(converted.________________)

    converted.__________(_____________)

    print("Output written to "+outputFilename+".")


if __name__ == "__main__":
    main()
