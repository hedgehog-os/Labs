#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <dirent.h>
#include <string.h>
#include <sys/stat.h>

#define MAX_FILES 1000
#define MAX_PATH 1024

// Структура для хранения информации о файле
typedef struct {
    char name[256];
    char full_path[MAX_PATH];
} FileInfo;

// Функция сравнения файлов (реальная)
int compareFiles(const char *file1, const char *file2) {
    FILE *f1 = fopen(file1, "rb");
    FILE *f2 = fopen(file2, "rb");

    if (!f1 || !f2) {
        printf("Процесс %d: Ошибка открытия файлов %s и %s\n", 
               getpid(), file1, file2);
        if (f1) fclose(f1);
        if (f2) fclose(f2);
        return -1;
    }

    int c1, c2;
    size_t bytesRead = 0;

    while (1) {
        c1 = fgetc(f1);
        c2 = fgetc(f2);

        if (c1 == EOF && c2 == EOF) {
            printf("Процесс %d: Файлы %s и %s ИДЕНТИЧНЫ, просмотрено байт: %zu\n", 
                   getpid(), file1, file2, bytesRead);
            fclose(f1);
            fclose(f2);
            return 1;
        }

        if (c1 == EOF || c2 == EOF || c1 != c2) {
            printf("Процесс %d: Файлы %s и %s РАЗЛИЧАЮТСЯ, просмотрено байт: %zu\n", 
                   getpid(), file1, file2, bytesRead);
            fclose(f1);
            fclose(f2);
            return 0;
        }
        
        bytesRead++;
    }
}

// Функция для получения списка файлов в каталоге
int getFilesFromDir(const char *dir_path, FileInfo files[], int max_files) {
    DIR *dir;
    struct dirent *entry;
    struct stat file_stat;
    int count = 0;
    
    dir = opendir(dir_path);
    if (dir == NULL) {
        printf("Ошибка: не могу открыть каталог %s\n", dir_path);
        return -1;
    }
    
    while ((entry = readdir(dir)) != NULL && count < max_files) {
        // Пропускаем специальные записи . и ..
        if (strcmp(entry->d_name, ".") == 0 || strcmp(entry->d_name, "..") == 0) {
            continue;
        }
        
        // Формируем полный путь
        char full_path[MAX_PATH];
        snprintf(full_path, sizeof(full_path), "%s/%s", dir_path, entry->d_name);
        
        // Проверяем, что это обычный файл (не каталог)
        if (stat(full_path, &file_stat) == 0 && S_ISREG(file_stat.st_mode)) {
            strncpy(files[count].name, entry->d_name, sizeof(files[count].name) - 1);
            strncpy(files[count].full_path, full_path, sizeof(files[count].full_path) - 1);
            count++;
        }
    }
    
    closedir(dir);
    return count;
}

// Функция для поиска файла по имени в массиве
int findFileByName(const char *filename, FileInfo files[], int file_count) {
    for (int i = 0; i < file_count; i++) {
        if (strcmp(filename, files[i].name) == 0) {
            return i; // Возвращаем индекс найденного файла
        }
    }
    return -1; // Файл не найден
}

int main(int argc, char *argv[]) {
    if (argc != 4) {
        printf("Использование: %s <Dir1> <Dir2> <N>\n", argv[0]);
        printf("Где:\n");
        printf("  Dir1 - первый каталог для сравнения\n");
        printf("  Dir2 - второй каталог для сравнения\n");
        printf("  N    - максимальное количество одновременных процессов\n");
        return 1;
    }
    
    char *dir1 = argv[1];
    char *dir2 = argv[2];
    int max_processes = atoi(argv[3]);
    int active_processes = 0;
    
    printf("Родительский процесс PID: %d\n", getpid());
    printf("Сравниваем каталоги: '%s' и '%s'\n", dir1, dir2);
    printf("Максимум одновременных процессов: %d\n\n", max_processes);
    
    // Получаем списки файлов из обоих каталогов
    FileInfo files_dir1[MAX_FILES];
    FileInfo files_dir2[MAX_FILES];
    
    int count1 = getFilesFromDir(dir1, files_dir1, MAX_FILES);
    int count2 = getFilesFromDir(dir2, files_dir2, MAX_FILES);
    
    if (count1 < 0 || count2 < 0) {
        printf("Ошибка чтения каталогов!\n");
        return 1;
    }
    
    printf("Найдено файлов в %s: %d\n", dir1, count1);
    printf("Найдено файлов в %s: %d\n", dir2, count2);
    
    // Создаем задачи для сравнения файлов, которые есть в обоих каталогах
    int comparison_tasks = 0;
    
    for (int i = 0; i < count1; i++) {
        int j = findFileByName(files_dir1[i].name, files_dir2, count2);
        if (j != -1) {
            // Файл найден в обоих каталогах - создаем задачу сравнения
            comparison_tasks++;
            
            // Ждем, если достигли максимума процессов
            while (active_processes >= max_processes) {
                int status;
                pid_t finished_pid = wait(&status);
                if (finished_pid > 0) {
                    active_processes--;
                }
            }
            
            // Создаем новый процесс для сравнения
            pid_t pid = fork();
            
            if (pid == 0) {
                // Дочерний процесс
                printf("Процесс %d: начинаю сравнение файлов:\n", getpid());
                printf("  %s\n", files_dir1[i].full_path);
                printf("  %s\n", files_dir2[j].full_path);
                
                compareFiles(files_dir1[i].full_path, files_dir2[j].full_path);
                exit(0); // Важно: завершаем дочерний процесс!
                
            } else if (pid > 0) {
                // Родительский процесс
                active_processes++;
                printf("Родитель: создал процесс %d для сравнения '%s'\n", 
                       pid, files_dir1[i].name);
            } else {
                printf("Ошибка при создании процесса для файла %s!\n", files_dir1[i].name);
            }
        }
    }
    
    printf("\nВсего задач для сравнения: %d\n", comparison_tasks);
    
    // Ждем завершения всех оставшихся процессов
    while (active_processes > 0) {
        int status;
        pid_t finished_pid = wait(&status);
        if (finished_pid > 0) {
            active_processes--;
            printf("Родитель: процесс %d завершился, осталось процессов: %d\n", 
                   finished_pid, active_processes);
        }
    }
    
    printf("\nРодитель: все процессы завершены! Программа закончена.\n");
    return 0;
}
