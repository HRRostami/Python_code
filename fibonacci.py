fibonacci=0
sum=0
fibonacci_list=[1]
for _ in range(20):
  fibonacci=fibonacci_list[-1]+sum
  sum=fibonacci_list[-1]
  fibonacci_list.append(fibonacci)
  if fibonacci >= 55:
    break
print(fibonacci_list)