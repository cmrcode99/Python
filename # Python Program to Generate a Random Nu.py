# Python Program to Generate a Random Number
import time

# Seed the random number generator using the current time
seed = int(time.time())
num_iterations = 10

# Generate a "random" number between 0 and 9 for each iteration
for i in range(num_iterations):
    seed = (seed * 1103515245 + 12345) % (2**31)
    random_number = seed % 10
    print(f"Random number {i + 1}: {random_number}")


