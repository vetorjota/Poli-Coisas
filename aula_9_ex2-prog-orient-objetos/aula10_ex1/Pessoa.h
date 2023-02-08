#ifndef PESSOA_H
#define PESSOA_H

#include "Perfil.h"


class Pessoa : public Perfil
{
    public:
        Pessoa(int numeroUSP, string nome, string email);
        virtual ~Pessoa();

        int getNumeroUSP();
        string getEmail();

    protected:
        string email;
        int numeroUSP;
    private:


};

#endif // PESSOA_H
