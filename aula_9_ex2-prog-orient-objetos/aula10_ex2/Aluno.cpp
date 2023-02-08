#include "Aluno.h"

Aluno::Aluno(int numeroUSP, string nome, string email) : Pessoa(numeroUSP,nome,email)
{
    //ctor
}

bool Aluno::receber(Publicacao* p){


    if (this->quantidadeDePublicacoesRecebidas < MAXIMO_PUBLICACOES){

        publicacoesRecebidas[quantidadeDePublicacoesRecebidas] = new Publicacao(p->getAutor(),p->getTexto());

        //this->recebidas[quantidadeDePublicacoesRecebidas]->setAutor(p->getAutor());
        //this->recebidas[quantidadeDePublicacoesRecebidas]->setTexto(p->getTexto());
        this->quantidadeDePublicacoesRecebidas++;

        return true;
    }

    else return false;

}

Aluno::~Aluno()
{
    //dtor
}
