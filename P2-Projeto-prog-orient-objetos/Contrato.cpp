#include "Contrato.h"
#include <stdexcept>
#include <iostream>

using namespace std;


Contrato::Contrato(Cliente* c)
{
    if (c == NULL) throw invalid_argument("Cliente nulo");
    cliente = c;
    produtos = new vector<Produto*>;
}

void Contrato::adicionar(Produto* p)
{
    vector<Produto*>::iterator i = produtos->begin();
    while (i != produtos->end()){
        if ((*i) == p) throw logic_error("Ja adicionado");
        i++;
    }

    produtos->push_back(p);
}

Cliente* Contrato::getCliente()
{
    return cliente;
}

vector<Produto*>* Contrato::getProdutos()
{
    return produtos;
}

double Contrato::getValor()
{
    double valor = 0;
    vector<Produto*>::iterator i = produtos->begin();
    while (i != produtos->end()){
        valor += (*i)->getPreco();
        i++;
    }
    return valor;
}

void Contrato::imprimir(){
    cout << "Contrato de " << cliente->getNome() << ": " << getValor() << endl;
}


Contrato::~Contrato()
{
    for (int i = 0; i < produtos->size();i++){
        delete produtos->at(i);
    }
    delete produtos;
    delete cliente;
}
