#include "Aluno.h"

void Aluno::imprimir()
{
    cout << numeroUSP << " - " << nome << endl;
    cout << "Seguidores: " << seguidores->size() << endl;
    cout << " --- " << endl;
    cout << "Escolha uma opcao:" << endl;
    cout << "1) Ver publicacoes feitas" << endl;
    cout << "2) Ver publicacoes recebidas" << endl;
    cout << "3) Fazer publicacao" << endl;
    cout << "4) Seguir perfil" << endl;
    cout << "0) Deslogar" << endl;
}


Aluno::Aluno(int numeroUSP, string nome, string email) : Pessoa(numeroUSP,nome,email)
{
    //ctor
}

Aluno::Aluno(int id, int numeroUSP, string nome, string email) : Pessoa(id,numeroUSP,nome,email)
{
    //ctor com id
}

Aluno::~Aluno()
{
    //dtor
}
