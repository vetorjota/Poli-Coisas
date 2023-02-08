#ifndef PLANODEINTERNET_H
#define PLANODEINTERNET_H

#include "Produto.h"

#include <string>
using namespace std;

// Crie atributos e faca outras alteracoes necessarias

class PlanoDeInternet : public Produto {
private:

    int velocidade;

public:
    PlanoDeInternet(string nome, int velocidade);
    virtual ~PlanoDeInternet();

    int getVelocidade();
    double getPreco();
};

#endif // PLANODEINTERNET_H
