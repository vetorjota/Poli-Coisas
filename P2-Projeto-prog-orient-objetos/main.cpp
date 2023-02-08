#include <iostream>
#include "Contrato.h"
#include "PlanoDeInternet.h"
#include "PlanoDeTelefone.h"
#include "Produto.h"
#include "Combo.h"

using namespace std;

int main() {
    // Criacao de um plano de internet basico e impressao

    PlanoDeInternet* intBasico = new PlanoDeInternet("Plano Basico",1);
    intBasico->imprimir();

    // Criacao de plano de telefone só voz e impressao

    PlanoDeTelefone* voz = new PlanoDeTelefone("Plano sem internet", 0, 100);
    voz->imprimir();


    // Criacao de um Combo composto pelo plano de telefone voz e dados e pelo plano de internet medio
    // Impressao do combo

    PlanoDeTelefone* vozEdados = new PlanoDeTelefone("Plano voz+dados",100,50);
    PlanoDeInternet* intMedio = new PlanoDeInternet("Plano medio", 20);
    Combo* combo = new Combo("Combo avancado", vozEdados, intMedio);
    combo->imprimir();

    // Criacao de cliente Maria e contrato para Maria

    Cliente* mar = new Cliente("Maria");
    Contrato* contrato = new Contrato(mar);

    // Colocacao nesse contrato o PlanoDeInternet "Plano Basico",
    // o PlanoDeTelefone "Plano sem internet" e o Combo "Combo avancado"

    contrato->adicionar(intBasico);
    contrato->adicionar(voz);
    contrato->adicionar(combo);

    // Impressao do contrato e destruicao

    contrato->imprimir();
    delete contrato;

    return 0;
}
