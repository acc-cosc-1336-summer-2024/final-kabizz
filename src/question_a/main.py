from question_a import create_multiplication_table, display_multiplication_table

def main():
    while True:
        # Call create_multiplication_table and save the result to a local variable
        multiplication_table = create_multiplication_table()
        # Call display_multiplication_table with the local variable
        display_multiplication_table(multiplication_table)
        # Ask the user if they want to continue or quit the program
        user_input = input("Do you want to create another multiplication table? (yes/no): ").strip().lower()
        if user_input == 'no':
            print("Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()