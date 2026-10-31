planet(mercury, rocky, 0).
planet(venus, rocky, 0).
planet(earth, rocky, 1).
planet(mars, rocky, 2).
planet(jupiter, gas_giant, 79).
planet(saturn, gas_giant, 82).
planet(uranus, ice_giant, 27).
planet(neptune, ice_giant, 14).

has_moons(Planet) :-
    planet(Planet, _, Moons),
    Moons > 0.
