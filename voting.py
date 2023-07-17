def is_eligible_to_vote(age):
    return age >= 18

def main():
    try:
        age = int(input("Enter your age: "))
        if is_eligible_to_vote(age):
            print("Congratulations! You are eligible to cast your vote.")
        else:
            print("Sorry, you are not eligible to vote yet.")
    except ValueError:
        print("Invalid input. Please enter a valid age (an integer).")

if __name__ == "__main__":
    main()
