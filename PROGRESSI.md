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
- Fatto: Python + venv (3.13), Git, GitHub, repo VLA_journey con cartelle per fase,
  quickstart NumPy, .gitignore, rimosso .vscode dal repo, attivazione venv
  da terminale (sbloccata execution policy di PowerShell), interprete .venv in VS Code,
  account Hugging Face e W&B (ora dentro CoreWeave Forge, piano Free/Academic),
  progetto Claude "VLA journey" con cartella collegata
- Capito: flusso status → add → commit → push (il commit resta in locale,
  è il push che manda su GitHub); .gitignore blocca solo i file nuovi,
  per quelli già tracciati serve `git rm --cached`; il venv serve solo per python/pip;
  nel terminale i commenti vanno dopo # (le parentesi danno errore)
- GPU: nessuna NVIDIA (Ryzen 5 3500U, grafica integrata) → CPU per le prime settimane,
  poi Colab/Kaggle
- Manca: esercizio classe Robot (basi Python: classi, dizionari, cicli, funzioni)
- Dubbi: ...