#include "Disciplina.h"
#include "Evento.h"
#include <string>


using namespace std;


void Disciplina::imprimir()
{
    cout << sigla << " - " << nome << endl;
    cout << "Seguidores: " << seguidores->size() << endl;
    cout << " --- " << endl;
    cout << "Escolha uma opcao:" << endl;
    cout << "1) Ver publicacoes feitas" << endl;
    cout << "2) Ver publicacoes recebidas" << endl;
    cout << "3) Fazer publicacao" << endl;
    cout << "0) Deslogar" << endl;
}

Disciplina::Disciplina(string sigla, string nome, Professor* responsavel) : Perfil(nome)
{
    this->sigla = sigla;
    this->responsavel = responsavel;
    this->adicionarSeguidor(responsavel);
}

Disciplina::Disciplina(int id, string sigla, string nome, Professor* responsavel) : Perfil(id,nome)
{
    this->sigla = sigla;
    this->responsavel = responsavel;
}


string Disciplina::getSigla(){
    return sigla;
}

Professor* Disciplina::getResponsavel(){
    return responsavel;
}


void Disciplina::receber(Publicacao* p){}


Disciplina::~Disciplina()
{}
    //dtor
