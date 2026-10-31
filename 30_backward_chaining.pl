% Rules
is_true(X) :- fact(X).
is_true(X) :- rule(X, Conditions), check_all(Conditions).

rule(animal, [has_hair]).
rule(mammal, [animal, gives_milk]).
rule(dog, [mammal, barks]).

fact(has_hair).
fact(gives_milk).
fact(barks).

check_all([]).
check_all([H|T]) :- is_true(H), check_all(T).

% Query:
% ?- is_true(dog).
