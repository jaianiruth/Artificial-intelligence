person(john, '1990-05-15').
person(alice, '1995-10-20').
person(bob, '1985-03-10').
person(mary, '2000-07-25').

get_dob(Name, DOB) :-
    person(Name, DOB).
