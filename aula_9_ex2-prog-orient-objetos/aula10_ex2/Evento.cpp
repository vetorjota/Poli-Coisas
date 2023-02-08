#include "Evento.h"
#include <string>

void Evento::imprimir(){
    cout<< data << " - " << texto << " (" << autor->getNome() << ") [" << curtidas << "]" << endl;
}

Evento::Evento(Perfil* autor, string texto, string data) : Publicacao(autor,texto)
{    
    this->data = data;
}

string Evento::getData(){
    return data;
}

Evento::~Evento()
{
    //dtor
}
