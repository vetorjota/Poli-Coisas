#include "RedeSocial.h"
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <stdexcept>

#include "PerfilInexistente.h"

using namespace std;


RedeSocial::RedeSocial(){

  vector<Perfil*>* perfis = new vector<Perfil*>();
  this->perfis = perfis;

}

Perfil* RedeSocial::getPerfil(int id){

    vector<Perfil*>::iterator p1 = perfis->begin();
    while (p1 != perfis->end()){
        if ( (*p1)->getId() == id ) return (*p1);
        p1++;}

    if (p1 == perfis->end()) throw new PerfilInexistente ();

    //NAO FAZER CATCH

}



void RedeSocial::adicionar(Perfil* perfil){

  vector<Perfil*>::iterator p1 = find(perfis->begin(), perfis->end(), perfil);

  if (p1 != perfis->end()) throw new invalid_argument("Perfil ja existente");

  else perfis->push_back(perfil);


}



void RedeSocial::imprimir () {


 cout << "=================Instagram=================" << endl;
 if (!perfis->empty()){
     cout << "Contem " << perfis->size() << " perfis:" << endl;
     for (unsigned int i = 0; i < perfis->size() ; i++){

        cout << "Nome do perfil " << i << ": "<< perfis->at(i)->getNome() << " - Id: " << perfis->at(i)->getId() << endl;
        if (perfis->at(i)->getSeguidores()->empty()) cout << "Sem seguidor." << endl;
        else cout << "Numero de seguidores: " << perfis->at(i)->getSeguidores()->size() << endl;
        cout << endl;
        }}
 else cout << "Sem perfis." << endl;
 cout << "===========================================" << endl;

}




vector<Perfil*>* RedeSocial::getPerfis(){
    return this->perfis;
}


RedeSocial::~RedeSocial() {
  cout << "Destrutor de RedeSocial: " << perfis->size() << " perfis" << endl << endl;

  if (!perfis->empty()){
    for (unsigned int i = 0; i < perfis->size(); i++){
      delete perfis->at(i);
    }
  }

  cout << "RedeSocial deletada " << endl;
}
