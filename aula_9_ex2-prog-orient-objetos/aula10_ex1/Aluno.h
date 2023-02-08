#ifndef ALUNO_H
#define ALUNO_H

#include "Pessoa.h"


class Aluno : public Pessoa
{
    public:
        Aluno(int numeroUSP, string nome, string email);
        virtual ~Aluno();
        bool receber(Publicacao* p);

    protected:

    private:
};

#endif // ALUNO_H
