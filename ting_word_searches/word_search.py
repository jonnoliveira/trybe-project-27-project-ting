def exists_word(word, instance):
    result = []
    counter = 0

    for i in range(instance.__len__()):
        # item da lista
        item = instance.search(i)

        # lista de linhas do arquivo
        occurrences = [
            {"linha": index + 1}
            # enumerate retorna uma tupla com o index e o valor
            for index, linha in enumerate(item["linhas_do_arquivo"])
            # case insensitive
            if word.lower() in linha.lower()
        ]

        # verifica se há ocorrência da palavra e incrementa o contador
        if len(occurrences) > 0:
            counter += 1

        # cria o dicionário com as informações
        info = {
            "palavra": word,
            "arquivo": item["nome_do_arquivo"],
            "ocorrencias": occurrences,
        }

        result.append(info)

    # verifica se não há ocorrência da palavra
    if counter == 0:
        return []

    return result


def search_by_word(word, instance):
    result = exists_word(word, instance)
    occurrences = []

    # verifica que não há ocorrência da palavra
    if len(result) == 0:
        return []

    for i in range(instance.__len__()):
        item = instance.search(i)

        occurrences.append(
            {
                "conteudo": [
                    {"linha": index + 1, "conteudo": linha}
                    # enumerate retorna uma tupla e agora adiciona
                    # o conteúdo da linha
                    for index, linha in enumerate(item["linhas_do_arquivo"])
                    if word.lower() in linha.lower()
                ]
            }
        )

    # adiciona as novas ocorrências com o conteúdo ao resultado final
    for i in range(len(result)):
        result[i]["ocorrencias"] = occurrences[i]["conteudo"]

    return result
