#ifndef PLANODETELEFONE_H
#define PLANODETELEFONE_H

#include "Produto.h"

#include <string>
using namespace std;

// Crie atributos e faca outras alteracoes necessarias

class PlanoDeTelefone : public Produto {
protected:

    int minutosDeVoz;
    int franquiaDeDados;

public:
    PlanoDeTelefone(string nome, int franquiaDeDados, int minutosDeVoz);
    virtual ~PlanoDeTelefone();

    int getFranquiaDeDados();
    int getMinutosDeVoz();
    double getPreco();
};

#endif // PLANODETELEFONE_H
