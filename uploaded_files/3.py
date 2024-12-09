def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def read_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        return content

filename = "my_file.txt"
content = "This is some text written to a file."

write_to_file(filename, content)
print(read_from_file(filename))