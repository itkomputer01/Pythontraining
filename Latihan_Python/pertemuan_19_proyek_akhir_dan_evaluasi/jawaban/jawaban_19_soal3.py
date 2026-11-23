# Pertemuan 19 - Jawaban soal 3
# ------------------------------------------------------------
# Soal:
#   Buat class Stack dengan method push(), pop(), peek(), is_empty(). pop() pada
#   stack kosong melempar IndexError.
# ------------------------------------------------------------

class Stack:
    def __init__(self):
        self._data = []

    def push(self, x):
        self._data.append(x)

    def pop(self):
        if not self._data:
            raise IndexError("stack kosong")
        return self._data.pop()

    def peek(self):
        if not self._data:
            raise IndexError("stack kosong")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

s = Stack()
s.push(1); s.push(2)
print(s.pop(), s.peek(), s.is_empty())

# Contoh output:
#   2 1 False
