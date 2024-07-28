def create_multiplication_table():
    """Creates a multiplication table with 5 rows and 10 columns."""
    table = []
    for i in range(1, 6):  # 5 rows
        row = []
        for j in range(1, 11):  # 10 columns
            row.append(i * j)
        table.append(row)
    return table

def display_multiplication_table(table):
    """Displays the multiplication table."""
    for row in table:
        print(" ".join(f"{x:2}" for x in row))