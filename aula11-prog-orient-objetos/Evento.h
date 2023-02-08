#ifndef EVENTO_H
#define EVENTO_H

#include "Publicacao.h"
#include <string>

class Evento : public Publicacao
{
    public:
        Evento(Perfil* autor, string texto, string data);
        virtual ~Evento();
        string getData();
        void imprimir();
        void curtir(Perfil* quemCurtiu);


    protected:

    private:
        string data;
};

#endif // EVENTO_H
