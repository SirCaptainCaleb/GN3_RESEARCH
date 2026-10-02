# Three-side fixed-defect transport

## Statement

When an exact deletion cover has a three-vertex side, fourfold replacement failure generates dense shell graphs of exact two-cover supports; at least two exterior defects can each be transported from one end of the long path to the other while preserving the same defect label throughout.

## Body

# Three-side exact-cover transport

Let `H` be a minimum-order counterexample to the two-cover conjecture. Fix a vertex `x` and an exact two-path cover
`H-x=P|Q`,
where
`P=(p_0,p_1,p_2)`
has order three and
`Q=(q_0,q_1,...,q_s)`.

Since `|V(H)|>10`, one has `|Q|>=7`, hence `s>=6`.

Put
`X=V(P) union {x}`
and
`M=(q_1,...,q_{s-1})`.

## Theorem

1. `H[X]` is non-Hamiltonian.
2. Both five-sets `X union {q_0}` and `X union {q_s}` are non-Hamiltonian.
3. For every `z in X`, the five-set
   `(X-{z}) union {q_0,q_s}`
   is Hamiltonian.
4. For every `z in X`, the induced tournament
   `H[V(M) union {z}]`
   is non-Hamiltonian.
5. Consequently, for every `z in X`,
   `(q_2,q_1,z)`
   and
   `(z,q_{s-1},q_{s-2})`
   are tight.

Thus one three-vertex side in a vertex-deletion cover creates four simultaneous exterior vertices that all fail to Hamiltonize the same long interior path `M`, while deleting any one of those four vertices from the six-set `X union {q_0,q_s}` leaves a Hamiltonian five-set.

## Proof

If `H[X]` were Hamiltonian, a Hamilton path on `X` together with `Q` would be a spanning two-path cover of `H`. Hence `H[X]` is non-Hamiltonian.

If `H[X union {q_0}]` were Hamiltonian, its complement is the tight path
`(q_1,...,q_s)`,
so the two Hamilton paths would two-cover `H`. Therefore `X union {q_0}` is non-Hamiltonian. The same argument with the other endpoint shows `X union {q_s}` non-Hamiltonian.

Now consider the six-set
`E=X union {q_0,q_s}`.
Among its six five-subsets, deleting `q_s` gives the non-Hamiltonian set `X union {q_0}`, while deleting `q_0` gives the non-Hamiltonian set `X union {q_s}`.

The four-of-six theorem says that at least four of the six five-subsets of `E` are Hamiltonian. Since two are already non-Hamiltonian, all four remaining five-subsets must be Hamiltonian. These are precisely
`(X-{z}) union {q_0,q_s}`
for `z in X`.

Fix `z in X`. The complement in `H` of this Hamiltonian five-set is exactly
`V(M) union {z}`.
If that complement were Hamiltonian, the two complementary Hamilton paths would form a spanning two-cover of `H`, contradiction. Thus every `M union {z}` is non-Hamiltonian.

Finally, `M=(q_1,...,q_{s-1})` is a tight path of order at least five. If `(z,q_1,q_2)` were tight, then `(z,M)` would Hamiltonize `M union {z}`, impossible. Boundary antisymmetry therefore gives `(q_2,q_1,z)` tight. Similarly, if `(q_{s-2},q_{s-1},z)` were tight, then `(M,z)` would Hamiltonize `M union {z}`; hence its reverse `(z,q_{s-1},q_{s-2})` is tight. ∎

This is a direct-induction obstruction valid at arbitrary ambient order. Any closure of the three-side case may now work with four synchronized nonabsorbable exterior vertices rather than a single failed insertion.

# Common multi-layer endpoint barriers

Let `H` be a minimum-order counterexample to the two-cover conjecture. Fix a vertex `x` and an exact two-path cover
`H-x=P|Q`,
where
`P=(p_0,p_1,p_2)`
has order three and
`Q=(q_0,q_1,...,q_s)`.
By `the fourfold-replacement theorem above`, `s>=6`.

