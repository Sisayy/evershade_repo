ZADANIE TESTOWE: przeglad par EN->PL z instrukcji gry planszowej.
Pracuj tylko w katalogu test_review. Nie czytaj innych plikow w repo.

Wejscie: test_review/test_review.csv (kolumny id, en, pl, ewentualnie why i sim). Wiersze sa kolejnymi parami z jednej ksiazki,
wiec sasiednie wiersze mozesz wykorzystac jako kontekst.
Dla KAZDEGO wiersza wybierz jedna decyzje: AS_IS (zostaje bez zmian), FIX (podaj poprawiony PL) albo DROP (wyrzucic z treningu).

Zasady:
- DROP ma pierwszenstwo przed FIX. FIX tylko gdy poprawka jest krotka i oczywista: kosmetyczne bledy OCR w PL, zdublowana numeracja,
  wyciek sasiedniego zdania, brakujaca koncowka widoczna w sasiednim wierszu.
- DROP: EN zepsuty (rozstrzelone litery, sklejone fragmenty, "fi rst", ucięte zdania, naglowki stron, kody kart, same ikony, listy tworcow),
  PL nie odpowiada EN (przesunieta para), smieci OCR w PL, angielskie zdanie w PL, para 1-3 znaki. Brakujace ikony sa normalne.
- Nie tlumacz od nowa i nie dopisuj wlasnego tekstu do PL poza minimalnym FIX.

Wyjscie: test_review/out/test_out.csv, kolumny: id,decision,pl_fixed. Jeden wiersz na KAZDY id z wejscia. decision to AS_IS, FIX lub DROP.
pl_fixed wypelnij tylko przy FIX. Zapisz plik w UTF-8.
Na koncu zrob commit i push na swoja galaz oraz napisz liczniki AS_IS, FIX i DROP.
