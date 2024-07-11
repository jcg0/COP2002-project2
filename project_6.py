# Jefferson Griebel / jcg0
# COP2002.0M1: PROGRAM LOGIC
# 07/06/2024
# Project6: Files and Functions
# Use functions to write files
from pathlib import Path

program_codes = [
    "1002, Computer_Science",
    "1030, Business_Admin",
    "3504, Computer_Information_Technology",
    "3840, IT_Security_–_Infrastructure_Track",
    "3841, IT_Security_–_Healthcare_Track",
    "3842, IT_Security_–_Risk_Management_Track",
    "3650, Network_System_Technology_–_Networking_Server_Administration",
    "3651, Network_System_Technology_–_Networking_Infrastructure",
    "1119, Exploring_General_Studies",
    "6625, Computer_Programmer",
    "6635, Computer_Programming_Specialist",
    "6645, Help_Desk_Support_Technician",
    "6623, Information_Technology_Support_Specialist",
    "6650, Network_Server_Administration",
    "6651, Network_Infrastructure",
    "6652, Network_Security",
    "3624, Programming_and_Analysis_–_Web_Development",
    "3520, Health_Information_Technology",
    "3330, Health_Services_Management"]

p_codes = ["3504",
           "3651",
           "3840",
           "3841",
           "3842",
           "3650",
           "3624"]

p_definitions = ["Computer_Information_Technology",
                 "Network_System_Technology_–_Networking_Infrastructure",
                 "IT_Security_–_Infrastructure_Track",
                 "IT_Security_–_Healthcare_Track",
                 "IT_Security_–_Risk_Management_Track",
                 "Network_System_Technology_–_Networking_Server_Administration",
                 "Programming_and_Analysis_–_Web_Development",
                 ]


def read_file(file_path):
    try:
        csv_file = Path(file_path)
        csv_file = csv_file.read_text()
    except:
        new_file_path = input("What is the correct file path: ")
        csv_file = Path(new_file_path)
        csv_file.read_text()

    return csv_file.splitlines()


def lookup_codes(program_codes, codes_to_lookup):
    for item in program_codes:
        split_item = item.split(", ")
        if split_item[0] == codes_to_lookup:
            return split_item[1]


def lookup_codes(p_definitions, codes_to_lookup):
    for item in p_definitions:
        split_item = item.split(", ")
        if split_item[0] == codes_to_lookup:
            return split_item[1]


def write_file(file_path, str_to_write):
    try:
        write_path = Path(write_file)
        write_path.write_text(str_to_write)
    except:
        print(f"{file_path} could not be written.")


def main():
    the_file = read_file(
        '/Users/jeffersongriebel/Desktop/document of things/school/COP2002_projects/student roster example.csv')
    p_codes = []
    # file_index = 0

    for file_index in range(1, len(the_file)):
        l = the_file[file_index].split(",")
        p_codes.append(l[5])
    print(p_codes)
    str_to_write = ""
    for code in p_codes:
        return_value = lookup_codes(program_codes, code)
        print(f"{return_value}")
        str_to_write += f"{return_value}"
    write_file(
        "/Users/jeffersongriebel/Desktop/document of things/school/COP2002_projects/result.txt", str_to_write)


if __name__ == "__main__":
    main()
