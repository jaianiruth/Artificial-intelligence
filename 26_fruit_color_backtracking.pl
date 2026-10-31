fruit(apple, red).
fruit(apple, green).
fruit(banana, yellow).
fruit(grape, green).
fruit(grape, purple).
fruit(orange, orange).

find_fruit_by_color(Color, Fruit) :-
    fruit(Fruit, Color).

% Use backtracking in query:
% ?- find_fruit_by_color(green, Fruit).
