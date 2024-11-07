leap_year = int(input("Please enter a year to check if it is a leap year: "))
if (leap_year % 4 == 0 and leap_year%100!=0)  or leap_year%400==0:
  print(leap_year, "is a leap year")
else:
  print(leap_year, "is not a leap year")