teaches(mr_smith, math, m101).
teaches(mrs_jones, physics, p201).
teaches(dr_brown, chemistry, c301).

studies(john, m101).
studies(alice, p201).
studies(bob, c301).
studies(mary, m101).

student_teacher(Student, Teacher) :-
    studies(Student, SubCode),
    teaches(Teacher, _, SubCode).
