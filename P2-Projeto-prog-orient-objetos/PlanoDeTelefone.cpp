#include "PlanoDeTelefone.h"
#include <stdexcept>
#include <iostream>

using namespace std;

PlanoDeTelefone::PlanoDeTelefone(string nome, int franquiaDeDados, int minutosDeVoz) : Produto(nome)
{
    this->franquiaDeDados = franquiaDeDados;
    this->minutosDeVoz = minutosDeVoz;
}


double PlanoDeTelefone::getPreco()
{
    return (10 + franquiaDeDados + minutosDeVoz*0.5);
}

int PlanoDeTelefone::getFranquiaDeDados()
{
    return franquiaDeDados;
}

int PlanoDeTelefone::getMinutosDeVoz()
{
    return minutosDeVoz;
}

PlanoDeTelefone::~PlanoDeTelefone()
{
    //dtor
}
