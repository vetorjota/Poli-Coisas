#ifndef PESSOA_H
#define PESSOA_H

#include "Perfil.h"
#include "Publicacao.h"


class Pessoa : public Perfil
{
    public:
        Pessoa(int numeroUSP, string nome, string email);
        Pessoa(int id, int numeroUSP, string nome, string email);
        virtual ~Pessoa();

        virtual int getNumeroUSP();
        virtual string getEmail();

        virtual void receber(Publicacao* p);

        virtual void imprimir() = 0;


    protected:
        string email;
        int numeroUSP;
        string nome;
    private:


};

#endif // PESSOA_H
