# Support-compatible deletion families force synchronized endpoint crossing multiplicity or order disagreement

## Statement


Let H be a minimum counterexample and let {F_t:t in D}, |D|>=3, be a pairwise support-compatible family localized as F_t=(X-{t})|Q, with H[X] non-Hamiltonian and Q Hamiltonian. Then for every y in Q and every exact two-cover G_y of H-y, G_y is support-compatible with at most one F_t; for |D|=3 some single F_t is support-incompatible with chosen covers at both endpoints of a Hamilton order of Q. Fix such t and write A=X-{t}. Every endpoint cover has at least two ordinary edges crossing the three-part partition A|(Q-{y})|{t}. Moreover, either one endpoint has at least three such crossings, or one endpoint has a direct A-(Q-{y}) crossing, or the two endpoint probes force relative-order disagreement and hence a reversed common edge, reversing tight triple, or vertex-simple tight cycle.


## Body


# Support-compatible deletion families force synchronized endpoint crossing multiplicity or order disagreement

Let H be a minimum counterexample. Suppose a pairwise support-compatible family of exact deletion covers has localized to
V(H)=X disjoint-union Q,
with D⊆X, |D|>=3, and
F_t=(X-{t})|Q
for t in D. Thus H[Q] is Hamiltonian, H[X-{t}] is Hamiltonian for every t in D, and H[X] is non-Hamiltonian.

## External deletion covers are compatible with at most one family member

Fix y in Q and an exact two-cover G_y of H-y. Suppose G_y is support-compatible with F_t on H-{t,y}. Then all vertices of X-{t} lie in one component of G_y and all vertices of Q-{y} lie in the other. The vertex t must join one of these two components.

It cannot join X-{t}, because then that component would Hamiltonize X. Hence the support partition of G_y is forced to be
(X-{t}) | ((Q-{y}) union {t}).

One fixed G_y cannot have this form for two distinct labels t,t'. The sets X-{t} and X-{t'} are distinct, while X-{t} cannot equal (Q-{y}) union {t'} because |D|>=3 leaves at least two X-vertices in X-{t}, whereas the latter support contains only one X-vertex. Thus G_y is support-compatible with at most one F_t and support-incompatible with at least |D|-1 members of the family.

When |D|=3, fix a Hamilton order
Q=(q_0,...,q_s).
Choose exact covers of H-q_0 and H-q_s. Each can be compatible with at most one family label, so among the three labels there is some t for which F_t is support-incompatible with both endpoint covers.

## Synchronized endpoint incompatibility forces structure

Fix such a label t and put
A=X-{t}.
Because F_t=A|Q is exact, A and Q are Hamiltonian. Also |Q|>=3: if |Q|<=2 then Q union {t} has order at most three and is Hamiltonian, so A|(Q union {t}) would two-cover H.

For an endpoint y of Q, put B=Q-{y}. The inherited endpoint deletion leaves B Hamiltonian and nonempty.

Let G_y be an exact cover of H-y that is support-incompatible with F_t. Count ordinary path edges of G_y joining different classes of
A | B | {t}.

There is at least one. If there were exactly one, cutting it from the two-component forest produces exactly three blocks, so the support partition must be one of
A union B | {t},
X=A union {t} | B,
A | B union {t}.

The first is impossible: a Hamilton path on A union B=H-{t,y} together with the two-vertex path (t,y) would two-cover H. The second is impossible because X is non-Hamiltonian. The third would make G_y support-compatible with F_t after deleting t. Therefore every endpoint cover has at least two three-part crossing edges.

Assume G_y has exactly two such edges and no direct A-B crossing. Then both crossing edges are incident with t. Cutting them gives four blocks, so exactly one of A,B splits into two blocks.

If B splits, t cannot be adjacent in the contracted forest to the unique A-block, because then A union {t}=X would appear as one contiguous tight path. Therefore t is adjacent to both B-blocks, and B union {t} is Hamiltonian.

If A splits, t cannot be adjacent to both A-blocks, again because that would Hamiltonize X. Hence t is adjacent to the unique B-block and one A-block, while the other A-block is the second component. Again B union {t} is a contiguous Hamilton path.

Thus an exactly-two-crossing endpoint state with no direct A-B crossing forces
(Q-{y}) union {t}
Hamiltonian.

Apply this at both endpoints. If neither endpoint has at least three cross-class edges and neither has a direct A-(Q-{y}) crossing, then both endpoint replacements
(Q-{q_0}) union {t},
(Q-{q_s}) union {t}
are Hamiltonian, while Q union {t} is not. The two-sided endpoint-replacement theorem then forces relative-order disagreement between the inherited Q-order and the two endpoint-replacement Hamilton paths. Path-intersection calculus yields a reversed common edge, a reversing tight triple, or a vertex-simple tight cycle.

Therefore synchronized endpoint support incompatibility cannot remain a featureless two-crossing state: it produces at least three three-part crossings, a direct mixed-support A-Q crossing, or explicit order disagreement.
