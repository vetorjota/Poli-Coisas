#ifndef PRODUTO_H
#define PRODUTO_H

#include <string>

// Crie atributos e faca outras alteracoes necessarias

using namespace std;

class Produto {

protected:
    double preco = -1;
    string nome;

public:
    Produto(string nome);
    virtual ~Produto();

    string getNome();
    virtual double getPreco() = 0;
    virtual void imprimir();
};

#endif // PRODUTO_H
