def sum_and_average_of_digits(s):
    digits = [int(c) for c in s if c.isdigit()]
    if not digits:
        return (0, 0)
    total_sum = sum(digits)
    average = total_sum / len(digits)
    return (total_sum, average)

user_string = input("Enter a string: ")
total_sum, average = sum_and_average_of_digits(user_string)
print(f"Sum of digits: {total_sum}")
print(f"Average of digits: {average}")


print("hello")