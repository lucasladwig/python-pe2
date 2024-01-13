class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, value):
        self.__stack_list.append(value)

    def pop(self):
        value = self.__stack_list[-1]
        del self.__stack_list[-1]
        return value


class AddingStack(Stack):
    def __init__(self):
        super().__init__(self)
        self.__sum = 0

    def push(self, value) -> None:
        super().push(self, value)
        self.__sum += value

    def pop(self) -> int:
        value = super().pop(self)
        self.__sum -= value
        return value