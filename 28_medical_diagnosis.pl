symptom(fever).
symptom(cough).
symptom(headache).
symptom(runny_nose).
symptom(sore_throat).

disease(flu, [fever, cough, headache]).
disease(cold, [cough, runny_nose, sore_throat]).
disease(covid, [fever, cough, sore_throat, headache]).

diagnose(Disease, PatientSymptoms) :-
    disease(Disease, DiseaseSymptoms),
    subset(DiseaseSymptoms, PatientSymptoms).

subset([], _).
subset([H|T], List) :- member(H, List), subset(T, List).