Put
`X=V(P) union {x}`.

## Theorem

There are at least two distinct vertices `z in X` for which all six triples

`(q_1,q_0,z)`,
`(q_2,q_1,z)`,
`(q_3,q_2,z)`,

`(z,q_s,q_{s-1})`,
`(z,q_{s-1},q_{s-2})`,
`(z,q_{s-2},q_{s-3})`

are tight.

Equivalently, at least two of the four exterior vertices in `X` are forced through three consecutive endpoint-barrier layers at both ends of the long path `Q`.

## Proof

From `the fourfold-replacement theorem above`, the five-set
`X union {q_0}`
is non-Hamiltonian.
Consider the six-set
`W_L=X union {q_0,q_1}`.
Every six-set has at least four Hamiltonian five-subsets. One five-subset of `W_L`, namely the one obtained by deleting `q_1`, is `X union {q_0}` and is non-Hamiltonian.

Therefore among the four five-sets
`L_z=(X-{z}) union {q_0,q_1}`, `z in X`,
at least three are Hamiltonian: even if the remaining five-subset `X union {q_1}` is Hamiltonian, three further Hamiltonian deletions are still required.

Let
`G_L={z in X : L_z is Hamiltonian}`.
Then
`|G_L|>=3`.

Symmetrically, `the fourfold-replacement theorem above` says
`X union {q_s}`
is non-Hamiltonian. Apply four-of-six to
`W_R=X union {q_{s-1},q_s}`.
At least three of the four five-sets
`R_z=(X-{z}) union {q_{s-1},q_s}`
are Hamiltonian. Hence, with
`G_R={z in X : R_z is Hamiltonian}`,
one has
`|G_R|>=3`.

Since `|X|=4`,
`|G_L intersection G_R|>=2`.
Fix
`z in G_L intersection G_R`.

The complement in `H` of the Hamiltonian five-set `L_z` is
`{z} union {q_2,q_3,...,q_s}`.
If that complement were Hamiltonian, the two complementary Hamilton paths would give a spanning two-cover of `H`. Hence it is non-Hamiltonian.

The displayed suffix
`(q_2,q_3,...,q_s)`
is tight. Therefore `z` cannot be prepended to it, so
`(z,q_2,q_3)`
is non-tight and boundary antisymmetry gives
`(q_3,q_2,z)`
tight. Likewise `z` cannot be appended to the suffix, so
`(q_{s-1},q_s,z)`
is non-tight and
`(z,q_s,q_{s-1})`
is tight.

Similarly, the complement of the Hamiltonian five-set `R_z` is
`{z} union {q_0,q_1,...,q_{s-2}}`,
which is non-Hamiltonian. Since
`(q_0,...,q_{s-2})`
is tight, failure to prepend and append `z` gives
`(q_1,q_0,z)`
and
`(z,q_{s-2},q_{s-3})`
tight.

Finally, `the fourfold-replacement theorem above` already gives, for every `z in X`,
`(q_2,q_1,z)`
and
`(z,q_{s-1},q_{s-2})`
tight.

Combining the three left barriers and three right barriers proves the claim for every
`z in G_L intersection G_R`,
of which there are at least two. ∎

This is a genuine defect-transport statement: the synchronized obstruction created by a three-vertex deletion-cover component propagates one full edge deeper at both ends of the complementary path for at least two common exterior vertices.

# Dense pair-exchange shell graphs

Let `H` be a minimum-order counterexample to the two-cover conjecture and let
`H-x=P|Q`,
where `|P|=3`,
`Q=(q_0,q_1,...,q_s)`,
and
`X=V(P) union {x}`.
By `the fourfold-replacement theorem above`, `s>=6`.

## Left exchange graph

Put
`A_L=X union {q_0,q_1}`
and consider the rooted seven-set
`W_L=A_L union {q_2}`.

Define a graph `G_L` on the six vertices of `A_L` by joining distinct `a,b` exactly when
`H[{q_2} union (A_L-{a,b})]`
is Hamiltonian.

