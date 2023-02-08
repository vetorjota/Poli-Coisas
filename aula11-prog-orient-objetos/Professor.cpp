#include "Professor.h"

string Professor::getDepartamento(){
    return departamento;
}

void Professor::imprimir()
{
    cout << numeroUSP << " - " << nome << endl;
    cout << "Departamento " << departamento << endl;
    cout << "Seguidores: " << seguidores->size() << endl;
    cout << " --- " << endl;
    cout << "Escolha uma opcao:" << endl;
    cout << "1) Ver publicacoes feitas" << endl;
    cout << "2) Ver publicacoes recebidas" << endl;
    cout << "3) Fazer publicacao" << endl;
    cout << "4) Seguir perfil" << endl;
    cout << "0) Deslogar" << endl;

}



Professor::Professor(int numeroUSP, string nome, string email, string departamento) : Pessoa(numeroUSP,nome,email)
{
    this->departamento = departamento;
}

Professor::Professor(int id, int numeroUSP ,string nome, string email, string departamento) : Pessoa(id, numeroUSP, nome, email)
{
    this->departamento = departamento;
}

Professor::~Professor()
{
    //dtor
}
