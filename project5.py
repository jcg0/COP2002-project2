# Jefferson Griebel / jcg0
# COP2002.0M1: PROGRAM LOGIC
# 07/03/2024
# Project5: Finish project 5
# Complete the game by creating more functions that hold the functionality of the main game

# importing functions from the random library in Python
from random import randrange
portNameArray = ['FTP', 'FTP', 'SSH', 'Telnet', 'SMTP', 'DNS', 'DHCP', 'DHCP', 'HTTP',
                 'POP3', 'NetBIOS', 'NetBIOS', 'IMAP', 'SNMP', 'SNMP', 'LDAP', 'HTTPS', 'SMB', 'RDP']


portNumArray = ['20', '21', '22', '23', '25', '53', '67', '68', '80',
                '110', '137', '139', '143', '161', '162', '389', '443', '445', '3389']


def numToName(portNumArray, portNameArray, portNumber) -> str:
    """giving this function a port number parameter will return the given port name"""
    index = 0

    for port in portNumArray:
        if port == portNumber:
            return portNameArray[index]
        else:
            index += 1
    return "Port name not found."


def nameToNum(portNumArray, portNameArray, portName):
    """finds the port number when give a name and stores that value in a list called result"""
    result = []
    for index in range(len(portNumArray)):
        if portName == portNameArray[index]:
            result.append(portNumArray[index])
    return result


def getInput():
    """takes user input for the menu options"""
    userInput = ""
    while userInput not in ["1", "2", "3", "m"]:
        userInput = input("Choice: ").rstrip()

    return userInput


def playGame():
    """This function represents the menu for the game and how the game functions"""
    prompt = "Main menu:"
    prompt += "\n1. Given a port number, identify the PROTOCOL (use abbreviation)."
    prompt += "\n2. Given a port protocol, identify a port NUMBER."
    prompt += "\n3. Exit\n"
    print(prompt)
    userInput = getInput()
    return userInput.strip()


#  This function determins what the port Number question will be and what happens when a correct or incorrect answer is given
def qWhatNumber():
    msg = "Option 2:  Identify the port's NUMBER."
    msg += "\n--------------------------------------\n"
    print(msg)
    selection = ""
    while selection != "m":
        qIndex = randrange(0, len(portNameArray))

        qName = portNameArray[qIndex]

        answer = nameToNum(portNumArray, portNameArray, qName)

        prompt = f"What is the name for protocol {qName} (m=Main Menu)?  "

        selection = input(prompt)

        while selection in ["", "\n"]:
            selection = input(prompt)

        if selection in answer:
            print("Correct answer!\n")
        else:
            msg = f"Incorrect. The correct answer is {portNumArray[qIndex]}"
            print(msg)


#  This function determins what the port PROTOCOL question will be and what happens when a correct or incorrect answer is given
def qWhatName():
    msg = "Option 1:  Identify the port's PROTOCOL."
    msg += "\n----------------------------------------\n"
    print(msg)
    selection = ""
    while selection != "m":
        qIndex = randrange(0, len(portNumArray))

        qNum = portNumArray[qIndex]

        answer = numToName(portNumArray, portNameArray, qNum)

        prompt = f"What is the protocol for port {qNum} (m=Main Menu)?  "

        selection = input(prompt)

        while selection in ["", "\n"]:
            selection = input(prompt)

        if selection in answer:
            print("Correct answer!\n")
        else:
            msg = f"Incorrect. The correct answer is {portNameArray[qIndex]}"
            print(msg)


def main():
    """takes our game functions and uses them together to let users play the game"""
    selection = ""
    while selection != "3":
        selection = playGame()
        if selection == "1":
            qWhatName()
        elif selection == "2":
            qWhatNumber()

    print("\nProgram Complete.  I hope this has helped in studying for the CompTIA A+ certification.")


if __name__ == "__main__":
    main()