Then:

1. `delta(G_L)>=3`, so `G_L` has at least nine edges;
2. `G_L` has a Hamilton cycle and a perfect matching;
3. for every edge `ab in E(G_L)`, the complementary support
   `L_{ab}={a,b} union {q_3,q_4,...,q_s}`
   is non-Hamiltonian and has path-cover number exactly two;
4. its canonical exact two-cover is
   `(a,b) | (q_3,q_4,...,q_s)`.

## Right exchange graph

Symmetrically put
`A_R=X union {q_{s-1},q_s}`
and root the seven-set
`W_R=A_R union {q_{s-2}}`
at `q_{s-2}`.

Join distinct `a,b in A_R` in `G_R` exactly when
`H[{q_{s-2}} union (A_R-{a,b})]`
is Hamiltonian.

Then `delta(G_R)>=3`, `G_R` has at least nine edges, a Hamilton cycle and a perfect matching, and every edge `ab` gives a non-Hamiltonian exact-two-cover support
`R_{ab}={a,b} union {q_0,q_1,...,q_{s-3}}`
with canonical cover
`(q_0,...,q_{s-3}) | (a,b)`.

## Proof

The graph-theoretic assertions are exactly the rooted seven-set Hamiltonian shell lemma, applied first to `W_L` with root `q_2` and then to `W_R` with root `q_{s-2}`.

Fix an edge `ab` of `G_L`. By definition the five-set
`F_{ab}={q_2} union (A_L-{a,b})`
is Hamiltonian.
Its complement in `H` is precisely
`L_{ab}={a,b} union {q_3,...,q_s}`.
If `L_{ab}` were Hamiltonian, Hamilton paths on `F_{ab}` and `L_{ab}` would give a spanning two-path cover of `H`, contradiction. Hence `L_{ab}` is non-Hamiltonian.

On the other hand, `(a,b)` is a vacuous tight two-vertex path and `(q_3,...,q_s)` is an inherited tight path. Hence `pc(L_{ab})<=2`. Non-Hamiltonicity gives
`pc(L_{ab})=2`.

The right-hand statement is identical after reversing the role of the two ends of `Q`. ∎

Thus a three-vertex side does not lead merely to isolated insertion failures. It creates two dense pair-exchange graphs, each of minimum degree three, whose Hamilton cycles consist entirely of exact-two-cover pair augmentations of a common long tail. These graphs are natural finite state spaces for the global exact-cover reconfiguration program.

# Left-to-right shell reconfiguration

Let `H` be a minimum-order counterexample to the two-cover conjecture and let
`H-x=P|Q`,
where `|P|=3`,
`Q=(q_0,...,q_s)`,
and
`X=V(P) union {x}`.
By `the fourfold-replacement theorem above`, `s>=6`.

For `j=0,1,2,3` define three-vertex endpoint shells

`D_0={q_0,q_1,q_2}`,
`D_1={q_0,q_1,q_s}`,
`D_2={q_0,q_{s-1},q_s}`,
`D_3={q_{s-2},q_{s-1},q_s}`,

and let
`W_j=X union D_j`.
The complementary vertices of `Q` form one contiguous tight path:

`T_0=(q_3,...,q_s)`,
`T_1=(q_2,...,q_{s-1})`,
`T_2=(q_1,...,q_{s-2})`,
`T_3=(q_0,...,q_{s-3})`.

For each `j`, define an omitted-pair graph `Omega_j` on the seven vertices of `W_j` by

`ab in E(Omega_j)` iff `H[W_j-{a,b}]` is Hamiltonian.

## Theorem

1. Every `Omega_j` has minimum degree at least four and at least fourteen edges. In particular every `Omega_j` is connected.

2. Every edge `ab in E(Omega_j)` determines a non-Hamiltonian induced support
   `T_j union {a,b}`
   of path-cover number exactly two, with canonical exact cover
   `T_j | (a,b)`.

