try:
    mark1 = float(input("Enter marks for Subject 1: "))
    mark2 = float(input("Enter marks for Subject 2: "))
    mark3 = float(input("Enter marks for Subject 3: "))
except ValueError:
    print("Invalid input Please enter numbers only.")
    exit()

total = mark1 + mark2 + mark3
average = total / 3
print(f"Total Marks: {total}")
print(f"Average Marks: {average:.2f}")