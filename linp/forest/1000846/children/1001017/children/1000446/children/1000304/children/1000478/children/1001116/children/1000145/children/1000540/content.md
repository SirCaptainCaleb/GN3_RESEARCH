# Two-contact counterexample to four-edge spacing

## Statement

The four-edge spacing conjecture 1ff3a09b18b7 is false. There is a linear 3-graph with four ascending nonspecial edges sharing one last vertex and having φ-values 12,16,20,20, so 2q_2=32<33=q_1+q_4+1.

## Body

Construction. Let E_i={a_{i-1},b_i,a_i} for 1<=i<=20 form a 20-edge linear path, and put v=b_20. Add F_1={b_11,b_16,v}, F_2={b_19,c_2,v}, and F_3={b_15,c_3,v}, where c_2,c_3 are new. The hypergraph is linear. Its intersection graph consists of the path E_1...E_20, the clique on {E_20,F_1,F_2,F_3}, and the extra adjacencies F_1E_11,F_1E_16,F_2E_19,F_3E_15.

The relevant longest induced paths are unique. For E_20 the unique longest induced path is E_1,...,E_20, of length 20, entering E_20 through a_19. For F_1 the unique longest induced path is E_1,...,E_11,F_1, of length 12, entering through b_11. Indeed, any path ending F_1 through E_16, E_20, F_2, or F_3 is forced to avoid the corresponding additional neighbors of F_1 and is shorter. For F_2 the unique longest path is E_1,...,E_19,F_2, of length 20, entering through b_19. For F_3 the unique longest path is E_1,...,E_15,F_3, of length 16, entering through b_15; routes through the terminal clique are shorter because they must avoid the attachment E_15.

The endpoint values of the entrance vertices are φ(a_19)=19, φ(b_11)=11, φ(b_19)=19, and φ(b_15)=15. These are witnessed by the corresponding base-path prefixes; the displayed unique longest paths into E_20,F_1,F_2,F_3 enter through those vertices, so those longest paths cannot end there, and the alternative incident-edge routes are shorter. Hence all four edges are ascending and nonspecial. Each has v=b_20 as a last vertex. Their ordered φ-values are (12,16,20,20), violating 2q_2>=q_1+q_4+1.

The mechanism is exactly the second contact of F_1 at b_16. It blocks the clean prefix-clique-suffix splice responsible for geometric spacing in 7989ed25c41f and 5945d7d896b0. Thus the clean geometric recurrence does not extend to arbitrary ascending attachments.
