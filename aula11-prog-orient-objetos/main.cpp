#include <iostream>
#include <string>
#include <stdexcept>

#include "Perfil.h"
#include "RedeSocial.h"
#include "Professor.h"
#include "Disciplina.h"
#include "Aluno.h"
#include "PersistenciaDaRede.h"
#include "PerfilInexistente.h"

using namespace std;

Perfil* selecionarPerfil(RedeSocial* insta){

    vector<Perfil*>::iterator item_perfil = insta->getPerfis()->begin();

    while (item_perfil != insta->getPerfis()->end()){
        cout << (*item_perfil)->getId() << ") " << (*item_perfil)->getNome() << endl;
        item_perfil++;}

    cout << "Digite o id ou 0 para cancelar: " << endl;

    int idEscolhido;
    cin >> idEscolhido;

    if (idEscolhido != 0 ){
        Perfil* p = insta->getPerfil(idEscolhido);
        return p;
    }

    else return NULL;

}


Perfil* cadastrarPerfil(){

    int nusp;
    string nome;
    string email;
    string prof;

    cout << "Informe os dados do Perfil" << endl;
    cout << "Numero USP: " << endl;
    cin >> nusp;
    cout << "Nome: " << endl;
    cin.ignore(100, '\n'); // Ignorando ate 100 caracteres que sobraram de cin anterior
    getline(cin, nome); // guardando uma linha em nome
    cout << "Email: " << endl;
    cin >> email;
    cout << "Professor (s/n): " << endl;
    cin >> prof;

      if (prof == "s"){
        string depto;

        cout << "Departamento: " << endl;
        cin >> depto;

        Professor *p = new Professor(nusp,nome,email,depto);
        return p;
      }

      else{
        Aluno *a = new Aluno(nusp,nome,email);
        return a;
      }

}


Disciplina* cadastrarDisciplina(RedeSocial* insta){

    string sigla;
    string nome;

    cout << "Informe os dados da Disciplina" << endl;
    cout << "Sigla: " << endl;
    cin >> sigla;
    cout << "Nome: " << endl;
    cin.ignore(100, '\n'); // Ignorando ate 100 caracteres que sobraram de cin anterior
    getline(cin, nome); // guardando uma linha em nome
    cout << "Responsavel: " << endl;

    Perfil* p = selecionarPerfil(insta);
    if (p == NULL) return NULL;

    Professor* prof_res = dynamic_cast<Professor*> (p);
    if (prof_res != NULL){
        Disciplina *d = new Disciplina(sigla,nome,prof_res );
        return d;}
    else {
        cout << "Somente professores podem ser responsaveis por disciplinas"<< endl;
        return NULL;
        }

}



