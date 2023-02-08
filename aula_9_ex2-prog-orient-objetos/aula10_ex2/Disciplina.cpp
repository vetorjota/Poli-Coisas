#include "Disciplina.h"
#include "Evento.h"
#include <string>


using namespace std;


Disciplina::Disciplina(string sigla, string nome, Professor* responsavel) : Perfil(nome)
{
    this->sigla = sigla;
    this->responsavel = responsavel;
    this->adicionarSeguidor(responsavel);

}

string Disciplina::getSigla(){
    return sigla;
}

Professor* Disciplina::getResponsavel(){
    return responsavel;
}

/*Diferentemente de outros Perfis, a lista de publicações de uma Disciplina deve ser limitada a apenas
Publicações feitas pela própria Disciplina. Ou seja, quando um seguidor é adicionado à Disciplina não
se deve adicionar a mensagem de aviso. Além disso, como não faz sentido uma disciplina seguir outros
Perfis, ela não deve fazer nada ao receber uma Publicação. */


void Disciplina::adicionarSeguidor(Perfil* seguidor){

    try{

    if (seguidor == this) throw new invalid_argument ("Seguidor nao pode ser o proprio perfil");


    for (int i = 0; i < quantidadeDeSeguidores; i++){ //invalid
        if (seguidores[i] == seguidor) throw new invalid_argument ("Seguidor ja segue o perfil");
    }

    if(quantidadeDeSeguidores == MAXIMO_SEGUIDORES) throw new invalid_argument ("Maximo de seguidores atingido");

    }catch (invalid_argument *e){
        cout << "Erro: " << e->what();
        delete e;
    }

    this->seguidores[quantidadeDeSeguidores] = seguidor;
    quantidadeDeSeguidores++;

}

bool Disciplina::receber(Publicacao* p){
    return true;
}


Disciplina::~Disciplina()
{}
    //dtor
