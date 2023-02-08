#ifndef PROFESSOR_H
#define PROFESSOR_H

#include "Pessoa.h"
#include "Funcionario.h"
#include <string>


class Professor : public Pessoa
{
private:
    string departamento;

protected:

public:

    string getDepartamento();

    bool receber(Publicacao* p);

    void imprimir();

    Professor(int numeroUSP, string nome, string email, string departamento);
    virtual ~Professor();
};

#endif // PROFESSOR_H
