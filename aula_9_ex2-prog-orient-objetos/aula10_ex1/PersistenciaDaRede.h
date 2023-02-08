#ifndef PERSISTENCIADAREDE_H
#define PERSISTENCIADAREDE_H

#include <string>
#include "RedeSocial.h"


class PersistenciaDaRede
{
    public:
        PersistenciaDaRede(string arquivo);
        virtual ~PersistenciaDaRede();
        void salvar(RedeSocial* r);

    protected:

    private:
        string arquivo;
};

#endif // PERSISTENCIADAREDE_H
