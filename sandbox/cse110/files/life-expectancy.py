import os
import math
import csv
os.chdir(r"G:\My Drive\School Related\Classes\BYU Idaho\Winter 2021\CSE 110\python_ilearn\files")
print()

with open("life-expectancy.csv") as data_set:
    for row in data_set:
        row = row.split(",")

        entity = row[0].strip()
        code = row[1].strip()
        year = int(row[2])
        life_expectancy = (row[3])

        max_life = -1
        min_life = min(life_expectancy)
        avg_life = sum(life_expectancy) / len(life_expectancy)

        max_country = ""
        max_year = max(year)
        min_country = min(entity)
        min_year = min(year)

        chosen_year = ""

print()
year_lookup = input(float("Enter the year of interest: "))
print()

if chosen_year == year_lookup:
    chosen_year = year_lookup
    print(f"For the year: {year_lookup}.\n")
    print(f"The average life expectancy across all countries was str{avg_life:.2f}\n")
    print(f"The max life expectancy was in {max_country} with {max_life:.2f}\n")
    print(f"The min life expectancy was in {min_country} with {min_life:.2f}\n")

    if life_expectancy > max_life:

        max_life = life_expectancy
        max_country = entity

    print()
    print(f"The overall max life expectancy is:{max_life:.2f} from {max_country} in {max_year:.2f}.\n")
    print(f"The overall min life expectancy is:{min_life:.2f} from {min_country} in {min_year:.2f}.\n")
