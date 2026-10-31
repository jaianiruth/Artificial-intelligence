disease(diabetes).
disease(hypertension).
disease(obesity).

diet(diabetes, 'Low carb, no sugar, high fiber').
diet(hypertension, 'Low sodium, DASH diet').
diet(obesity, 'Caloric deficit, high protein, low fat').
diet(general, 'Balanced diet').

suggest_diet(Disease, Diet) :-
    diet(Disease, Diet).
suggest_diet(Disease, Diet) :-
    \+ diet(Disease, _),
    diet(general, Diet).
