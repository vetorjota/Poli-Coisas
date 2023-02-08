#include "Perfil.h"

#include "Publicacao.h"
#include "Evento.h"
#include "Mensagem.h"
#include <iostream>
#include <string>
#include <list>
#include <vector>
#include <stdexcept>



using namespace std;

void Perfil::adicionarSeguidor(Perfil* seguidor){

    try{

    if (seguidor == this) throw new invalid_argument ("Seguidor nao pode ser o proprio perfil");
    if (!seguidores->empty()){
        for (unsigned int i = 0; i < seguidores->size(); i++){
            if (seguidores->at(i) == seguidor ) throw new invalid_argument ("Seguidor ja segue o perfil");
        }
    }

    seguidores->push_back(seguidor);

    string t = ( "Novo seguidor: " + seguidor->getNome() ) ;
    this->receber(new Mensagem(this,t));


    }catch (invalid_argument *e){
        cout << "Erro: " << e->what() << endl;
        delete e;
    }

}


void Perfil::publicar(string texto){

    //Armazenamento nas feitas

    publicacoesFeitas->push_back( new Mensagem(this,texto) );

    //Divulgacao aos seguimores
    if (!(this->seguidores->empty())){

      for (unsigned int i = 0; i < seguidores->size() ; i++){
        this->seguidores->at(i)->receber( publicacoesFeitas->back() );
      }
    }

}

void Perfil::publicar(string texto, string data){


    publicacoesFeitas->push_back( new Evento(this,texto,data) );

    if (!(this->seguidores->empty())){

      for (unsigned int i = 0; i < seguidores->size() ; i++){
        this->seguidores->at(i)->receber( publicacoesFeitas->back() );
      }
    }
}





// =========================== GETTERS E SETTERS ==========================================================


string Perfil::getNome(){
    return nome;
}


list<Publicacao*>* Perfil::getPublicacoesRecebidas(){
    return publicacoesRecebidas;
}

list<Publicacao*>* Perfil::getPublicacoesFeitas(){
    return publicacoesFeitas;
}

vector<Perfil*>* Perfil::getSeguidores(){
    return seguidores;
}

//              =========================================================================================


//void Perfil::imprimir() {


    /*
    cout << endl << "Nome: " << nome << " - id: " << this->getId() << endl;

    if (seguidores->empty()) cout << "Sem seguidor " << endl;

    else {
        for (int i = 0; i < seguidores->size() ; i++) {
        cout << "Seguidor "<< seguidores->at(i)->getNome() << endl;
        }}

    cout << "Numero de publicacoes feitas: " << publicacoesFeitas->size() << endl;
    list<Publicacao*>::iterator i_f = publicacoesFeitas->begin();
    while (i_f != publicacoesFeitas->end()){
        (*i_f)->imprimir();
        i_f++;
        cout << endl;
    }


    cout << "Numero de publicacoes recebidas: " << publicacoesRecebidas->size() << endl;
    list<Publicacao*>::iterator i_r = publicacoesRecebidas->begin();
    while (i_r != publicacoesRecebidas->end()){
        (*i_r)->imprimir();
        i_r++;
        cout << endl;
    }*/


//}




int Perfil::getUltimoId(){
    return ultimoId;
}

void Perfil::setUltimoId(int ultimoId){
    Perfil::ultimoId = ultimoId;
}

int Perfil::getId(){
    return id;
}


// ================= CONSTRUTOR E DESTRUTOR =================================================================

int Perfil::ultimoId = 0;

Perfil::Perfil(string nome){
 this->nome = nome;
 this->id = this->getUltimoId() + 1;
 this->ultimoId = this->id;

}

Perfil::Perfil(int id,string nome){
    this->id = id;
    this->nome = nome;
}

Perfil::~Perfil(){
 cout << "Destrutor de perfil: " << nome << " - Quantidade de publicacoes feitas: " << publicacoesFeitas->size() << endl;

 while (!publicacoesFeitas->empty()) {

    Publicacao *ultima = publicacoesFeitas->back();
    delete ultima;
 }

 delete publicacoesFeitas;

 cout << "Perfil deletado" << endl;

}
