from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = list()

    # verifica o tamanho da fila
    def __len__(self):
        return len(self._data)

    # verifica se a fila está vazia
    def is_empty(self):
        return not bool(self.__len__())

    # adiciona um elemento ao final da fila
    def enqueue(self, value):
        self._data.append(value)

    # remove o primeiro elemento da fila
    def dequeue(self):
        if self.is_empty():
            raise IndexError("The queue is empty")
        return self._data.pop(0)

    # busca um elemento na fila
    def search(self, index):
        if self.is_empty() or index < 0 or index >= self.__len__():
            raise IndexError(" Índice Inválido ou Inexistente")
        return self._data[index]
