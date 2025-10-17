#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdlib.h>

void process_chain(int depth, int max_depth) {
    pid_t pid, ppid;

    pid = getpid();
    ppid = getppid();

    printf("Процесс %d: PID=%d, PPID=%d\n", depth, pid, ppid);
    fflush(stdout);

    if (depth < max_depth) {
        pid_t child_pid = fork();

        if (child_pid < 0) {
            perror("fork error");
            exit(1);
        } else if (child_pid == 0) {
            // потомок
            process_chain(depth + 1, max_depth);
            exit(0);
        } else {
            // родитель ждёт завершения ребёнка
            wait(NULL);
        }
    } else {
        printf("Процесс %d (PID=%d): выполняет exec -> ls -l\n", depth, pid);
        execlp("ls", "ls", "-l", NULL);
        perror("exec error");
        exit(1);
    }

    printf("Процесс %d (PID=%d, PPID=%d) завершает работу\n", depth, getpid(), getppid());
}

int main() {
    printf("=== Вариант 5: цепочка fork и exec ===\n");
    process_chain(0, 5);
    printf("Главный процесс завершён.\n");
    return 0;
}

