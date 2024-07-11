# Jefferson Griebel / jcg0
# COP2002.0M1: PROGRAM LOGIC
# 07/06/2024
# Project6: Files and Functions
# Use functions to write files
from pathlib import Path

# hard coded the class codes into a list to make it easier for me to access
p_codes = ["3504",
           "3651",
           "3840",
           "3841",
           "3842",
           "3650",
           "3624"]

# hard coded the class names into their own list
p_definitions = ["Computer_Information_Technology",
                 "Network_System_Technology_–_Networking_Infrastructure",
                 "IT_Security_–_Infrastructure_Track",
                 "IT_Security_–_Healthcare_Track",
                 "IT_Security_–_Risk_Management_Track",
                 "Network_System_Technology_–_Networking_Server_Administration",
                 "Programming_and_Analysis_–_Web_Development",
                 ]

# basic read file function with a try except block to catch any errors


def read_file(file_path):
    try:
        csv_file = Path(file_path)
        csv_file = csv_file.read_text()
    except:
        new_file_path = input("What is the correct file path: ")
        csv_file = Path(new_file_path)
        csv_file.read_text()

    return csv_file.splitlines()

# displays the class codes


def lookup_codes(p_codes, p_definitions):
    for code in p_codes:

        print(f"*{code}*")

# displays the class definitions


def lookup_definitions(p_definitions):
    for definition in p_definitions:
        print(f"\t{definition}")

# writes the output to a new file


def write_file(file_path, str_to_write):
    try:
        write_path = Path(write_file)
        write_path.write_text(str_to_write)
    except:
        print(f"{file_path} could not be written.")


def main():
    read_file("/Users/jeffersongriebel/Desktop/document of things/school/COP2002_projects/student roster example.csv")

    print("Procession student input file...")
    lookup_codes(p_codes, p_definitions)
    print()
    print("Writing to file...")
    lookup_definitions(p_definitions)
    print()

    codes = []
    str_to_write = ""
    for code in codes:
        return_value = lookup_codes(p_definitions, code)
        print(f"hello {return_value}")
        str_to_write += f"{return_value}"
    write_file(
        "/Users/jeffersongriebel/Desktop/document of things/school/COP2002_projects/result.txt", str_to_write)
    print("Program Completed.")


if __name__ == "__main__":
    main()
