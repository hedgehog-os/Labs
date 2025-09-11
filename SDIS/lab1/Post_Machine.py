class PostMachine:
    """
    @brief Класс машины Поста.
    @details Реализует вычислительную модель с лентой, кареткой и набором команд.
    """

    def __init__(self, string, commands):
        """
        @brief Инициализация машины.
        @param string Строка из 0 и 1 — начальное состояние ленты.
        @param commands Список команд для выполнения.
        """
        ...

        self.tape = {}              # Лента машины Поста
        self.commands = commands    # Список с выполняемыми командами
        self.head = 0               # Каретка
        self.index = 0              # Номер текущей команды
        self.stopped = False        # Остановка программы

        for i, c in enumerate(string):
            self.tape[i] = int(c)

    def run(self):
        """
        @brief Запуск машины Поста.
        @details Выполняет команды по очереди, пока не встретит Stop.
        """
        ...

        i = 1
        self.stopped = False

        while not self.stopped and self.index < len(self.commands):
            command = self.commands[self.index]
            command.execute(self)

            print(f"{i}.")
            print('')
            print(list(self.tape.values()))
            print(f"каретка: {self.head}")
            print(f"комманда: {self.index}")
            print('')
            i += 1

class Command:
    """
    @brief Базовый класс команды машины Поста.
    @param j Номер следующей команды.
    """
    ...

    def __init__(self, j):
        self.j = j      # Переход к строке j

class Mark(Command):
    """
    @brief Команда отметки: установить 1 на текущей ячейке.
    """

    def execute(self, machine):
        """
        @brief Выполнение команды.
        @param machine Экземпляр PostMachine.
        """
        ...

        machine.tape[machine.head] = 1
        machine.index = self.j

class Clear(Command):
    """
    @brief Команда очистки: установить 0 на текущей ячейке.
    """
    ...

    def execute(self, machine):
        machine.tape[machine.head] = 0
        machine.index = self.j

class Right(Command):
    """
    @brief Команда сдвига вправо.
    """
    ...

    def execute(self, machine):
        machine.head += 1
        machine.index = self.j

class Left(Command):
    """
    @brief Команда сдвига влево.
    """
    ...

    def execute(self, machine):
        machine.head -= 1
        machine.index = self.j

class Jump:
    """
    @brief Команда условного перехода.
    @details Переход зависит от значения текущей ячейки.
    @param j1 Переход, если 0.
    @param j2 Переход, если 1.
    """
    ...

    def __init__(self, j1, j2):
        self.j1 = j1
        self.j2 = j2

    def execute(self, machine):
        if not machine.tape[machine.head]:
            machine.index = self.j1
        else:
            machine.index = self.j2

class Stop(Command):
    """
    @brief Команда остановки машины.
    """
    ...
    
    def __init__(self):
        super().__init__(None)

    def execute(self, machine):
        machine.stopped = True


def parse(commands):
    """
    @brief Парсинг текстовых команд в объекты.
    @param commands Список строковых команд.
    @return Список объектов-команд.
    """
    ...

    result = []

    for command in commands:
        
        command = command.strip()
        if not command:
            continue
        
        if command[0] == 'V':
            _, j = command.split()
            result.append(Mark(int(j)))
        
        elif command[0] == 'X':
            _, j = command.split()
            result.append(Clear(int(j)))
        
        elif command[0] == '→':
            _, j = command.split()
            result.append(Right(int(j)))

        elif command[0] == '←':
            _, j = command.split()
            result.append(Left(int(j)))

        elif command[0] == '?':
            parts = command[1:].split(";")
            j1 = int(parts[0].strip())
            j2 = int(parts[1].strip())
            result.append(Jump(int(j1), int(j2)))

        elif command[0] == '!':
            result.append(Stop())

        else:

            raise ValueError(f'Неизвестная команда: {command}')
    
    return result


program = [
    "? 1; 3",   
    "V 2",      
    "→ 4",      
    "X 5",      
    "!",        
    "← 4"      
]

parsed_commands = parse(program)
tape = "01001"

machine = PostMachine(tape, parsed_commands)
machine.run()