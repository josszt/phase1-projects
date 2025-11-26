def greet(name):
    return f"Hello, {name}!"

name_input = input ("Enter your name:")
print(greet(name_input))

def multiply(a,b):
    return a*b

print("5*3 =", multiply(5,3))
print("851*54 =", multiply(851,54))

def divide(a,b):
    return a/b

print("27/9 =", divide(27,9))
print("935/5=", divide(935,5))

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

number = int(input("Enter a number"))
if is_even(number):
    print("That number is even.")
else:
    print("That number is odd.")

def average(numbers):
    return sum(numbers) / len(numbers)

scores = [80, 92, 77, 88, 86, 72]
print("Average score:", average(scores))

from day4_helpers import greet, add_numbers, is_even

print(greet("Josh"))

print("5 + 7 =", add_numbers(5, 7))

print("Is 10 even?", is_even(10))

def c_to_f(celsius):
    return (celsius * 9/5) + 32

def f_to_c(farenheit):
    return(farenheit - 32) * 5/9

def main():
    print("Temperature Converter")
    print("1. Celsius to Farenheit")
    print("2. Farenheit to Celsius")

    choice = input("Choose optioin 1 or 2")

    if choice == "1":
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c}°C = {c_to_f(c):.2f}°F")
    
    elif choice == "2":
        f = float(input("Enter temperature in Farenheit: "))
        print(f"{f}°F = {f_to_c(f):.2f}°C")

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()

def calculate_tip(total, percentage):
    return total * (percentage / 100)

def split_bill(amount, people):
    return amount / people

def main():
    print("Tip Calculator")

    total = float(input("Enter bill total: $"))
    percentage = float(input("Enter tip percentage: "))
    people = int(input("How many people are splitting the bill? "))

    tip_amount = calculate_tip(total, percentage)
    total_with_tip = total + tip_amount
    per_person = split_bill(total_with_tip, people)

    print(f"\nTip: ${tip_amount:.2f}")
    print(f"Total with tip: ${total_with_tip:.2f}")
    print(f"Amount per person: ${per_person}")

if __name__ == "__main__":
    main()

def word_count(text):
    words = text.split()
    return len(words)

def main():
    sentence = input("Enter a sentence: ")
    count = word_count(sentence)
    print(f"Word count: {count}")
if __name__ == "__main__":
    main()