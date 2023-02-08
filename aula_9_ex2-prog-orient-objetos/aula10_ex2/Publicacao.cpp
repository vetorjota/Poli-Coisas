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

void Publicacao::curtir(Perfil* quemCurtiu){
    if (quemCurtiu != this->autor){
        curtidas ++;
    }
}

void Publicacao::imprimir(){

    cout << texto << " (" << autor->getNome() << ") [" << curtidas << "]" << endl;
}

Publicacao::Publicacao(Perfil* autor, string texto){
    this->autor = autor;
    this->texto = texto;
    this->curtidas = 0;
}

Publicacao::~Publicacao(){
 cout << "Destrutor de publicacao: " << texto << endl;
}
