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

 virtual void imprimir(); 
 void curtir(Perfil* quemCurtiu);

 // Getters
 string getTexto();
 Perfil* getAutor();
 virtual int getCurtidas(); 

 // Setters
 void setTexto(string nome);
 void setAutor(Perfil* autor);

  // Construtor
 Publicacao(Perfil* autor, string texto);
 // Destrutor
 virtual ~Publicacao();







};

#endif // PUBLICACAO_H
