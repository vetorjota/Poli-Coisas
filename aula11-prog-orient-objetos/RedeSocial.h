#ifndef REDESOCIAL_H
#define REDESOCIAL_H

#include <iostream>
#include <string>
#include <vector>
#include "Perfil.h"

using namespace std;


class RedeSocial {
public:

    RedeSocial();
    virtual ~RedeSocial();

    vector<Perfil*>* getPerfis();
    void adicionar(Perfil* p);
    Perfil* getPerfil(int id);

    void imprimir();

private:
    vector<Perfil*>* perfis;

};



#endif // REDESOCIAL_H
