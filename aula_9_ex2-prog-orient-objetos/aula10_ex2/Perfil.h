#ifndef PERFIL_H
#define PERFIL_H

#include <iostream>
#include <string>
#include "Publicacao.h"


#define MAXIMO_PUBLICACOES 20
#define MAXIMO_SEGUIDORES 2

using namespace std;

class Publicacao;


class Perfil {
  //Atributos
protected:

  int id;
  static int ultimoId;

  string nome;


  Perfil* seguidores[MAXIMO_SEGUIDORES];
  Publicacao* publicacoesFeitas[MAXIMO_PUBLICACOES];
  Publicacao* publicacoesRecebidas[MAXIMO_PUBLICACOES];

  int quantidadeDeSeguidores = 0;
  int quantidadeDePublicacoesFeitas = 0;
  int quantidadeDePublicacoesRecebidas = 0;

public:
  //Métodos
    virtual void adicionarSeguidor(Perfil* seguidor);

    virtual bool publicar(string texto);
    virtual bool publicar(string texto, string data);

    virtual bool receber(Publicacao* p) = 0;

    virtual void imprimir(); // mudar como mais conveniente

  //Getters e Setters
    string getNome();

    int getId();
    static int getUltimoId();


    virtual int getQuantidadeDePublicacoesFeitas();
    virtual Publicacao** getPublicacoesFeitas();

    virtual Publicacao** getPublicacoesRecebidas();
    virtual int getQuantidadeDePublicacoesRecebidas();

    virtual Perfil** getSeguidores();
    virtual int getQuantidadeDeSeguidores();



  // Construtor
    Perfil(string nome); //dev
 // Destrutor
    virtual ~Perfil(); //dev

};

#endif // PERFIL_H
