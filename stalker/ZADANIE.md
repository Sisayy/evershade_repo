ZADANIE: przeglad par EN->PL z instrukcji gry planszowej S.T.A.L.K.E.R. The Board Game (oficjalne EN i PL, tekst odczytany OCR-em).
Pracuj tylko w katalogu stalker. Przetwarzaj WYLACZNIE pliki wymienione w wiadomosci uzytkownika, jeden po drugim.

Wejscie: stalker/in/<nazwa>.csv, kolumny id, en, pl, sim (plik *_slim.csv ma jeszcze kolumne why). Sasiednie wiersze to kolejne pary z jednej ksiazki, mozesz uzywac ich jako kontekstu.
Dla KAZDEGO wiersza wybierz jedna decyzje: AS_IS (zostaje), FIX (podaj poprawiony PL) albo DROP (wyrzucic z treningu).

Zasady:
- Gdy masz watpliwosc: DROP. DROP ma pierwszenstwo przed FIX.
- FIX tylko gdy poprawka to kilka slow: 1-2 oczywiste literowki OCR w PL, zdublowana numeracja, pojedynczy wyciek sasiedniego zdania do usuniecia, pojedynczy znak interpunkcyjny. Nie dopisuj zdan ani koncowek, ktorych nie ma w PL. Nie tlumacz od nowa.
- DROP: EN zepsuty (rozstrzelone litery, sklejone fragmenty, urwane zdania, naglowki i stopki stron, kody kart, listy komponentow, listy tworcow); PL nie odpowiada EN (przesunieta para, brak czesci zdania); poszatkowany tekst z tabel, kart i obrazkow; wiecej niz 2 bledy OCR w parze; obce znaki w PL typu Ǹ ǲ Ĉ Ȗ; angielskie zdanie w PL; para 1-3 znaki; same numery sekcji.
- Rozne liczby w EN i PL (np. 18 vs 6): DROP.
- Ikony odczytane jako znaki (np. (c) (R) 14* [c]) oraz brakujace ikony sa normalne: nie sa powodem do DROP, jesli reszta pary sie zgadza.
- DUPLIKATY: gdy to samo EN wystepuje w kilku wierszach, a PL jest dobre, kazdy wiersz zostaje AS_IS. DROP tylko gdy wszystkie kopie sa zle (DROP usuwa pozniej wszystkie pary o tym EN).
- Rozbite slowo w EN typu "Ger- man" nie jest powodem do DROP, jesli reszta pary jest dobra.
- Terminologii nie zmieniaj.

Wyjscie: stalker/out/<ta sama nazwa pliku>.csv, UTF-8, kolumny: id,decision,pl_fixed. Wpisuj TYLKO wiersze z decyzja DROP lub FIX. Wiersz AS_IS pomijaj (brak wiersza w wyjsciu = AS_IS). pl_fixed wypelnij tylko przy FIX. Nie przepisuj EN ani PL poza pl_fixed.
Oszczedzaj zasoby: przeczytaj plik wejsciowy DOKLADNIE RAZ i nie wypisuj go ponownie. Zapisz skrypt z lista id DROP i slownikiem FIX i uruchom go, zamiast pisac decyzje wiersz po wierszu. Nie wywoluj narzedzi dla pojedynczych wierszy.
Po pliku: zrob commit i push na swoja galaz i napisz TYLKO trzy liczby: wierszy wejscia, DROP, FIX. Nie dodawaj innego tekstu.
