#include "PersistenciaDaRede.h"
#include <fstream>
#include <iostream>
#include "RedeSocial.h"
#include <string>
#include "Aluno.h"
#include "Disciplina.h"
#include "Professor.h"
#include "Perfil.h"

using namespace std;

PersistenciaDaRede::PersistenciaDaRede(string arquivo)
{
    this->arquivo = arquivo;
}

void PersistenciaDaRede::salvar(RedeSocial* r){

    ofstream output;
    output.open(arquivo);

    output << r->getPerfis()->front()->getUltimoId() << endl;


    // ------------ Contagem de Perfis por tipo -------------

    int numAlunos = 0;
    int numProfs = 0;
    int numDis = 0;

    vector<Perfil*>::iterator p = r->getPerfis()->begin();
    while (p != r->getPerfis()->end()){

        if ( (dynamic_cast<Aluno*>(*p) ) != NULL ) numAlunos++;

        else if ( (dynamic_cast<Professor*>(*p) ) != NULL ) numProfs++;

        else if ( (dynamic_cast<Disciplina*>(*p) ) != NULL ) numDis++;

        p++;
    }

    // -------------- Persistindo no arquivo --------------

    output << numAlunos << endl ; // ------ ALUNOS

    p = r->getPerfis()->begin();
    while (p != r->getPerfis()->end()){

        Aluno* alu = dynamic_cast <Aluno*>((*p));
        if ( alu != NULL ){
            output << alu->getId() << " " << alu->getNumeroUSP() << " " << alu->getNome() << " " << alu->getEmail() << endl;
        }
        p++;
    }

    output << numProfs << endl ; // ------- PROFESSORES

    p = r->getPerfis()->begin();
    while (p != r->getPerfis()->end()){

        Professor* prof = dynamic_cast <Professor*>((*p));
        if ( prof != NULL ){
            output << prof->getId() << " " << prof->getNumeroUSP() << " " << prof->getNome() << " " << prof->getEmail() << " " << prof->getDepartamento() << endl;
        }
        p++;
    }

    output << numDis << endl ; // -------- DISCIPLINAS

    p = r->getPerfis()->begin();
    while (p != r->getPerfis()->end()){

        Disciplina* dis = dynamic_cast <Disciplina*>((*p));
        if ( dis != NULL ){
            output << dis->getId() << " " << dis->getSigla() << " " << dis->getNome() << " " << dis->getResponsavel()->getId() << endl;
        }
        p++;
    }

    p = r->getPerfis()->begin(); // --------- RELACOES DE SEGUIDORES
    while (p != r->getPerfis()->end()){
        Perfil* p1 = (*p);
        vector<Perfil*>::iterator s = p1->getSeguidores()->begin();

        while (s != (p1->getSeguidores()->end())){
            Perfil* pSeguidor = (*s);
            output << p1->getId() << " " << pSeguidor->getId() << endl;
            s++;
        }
        p++;
    }

    output.close();

}

RedeSocial* PersistenciaDaRede::carregar(){

    ifstream input;
    input.open(this->arquivo);

    RedeSocial* insta = new RedeSocial();

    int id;
    int nusp;
    string nome;
    string email;

    string departamento;

    string sigla;
    int id_aux;

    int ultimoId;
    int quantAlunos;
    int quantProf;
    int quantDisc;


    while (input.good()){

        input >> ultimoId;

        input >> quantAlunos;

        for ( int i = 0; i < quantAlunos; i++){  // ---------- ALUNOS

            input >> id;
            input >> nusp;
            input >> nome;
            input >> email;

            Aluno* alu = new Aluno(id,nusp,nome,email);
            insta->adicionar(alu);
            if (insta->getPerfil(id)->getUltimoId() != ultimoId) insta->getPerfil(id)->setUltimoId(ultimoId);
        }

        input >> quantProf;

        for (int i = 0; i < quantProf; i++){    // ----------- PROFESSORES

            input >> id;
            input >> nusp;
            input >> nome;
            input >> email;
            input >> departamento;

            Professor* prof = new Professor(id,nusp,nome,email,departamento);
            insta->adicionar(prof);
            if (insta->getPerfil(id)->getUltimoId() != ultimoId) insta->getPerfil(id)->setUltimoId(ultimoId);
        }

        input >> quantDisc;

        for (int i  = 0; i < quantDisc; i++){    // ------------ DISCIPLINAS

            input >> id;
            input >> sigla;
            input >> nome;
            input >> id_aux;

            Professor* prof_res = dynamic_cast<Professor*>(insta->getPerfil(id_aux));

            Disciplina* dis = new Disciplina(id,sigla,nome,prof_res);
            insta->adicionar(dis);

            if (insta->getPerfil(id)->getUltimoId() != ultimoId) insta->getPerfil(id)->setUltimoId(ultimoId);

        }


        while (input.good()) // --------- RELACOES DE SEGUIDORES
        {
            input >> id;
            input >> id_aux;

            if (id!=0 && id_aux!=0){
                Perfil* p1 = insta->getPerfil(id);
                Perfil* seguidor = insta->getPerfil(id_aux);


                p1->adicionarSeguidor(seguidor);
                id = 0;
                id_aux =0;
                }
        }

    }


    return insta;

}


PersistenciaDaRede::~PersistenciaDaRede()
{
    //dtor
}
