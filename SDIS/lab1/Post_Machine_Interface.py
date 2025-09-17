from Post_Machine import PostMachine, Command, Jump, Right, Left, Stop, Clear, Mark
from Post_Machine import parse
def main():
    machine = None
    program = []
    tape = ''

    print('''Available commands:
    run                 — execute full program
    step                — execute one command
    reset               — reset machine to initial state
    add <command>       — add command to program
    tape                — show tape
    tape <tape>         — set tape (e.g. 01001)
    program             — show current program
    show                — show full machine state
    rm program          — clear all commands
    delete <n>          — delete command at index n
    exit                — quit interface
          
    Command formats:
    V <n>          - mark the current cell (set to 1) and jump to command n  
    X <n>          - clear the current cell (set to 0) and jump to command n  
    → <n> or r <n> - move the head right and jump to command n  
    ← <n> or l <n> - move the head left and jump to command n  
    ? <n1>; <n2>   - if current cell is 0, jump to n1; if 1, jump to n2  
    !              - stop the program

    ''')

    while True:
        try:
            cmd = input('>>> ').strip()
            if not cmd:
                continue

            parts = cmd.split()

            if parts[0] == 'exit':
                break

            elif parts[0] == 'help':
                print('''Available commands:
    run                 — execute full program
    step                — execute one command
    reset               — reset machine to initial state
    add <command>       — add command to program
    tape                — show tape
    tape <tape>         — set tape (e.g. 01001)
    program             — show current program
    show                — show full machine state
    rm program          — clear all commands
    delete <n>          — delete command at index n
    exit                — quit interface
                      
    Command formats:
    V <n>          - mark the current cell (set to 1) and jump to command n  
    X <n>          - clear the current cell (set to 0) and jump to command n  
    → <n> or r <n> - move the head right and jump to command n  
    ← <n> or l <n> - move the head left and jump to command n  
    ? <n1>; <n2>   - if current cell is 0, jump to n1; if 1, jump to n2  
    !              - stop the program
                ''')

            elif parts[0] == 'tape' and len(parts) == 1:
                if machine:
                    print(machine.tape)
                else:
                    print("Machine not initialized.")

            elif parts[0] == 'tape' and len(parts) == 2:
                tape_candidate = parts[1]
                if all(c in '01' for c in tape_candidate):
                    tape = tape_candidate
                    machine = PostMachine(tape, [cmd for group in program for cmd in group])
                    print("Tape updated.")
                else:
                    print("Invalid tape format. Use only 0 and 1.")

            elif parts[0] == 'program':
                for i, group in enumerate(program):
                    print(f"{i}: {group[0].__class__.__name__} → {group[0].__dict__}")

            elif parts[0] == 'add':
                raw = cmd[len('add'):].strip()
                if not raw:
                    raw = input("Enter command: ").strip()
                try:
                    parsed = parse([raw])
                    program.append(parsed)
                    if tape:
                        machine = PostMachine(tape, [cmd for group in program for cmd in group])
                    print("Command added.")
                except Exception as e:
                    print(f"Parse error: {e}")

            elif parts[0] == 'rm' and parts[1] == 'program':
                program.clear()
                if tape:
                    machine = PostMachine(tape, [])
                print("Program cleared.")

            elif parts[0] == 'delete' and len(parts) == 2 and parts[1].isdigit():
                idx = int(parts[1])
                if 0 <= idx < len(program):
                    program.pop(idx)
                    if tape:
                        machine = PostMachine(tape, [cmd for group in program for cmd in group])
                    print(f"Deleted command at index {idx}.")
                else:
                    print("Invalid index.")

            elif parts[0] == 'show':
                if machine:
                    print("Tape:", machine.tape)
                    print("Head:", machine.head)
                    print("Index:", machine.index)
                    print("Stopped:", machine.stopped)
                    print("Program:")
                    for i, group in enumerate(program):
                        print(f"{i}: {group[0].__class__.__name__} → {group[0].__dict__}")
                else:
                    print("Machine not initialized.")

            elif parts[0] == 'run':
                if machine:
                    machine.run()
                else:
                    print("Machine not initialized.")

            elif parts[0] == 'step':
                if machine and not machine.stopped and machine.index < len(machine.commands):
                    machine.commands[machine.index].execute(machine)
                    print(f"Step executed. Head={machine.head}, Index={machine.index}")
                else:
                    print("Machine not ready or already stopped.")

            elif parts[0] == 'reset':
                if tape:
                    machine = PostMachine(tape, [cmd for group in program for cmd in group])
                    print("Machine reset.")
                else:
                    print("No tape to reset with.")

            else:
                print("Unknown command. Type 'help' for list.")

        except Exception as e:
            print(f"⚠️ Error: {e}")

main()