% state(MonkeyLocation, MonkeyOnBox, BoxLocation, HasBanana)
move(state(middle, onbox, middle, hasnot),
     grasp,
     state(middle, onbox, middle, has)).

move(state(L, onfloor, L, Has),
     climb,
     state(L, onbox, L, Has)).

move(state(L1, onfloor, L1, Has),
     push(L1, L2),
     state(L2, onfloor, L2, Has)).

move(state(L1, onfloor, Box, Has),
     walk(L1, L2),
     state(L2, onfloor, Box, Has)).

canget(state(_, _, _, has)).
canget(State1) :-
    move(State1, _, State2),
    canget(State2).
