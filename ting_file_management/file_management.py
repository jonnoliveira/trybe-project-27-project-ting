import sys
import os


def txt_importer(path_file):
    # verifica existência do arquivo (True/False)
    if not os.path.exists(path_file):
        error = f"Arquivo {path_file} não encontrado"
        print(error, file=sys.stderr)
        return None

    # verifica extensão do arquivo
    file_extension = os.path.splitext(path_file)[1]
    if file_extension != ".txt":
        error = "Formato inválido"
        print(error, file=sys.stderr)
        return None

    # lê o arquivo e retorna uma lista separada por "\n"
    with open(path_file, "r") as arquivo:
        return arquivo.read().split("\n")
