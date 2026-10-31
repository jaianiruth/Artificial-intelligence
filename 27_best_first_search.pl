% heuristic distances to goal
h(a, 5).
h(b, 4).
h(c, 4).
h(d, 3).
h(e, 2).
h(f, 0). % goal

% edges (Node, Neighbor, Cost)
edge(a, b, 1).
edge(a, c, 2).
edge(b, d, 2).
edge(c, e, 2).
edge(d, f, 3).
edge(e, f, 2).

bfs(Start, Goal, Path) :-
    bfs_queue([[Start]], Goal, RevPath),
    reverse(RevPath, Path).

bfs_queue([[Goal|Rest]|_], Goal, [Goal|Rest]).
bfs_queue([[Node|Rest]|Queue], Goal, Path) :-
    findall([Next,Node|Rest],
            (edge(Node, Next, _), \+ member(Next, [Node|Rest])),
            Children),
    append(Queue, Children, NewQueue),
    sort_queue(NewQueue, SortedQueue),
    bfs_queue(SortedQueue, Goal, Path).

sort_queue(Queue, Sorted) :-
    predsort(compare_h, Queue, Sorted).

compare_h(Order, [Node1|_], [Node2|_]) :-
    h(Node1, H1), h(Node2, H2),
    (H1 =< H2 -> Order = '<' ; Order = '>').
