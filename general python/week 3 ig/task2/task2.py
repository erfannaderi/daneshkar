user_input = input("enter a value separated by spaces ")
values = user_input.split()
result = "*".join(values)
print(result)

sep = input("Enter the value of sep: ")
names = ["Alice", "Bob", "Charlie"]

output = ""
for i, name in enumerate(names):
    output += name
    if i < len(names) - 1:
        output += sep

print(output)
print("Done!")
