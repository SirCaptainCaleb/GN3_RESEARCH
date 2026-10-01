# A doubled cross barrier always yields a Hamiltonian four- or five-window

## Statement

Let H be a minimum counterexample and let H-x=P|Q be a deletion cover whose two failed-insertion obstructions are second-type and lie in the doubled-cross-barrier branch. Let the pivot gaps be p_i|p_{i+1} and q_j|q_{j+1}, and put
F={x,p_i,p_{i+1},q_j,q_{j+1}}.
Then H contains a proper Hamiltonian induced set W of order four or five, with x in W, whose complement is non-Hamiltonian of path-cover number two. More precisely: if H[F] is Hamiltonian take W=F; if H[F] is non-Hamiltonian, at least three of the four subsets F-{v} with v!=x are Hamiltonian, so one may take a Hamiltonian four-set W containing x.

## Body

If H[F] is Hamiltonian there is nothing to prove except the complement conclusion, which follows from minimum-counterexample calculus because F is proper.

Assume H[F] is non-Hamiltonian. The certified small-set theorem smallset01, Section 7, says that a non-Hamiltonian five-set has at most one non-Hamiltonian four-subset. There are exactly four four-subsets of F containing x, namely F-{p_i}, F-{p_{i+1}}, F-{q_j}, and F-{q_{j+1}}. Since at most one of all five four-subsets is non-Hamiltonian, at least three of these four x-containing subsets are Hamiltonian. Choose one as W. Again W is a proper Hamiltonian set in the minimum counterexample, so H-W is non-Hamiltonian and has path-cover number two.