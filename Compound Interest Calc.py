#Compound interest calculator
# A = P(1 + r/12)^t , A = Final Amount , P = Principle amount , r = Rate of Interest (e.g. 5% a year), n = number of time periods, t is repetition of time periods
#Rate of Interest = X% per annum

print("Welcome to Interest rate calculator calculator!")
print("State your initial deposit below.")

def calculator():
    while True:
        principle_amount = float(input("Principle amount: $"))
        months = float(input("How many months would you like to use OCBC for: "))

        if months <= 0:
            print("Please key in a value that is more than 0")

        elif principle_amount <= 0:
            print("Please key in an amount of more than $0")

        else:
            r = float(input("Key in your interest rate per annum: "))
            if r < 0 or r > 100:
                print("Key in a number between 0-100")
            else:
                r_percentage = r / 100

            addition = r_percentage / 12
            constant = 1.00
            multiplicator = constant + addition

            second_multiplicator = multiplicator ** months
            final_amount = principle_amount * second_multiplicator

            print(f"Your balance would be ${final_amount}!")

calculator()


