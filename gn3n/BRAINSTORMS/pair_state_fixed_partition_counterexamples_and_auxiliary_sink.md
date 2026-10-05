# Pair-state fixed-partition counterexamples and auxiliary sink

Record pruning results for the pair-state matching route without overwriting the concurrently advanced coupled-transversal brainstorm.

The pair-state digraph for a balanced split A union B has vertex set A x B and arc
  (a,b)->(a',b')
iff (a,b,a') and (b,a',b') are tight.
A directed path of matched states is exactly an alternating tight path on the original vertices.

Axiom verification: the canonical boundary-3-tournament definition only requires exactly one of (u,v,w) and (w,v,u) to be tight. Hence, for each middle vertex v, the induced local tournament T_v on V-{v} is arbitrary, with no compatibility condition between different middle vertices. The computational counterexamples below are therefore legitimate local-tournament systems.

FIXED-PARTITION SHORTCUT 1 IS FALSE. There are balanced 5x5 systems for which every perfect matching M in A x B satisfies alpha(D[M])>=3. Thus one cannot prove the grand theorem by fixing an arbitrary balanced split and invoking Gallai-Milgram after finding alpha<=2.

FIXED-PARTITION SHORTCUT 2 IS ALSO FALSE. There are balanced 5x5 systems for which no perfect matching M gives a directed two-path cover of D[M]. Therefore even the direct state-digraph two-path-cover target is too strong when the parity split A|B is fixed. Any viable pair-state theorem must allow the bipartition/pairing itself to vary globally.

These failures do not invalidate the state language. In a separate 5x5 obstruction to the alpha<=2 shortcut, 39 of the 120 perfect matchings still admit a directed two-path cover, showing alpha<=2 was substantially stronger than necessary.

AUXILIARY VERTEX NORMALIZATION. In H+ place the auxiliary vertex rho on the B-side and match it to a in A. The state s_rho=(a,rho) is an absolute sink: no state can follow it because triples beginning with rho are forced non-tight. An old state (x,b) points into s_rho iff (x,b,a) is tight; the second transition condition is automatic from the auxiliary construction. Thus auxiliary exactification becomes a variable-pairing two-path-cover problem with one path automatically terminating at s_rho.

LOCAL 3x3 COMPUTATIONAL FACT. Exhaustive enumeration of all 2^18 local sign systems on a 3x3 pair-state subproblem shows that among the six bijections at most three induce an independent triple. This is a computationally certified observation, not yet a human theorem. Equality patterns are structured. The local half-good bound alone is insufficient for a global averaging proof because forbidden triples can overlap heavily.

RECTANGLE EXCHANGE. For a 2x2 rectangle with A-vertices x,y and B-vertices p,q, simultaneous nonadjacency of both diagonal and antidiagonal matched pairs occurs exactly in the aligned checkerboard case
  tau_p(x,y)=tau_x(p,q),
  tau_q(x,y)=tau_y(p,q),
with those two displayed values opposite.
Thus persistence of nonadjacency under a matching 2-switch has a rigid local form.

Recommended status of this route: retain pair-state/checkerboard language as a global variable-pairing model; do not use the two false fixed-partition conjectures.
