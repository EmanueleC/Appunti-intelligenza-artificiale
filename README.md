# Appunti-intelligenza-artificiale

## Appunti del corso di Intelligenza artificiale in italiano (a.a. 2017/2018) - università degli studi di Padova

### Contenuti coperti finora:

- Breve introduzione dell'intelligenza artificiale
- Tipi di agenti e di ambienti (specifica p.e.a.s.)
- Problem solving agents ed esempi di formulazione di problemi
- Ricerca su alberi
- Ricerca non informata e informata
- Stable matching: algoritmo di Gale-Shapley
- Problemi con vincoli (in progress)
  - Tipi di consistenza locale (node, arc, path consistency)
  - Vincoli soft (esempi di proiezione e combinazione)
- Sistemi di voto
  - k-approval (plurality, majority, 3-approval...)
  - Borda
  - Copeland
  - i formalismi dei vincoli soft e delle reti CSP
- Reti bayesiane (in progress)
  - Inferenza probabilistica in una rete bayesiana (enumerazione ed eliminazione)
- Introduzione e cenni di reinforcement learning (in progress)

### Esercizi

- Stable matching problem
- Dare esempi di problemi csp arco consistenti ma non consistenti
- Problema csp con backtracking, forward checking e arc consistency
- Esercizio di combinazione per i vincoli soft
- Esercizio di inferenza probabilistica data una rete bayesiana (sia per eliminazione che per enumerazione)

### Laboratori

- Problem solving agent vacuum e space problem (Python + networkx)
- Ricerca in ampiezza su un grafo (Python + networkx)
- Algoritmo di stable matching (Gale-Shapley) (Python + networkx)
- Problema di colorazione di un grafo (Python + networkx + python-constraint)
- Problema delle n regine (Python + python-constraint)
- Voting problem (Python + networkx)
- 10-Bandit problem (Python)
- Reti neurali: classificazione di vini (Python + Keras + Theano)
- Reti neurale da zero (niente dipendenze, derivate calcolate esplicitamente) (Python)

### Approfondimento - Paper

- Predizione della struttura di una proteina in nun reticolo bidimensionale
- Definizione di problema con vincoli
- Hill climbing search
- Q-Learning

Fonti:

- Gabriela Czibula, Maria-Iuliana Bocicor and Istvan-Gergely Czibula "A Reinforcement Learning Model for Solving the Folding Problem" Babes-Bolyai University, Department of Computer Science
- William E. Hart, Alantha Newman Protein Structure Prediction with Lattice Models Sandia National Laboratories & Massachusetts Institute of Technology
- Mao Chen, Wen-Qi Huang A Branch and Bound Algorithm for the Protein Folding Problem in the HP Lattice Model School of Computer Science and Technology, Huazhong University of Science and Technology, Wuhan 430074, China
