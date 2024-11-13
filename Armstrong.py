number=input("enter a number")
power=int(len(number))
sum=0
if number.isdigit():
  for i in number:
        i=int(i)
        sum=i**power+sum
  if sum==int(number):
    print(number,"is an Armstrong number")
  else:
    print(number,"is not an Armstrong number")
else:
  print("It is an invalid entry. Don't use non-numeric, float, or negative values!")