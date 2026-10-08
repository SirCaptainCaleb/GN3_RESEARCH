# Audit: short-phase scan rises and the missing A2 suffix window — preserved pre-item development

## Composition

(none yet)

## Development

## Audit of short-phase scan classification and the A2 spanning splice

This note distinguishes two unproved deductions from the useful local replacement formulas. It does not refute NOR.

### 1. Blocking inside a monochromatic suffix does not imply a monotone scan

In a deletion word 0^p1^q, insertion strictly within the 1-phase leaves an already completed 0-to-1 transition to its left. Its three-window packet must be 111 for the resulting full word to have at most one change. A monotone packet 001 or 011 still introduces a new descent after the inherited 1. Thus failure excludes scan triple 101; it does not force a nonincreasing scan.

The short-phase classification in Article III ternary subsection 10 uses the latter invalid implication. Here is an explicit flat realization of a blocked p=2 carrier with a later scan rise.

Take ten old coordinates v_1,...,v_10 and omitted x. Prescribe old consecutive statuses w=00111111 and scan s=110001100. Inserting x after i old coordinates gives the following full status words:
i=0: 100111111
i=1: 010111111
i=2: 100111111
i=3: 011011111
i=4: 000101111
i=5: 001011111
i=6: 001100111
i=7: 001111001
i=8: 001111110
i=9: 001111101
i=10: 001111110.
Every word has at least two changes.

For a global flat alternating realization, choose tournament bits t(a,b) with t(b,a)=1 xor t(a,b), and define alpha(a,b,c)=1 xor t(a,b) xor t(b,c) xor t(c,a). Set t(v_i,v_{i+1})=0 and t(v_i,v_{i+2})=w_i. Choose q_1=0 and q_{i+1}=q_i xor s_i, and put t(x,v_i)=q_i. Then alpha(v_i,v_{i+1},v_{i+2})=w_i and alpha(x,v_i,v_{i+1})=s_i. Assign all other tournament edges arbitrarily. Alternation and vanishing four-face coboundary hold globally.

This example refutes the deduction from flatness and all-insertion blocking to s=110*. It is not a minimum NOR counterexample. The subsequent size-three-curvature-tube argument (ternary subsection 11) remains conditional on its special scan; this example alone does not refute its final conjectural conclusion. Article II subsection 218 is the appropriate repair route: it uses only the forced prefix 11000 and allows later scan bits to vary.

### 2. A boundary window is omitted in the g=1 A2 splice

In Article II subsection 214 the g=1 branch proposes replacing
...A,B,u,v,C,D,E,...
by
...A,B,a,C,b,c,D,E,...
where a,b,c are the three residual coordinates in cyclic order.
Even granting all five advertised internal statuses 00011, the next window is alpha(c,D,E), whereas the old window was alpha(C,D,E)=1. The former is a new boundary condition. If there is a further suffix, the next old window alpha(D,E,F)=1 resumes. Therefore the displayed splice closes only if alpha(c,D,E)=1 (or D is the final coordinate). The supplied internal calculation does not establish that bit. In the presence of the later companion constraint alpha(c,D,E)=0, this particular splice fails at that boundary.

Consequently subsection 214 has not excluded g=1 for an arbitrary suffix. Subsection 215's global claim to eliminate the A2 branch inherits that obligation.

### 3. A valid simplification of the g=0 branch

Assume the actual cyclic deletion carriers and g=alpha(u,B,C)=0. For a forward residual pair u,v, replace A,B,u,v,C by A,v,B,u,C, keeping the omitted coordinate and all outside coordinates fixed. The new statuses from (A,v,B) through (u,C,D) are 1111: alternation gives alpha(A,v,B)=1, the forward residual edge gives alpha(v,B,u)=1, g=0 gives alpha(B,u,C)=1, and the old carriers give alpha(u,C,D)=1. The right ordered pair C,D is unchanged. On the left, A is unchanged and only alpha(R,A,v) is new; either value is compatible with the old zero prefix followed by the displayed ones. Hence the first phase strictly decreases, contradicting global minimum first phase (with an absent prefix giving a monochromatic carrier). The extra hypothesis h=alpha(A,B,C)=1 is unnecessary for this calculation.

Thus the remaining obligation for this A2 argument is specifically the g=1 boundary branch, alongside the antipodal backtrack and recurrence coverage. Do not use the unproved h=0 finite-drift escape to justify the g=0 surgery.

### Strategy

Prefer local moves that preserve the right ordered boundary pair while tolerating one free left window, as the g=0 surgery does. For ternary windows, if a replacement changes the final ordered pair, explicitly include the next suffix coordinate before calling it a spanning splice.

The antipodal hexagon of Article II subsection 221 and the surviving g=1 A2 branch should be investigated as related boundary transport problems. Seek an augmenting sequence of actual good deletion witnesses, tracking omitted coordinate, ordered boundary pairs, and threshold position. A repeated state is an unresolved cycle unless an additional exit is proved. A finite bound on one kind of drift does not establish termination of the whole process.

This is a concrete repair target: prove a boundary-preserving alternative for g=1, or show how its failed boundary window yields another usable deletion witness with a justified strict improvement. The local g=0 elimination and subsection 218's arbitrary-scan boundary replacement remain useful inputs.
