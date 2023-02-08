#include "Pessoa.h"

Pessoa::Pessoa(int numeroUSP, string nome, string email) : Perfil(nome)
{
    this->numeroUSP = numeroUSP;
    this->email = email;
}


string Pessoa::getEmail(){
    return email;
}

int Pessoa::getNumeroUSP(){
    return numeroUSP;
}

Pessoa::~Pessoa()
{
    //dtor
}
