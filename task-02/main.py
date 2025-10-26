import re
# Functiion-generator to extract floating-point numbers from text
def generator_numbers(text):
    # Regular expression pattern to match floating-point numbers
    pattern = r'(?<=\s)(-?\d+\.\d+)(?=\s)'
    # Find all matches in the text
    matches = re.findall(pattern, text)
    # Yield each match as a float
    for match in matches:
        yield float(match)

# Function to sum up the extracted numbers using the generator
def sum_profit(text, func):
    total = 0.0
    for number in func(text):
        total += number
    return total

# Result demonstration
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
