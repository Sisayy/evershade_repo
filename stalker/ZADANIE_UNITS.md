ZADANIE: przeglad par jednostkowych EN->PL z instrukcji gry planszowej (oficjalne EN i PL, tekst z warstwy tekstowej PDF).
Pracuj tylko w katalogu stalker. Przetwarzaj WYLACZNIE pliki wymienione w wiadomosci uzytkownika, jeden po drugim.

Wejscie: stalker/in/<nazwa>.csv, kolumny id, en, pl, sim. Sasiednie wiersze moga byc z tej samej strony, mozesz uzywac ich jako kontekstu.
Jedna para to jedna jednostka tekstu (akapit, naglowek, etykieta albo komorka tabeli), nie pojedyncze zdanie. Dlugie akapity sa normalne.
Dla KAZDEGO wiersza wybierz jedna decyzje: AS_IS (zostaje), FIX (podaj poprawiony PL) albo DROP (wyrzucic z treningu).

ZNACZNIKI I TOKENY (najwazniejsze): w tekscie wystepuja znaczniki 【B】 【/B】 【S】 【/S】 oraz tokeny [[ICON1]] [[ICON2]] itd. To formatowanie, nie tresc.
- Zestaw znacznikow i tokenow w PL musi byc identyczny jak w EN (te same znaczniki, te same tokeny, ta sama liczba). Gdy PL ma inny zestaw: FIX przywracajacy zestaw z EN, jesli to prosta poprawka, w przeciwnym razie DROP.
- Nigdy nie usuwaj, nie dodawaj, nie renumeruj i nie przepisuj znacznikow ani tokenow w pl_fixed poza przywroceniem zgodnosci z EN.
- Kolejnosc tokenow w PL moze sie roznic od EN, jesli wynika z polskiego szyku zdania.
- Token [[ICONn]] na poczatku krotkiej etykiety (np. "[[ICON1]]Innovation" -> "[[ICON1]]Innowacja") jest poprawny. Nie licz tokenow ani znacznikow jako bledow OCR.

Zasady:
- Gdy masz watpliwosc: DROP. DROP ma pierwszenstwo przed FIX.
- FIX tylko gdy poprawka to kilka slow: 1-2 oczywiste literowki w PL, zdublowana numeracja, pojedynczy wyciek sasiedniej jednostki do usuniecia, pojedynczy znak interpunkcyjny, przywrocenie znacznika lub tokenu zgodnie z EN. Nie dopisuj zdan ani koncowek, ktorych nie ma w PL. Nie tlumacz od nowa.
- DROP: EN zepsuty (rozstrzelone litery, sklejone fragmenty, urwane zdania, naglowki i stopki stron, kody kart, listy komponentow, listy tworcow); PL nie odpowiada EN (przesunieta para, brak czesci tekstu, dwie jednostki sklejone w jedna); poszatkowany tekst z tabel, kart i obrazkow; wiecej niz 2 bledy w parze; obce znaki w PL typu Ǹ ǲ Ĉ Ȗ; angielskie zdanie w PL; para o treści 1-3 liter bez znaczenia; same numery sekcji.
- Rozne liczby w EN i PL (np. 18 vs 6): DROP.
- DUPLIKATY: gdy to samo EN wystepuje w kilku wierszach, a PL jest dobre, kazdy wiersz zostaje AS_IS. DROP tylko gdy wszystkie kopie sa zle.
- Terminologii nie zmieniaj.

Wyjscie: stalker/out/<ta sama nazwa pliku>.csv, UTF-8, kolumny: id,decision,pl_fixed. Wpisuj TYLKO wiersze z decyzja DROP lub FIX. Wiersz AS_IS pomijaj. pl_fixed wypelnij tylko przy FIX. Nie przepisuj EN ani PL poza pl_fixed.
Oszczedzaj zasoby: przeczytaj plik wejsciowy DOKLADNIE RAZ i nie wypisuj go ponownie. Zapisz skrypt z lista id DROP i slownikiem FIX i uruchom go, zamiast pisac decyzje wiersz po wierszu. Skrypt ma sprawdzic, ze kazdy pl_fixed ma ten sam zestaw znacznikow i tokenow co EN danego wiersza. Nie wywoluj narzedzi dla pojedynczych wierszy.
Po pliku: zrob commit i push na swoja galaz i napisz TYLKO trzy liczby: wierszy wejscia, DROP, FIX. Nie dodawaj innego tekstu.
