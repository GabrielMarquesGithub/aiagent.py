from functions.write_file import write_file


test = write_file("calculator", "__pycache__", "wait, this isn't lorem ipsum")
print(test)
test = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
print(test)
test = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
print(test)