int main() {

  string arquivoTxt;

  cout << "Arquivo: " << endl;
  cin >> arquivoTxt;

  PersistenciaDaRede* persInsta = new PersistenciaDaRede(arquivoTxt);
  RedeSocial* insta = persInsta->carregar();
  //insta->imprimir();


  int opcao = 5;
  while (opcao != 0){
//-----------------------------------------------------------TELA INICIO

    cout << endl;
    cout << "================================="<< endl;
    cout << "Escolha uma opcao: " << endl;
    cout << "1) Cadastrar Perfil" << endl;
    cout << "2) Cadastrar Disciplina" << endl;
    cout << "3) Logar" << endl;
    cout << "0) Terminar" << endl;
    cin >> opcao;

    if (opcao == 0){
      string salva;
      cout << "Deseja salvar? (s/n) " << endl;
      cin >> salva;
      if (salva == "s") persInsta->salvar(insta);
      else return 0;
    }
//----------------------------------------------------------------TELA Cadastro Perfil
    else if (opcao == 1){
      cout << endl;
      cout << "================================="<< endl;
      insta->adicionar(cadastrarPerfil());
    }
//--------------------------------------------------------------- Tela Cadastro Disciplina
    else if (opcao == 2){

      cout << endl;
      cout << "================================="<< endl;
      Disciplina* disciplina_nova = cadastrarDisciplina(insta);
      if ( disciplina_nova != NULL){
        insta->adicionar(disciplina_nova);
      }
    }
//---------------------------------------------------------------  Tela Logar
    else if (opcao == 3){
      int opcao_login = -1;
      while (opcao_login !=0 ){  // ------ se for teclado 0 volta para menu inicial

        cout << endl;
        cout << "================================="<< endl;
        cout << "Escolha um perfil:"<< endl;

        Perfil* perfilLogado;
        bool logado = 1;

        try {
            perfilLogado = selecionarPerfil(insta);
        }catch(PerfilInexistente *e){
            cout << "Erro: " << e->what() << endl;
            logado = 0;
            delete e;}


        if (perfilLogado == NULL) {
                logado = 0;
                opcao_login = 0;
        }

        while (logado){
            cout << endl;
            cout << "================================="<< endl;

            perfilLogado->imprimir(); // ---------- TELA LOGADA ------

            cin >> opcao_login;

            if (opcao_login == 0){
              logado = 0;
            }

            else if (opcao_login == 1){
              cout << endl;
              cout << "================================="<< endl;

              cout << "Publicacoes feitas:" <<endl;

              list<Publicacao*>::iterator i_f = perfilLogado->getPublicacoesFeitas()->begin();
              while (i_f != perfilLogado->getPublicacoesFeitas()->end()){
                (*i_f)->imprimir();
                i_f++;

                }

            }
            else if (opcao_login == 2){
              cout << endl;
              cout << "================================="<< endl;

              cout << "Publicacoes recebidas:" <<endl;


              int mensagem = 1;
              list<Publicacao*>::iterator i_r = perfilLogado->getPublicacoesRecebidas()->begin();
              while (i_r != perfilLogado->getPublicacoesRecebidas()->end()){
                cout << mensagem << ") ";
                (*i_r)->imprimir();
                i_r++;
                mensagem++;
                }

              cout << "Digite o numero da mensagem para curtir ou 0 para voltar:" << endl;
              mensagem = 0;
              cin >> mensagem;

              if (mensagem != 0 ){     //se for 0 volta para tela "logado"
                int identificador = 1;
                i_r = perfilLogado->getPublicacoesRecebidas()->begin();
                while (i_r != perfilLogado->getPublicacoesRecebidas()->end()){
                    if (identificador == mensagem){
                        (*i_r)->curtir(perfilLogado);
                    }
                    i_r++;
                    identificador++;
                }
              }

            }
            else if (opcao_login == 3){ // --------------------------------------------- Fazer publicacao
              cout << endl;
              cout << "================================="<< endl;

              string sn;
              string data;
              string texto;

              cout << "Evento (s/n):" << endl;
              cin >> sn;

              if (sn == "s"){
                cout << "Data:" << endl;
                cin >> data;
                cout << "Texto:" << endl;
                cin >> texto;
                perfilLogado->publicar(texto,data);

              }

              else if (sn == "n"){
                cout << "Texto:" << endl;
                cin >> texto;
                perfilLogado->publicar(texto);
                }
            }
        //================================================TELA LOGAR 4: SEGUIR ==================================

            else if ((opcao_login == 4) && (dynamic_cast<Disciplina*>(perfilLogado) == NULL)   ){ // nao pode escolher 4 sendo disciplina

                // escolher perfil para seguir

                cout << endl;
                cout << "================================="<< endl;
                cout << "Perfil:"<< endl;

                Perfil* p_seg;

                try {
                    p_seg = selecionarPerfil(insta);
                    if (p_seg != NULL) p_seg -> adicionarSeguidor(perfilLogado);
                    }catch(PerfilInexistente *e){
                        cout << "Erro: " << e->what() << endl;
                        delete e;}



                }

        }



        }
      }
    }
    return 0;}








