from functions.run_python_file import run_python_file


test = run_python_file("calculator", "main.py")
print(test)
test = run_python_file("calculator", "tests.py")
print(test)
test = run_python_file("calculator", "../main.py")
print(test)
test = run_python_file("calculator", "nonexistent.py")
print(test)
