def check_eligibility():
    try:
        age = int(input("Please enter your age: "))
        if age < 18:
            print("Sorry, you are still young to do the job.")
        else:
            print("Congratulations, you are qualified for adult jobs!")
    except ValueError:
        print("Invalid input. Please enter a valid age (a number).")

if __name__ == "__main__":
    check_eligibility()
13