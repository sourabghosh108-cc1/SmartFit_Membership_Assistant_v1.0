# SmartFit Membership Decision-Making Assistant

print("========================================")
print(" Welcome to SmartFit Fitness Assistant ")
print("========================================")

# Get user's age
age = int(input("Enter your age: "))

# Q1: Determine Fitness Program
if age < 18:
    print("\nYou are eligible for the Teen Fitness Program.")
elif age <= 40:
    print("\nYou are eligible for the Regular Fitness Program.")
else:
    print("\nYou are eligible for the Senior Wellness Program.")

# Get medical condition
medical = input("\nDo you have any medical condition? (yes/no): ").lower()

# Q2: Logical Operators
if medical != "yes" and medical != "no":
    print("Invalid input. Please enter 'yes' or 'no'.")
else:
    if age >= 40 and medical == "yes":
        print("Medical clearance required before joining.")
    elif age < 40 or medical == "no":
        print("You can proceed with registration.")

    # Get membership type
    membership = input("\nChoose your membership (Basic/Premium): ").lower()

    personal_training = "no"

    # Q3A: Nested Conditional Statements
    if membership == "basic":
        personal_training = input(
            "Do you want personal training? (yes/no): "
        ).lower()

        if personal_training == "yes":
            print("Basic plan with personal training: $45 per month.")
        elif personal_training == "no":
            print("Basic plan: $30 per month.")
        else:
            print("Invalid input for personal training.")

    elif membership == "premium":
        print("Premium plan: $60 per month.")

    else:
        print("Invalid membership type.")

    # Q3B: Nested Conditionals with Logical Operators
    if membership == "premium" and age < 30:
        print("You qualify for a youth discount! 10% off your plan.")

    if membership == "basic" and personal_training == "no":
        print("Consider upgrading to Premium for more benefits!")

    if membership == "premium" and medical == "yes":
        print("We recommend a free consultation before starting.")

print("\nThank you for using the SmartFit Membership Assistant!")

print("\n========================================")
print("   Thank you for choosing SmartFit!")
print(" We wish you a healthy fitness journey.")
print("========================================")

input("\nPress Enter to exit...")
