#ifndef COMBO_H
#define COMBO_H

#include "PlanoDeInternet.h"
#include "PlanoDeTelefone.h"
#include "Produto.h"

#include <string>
using namespace std;

// Crie atributos e faca outras alteracoes necessarias

class Combo : public Produto{
protected:
    PlanoDeTelefone* telefone;
    PlanoDeInternet* internet;

public:
    Combo(string nome, PlanoDeTelefone* telefone, PlanoDeInternet* internet);
    virtual ~Combo();

    double getPreco();
    void imprimir();

};

#endif // COMBO_H
