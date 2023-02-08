#include "Mensagem.h"
#include <stdexcept>

Mensagem::Mensagem(Perfil* autor, string texto) : Publicacao(autor,texto)
{
    //ctor
}

void Mensagem::imprimir(){

    cout << texto << " (" << autor->getNome() << ") [" << curtidas << "]" << endl;
}

void Mensagem::curtir(Perfil* quemCurtiu){

    try{

    if (quemCurtiu == this->getAutor()) throw new invalid_argument ("Autor nao pode curtir a propria mensagem.");

    curtidas++;

    }catch (invalid_argument *e){
        cout << "Erro: " << e->what() << endl;
        delete e;
    }
}


Mensagem::~Mensagem()
{
    //dtor
}
