# Quizlet pdf generátor
Ez a program azért jött létre, hogy lehetőség legyen a quizletben tárolt tanulókártyákat ékezethelyes formátumban kinyomtatni.
A szoftver a nyelvtanárok munkályáát igyekszik ezáltal könyebbé tenni.

## Funkciók
A program az alábbi funkciókra képes:
* képes importálni tabulátorral tagolt .txt állományt és excel állományt
* bemimportált állomány a programon belül előnézhető
* lehetőség van a tanulókártyák megfordítására
* a quizlet által használt formátumokban képes ékezethelyes pdf fájlt létrehozni

Az excel fájl felépítésében megegyezik azzal formátummal, amit a quizlet is elfogad importálás során; tehát az első oszlop a szavakat, míg a második oszlop a definíciókat tartalmazza.

## Telepítés
A rendszer telepítője a [szoftver Github oldaláról](https://github.com/torokbi/wordlist-pdf-generator) a [Releases menüpont](https://github.com/torokbi/wordlist-pdf-generator/releases) alól tölthető le.

A program az alábbi rendszerekre érhető el:
* Windows
* Linux
* Mac OS

Az alábbi lista nem zárja ki egyéb rendszerre történő telepítés lehetőségét. Ha fenti felsorolásban szereplő rendszeren szeretné a programot használni, akkor nyisson egy issuet, és a lehetőségeknek megfelelően készülni fog az adott rendszerhez telepítő;
vagy a forráskód segítségével futtathatja a programot, ehez azonban megfelelő ismeret (ennek hiányában kutatómunka) szükséges.

## Használat lépései
Az alábbi fejezet a program használatán keresztül mutatja be a különböző gombok és mezők szerepét.
Minden elemhez tartozik egy sorszám, amely azt a felyezetet jelöli ahol az adott elem tárgyalásra kerül.
![A képen a program ablaka látható, melyen az egyes elemek sorszámozva vannak.](https://github.com/torokbi/wordlist-pdf-generator/blob/main/helper-items/program-window-with-counters.png)

### 1. Importálás
Az importálás két féle módon lehetséges:

1. Nyissuk meg a quizletet és keressük ki azt a paklit amit ki szeretnénk nyomtatni!
A három pont opciói között találjuk az exportálás lehetőségét.
Az exportálásnál a tabulátorral történő tagolást és az oszlopok elválasztásához pedig az új sort!
A kapott szöveget   'copy text' gomb segítségével másoljuk be a szövegszerkesztőbe (windows esetén jegyzettömb) és mentsük el .txt formátumban!
Ezután nincs más dolgunk, mint a korábban létrehozott fájl kikeresni.
2. Lehetőség van excel táblából történő exportálásra is. Az excel tábla formája a következő kell legyen: A oszlop tartalmazza a kifejezést, B oszlop pedig a hozzá tartozó fogalmat.
Fontos, hogy egyéb adat ne legyen a táblázatban!
Ez a formátum megegyezik azzal a formátummal, amit a Quizlet vár el táblázatból történő importálás során.

**Figyelem! Amennyiben már megnyitott egy paklit és újra megnyomja az importálás gombot a szoftverből törlésre kerül a korábban megnyitott pakli!**

### 2. Táblázat
Ennek a táblázatnak a célja, hogy nyomtatás előtt ellenőrizni lehessen a pakli tartalmát és a megfelelő sorrendet.
Sikeres importálás esetén az üres táblázatban megjelennek az általunk megnyitott szókártyák.

### 3. Felcsrélés
A felcserélés gomb megnyomásával a kifejezés és a fogalom oszlopok felcserélésre kerülnek.

**Figyelem! A gomb inaktív állapotban van amíg egy paklit nem importál!**

### 4. Cím
Ebbe a mezőbe azt a szöveget kell begépelnie amit a kész dokumentum fejlécében címként szeretne látni.

### 5. Típus
Ebben a legördülő menüben kiválaszthatja, hogy milyen elrendezést szeretne használni.
A listában szereplő elrendezések közel azonosak a Quizlet által nyújtott elrendezésekkel.

### 6. Exportálás
A gomb lenyomásávál a program elkészíti a kért kártyákból a pdf állományt az ön álltal megadott paraméterekkel.
A kész dokumentum mentést követően azonnal nyomtatható.
A szoftver az alapértelmezett fájlnevet az ön általl megadott címből állítja elő a következő módon:
az ékezetes karaktereket ékezet nélkülire cseréli, a szóközöket pedig kötőjelekre cseréli;
a nagybetükből pedig kisbetüt csinál.

**Figyelem! Az exportálás gomb inaktív addig, amig a felhasználó nem importál be egy paklit, nem ad címet a dokumentumnak és nem választja ki a dokumentum típusát!**

### Sugó
Ha bármilyen kérdése merül fel a szoftver használatával kapcsolatban, akkor nyomja meg a sugó gombot és erre az oldalra fog jutni 😀

**Figyelem! A sugó használatához aktív internetkapcsolat szükséges!**

## License
A szoftver BSD 3 pontos licent használ.
