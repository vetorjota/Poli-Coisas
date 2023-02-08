#include "Combo.h"
#include <stdexcept>
#include <iostream>

using namespace std;

Combo::Combo(string nome, PlanoDeTelefone* telefone, PlanoDeInternet* internet) : Produto(nome)
{
    if (telefone == NULL || internet == NULL) throw invalid_argument("Algum dos planos eh nulo");
    else {
        this->telefone = telefone;
        this->internet = internet;
    }
}

void Combo::imprimir()
{
    Produto::imprimir();
    cout << telefone->getNome() << ": " << telefone->getPreco() << endl;
    cout << internet->getNome() << ": " << internet->getPreco() << endl;

}

double Combo::getPreco()
{
    double preco = (internet->getPreco() + telefone->getPreco())*0.9;
    return (preco);
}

Combo::~Combo()
{
    //dtor;
}
