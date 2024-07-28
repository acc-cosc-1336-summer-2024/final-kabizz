from question_b import calculate_statistics

def main():
    # Initialize an empty list to store the numbers
    numbers = []
    
    # Prompt the user to enter 5 numbers
    print("Please enter 5 numbers:")
    for i in range(5):
        while True:
            try:
                # Get input from the user and convert it to a float
                num = float(input(f"Number {i + 1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
    # Calculate the required statistics
    try:
        lowest, highest, total, average = calculate_statistics(numbers)
    except ValueError as e:
        print(e)
        return
    
    # Display the results
    print(f"The lowest number in the list is: {lowest}")
    print(f"The highest number in the list is: {highest}")
    print(f"The total of the numbers in the list is: {total}")
    print(f"The average of the numbers in the list is: {average:.2f}")

if __name__ == "__main__":
    main()