from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    result_dict = {}

    # verifica os nomes dos arquivos na fila
    for i in range(instance.__len__()):
        result = instance.search(i)
        if result["nome_do_arquivo"] == path_file:
            return

    # importa o arquivo
    arquivo = txt_importer(path_file)

    # implementa o dicionário
    result_dict["nome_do_arquivo"] = path_file
    result_dict["qtd_linhas"] = len(arquivo)
    result_dict["linhas_do_arquivo"] = arquivo

    # adiciona o dicionário à fila
    instance.enqueue(result_dict)
    print(result_dict)


def remove(instance):
    # verifica se a fila está vazia
    if instance.is_empty():
        message_empty = "Não há elementos"
        print(message_empty, file=sys.stdout)
        return None

    # remove o primeiro elemento da fila
    file = instance.dequeue()
    message_success = f"Arquivo {file['nome_do_arquivo']} removido com sucesso"
    print(message_success, file=sys.stdout)


def file_metadata(instance, position):
    # tenta apresentar info de um arquivo na fila
    try:
        print(instance.search(position), file=sys.stdout)

    # lança um erro caso a posição seja inválida
    except IndexError:
        message_error = "Posição inválida"
        print(message_error, file=sys.stderr)
