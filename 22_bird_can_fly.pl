bird(sparrow).
bird(eagle).
bird(penguin).
bird(ostrich).
bird(pigeon).

cannot_fly(penguin).
cannot_fly(ostrich).

can_fly(X) :-
    bird(X),
    \+ cannot_fly(X).

% Queries to test:
% ?- can_fly(eagle).
% ?- can_fly(penguin).
