import os
os.chdir(r"C:\Users\toshu\Google Drive\School Related\Classes\Winter 2021\CSE 110\python_ilearn\files")
print()

with open("hr_system.txt") as hr_system:
    for line in hr_system:
        clean_hr = line.strip()
        line_list = clean_hr.split(" ")
        
        name = line_list[0]
        id_num = line_list[1]
        title = line_list[2]
        salary = line_list[3]

        paycheck = float(salary) / 24

        if title == "Engineer":
            paycheck += 1000
        
        print(f"Name: {name} (ID: {id_num}), Title: {title} - ${paycheck:.2f}")
