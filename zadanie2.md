Zadanie 2

1.1
- a)bracia/siostry
- b)przyrodni kuzyni
- c)swat
- d)macocha/ojczym
- e)przyrodni bracia/siostry
- f)
- g)

1.2
- a)
- b)
- c)
- d)
- e)
- f)
- g)


Zad2
- 1) % kobieta(X) - X jest kobietą
- kobieta(X) :- rodzic(X, _), \+ mezczyzna(X).
- 2) % ojciec(X, Y) - X jest ojcem Y
- ojciec(X, Y) :- rodzic(X, Y), mezczyzna(X).
- 3)% matka(X, Y) - X jest matką Y
- matka(X, Y) :- rodzic(X, Y), kobieta(X).

- 4)% corka(X, Y) - X jest córką Y
- corka(X, Y) :- rodzic(Y, X), kobieta(X).

- 5)% brat_rodzony(X, Y) - X jest rodzonym bratem Y
- brat_rodzony(X, Y) :- rodzic(Z, X), rodzic(Z, Y), mezczyzna(X), X \= Y.

- 6)% brat_przyrodni(X, Y) - X jest przyrodnim bratem Y
- brat_przyrodni(X, Y) :- rodzic(Z, X), rodzic(W, Y), kobieta(Z), kobieta(W), X \= Y, Z \= W.

- 7) % kuzyn(X, Y) - X jest kuzynem Y
- kuzyn(X, Y) :- rodzic(Z, X), rodzic(W, Y), brat_przyrodni(Z, W).

- 8)% dziadek_od_strony_ojca(X, Y) - X jest dziadkiem od strony ojca dla Y
- dziadek_od_strony_ojca(X, Y) :- ojciec(X, Z), rodzic(Z, Y).

- 9)% dziadek_od_strony_matki(X, Y) - X jest dziadkiem od strony matki dla Y
- dziadek_od_strony_matki(X, Y) :- matka(X, Z), rodzic(Z, Y).

- 10)% dziadek(X, Y) - X jest dziadkiem Y
- dziadek(X, Y) :- dziadek_od_strony_ojca(X, Y); dziadek_od_strony_matki(X, Y).

- 11)% babcia(X, Y) - X jest babcią Y
- babcia(X, Y) :- matka(X, Z), rodzic(Z, Y).

- 12)% wnuczka(X, Y) - Y jest wnuczką X
- wnuczka(X, Y) :- babcia(X, Y), kobieta(Y).

- 13)% przodek_do2pokolenia_wstecz(X, Y) - X jest przodkiem Y do drugiego pokolenia wstecz
- przodek_do2pokolenia_wstecz(X, Y) :- rodzic(X, Z), rodzic(Z, Y).

- 14)% przodek_do3pokolenia_wstecz(X, Y) - X jest przodkiem Y do trzeciego pokolenia wstecz
- przodek_do3pokolenia_wstecz(X, Y) :- rodzic(X, Z), przodek_do2pokolenia_wstecz(Z, Y).
