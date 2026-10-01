# Defect-span three and deletion-cover compatibility give the canonical global obstruction interface

## Statement

A finite boundary tournament has a spanning cover by at most two tight paths exactly when some spanning ordering has defect span at most two. Every minimum counterexample has minimum defect span exactly three: any exact deletion cover P|Q of H-x yields the canonical ordering P,x,Q with defects confined to the three join centers and with the two outer centers always defective; if all three join triples are defective, the five-vertex join window reverses to a tight path. Deletion covers can be compared through compatibility: at least max(4,q+2) pairwise compatible q-path deletion covers glue to a global q-path cover. Pairwise support-compatible exact two-covers localize to one non-Hamiltonian class X with many Hamiltonian vertex deletions and one inert Hamiltonian class Q. For a compatible pair, the two omitted vertices must insert into the same common class at identical or adjacent slots; separated slots glue, while adjacent slots force a reversing triple through the unique intervening common vertex.

## Body

# Defect-span three and deletion-cover compatibility give the canonical global obstruction interface

Let H be a finite boundary tournament.

## Defect span and the exact two-cover reformulation

For a spanning ordering
pi=(v_1,...,v_n),
call an internal position i a defect center when
(v_{i-1},v_i,v_{i+1})
is non-tight. If D(pi) is the set of defect centers, define span(pi)=0 when D(pi) is empty and otherwise
span(pi)=max D(pi)-min D(pi)+1.

Then H has a spanning cover by at most two tight paths if and only if some spanning ordering has defect span at most two.

Indeed, concatenating two covering paths P=(v_1,...,v_j), Q=(v_{j+1},...,v_n) leaves possible defects only at the two join centers j,j+1. Conversely, if all defect centers lie in one such adjacent pair, the prefix through v_j and suffix from v_{j+1} are tight paths covering H.

Now let H be a minimum counterexample and let
H-x=P|Q
be any exact deletion two-cover, with
P=(p_0,...,p_m), Q=(q_0,...,q_s).
The ordering
(p_0,...,p_m,x,q_0,...,q_s)
has defects only at the three centers p_m,x,q_0. The outer centers are necessarily defects: if (p_{m-1},p_m,x) were tight then (P,x)|Q would two-cover H; if (x,q_0,q_1) were tight then P|(x,Q) would. Therefore its defect span is exactly three. Since no counterexample admits span at most two, every minimum counterexample satisfies
min_pi span(pi)=3.

If the middle join triple (p_m,x,q_0) is also non-tight, boundary antisymmetry reverses all three failed join triples:
(x,p_m,p_{m-1}), (q_0,x,p_m), (q_1,q_0,x)
are tight. Hence
(q_1,q_0,x,p_m,p_{m-1})
is a tight five-vertex path.

Thus closure is exactly defect compression from the canonical width-three window to width at most two.

## Compatible deletion covers glue globally

An ordered path cover assigns to every ordered pair of vertices in its domain one of three pair states: same component with the first preceding the second, same component with the reverse precedence, or different components. Two covers are compatible on their intersection when all such pair states agree.

Let q>=1 and D be a set of deletion labels with
|D|>=max(4,q+2).
For each d in D let F_d be a cover of H-d by at most q tight paths, and suppose every two F_d are compatible on their intersection.

For distinct u,v choose d in D-{u,v}; compatibility makes the pair state independent of d. The induced same-component relation is transitive because any three vertices occur together in some F_d, except only the |D|=3 case which is excluded here. Each equivalence class inherits a total order, because every triple of vertices is seen inside one path cover. There are at most q classes, else q+1 representatives survive in some deletion cover. Every three consecutive vertices in a class remain consecutive in some F_d avoiding them, hence form a tight triple. Therefore the classes themselves are tight paths and give a global cover by at most q paths, restricting exactly to the deletion covers.

For q=2, any four exact deletion covers in a counterexample cannot be mutually compatible.

The threshold four is genuinely needed for exact one-path gluing. On four vertices {0,1,2,3}, take the tight triples
(2,0,1),(1,0,3),(3,0,2),
(0,1,2),(3,1,0),(2,1,3),
(1,2,0),(0,2,3),(3,2,1),
(0,3,1),(2,3,0),(1,3,2),
with all reverses non-tight. The Hamilton paths
(0,1,2), (0,2,3), (0,3,1)
on the deletions of 3,1,2 are pairwise compatible, yet no Hamilton path on all four vertices exists. This does not contradict two-path coverability.

## Support-compatible families localize to one critical class

Now assume pc(H)>2. Let |D|>=3 and let F_d be exact two-covers of H-d that are pairwise support-compatible: they agree only on whether common pairs lie in the same component, not necessarily on order.

Define u~v using any F_d with d outside {u,v}. Support compatibility makes this well-defined. Transitivity follows by viewing triples inside one cover; in the only exceptional case D={u,v,w}, an auxiliary vertex outside D rules out a failure of transitivity using the two-component bound. Hence ~ is an equivalence relation with exactly two classes, say X,Q.

All deletion labels lie in the same class. If a in D∩X and b in D∩Q, then F_b Hamiltonizes X and F_a Hamiltonizes Q, so X|Q would two-cover H. Thus D⊆X. Every F_d has support partition
(X-{d}) | Q.
Consequently H[Q] and every H[X-{d}] are Hamiltonian, while H[X] is non-Hamiltonian. One may normalize the Q-component to one fixed Hamilton order across the entire family. All remaining incompatibility is therefore relative-order disagreement inside the varying Hamilton paths on X-{d}.

## A compatible pair localizes to one insertion obstruction

Take two exact deletion covers F_a of H-a and F_b of H-b that are fully compatible on
W=V(H)-{a,b}.
Their common pair data give exactly two nonempty ordered support classes P,Q. In F_a the missing vertex b is inserted at one slot of exactly one common class; in F_b the missing vertex a is inserted at one slot of one class.

If a and b insert into different common classes, taking those two augmented components gives a spanning two-cover. Thus both insert into the same class, say
P=(p_1,...,p_m),
while Q is unchanged.

If their insertion slots differ by at least two, insert both vertices into P at their respective slots. No consecutive triple contains both inserted vertices; every triple is inherited from one deletion cover or from the common P-order. The resulting path together with Q spans H, contradiction. Therefore compatible insertions use identical or adjacent slots.

If the slots are adjacent, write the common order as
P=L,z,R
with
F_b=(L,a,z,R)|Q,
F_a=(L,z,b,R)|Q.
Every triple of
(L,a,z,b,R)
is certified except possibly (a,z,b). If that triple were tight, the displayed path with Q would two-cover H. Hence (a,z,b) is non-tight, and boundary antisymmetry forces
(b,z,a)
tight.

Thus deletion compatibility supplies the exact local obstruction interface for defect compression: four compatible states glue globally; a support-compatible family collapses to one critical Hamilton-deletion class; and a compatible pair can fail only through a single common insertion slot or an adjacent-slot reversing triple.
