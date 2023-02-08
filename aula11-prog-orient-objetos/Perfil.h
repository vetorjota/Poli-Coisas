#ifndef PERFIL_H
#define PERFIL_H

#include <iostream>
#include <string>
#include <list>
#include <vector>
#include "Publicacao.h"


using namespace std;

class Publicacao;


class Perfil {
  //Atributos
protected:

  int id;
  static int ultimoId;

  string nome;

  vector<Perfil*>* seguidores = new vector<Perfil*>();

  list<Publicacao*>* publicacoesFeitas = new list<Publicacao*>();
  list<Publicacao*>* publicacoesRecebidas = new list<Publicacao*>();


public:
  //Metodos
    virtual void adicionarSeguidor(Perfil* seguidor);

    virtual void publicar(string texto);
    virtual void publicar(string texto, string data);

    virtual void receber(Publicacao* p) = 0;

    virtual void imprimir() = 0; // como mais conveniente

  //Getters e Setters

    string getNome();
    int getId();
    static int getUltimoId();
    static void setUltimoId(int ultimoId);


    virtual list<Publicacao*>*  getPublicacoesFeitas();
    virtual list<Publicacao*>*  getPublicacoesRecebidas();


    virtual vector<Perfil*>* getSeguidores();
    // === virtual int getQuantidadeDeSeguidores();

    // === void removerPublicacoesRecebidasDe(Perfil* autor);


  // Construtores

    Perfil(string nome);
    Perfil(int id, string nome);

 // Destrutor
    virtual ~Perfil();

};

#endif // PERFIL_H