3. Consecutive shell graphs share an edge on their six common vertices:

   `E(Omega_0[W_0 intersect W_1]) intersect E(Omega_1[W_0 intersect W_1]) != empty`,

   and similarly for `(Omega_1,Omega_2)` and `(Omega_2,Omega_3)`.

4. Consequently there exists a finite reconfiguration chain of exact-two-cover five-complement states running from a state based on the left tail `T_0` to a state based on the right tail `T_3`. Every step is of one of two kinds:

   - the tail `T_j` is fixed and the exterior pair changes by one vertex, through two adjacent edges of the connected graph `Omega_j`;
   - the exterior pair is fixed and the tail slides from `T_j` to `T_{j+1}`, using an edge shared by `Omega_j` and `Omega_{j+1}`.

Thus the three-side obstruction contains a proved global exchange route across the entire long path; it is not a collection of isolated endpoint failures.

## Proof

Fix `j` and a vertex `a in W_j`. The six-set `W_j-{a}` has at least four Hamiltonian five-subsets by the four-of-six theorem. Those six five-subsets are exactly
`W_j-{a,b}`
as `b` ranges over `W_j-{a}`.
Hence `a` has degree at least four in `Omega_j`.

Therefore
`delta(Omega_j)>=4`
and the handshake lemma gives
`|E(Omega_j)|>=14`.
A disconnected graph on seven vertices with minimum degree four would need every connected component to have at least five vertices, impossible. Hence every `Omega_j` is connected.

Now fix an edge `ab in E(Omega_j)`. The five-set
`F=W_j-{a,b}`
is Hamiltonian. Its complement in `H` is exactly
`V(T_j) union {a,b}`.
If this complement were Hamiltonian, complementary Hamilton paths would give a spanning two-cover of `H`, contradiction. Hence it is non-Hamiltonian.

But `T_j` is tight and `(a,b)` is a vacuous two-vertex tight path, so the complement has path-cover number at most two. Therefore its path-cover number is exactly two, with the displayed canonical cover.

Next fix consecutive shells `W_j,W_{j+1}` and put
`U=W_j intersect W_{j+1}`.
Then `|U|=6`, and each of `W_j,W_{j+1}` has exactly one vertex outside `U`.

Since `Omega_j` has at least fourteen edges and at most six of them can be incident with its unique vertex outside `U`,
`Omega_j[U]`
has at least eight edges. The same is true for
`Omega_{j+1}[U]`.

There are only
`binom(6,2)=15`
possible edges on `U`. Since
`8+8>15`,
the two induced edge sets intersect. Thus the consecutive shell graphs share an edge.

Choose shared edges
`e_{01}`, `e_{12}`, `e_{23}`
for the three consecutive shell pairs.
Because `Omega_1` is connected, its line graph is connected, so there is a sequence of edges of `Omega_1` beginning at `e_{01}` and ending at `e_{12}` in which consecutive edges share one vertex. Each edge of this sequence gives an exact-two-cover support with fixed tail `T_1`, and sharing one endpoint means the exterior pair changes by one vertex.

Likewise `Omega_2` supplies an edge sequence from `e_{12}` to `e_{23}`.
The shared edges themselves permit the tail changes
`T_0 -> T_1`,
`T_1 -> T_2`,
`T_2 -> T_3`
while keeping the exterior pair fixed.

Concatenating these moves gives the asserted left-to-right reconfiguration chain. ∎

This is a concrete global no-isolation statement inside the three-side branch. It does not yet reach a spanning two-cover, but it proves that the exact-cover obstruction can be transported globally across `Q` through overlapping five-complement states.

# Fixed-defect transport theorem

Assume the three-side setup of `the fourfold-replacement theorem above` and the four shell graphs of `the shell-reconfiguration theorem above`.
Thus
`H-x=P|Q`,
`|P|=3`,
`Q=(q_0,...,q_s)`,
`X=V(P) union {x}`,
and `s>=6`.

