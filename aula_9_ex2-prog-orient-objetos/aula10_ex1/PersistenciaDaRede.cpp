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

        output << alu->getId() << " " ;
        output << alu->getNumeroUSP() << " " ;
        output << alu->getNome() << " " ;
        output << alu->getEmail() << endl;
    }

    output.close();

}

PersistenciaDaRede::~PersistenciaDaRede()
{
    //dtor
}
