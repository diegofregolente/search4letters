import os

print(os.getcwd()) # Mostra o diretorio atual do código rodando
print(os.environ) # Mostra todas as variaveis do ambiente OBS: Retorna uma tupla com dicionario dentro.
print(os.getenv('USERDOMAIN_ROAMINGPROFILE')) # Ou acesse uma variavel especifica e veja seu valor, Key and Value
