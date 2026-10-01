# The witness-free unique-small plateau forces a standard transport disturbance

## Statement

Let H be a minimum counterexample and let K be a trapped pairwise-repartition component at minimum quadratic potential in which every three-cover has path-order multiset {r+1,r+1,r}, r>=3. Assume none of the canonical terminal-frontier witnesses occurs: no proper Hamiltonian four- or five-set with path-cover-two complement, cross triple, interval connector, order disagreement, inherited-edge crossing, bounded local defect-compression obstruction, or reversed join. Then there are disjoint tight paths A,B,C of order r and distinct vertices x,y outside them such that x and y both extend the same endpoint of each of A,B,C. Moreover every two-cover T of H-{x,y} has at least one of the following disturbances: (1) order disagreement with a displayed core path; (2) at least three T-edges joining different cores; (3) an ordinary edge of one displayed core whose endpoints lie in different components of T; or (4) one T-component contains two nonempty blocks from the same core separated by a nonempty block from another core.

## Body

At every state of K, the two large paths each admit a neutral transfer into the unique small path: otherwise the gap-one dichotomy produces one of the excluded canonical witnesses. In the witness-free branch, terminal-frontier localization forces those two transfers to use one common endpoint gap and to move the matching donor endpoint. Fix one state and, after reversing all displayed paths if necessary, write it as (x,A)|B|(y,C), where A,B,C have order r and all chosen transfers use the initial side.

Continue by always taking the nonbacktracking neutral transfer. The reverse of the preceding move is one of the two available transfers into the new small path, so nonbacktracking forces the other large donor. Thus the donor sequence is forced:
x:A→B, y:C→A, x:B→C, y:A→B, x:C→A, y:B→C.
After six moves the original support state is restored. Reading the first three states and their alternate available moves shows that both x and y initial-extend each of A,B,C. The terminal-side case is symmetric.

Now fix any two-cover T of H-{x,y}=A∪B∪C. Let t be the number of ordinary T-edges joining different cores. If T has order disagreement with a displayed core, outcome (1) holds, so assume it is order-neutral. Write b_A,b_B,b_C for the numbers of monochromatic T-blocks in the three cores. The standard transition identity gives t=b_A+b_B+b_C-2, hence t≥1.

If t=1 then b_A=b_B=b_C=1. Thus the three cores occur as three whole ordered blocks distributed over two T-components: one T-path concatenates two whole cores D,E and the other is the third core F. Since x and y both initial-extend every core, prepend x to the D-E path and y to F. These two tight paths cover H, contradicting that H is a counterexample. Therefore t≥2.

If t≥3, outcome (2) holds. If t=2, cutting the two cross-core T-edges produces four nonempty monochromatic blocks, so after relabeling the block counts are (2,1,1). Let A be the split core. If its two blocks lie in different T-components, connectedness of the displayed path A forces some ordinary edge of A to have endpoints in different T-components, giving outcome (3). If the two A-blocks lie in the same T-component, their maximality forces a nonempty B- or C-block between them, giving outcome (4). These cases exhaust all possibilities.
