#ifndef ALUNO_H
#define ALUNO_H

#include "Pessoa.h"


class Aluno : public Pessoa
{
    public:
        Aluno(int numeroUSP, string nome, string email);
        Aluno(int id, int numeroUSP, string nome, string email);
        virtual ~Aluno();

        void imprimir();


    protected:

    private:
};

#endif // ALUNO_H
