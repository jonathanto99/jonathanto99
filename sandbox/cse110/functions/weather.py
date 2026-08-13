import math

print()
temp_number = input("What is the temperature? ")
temp_type = input("Fahrenheit or Celsius (F/C)? ")


if temp_type == "F":
    temp_num_f = float(temp_number) * 1
    print()

    for v in range(5, 65, 5):
        wind_chill_f = 35.74 + 0.6215 * temp_num_f - 35.75 * v ** 0.16 + 0.4215 * temp_num_f * v ** 0.16
        print(f"At temperature {temp_num_f:.2f} F, and wind speed is {v:.2f} mph, the windchill is: {wind_chill_f:.2f} F.")

if temp_type == "C":
    temp_num_c = float(temp_number) * 1.8 + 32
    print()

    for v in range(5, 65, 5):
        wind_chill_c = 35.74 + 0.6215 * (temp_num_c) - 35.75 * v ** 0.16 + 0.4215 * (temp_num_c) * v ** 0.16
        print(f"At temperature {temp_num_c:.2f} F, and wind speed is {v:.2f} mph, the windchill is: {wind_chill_c:.2f} F.")
