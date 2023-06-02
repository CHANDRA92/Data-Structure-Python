def reverse_integer(num):
    # Check if the number is negative
    is_negative = False
    if num < 0:
        is_negative = True
        num = -num

    reversed_num = 0
    while num > 0:
        # Extract the last digit
        last_digit = num % 10

        # Update the reversed number
        reversed_num = (reversed_num * 10) + last_digit

        # Remove the last digit from the original number
        num //= 10

    # Apply the sign if the original number was negative
    if is_negative:
        reversed_num = -reversed_num

    return reversed_num
