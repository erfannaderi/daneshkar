import csv

def save_to_csv(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('numbers.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(result)
        return result
    return wrapper

@save_to_csv
def generate_numbers(n):
    return [i for i in range(n)]

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    generate_numbers(num)
    print(f"Numbers smaller than {num} have been saved to 'numbers.csv'.")