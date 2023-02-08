#include "Funcionario.h"



/*Crie uma classe Funcionario (sem superclasse), a qual possui um nomeCompleto (string) e
um salario (double). A classe deve possuir apenas um construtor (recebendo o
nomeCompleto e o salario) e métodos getters. Usando o conceito de herança múltipla, faça
com que um Professor seja subclasse de Pessoa e de Funcionario.
Altere o método imprimir do Professor para apresentar também esses dados. Faça o
construtor do Professor receber o salário e use o nome passado como nomeCompleto. No
main crie também um Funcionario e um Professor e os imprima. */

string Funcionario::getNomeCompleto(){
    return nomeCompleto;
}

double Funcionario::getSalario(){
    return salario;
}


Funcionario::Funcionario(string nomeCompleto, double salario)
{
    this->nomeCompleto = nomeCompleto;
    this->salario = salario;
}

Funcionario::~Funcionario()
{
    //dtor
}
