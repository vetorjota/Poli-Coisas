#ifndef REDESOCIAL_H
#define REDESOCIAL_H

#include <iostream>
#include <string>
#include "Perfil.h"

using namespace std;


class RedeSocial {
public:

    RedeSocial(int numeroMaximoDePerfis);
    virtual ~RedeSocial();

    int getQuantidadeDePerfis();
    Perfil** getPerfis();
    bool adicionar(Perfil* p);
    virtual void imprimir();

    Perfil* getPerfil(int id);

private:
    Perfil** perfis;
    int numeroMaximoDePerfis;
    int quantidadeDePerfis = 0;
};

#endif // REDESOCIAL_H
