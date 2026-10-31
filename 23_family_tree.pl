male(john).
male(bob).
male(tom).
female(mary).
female(alice).
female(susan).

parent(john, bob).
parent(john, alice).
parent(mary, bob).
parent(mary, alice).
parent(bob, tom).
parent(bob, susan).

father(F, C) :- male(F), parent(F, C).
mother(M, C) :- female(M), parent(M, C).
child(C, P) :- parent(P, C).
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.
grandparent(GP, GC) :- parent(GP, P), parent(P, GC).
