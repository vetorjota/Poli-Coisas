#include "PlanoDeInternet.h"
#include <stdexcept>
#include <iostream>

using namespace std;

PlanoDeInternet::PlanoDeInternet(string nome, int velocidade) : Produto(nome)
{
    if (velocidade == 0) throw invalid_argument("Velocidade nula");
    else this->velocidade = velocidade;
}

double PlanoDeInternet::getPreco()
{
    return (50 + (velocidade * 0.75));
}

int PlanoDeInternet::getVelocidade()
{
    return velocidade;
}

PlanoDeInternet::~PlanoDeInternet()
{
    //dtor
}
