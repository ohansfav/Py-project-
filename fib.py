
#write a program to sum the first 50 _ fibonacci sequence

def fibonacci_sum(n):
    fib_sequence = [0, 1]  # Initialize with the first two Fibonacci numbers together
    sum_fib = 1  # Initialize the sum with the second Fibonacci number

    for i in range(2, n):
        next_fib = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_fib)
        sum_fib += next_fib

    return sum_fib

# sum of the first 50 Fibonacci numbers
n = 50
sum_fibonacci = fibonacci_sum(n)

# Print the sum
print("Sum of the first", n, "Fibonacci numbers:", sum_fibonacci)
