#Tu tarea es extender ligeramente las capacidades de la clase Queue. Queremos que tenga un método sin #parámetros que devuelva True si la cola está vacía y False de lo contrario.

#Completa el código que te proporcionamos en el editor. Ejecútalo para comprobar si genera un resultado #similar al nuestro.

#A continuación, puedes copiar el código que usamos en el laboratorio anterior:

#Saluda Esperada
#1
#perro
#False
#Cola vacía

class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.queue_en_lista = []

    def put(self, elem):
        self.queue_en_lista.append(elem)

    def get(self):
        if len(self.queue_en_lista) > 0:
            val = self.queue_en_lista[0]
            del self.queue_en_lista[0]
            return val
        else:
            raise QueueError


class SuperQueue(Queue):
    def isempty(self):
        if len(self.queue_en_lista) > 0:
            return False
        else:
            return True


que = SuperQueue()
que.put(1)
que.put("perro")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Cola vacía")
