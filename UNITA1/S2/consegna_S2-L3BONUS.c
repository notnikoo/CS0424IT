#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#define N 32
#define M 64

typedef struct
{
	char nome[N], cognome[N], via[M], citta[M], provincia[3];
	int num_civico, giorno_data_nascita, mese_data_nascita, anno_data_nascita;
} persona;

int main()
{
	persona p;

	printf("Inserire il nome della persona\n");
	scanf("%s", p.nome);

	printf("Inserire il cognome della persona\n");
	scanf("%s", p.cognome);

	printf("Inserire l'indirizzo di %s %s\nvia ", p.nome, p.cognome);
	scanf("%s", p.via);
	printf("n ");
	scanf("%d", &p.num_civico);
	printf("Citta' ");
	scanf("%s", p.citta);
	printf("Provincia (solo la sigla) ");
	scanf("%s", p.provincia);

	printf("Inserire la data di nascita di %s %s (formato: dd/mm/aaaa)\n", p.nome, p.cognome);
	scanf("%d/%d/%d", &p.giorno_data_nascita, &p.mese_data_nascita, &p.anno_data_nascita);

	printf("\n\nPersona inserita:\n");
	printf("%s %s\n  Nato il:\n    %d/%d/%d\n  Residente in:\n    via %s, %d\n    %s (%s)\n", p.nome, p.cognome, p.giorno_data_nascita, p.mese_data_nascita, p.anno_data_nascita, p.via, p.num_civico, p.citta, p.provincia);
}
