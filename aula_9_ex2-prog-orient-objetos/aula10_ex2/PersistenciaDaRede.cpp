#include "PersistenciaDaRede.h"
#include <fstream>
#include <iostream>
#include "RedeSocial.h"
#include <string>
#include "Aluno.h"
#include "Perfil.h"

using namespace std;

PersistenciaDaRede::PersistenciaDaRede(string arquivo)
{

    this->arquivo = arquivo;


}

void PersistenciaDaRede::salvar(RedeSocial* r){

    ofstream output;
    output.open(arquivo);


    output << r->getQuantidadeDePerfis() << endl ;

    for (int i = 0; i < r->getQuantidadeDePerfis() ; i++){

        Aluno* alu = dynamic_cast <Aluno*> (r->getPerfis()[i]);

        output << alu->getId() << " " << alu->getNumeroUSP() << " " ;
        output << alu->getNome() << " " << alu->getEmail() << endl;
    }

    output.close();

}

RedeSocial* PersistenciaDaRede::carregar(){

    ifstream input;
    input.open(arquivo);

    int quantidadeDePerfis = 1;
    input >> quantidadeDePerfis;

    RedeSocial* insta = new RedeSocial(quantidadeDePerfis);

    int id;
    int nusp;
    string nome;
    string email;


    while (input.good() ){
        input >> id;
        input >> nusp;
        input >> nome;
        input >> email;

        Aluno* alu = new Aluno(nusp,nome,email);
        insta->adicionar(alu);

    }

    return insta;

}


PersistenciaDaRede::~PersistenciaDaRede()
{
    //dtor
}
