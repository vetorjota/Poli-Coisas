#include "Pessoa.h"



Pessoa::Pessoa(int numeroUSP, string nome, string email) : Perfil(nome)
{
    this->numeroUSP = numeroUSP;
    this->email = email;
}

Pessoa::Pessoa(int id, int numeroUSP, string nome, string email) : Perfil(id,nome)
{
    this->numeroUSP = numeroUSP;
    this->email = email;
    this->nome = nome;
}


string Pessoa::getEmail(){
    return email;
}

void Pessoa::receber(Publicacao* p) {

    publicacoesRecebidas->push_back( p );

}


int Pessoa::getNumeroUSP(){
    return numeroUSP;
}

Pessoa::~Pessoa()
{
    //dtor
}
