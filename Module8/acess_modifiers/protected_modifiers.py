from tensorflow.compiler.tf2xla.python.xla import self_adjoint_eig
from tensorflow.python.ops.gen_string_ops import string_length_eager_fallback


class rectangle:
    def __init__(self):
        self._length = "this variable is with length 5"
    def _area(self,length):
        return self._length * self._length

rectangle = rectangle()
print(rectangle._length)