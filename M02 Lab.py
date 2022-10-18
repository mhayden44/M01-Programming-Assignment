"""
Matthew Hayden
M02 Lab
Program takes last name, first name, and GPA and checks to see if the person made either the Dean's List or the Honor Roll.
Variables:
    last_name is the person's last name
    first_name is the person's first name
    GPA is the person's GPA stored as a float
"""
print("Enter 'ZZZ' as last name to exit.")
while True:
    last_name = input("Enter last name: ")
    if last_name == "ZZZ":
        break;
    first_name = input("Enter first name: ")
    GPA = float(input("Enter GPA: "))
    if GPA >= 3.5:
        print(first_name + " " + last_name + " has made the Dean's List.")
    elif GPA >= 3.25:
        print(first_name + " " + last_name + " has made the Honor Roll.")
    else:
        print(first_name + " " + last_name + " has not made the Dean's List or Honor Roll.")
