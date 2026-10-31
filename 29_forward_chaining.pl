:- dynamic fact/1.

rule(animal, [has_hair]).
rule(mammal, [animal, gives_milk]).
rule(dog, [mammal, barks]).

fact(has_hair).
fact(gives_milk).
fact(barks).

forward_chain :-
    rule(Conclusion, Conditions),
    \+ fact(Conclusion),
    check_conditions(Conditions),
    assert(fact(Conclusion)),
    write('Derived fact: '), write(Conclusion), nl,
    forward_chain.
forward_chain :- write('Finished forward chaining.'), nl.

check_conditions([]).
check_conditions([H|T]) :- fact(H), check_conditions(T).
