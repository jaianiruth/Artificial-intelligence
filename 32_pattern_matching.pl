match([], []).
match([H|T], [H|T2]) :- match(T, T2).
match([H|T], [_|T2]) :- match([H|T], T2).

% Query:
% ?- match([a, b], [x, a, y, b, z]).
