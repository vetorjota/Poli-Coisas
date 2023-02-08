#ifndef PROFESSOR_H
#define PROFESSOR_H

#include "Pessoa.h"
#include <string>


class Professor : public Pessoa
{
private:
    string departamento;

protected:

public:

    string getDepartamento();

    void imprimir();

    Professor(int numeroUSP, string nome, string email, string departamento);
    Professor(int id, int numeroUSP, string nome, string email, string departamento);
    virtual ~Professor();
};

#endif // PROFESSOR_H
