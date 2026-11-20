a = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços? ', a.isspace())  #vai dizer se na variavel a so tem espaços.Se sim retorna true, que é do tipo boolean
print('É um número? ', a.isnumeric()) # para verificar se é um número. Fe sim retorna true, que é do tipo boolean
print('É alfabético? ', a.isalpha()) # para verificar se é alfabético. Se sim retorna true, que é do tipo boolean
print('É alfanumérico? ', a.isalnum()) # para verificar se é alfanumérico. Se tem letras e números, se sim retorna true, que é do tipo boolean
print('Está em maiúsculas? ', a.isupper()) # para verificar se está em maiúsculas. Se sim retorna true, que é do tipo boolean
print('Está em minúsculas? ', a.islower()) # para verificar se está em minúsculas. Se sim retorna true, que é do tipo boolean
print('Está capitalizada? ', a.istitle()) # para verificar se está capitalizada, se tem letras maiúsculas e minúsculas. Se sim retorna true, que é do tipo boolean
