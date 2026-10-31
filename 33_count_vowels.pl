vowel(a). vowel(e). vowel(i). vowel(o). vowel(u).
vowel('A'). vowel('E'). vowel('I'). vowel('O'). vowel('U').

count_vowels([], 0).
count_vowels([H|T], Count) :-
    vowel(H), !,
    count_vowels(T, RestCount),
    Count is RestCount + 1.
count_vowels([_|T], Count) :-
    count_vowels(T, Count).

% helper to process strings
count_string_vowels(String, Count) :-
    string_chars(String, Chars),
    count_vowels(Chars, Count).
