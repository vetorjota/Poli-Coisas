#ifndef PERFILINEXISTENTE_H
#define PERFILINEXISTENTE_H

#include <stdexcept>
using namespace std;


class PerfilInexistente : public logic_error
{
    public:
        PerfilInexistente();
        virtual ~PerfilInexistente();

    protected:

    private:
};

#endif // PERFILINEXISTENTE_H
