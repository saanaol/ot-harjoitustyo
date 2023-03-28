# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksella on mahdollista luoda pdf-muotoinen lasku, josta löytyvät laskuttajan ja laskutettavan tiedot sekä laskun viitenumero. 

## Käyttäjät

Sovelluksella on yksi käyttäjärooli eli laskuttaja/normaali käyttäjä.

## Käyttöliittymä

Sovellus aukeaa “syötä tiedot” -näkymään, jossa käyttäjä voi syöttää tarvittavat tiedot, jonka jälkeen sovellus luo laskulle viitenumeron ja tulostaa sen pdf-muotoisena. 

## Perusversion tarjoama toiminnallisuus

### Ennen tarvittavien tietojen syöttämistä

- Käyttäjälle aukeaa näkymä, jossa tarvittavat tietoja kysytään ja johon ne voidaan syöttää
- Sovellus edellyttää tietojen täyttämistä, jotta lasku on mahdollista muodostaa
- Laskuttajan tiedot ovat etunimi, sukunimi, tilinumero
- Laskutettavan tiedot ovat etunimi, sukunimi, tilinumero

### Tietojen syöttämisen jälkeen
- Sovellus luo laskulle viitenumeron 
- Sovellus kokoaa tiedot laskua varten 
- Sovellus tulostaa valmiin laskun pdf-muodossa

## Jatkokehitysideoita

Perusversion valmistuttua sovellusta on mahdollista kehittää esimerkiksi seuraavilla toiminnallisuuksilla:
- Tilinumeron oikeellisuuden tarkastaminen
- Nimissä kirjoitusasun tarkistus (alkukirjaimet isolla ja muut kirjaimet pienellä)
- Tuoteluettelo, jossa on eri tuotteet ja niiden hinnat
