#include <iostream>
#include <string>
#include <stdexcept>

#include "Perfil.h"
#include "RedeSocial.h"
#include "Professor.h"
#include "Disciplina.h"
#include "Aluno.h"
#include "PersistenciaDaRede.h"


using namespace std;


int main() {


    /*
    Aluno* gab = new Aluno(123456,"Gabriela", "gabriela@usp.br" );
    Aluno* jor = new Aluno(47879123, "Jorge", "jorge@usp.br" );
    Aluno* lui = new Aluno(654321,"Luisa", "luisa@usp.br" );


    RedeSocial* insta = new RedeSocial(10);

    insta->adicionar(gab);
    insta->adicionar(jor);
    insta->adicionar(lui);

    insta->imprimir(); */

    PersistenciaDaRede* persist = new PersistenciaDaRede("teste.txt");
    RedeSocial* insta = persist->carregar();
    insta->imprimir();

    delete insta;

    /**/

}
