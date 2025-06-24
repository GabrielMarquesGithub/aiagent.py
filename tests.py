from functions.get_file_content import get_file_content


test = get_file_content("calculator", "main.py")
print(test)
test = get_file_content("calculator", "pkg/calculator.py")
print(test)
test = get_file_content("calculator", "/bin/cat")
print(test)
