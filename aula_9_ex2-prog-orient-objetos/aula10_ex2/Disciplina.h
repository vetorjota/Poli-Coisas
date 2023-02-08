#ifndef DISCIPLINA_H
#define DISCIPLINA_H

#include "Perfil.h"
#include "Professor.h"
#include <string>

using namespace std;

class Disciplina : public Perfil
{
    public:
        Disciplina(string sigla, string nome, Professor* responsavel);
        virtual ~Disciplina();


        void adicionarSeguidor(Perfil* seguidor);
        bool receber(Publicacao* p);


        //getters e setters
        string getSigla();
        Professor* getResponsavel();


    protected:

    private:
        Professor* responsavel;
        string sigla;

};

#endif // DISCIPLINA_H
