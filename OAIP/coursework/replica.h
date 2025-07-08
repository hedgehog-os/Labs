#ifndef REPLICA_H
#define REPLICA_H

const int maxsize = 500;

struct Replica {
    int id;
    char phrase[maxsize];
    char name[maxsize];
    char branch[maxsize];
};

#endif