Retain the sets `G_L,G_R subseteq X` defined in the proof of `the multi-layer barrier theorem above`, and put
`Z=G_L intersection G_R`.
Then `|Z|>=2`, and every `z in Z` has both endpoint-shell Hamiltonian deletions used below as well as the six barrier triples.

## Theorem

For every `z in Z`, there is a left-to-right reconfiguration chain of non-Hamiltonian exact-two-cover supports in which **every exterior pair contains the same vertex `z`**.

More precisely, using the shell graphs `Omega_0,...,Omega_3` and tails `T_0,...,T_3` of `the shell-reconfiguration theorem above`:

1. `{z,q_2}` is an edge of `Omega_0`;
2. `{z,q_{s-2}}` is an edge of `Omega_3`;
3. for each `j=0,1,2`, the consecutive shell graphs `Omega_j,Omega_{j+1}` have a common edge of the form `{z,c_j}`;
4. hence one can pass through exact-two-cover states
   `T_j union {z,c}`
   while changing only the second exterior vertex at fixed tail, and slide from `T_j` to `T_{j+1}` while keeping the pair `{z,c_j}` fixed.

The chain begins at the exact support
`{z} union {q_2,q_3,...,q_s}`
and ends at
`{z} union {q_0,q_1,...,q_{s-2}}`.

Thus the same exterior vertex `z` is transported from a failed one-vertex extension of the long suffix to a failed one-vertex extension of the long prefix through a connected family of exact-two-cover five-complement states.

## Proof

Fix `z in Z`.

By the construction in `the multi-layer barrier theorem above`,
`(X-{z}) union {q_0,q_1}`
is Hamiltonian. But
`W_0=X union {q_0,q_1,q_2}`.
Therefore
`W_0-{z,q_2}`
is Hamiltonian, so
`{z,q_2} in E(Omega_0)`.

Similarly
`(X-{z}) union {q_{s-1},q_s}`
is Hamiltonian. Since
`W_3=X union {q_{s-2},q_{s-1},q_s}`,
we obtain
`{z,q_{s-2}} in E(Omega_3)`.

Now fix consecutive shell graphs `Omega_j,Omega_{j+1}` and let
`U=W_j intersect W_{j+1}`.
Then `|U|=6`, `z in U`, and each shell has exactly one vertex outside `U`.

By `the shell-reconfiguration theorem above`, every shell graph has minimum degree at least four. Hence `z` has at least four neighbors in `Omega_j`, at most one of which lies outside `U`. Therefore `z` has at least three neighbors inside
`U-{z}`.
The same holds in `Omega_{j+1}`.

There are only five possible neighbors of `z` in `U`. Two subsets of this five-element set of size at least three must intersect. Hence there exists
`c_j in U-{z}`
such that
`{z,c_j}`
is an edge of both `Omega_j` and `Omega_{j+1}`.

Inside a fixed shell `Omega_j`, any two edges incident with `z` are adjacent in the line graph, so the exterior pair can change from `{z,c}` to `{z,c'}` in one pair-exchange step while preserving `z`.

At a shared edge `{z,c_j}`, `the shell-reconfiguration theorem above` permits the tail slide
`T_j -> T_{j+1}`
with the exterior pair fixed.

Starting at `{z,q_2}` in `Omega_0`, pass to a common `z`-edge of `Omega_0,Omega_1`, slide the tail, change to a common `z`-edge of `Omega_1,Omega_2`, slide again, and repeat through `Omega_3`, finally changing the pair to `{z,q_{s-2}}`.

Every encountered edge gives a non-Hamiltonian exact-two-cover support by `the shell-reconfiguration theorem above`.

Finally,
`T_0 union {z,q_2}={z} union {q_2,...,q_s}`,
while
`T_3 union {z,q_{s-2}}={z} union {q_0,...,q_{s-2}}`.
This proves the asserted fixed-defect transport. ∎

This is an explicit no-trapping phenomenon of exactly the type sought in the global no-trapping program: in the three-side branch, at least two exterior vertices can each be moved globally from one end of `Q` to the other without leaving the family of exact-two-cover obstruction states.