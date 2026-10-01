# Four common-last ascending edges can have values 11,11,17,17

## Statement

There is a finite linear 3-graph with four ascending nonspecial edges having a common last vertex and ordered φ-values (11,11,17,17). Hence even the weakened four-edge midpoint inequality 2q_2>=q_1+q_4 is false.

## Body

Let E_i={a_{i-1},b_i,a_i}, 1<=i<=17, be a 17-edge linear path, put v=b_17, and add F_1={v,a_10,c_1}, F_2={v,b_16,c_2}, and F_3={v,b_15,b_10}, with c_1,c_2 new. The intersection graph is the path E_1...E_17 together with the clique on {E_17,F_1,F_2,F_3}; the extra path adjacencies are F_1E_10,F_1E_11,F_2E_16,F_3E_10,F_3E_15. The longest induced paths ending E_17 and F_2 have length 17, realized respectively by E_1,...,E_17 and E_1,...,E_16,F_2. The longest induced paths ending F_1 and F_3 have length 11, realized by E_1,...,E_10,F_1 and E_1,...,E_10,F_3. The additional adjacencies listed above prevent a longer induced route through the clique or through the second contact. The corresponding unique entrance vertices are a_16,b_16,a_10,b_10, whose endpoint values are 16,16,10,10 from the base-path prefixes; alternative clique routes are shorter. Thus E_17,F_2,F_1,F_3 are ascending and nonspecial, all have v as a last vertex, and their ordered φ-values are 11,11,17,17. Therefore 2q_2=22<28=q_1+q_4.
