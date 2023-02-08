#include "Publicacao.h"

#include <iostream>
#include <string>

using namespace std;

Perfil* Publicacao::getAutor(){
    return autor;}

string Publicacao::getTexto(){
    return texto;}

int Publicacao::getCurtidas(){
    return curtidas;}


Publicacao::Publicacao(Perfil* autor, string texto){
    this->autor = autor;
    this->texto = texto;
    this->curtidas = 0;
}

Publicacao::~Publicacao(){
 cout << "Destrutor de publicacao: " << texto << endl;
}
