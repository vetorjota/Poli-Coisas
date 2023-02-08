#include "RedeSocial.h"
#include <iostream>
#include <string>

#include "PerfilInexistente.h"

using namespace std;

RedeSocial::RedeSocial(int numeroMaximoDePerfis){

  this->numeroMaximoDePerfis = numeroMaximoDePerfis;
  perfis = new Perfil*[numeroMaximoDePerfis];

}

Perfil* RedeSocial::getPerfil(int id){

    if (id > quantidadeDePerfis + 1) throw new PerfilInexistente ();

    for (int i = 0; i < quantidadeDePerfis ; i++){
        if (perfis[i]->getId() == id) {
            return perfis[i];}
    }

    throw new PerfilInexistente ();

    //NAO FAZER CATCH

}



bool RedeSocial::adicionar(Perfil* perfil){


    if (quantidadeDePerfis < numeroMaximoDePerfis){
        //cout << "Adicionando perfil à rede." << endl;

        this->perfis[quantidadeDePerfis] = perfil;
        quantidadeDePerfis ++;


        return true;
    }
    else {
        cout << "Rede social lotada. O perfil não foi adicionado.  === " << endl;
        return false;
        }
}



void RedeSocial::imprimir () {

cout << endl << "------------------------------ " << endl;
 cout << "RedeSocial: " << quantidadeDePerfis << " perfis" << endl;
 cout << "------------------------------ " << endl;
 if (quantidadeDePerfis == 0){
 cout << "Sem perfis" << endl;
 cout << "------------------------------ " << endl;
 } else {
 for (int i = 0; i < quantidadeDePerfis; i++){
 perfis[i]->imprimir();
 cout << "------------------------------ " << endl;
 }
 }
 cout << endl;

}




Perfil** RedeSocial::getPerfis(){
    return this->perfis;
}

int RedeSocial::getQuantidadeDePerfis(){
    return this->quantidadeDePerfis;
}

RedeSocial::~RedeSocial() {
  cout << "Destrutor de RedeSocial: " << quantidadeDePerfis << " perfis" << endl << endl;

  if (quantidadeDePerfis != 0){
    for (int i = 0; i < quantidadeDePerfis; i++){
      delete perfis[i];
    }
    quantidadeDePerfis = 0;
  }

  cout << "RedeSocial deletada " << endl;
}
