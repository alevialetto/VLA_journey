# Progressi

## ISTRUZIONI DI LAVORO

- Attivare il venv:
  .\.venv\Scripts\activate          # serve solo per python e pip

- Comandi Git a fine sessione:
  git status                        # cosa è cambiato
  git add .                         # metti tutto nella "scatola"
  git commit -m "cosa ho fatto"     # salva una versione in locale
  git push                          # manda su GitHub

- Primo messaggio di ogni chat (nel progetto Claude "VLA journey"):
  Leggi PROGRESSI.md. Oggi è [sabato / sera infrasettimanale],
  ho [4 / 2] ore e voglio fare: [obiettivo della sessione].


## Settimana 1 (7-13 nov) - Setup e basi
- Fatto (aggiunto): mini-corso di Python in 6 lezioni, con esercizi in
  00_Setup/python_basi/ (01 sintassi, 02 liste e dizionari, 03 cicli, 04 funzioni,
  05 classi, 06 import e numpy.random); celle # %% in VS Code (estensione Jupyter + ipykernel nel venv)
- Capito (aggiunto): indici negativi e slicing (fine esclusa); b = a non copia, serve .copy();
  `nome[...] = ...` modifica l'oggetto, `nome = ...` sposta l'etichetta; return al posto di print;
  variabili locali nelle funzioni e nei metodi; self e attributi (self.x = parametro);
  import e `if __name__ == "__main__"`; seme di rng per rumore riproducibile;
  anello chiuso Giunto + ControlloreP con saturazione
- Da ripassare (non bloccanti):
  - 03: bonus punto 6 con kp = 1.5 e 2.5
  - 04: chiamate di prova per saturazione, controllo_p, statistiche, simula_p, azzera_primo
  - 05: punto 5 (errore guidato senza self) saltato
  - 06: verificare il punto 6 (utils.py e import); rinominare il file senza la &
- Fatto (aggiunto): esercizio finale classe Robot in 00_Setup/esercizio_robot.py:
  Robot (nome, n_giunti, seed; q come dizionario), stato(), misura(sigma),
  passo(riferimenti, kp, sigma, dt), funzioni simula() ed estrai(), errore a regime
  e deviazione standard sugli ultimi 50 campioni
- Capito (aggiunto): rng ha uno stato interno (il seme è la condizione iniziale) e
  .normal() è la distribuzione da cui pesca; return self.q senza .copy() espone lo
  stato interno (traiettoria con stati tutti uguali); metodo (self) contro funzione
  normale (riceve l'oggetto come argomento); dt = passo di Eulero (q += u*dt),
  polo 1 - kp*dt; l'anello chiuso filtra il rumore del sensore (std a regime < sigma)
- Dubbi: deviazione standard teorica (circa 0.011) contro quella misurata (0.0064) con soli 50 campioni