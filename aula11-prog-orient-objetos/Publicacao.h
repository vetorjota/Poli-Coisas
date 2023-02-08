#ifndef PUBLICACAO_H
#define PUBLICACAO_H

#include "Perfil.h"
#include <string>
#include <iostream>

using namespace std;

class Perfil; //prototipo

class Publicacao {

protected:
 string texto;
 Perfil* autor;
 int curtidas;

public:

 virtual void imprimir() = 0;
 virtual void curtir(Perfil* quemCurtiu) = 0; // puramente virtual

 // Getters
 string getTexto();
 Perfil* getAutor();
 virtual int getCurtidas();


  // Construtor
 Publicacao(Perfil* autor, string texto);
 // Destrutor
 virtual ~Publicacao();

};

#endif // PUBLICACAO_H
