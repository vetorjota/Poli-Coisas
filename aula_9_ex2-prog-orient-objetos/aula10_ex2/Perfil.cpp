#include "Perfil.h"

#include "Publicacao.h"
#include "Evento.h"
#include <iostream>
#include <string>

#define MAXIMO_PUBLICACOES 20
#define MAXIMO_SEGUIDORES 2

using namespace std;

void Perfil::adicionarSeguidor(Perfil* seguidor){

    try{

    if (seguidor == this) throw new invalid_argument ("Seguidor nao pode ser o proprio perfil");


    for (int i = 0; i < quantidadeDeSeguidores; i++){ //invalid
        if (seguidores[i] == seguidor) throw new invalid_argument ("Seguidor ja segue o perfil");
    }

    if(quantidadeDeSeguidores == MAXIMO_SEGUIDORES) throw new invalid_argument ("Maximo de seguidores atingido");


    this->seguidores[quantidadeDeSeguidores] = seguidor;
    quantidadeDeSeguidores++;

    string t = ("Novo seguidor: " + seguidor->getNome() ) ;
    this->publicacoesRecebidas[quantidadeDePublicacoesRecebidas] = new Publicacao(this,t);
    quantidadeDePublicacoesRecebidas++;

    }catch (invalid_argument *e){
        cout << "Erro: " << e->what() << endl;
        delete e;
    }

}


bool Perfil::publicar(string texto){

  if (this->quantidadeDePublicacoesFeitas < MAXIMO_PUBLICACOES){
    //Armazenamento nas feitas

    publicacoesFeitas[quantidadeDePublicacoesFeitas] = new Publicacao(this,texto);


    //Divulgacao aos seguimores
    if (this->quantidadeDeSeguidores != 0){
      for (int i = 0; i < quantidadeDeSeguidores; i++){
        this->seguidores[i]->receber( publicacoesFeitas[quantidadeDePublicacoesFeitas] );
      }
    }

    this->quantidadeDePublicacoesFeitas++;
    return true;
  }

  else return false;

}

bool Perfil::publicar(string texto, string data){

    if (this->quantidadeDePublicacoesFeitas < MAXIMO_PUBLICACOES){

    publicacoesFeitas[quantidadeDePublicacoesFeitas] = new Evento(this,texto,data);

        if (this->quantidadeDeSeguidores != 0){
            for (int i = 0; i < quantidadeDeSeguidores; i++){
                this->seguidores[i]->receber( publicacoesFeitas[quantidadeDePublicacoesFeitas] );
            }
        }

        this->quantidadeDePublicacoesFeitas++;
        return true;
    }

    else return false;

}





// =========================== GETTERS E SETTERS ==========================================================


string Perfil::getNome(){
    return this->nome;
}


int Perfil::getQuantidadeDePublicacoesFeitas(){
    return quantidadeDePublicacoesFeitas;
}

int Perfil::getQuantidadeDePublicacoesRecebidas(){
    return quantidadeDePublicacoesRecebidas;
}

int Perfil::getQuantidadeDeSeguidores(){
    return quantidadeDeSeguidores;
}

Publicacao** Perfil::getPublicacoesRecebidas(){
    return publicacoesRecebidas;
}

Publicacao** Perfil::getPublicacoesFeitas(){
    return publicacoesFeitas;
}

Perfil** Perfil::getSeguidores(){
    return seguidores;
}

//              =========================================================================================


void Perfil::imprimir() {

    cout << endl << "Nome: " << nome << " - id: " << this->getId() << endl;

    if (quantidadeDeSeguidores == 0) cout << "Sem seguidor " << endl;

    else {
        for (int i = 0; i < quantidadeDeSeguidores; i++) {
        cout << "Seguidor "<< seguidores[i]->getNome() << endl;
        }}

    cout << "Numero de publicacoes feitas: " << quantidadeDePublicacoesFeitas << endl;
    for (int i = 0; i < quantidadeDePublicacoesFeitas; i++) publicacoesFeitas[i]->imprimir();

    cout << "Numero de publicacoes recebidas: " << quantidadeDePublicacoesRecebidas << endl;
    for (int i = 0; i < quantidadeDePublicacoesRecebidas; i++) publicacoesRecebidas[i]->imprimir();



    }






int Perfil::getUltimoId(){
    return ultimoId;
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

Perfil::~Perfil(){
 cout << "Destrutor de perfil: " << nome << " - Quantidade de publicacoes feitas: " << quantidadeDePublicacoesFeitas << endl;

 if (quantidadeDePublicacoesFeitas != 0) {
  for (int i = 0; i < quantidadeDePublicacoesFeitas; i++){
    delete publicacoesFeitas[i];
    quantidadeDePublicacoesFeitas--;
  }
 }

 cout << "Perfil deletado" << endl;

}
