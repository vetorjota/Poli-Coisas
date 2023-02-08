#include "Produto.h"
#include <iostream>

using namespace std;


Produto::Produto(string nome)
{
    this->nome = nome;
}

string Produto::getNome()
{
    return nome;
}


void Produto::imprimir()
{
    cout << nome << ": " << getPreco() << endl;
}

Produto::~Produto()
{
    //cout << "Deletado o produto: " << nome << endl;
}
