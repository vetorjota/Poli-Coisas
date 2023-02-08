#include "Professor.h"

string Professor::getDepartamento(){
    return departamento;
}

void Professor::imprimir() {

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



bool Professor::receber(Publicacao* p) {


    if (this->quantidadeDePublicacoesRecebidas < MAXIMO_PUBLICACOES){

        publicacoesRecebidas[quantidadeDePublicacoesRecebidas] = new Publicacao(p->getAutor(),p->getTexto());
        this->quantidadeDePublicacoesRecebidas++;

        return true;
    }

    else return false;

}

Professor::Professor(int numeroUSP, string nome, string email, string departamento) : Pessoa(numeroUSP,nome,email)
{
    this->departamento = departamento;
}

Professor::~Professor()
{
    //dtor
}
