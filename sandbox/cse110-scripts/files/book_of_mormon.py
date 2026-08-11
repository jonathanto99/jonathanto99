import os
os.chdir(r"C:\Users\toshu\Google Drive\School Related\Classes\Winter 2021\CSE 110\python_ilearn\files")
print()

with open("books.txt") as book_of_mormon:
    for line in book_of_mormon:
        clean_bom = line.strip()
        print(clean_bom)