age = input("Are you a cigarette addict older than 75 years old? Yes/No   ").capitalize() == "Yes"
chronic = input("Do you have a severe chronic disease? Yes/No   ").capitalize() == "Yes"
immune = input("Is your immune system too weak? Yes/No   ").capitalize() == "Yes"
risk = age or chronic or immune
print("Risk of death:", risk)