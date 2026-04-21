print("Without using with statement:\n")

path = "../../data/File Handling/notes.txt"

file = open(path, "r")
content = file.read()
print(content)
file.close()

print("\nUsing with statement:\n")

with open(path, "r") as file:
    content = file.read()
    print(type(content))
    print(len(content))
    print(content)


with open(path, "r") as file:
    lines = file.readlines()
for line in lines:
    line = line.strip()
    print(line)

print("\nUsing with statement and iterating through file object:\n")

with open(path, "r") as file:
    for line in file:
        line = line.strip()
        print(line)
