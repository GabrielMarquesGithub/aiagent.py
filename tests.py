from functions.get_files_info import get_files_info


teste = get_files_info("calculator", ".")
print(teste)
teste = get_files_info("calculator", "pkg")
print(teste)
teste = get_files_info("calculator", "/bin")
print(teste)
teste = get_files_info("calculator", "../")
print(teste)
