#include <stdio.h>

void menu(){

    printf("Inizio nuova partita\n");                                   #creazione funzione menu
    printf("Premi il tasto A per cominciare una nuova partita\n");
    printf("Premi il tasto B per terminare il gioco\n");

}

int start(){
    int punteggio = 0;                                                  #creazione della partita
    char nome[15];
    int risposta;
    printf("Inserisci il tuo nickname\n");
    scanf("%s", &nome);

    printf("Domanda 1: Qual è l'oceano più grande?\n\n");
    printf("1-Oceano Indiano\n2-Oceano Pacifico\n3-Oceano Atlantico\n");
    scanf("%d", &risposta);

    if (risposta == 2){
        printf("Risposta corretta\n");
        punteggio++;
        printf("Il tuo punteggio è: %d\n", punteggio);
    } else if (risposta != 2){
        printf("Risposta sbagliata\n");
        printf("Il tuo punteggio è: %d\n", punteggio);
    }


    printf("Domanda 1: Qual è la lingua più parlata al mondo?\n\n");
    printf("1-Cinese\n2-Inglese\n3-Quechua\n");
    scanf("%d", &risposta);

    if (risposta == 1){
        printf("Risposta corretta\n");
        punteggio++;
        printf("Il tuo punteggio è: %d\n", punteggio);
    } else if (risposta != 1){
        printf("Risposta sbagliata\n");
        printf("Il tuo punteggio è: %d\n", punteggio);
    }

    printf("Partita conclusa, punteggio di %s : %d\n", nome, punteggio);

    return 0;
    
}

int main(){                                                                 


    char tasto;
    menu();
    scanf("%c", &tasto);

    if (tasto == 'B' || tasto == 'b'){
        printf("Partita terminata\n");
        return 0;
    }

    do {
        start();
        menu();
        scanf("%c", &tasto);
    } while (tasto == 'A' || tasto == 'a');

return 0;

}