# Initialize a function that computes Fibonacci numbers with caching
def caching_fibonacci():
    # Dictionary to store previously computed Fibonacci numbers
    cache = {}
    # Inner function to compute Fibonacci numbers
    def fibonacci(n):
        # return zero Fibonacci number for n <= 0
        if n <= 0:
            return 0
        # return first Fibonacci number for n == 1
        if n == 1:
            return 1
        # Check if the value is already in the cache
        if n in cache:
            return cache[n]
        # Compute the Fibonacci number and store it in the cache
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

fib = caching_fibonacci()

print(fib(10))
print(fib(15))
