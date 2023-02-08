#ifndef CONTRATO_H
#define CONTRATO_H

#include "Produto.h"
#include "Cliente.h"
#include <vector>


class Contrato {

private:

    Cliente* cliente;
    vector<Produto*>* produtos;

public:
    Contrato(Cliente* c);
    virtual ~Contrato();

    Cliente* getCliente();
    void adicionar(Produto* p);
    vector<Produto*>* getProdutos();
    double getValor();
    void imprimir();
};

#endif // CONTRATO_H
