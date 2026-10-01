# Two universally internal cube labels force double crossing or a direct bypass of their adjacent block

## Statement


Let G be a boundary tournament and let x,y be distinct vertices such that G and G-{x,y} are non-Hamiltonian with path-cover number two. Suppose x and y are internal in every two-cover of G.

Fix any displayed two-cover F=P|Q of G.

(A) If x and y lie on different displayed components of F, then deleting x and y splits P|Q into four nonempty inherited tight-path fragments, and every two-cover of G-{x,y} has at least two ordinary edges joining different fragments.

(B) If x and y lie on the same displayed component but are not consecutive there, deleting x and y again leaves four nonempty inherited tight-path fragments, and every two-cover of G-{x,y} has at least two ordinary cross-fragment edges.

(C) If x and y are consecutive on one displayed component, write
P=(A,x,y,B),
where A and B are nonempty inherited tight paths. Relative to the three-class partition
V(A) | V(B) | V(Q)
of G-{x,y}, every two-cover has at least one cross-class ordinary edge. Moreover, if a lower two-cover has exactly one cross-class edge, then that edge joins V(A) to V(B), while the other lower component has support exactly V(Q). Thus a minimum-crossing lower cover must bypass the deleted adjacent block directly; it cannot merge A with Q or B with Q.

Consequently, for every top two-cover, the universally internal pair x,y yields either a doubly crossed lower fragmentation or an adjacent-block state whose sparse lower covers are forced direct A-to-B bypasses.

If, in addition, all two-covers of G have one common unordered support partition and no common-support order disagreement, then in the residue where x,y are adjacent in every top cover they lie in one fixed support class and occur there as one fixed ordered adjacent pair in every two-cover.


## Body


Fix a displayed two-cover F=P|Q of G.

Suppose first that x and y lie on different displayed components. Since both are internal, deleting them splits each top component into two nonempty contiguous tight subpaths. Hence G-{x,y} is partitioned into four nonempty inherited tight-path fragments. Let T=T_1|T_2 be any two-cover of G-{x,y}. If a displayed T-component visits r fragment-blocks, it has at least r-1 ordinary transitions between distinct fragments. Summing over the two T-components gives at least
4-2=2
cross-fragment edges.

Now suppose x,y lie on the same displayed component, with x preceding y. Write
P=(A,x,M,y,B),
where A,B are nonempty and M is the possibly empty displayed subpath strictly between x and y. If M is nonempty, then A,M,B,Q are four nonempty inherited tight-path fragments after deleting x,y, and the same transition count gives at least two cross-fragment edges in every lower two-cover. This proves (A) and (B).

It remains to analyze the adjacent case M empty. Thus
P=(A,x,y,B),
with A,B,Q all nonempty. Any two-cover T of G-{x,y} must have at least
3-2=1
ordinary edge crossing the three inherited classes A,B,Q.

Assume equality: T has exactly one cross-class edge. Across its two displayed components, the total number of maximal class-blocks is then exactly three. Since all three classes A,B,Q are nonempty and must be covered, each class occurs in exactly one block. Therefore one T-component consists of two class-blocks joined by the unique cross edge, while the other T-component is supported exactly on the remaining class.

The unique merge cannot be A with Q. For then the other T-component has support exactly B. Replace that component, if necessary, by the inherited tight path B. The path
(x,y,B)
is tight because it is the terminal segment of the original displayed top path P. Together with the unchanged T-component on A union Q, this gives a two-cover of G in which x is a displayed endpoint, contradicting that x is internal in every two-cover of G.

Symmetrically, the unique merge cannot be B with Q. If it were, the other component would have support exactly A; replacing it by the inherited path A makes
(A,x,y)
a tight path, and together with the B union Q component gives a two-cover of G in which y is a displayed endpoint, contradicting universal internality of y.

Hence the only possible equality case merges A with B and leaves Q as the other component. Its unique cross-class edge therefore joins V(A) directly to V(B). This proves (C).

Finally, if every top two-cover has one common unordered support partition and there is no common-support order disagreement, then any residue in which x,y are adjacent in every top cover places them in the same fixed support class. Their relative order cannot reverse between two Hamilton paths on that support without giving order disagreement, so they occur as one fixed ordered adjacent pair throughout.
