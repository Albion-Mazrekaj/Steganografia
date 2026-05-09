# Stegano-Grafia/Albion_Mazrekaj
# Projekti i Steganografisë me Imazhe

## Përshkrimi i përgjithshëm

Ky projekt trajton konceptin e steganografisë në imazhe digjitale, një teknikë e cila përdoret për të fshehur të dhëna brenda një imazhi pa ndryshuar dukshëm pamjen e tij. Ideja kryesore është që mesazhi të ekzistojë brenda imazhit pa u vërejtur nga përdoruesi.

Në këtë implementim është përdorur gjuha Python së bashku me bibliotekën Pillow për manipulimin e imazheve. Projekti është i ndarë në dy pjesë kryesore: procesi i fshehjes së mesazhit (embedding) dhe procesi i nxjerrjes së mesazhit (extraction).

---

## Si funksionon sistemi

Procesi i steganografisë në këtë projekt bazohet në teknikën **Least Significant Bit (LSB)**. Çdo pixel i një imazhi përbëhet nga tre vlera kryesore (RGB). Duke ndryshuar vetëm bitin më pak të rëndësishëm të këtyre vlerave, mund të ruhet informacion pa ndikuar në mënyrë të dukshme në pamjen e imazhit.

Në fazën e embedding, programi merr një mesazh dhe e shndërron atë në formë binare. Ky mesazh pastaj futet gradualisht në pixel-at e imazhit. Pas përfundimit, krijohet një imazh i ri i quajtur zakonisht `stego-img.bmp`, i cili përmban mesazhin e fshehur.

Në fazën e extraction, programi lexon pixel-at e imazhit të modifikuar dhe nxjerr bitët e fshehur për të rikonstruktuar mesazhin origjinal.

---

## Struktura e projektit

Projekti përbëhet nga disa skedarë kryesorë. Skedari `embed.py` është përgjegjës për fshehjen e mesazhit brenda imazhit, ndërsa `extract.py` përdoret për nxjerrjen e këtij mesazhi. Ekziston edhe një folder `images/` ku ruhen imazhet hyrëse që përdoren për testim.

---

## Ekzekutimi i projektit

Për të ekzekutuar projektin është e nevojshme që Python të jetë i instaluar në sistem, së bashku me bibliotekën Pillow. Pas konfigurimit të ambientit, fillimisht ekzekutohet skedari për embedding, i cili gjeneron një imazh të ri me mesazhin e fshehur. Më pas mund të ekzekutohet skedari i extraction për të rikthyer mesazhin origjinal.

---

## Konkluzion

Ky projekt demonstron në mënyrë praktike se si të dhënat mund të fshihen brenda imazheve digjitale duke përdorur teknikën LSB. Ai tregon se si manipulimi i vogël në nivelin e pikselëve mund të përdoret për ruajtjen e informacionit pa ndryshuar pamjen vizuale të imazhit, duke e bërë steganografinë një metodë të thjeshtë por efektive për fshehjen e të dhënave.
