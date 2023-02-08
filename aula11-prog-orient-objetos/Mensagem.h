#ifndef MENSAGEM_H
#define MENSAGEM_H

#include "Publicacao.h"


class Mensagem : public Publicacao
{
    public:
        Mensagem(Perfil* autor, string texto);
        virtual ~Mensagem();

        void imprimir();
        void curtir(Perfil* quemCurtiu);

    protected:

    private:
};

#endif // MENSAGEM_H
