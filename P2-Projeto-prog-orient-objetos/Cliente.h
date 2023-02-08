#ifndef CLIENTE_H
#define CLIENTE_H

#include <string>
using namespace std;

// CLASSE JA IMPLEMENTADA. NAO ALTERE

class Cliente {
public:
    Cliente(string nome);
    virtual ~Cliente();
    string getNome();
private:
    string nome;
};

#endif // CLIENTE_H
