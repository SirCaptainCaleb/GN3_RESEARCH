# S9023 — Fixed-Trimer Extension and Triangle-Free Bad Graph

## Theorem A — three exterior vertices force a good pair

Let `P` be a three-vertex support carrying a tight trimer in a Strong Level-(1) boundary tournament, and let `x,y,z` be three distinct vertices outside `P`. Then at least one of the three five-sets

`P∪{x,y}`, `P∪{x,z}`, `P∪{y,z}`

supports a tight Hamilton `P5`.

### Proof

We use S9022, the parallel-source-turn theorem: if distinct `a,c,p,q,r` satisfy

`(a,p,c), (a,q,c), (a,r,c)`

tight, then `{a,c,p,q,r}` has a Hamilton `P5`.

Up to relabelling, the restriction to the three vertices of `P` is cyclic or transitive.

### Cyclic core

Write `P={a,b,c}` with

`abc, bca, cab`

tight. For an exterior vertex `w`, define

`S(w)={1 : awc tight, 2 : bwa tight, 3 : cwb tight}`.

Assume for contradiction that all three pair-extensions are non-Hamiltonian.

The sets `S(x),S(y),S(z)` are pairwise disjoint. Indeed, if, say, `1∈S(x)∩S(y)`, then

`abc, axc, ayc`

are three parallel tight trimers, so S9022 gives a Hamilton `P5` on `P∪{x,y}`. Coordinates `2` and `3` are identical after cyclic relabelling.

No `S(w)` is empty. Suppose `S(x)=∅`. Boundary antisymmetry gives

`cxa, axb, bxc`

tight. Since `S(y)` and `S(z)` are disjoint, one of them, say `S(y)`, has size at most one.

If `S(y)=∅` or `{1}`, then `ayb,byc` are tight. Comparing the reversal pair `xby,ybx` gives respectively

`a,x,b,y,c` or `a,y,b,x,c`,

so one is a Hamilton `P5`.

If `S(y)={2}`, then `cya,byc` are tight. Comparing `xcy,ycx` gives

`b,x,c,y,a` or `b,y,c,x,a`.

If `S(y)={3}`, then `cya,ayb` are tight. Comparing `xay,yax` gives

`c,x,a,y,b` or `c,y,a,x,b`.

Each case contradicts the assumed non-Hamiltonicity. Hence the three pairwise-disjoint nonempty signatures are exactly the three singletons. Relabel so

`S(x)={1}, S(y)={2}, S(z)={3}`.

Thus, besides the core turns, we know

`axc, axb, bxc; cya, bya, byc; cza, azb, czb`

are tight. Compare `bxy` with its reverse `yxb`.

If `bxy` is tight, successive failure of

`a x b y c`, `y b x c a`, `b y a c x`, `b c a y x`, `c b x y a`

forces

`ybx, acx, cay, xya, xbc`

tight. Then

`x,b,c,a,y`

is a Hamilton `P5`, contradiction.

If `yxb` is tight, successive failure of

`b x c y a`, `a b y c x`, `y b a x c`, `x a b c y`,
`y x a b c`, `a x y c b`, `a c y x b`, `c y x b a`

forces

`ycx, yba, xab, ycb, axy, cyx, yca, abx`

tight, and then

`y,c,a,b,x`

is a Hamilton `P5`, contradiction.

Thus the cyclic case is impossible under the assumption that all three pair-extensions are non-Hamiltonian.

### Transitive core

Now relabel the core so

`abc, acb, bac`

are tight. For an exterior vertex `w`, consider the four two-turn packets

`M1(w): caw,cwb`,

`M2(w): wca,bwa`,

`P1(w): acw,bwc`,

`P2(w): awb,wac`.

Call the `M` packets negative and the `P` packets positive.

First, every vertex belonging to a non-Hamiltonian pair-extension carries at least one packet. Put

`r=[acw], s=[awb], t=[bwc], u=[caw]`.

The four packets are respectively

`u∧¬t`, `¬r∧¬s`, `r∧t`, `s∧¬u`.

If none occurs and `r=0`, absence of `M2` gives `s=1`, absence of `P2` gives `u=1`, and absence of `M1` gives `t=1`. If `r=1`, absence of `P1` gives `t=0`, then absence of `M1` gives `u=0`, and absence of `P2` gives `s=0`. Thus the only packet-free patterns are

`(r,s,t,u)=(0,1,1,1)` and `(1,0,0,0)`.

In the first pattern `wca,awb,bwc,caw` are tight. For any fifth vertex `v`, comparison of `vbw` and `wbv` gives respectively the Hamilton paths

`v,b,w,c,a` or `c,a,w,b,v`.

In the second pattern `acw,bwa,cwb,wac` are tight, and the same comparison gives

`a,c,w,b,v` or `v,b,w,a,c`.

Therefore a vertex that belongs to a bad pair must carry at least one sign.

Vertices carrying the same sign cannot form a bad pair. It is enough to check the three packet-type pairs for each sign; reversing the order of `x,y` supplies the symmetric orientation when needed.

For `M1(x),M1(y)`, compare `xby,ybx`. If `xby` is tight, failure of `a c x b y` and then `c x b y a` forces `xca,ayb`, after which

`x,c,a,y,b`

is a `P5`. The other orientation is symmetric.

For `M1(x),M2(y)`, if `axb` is tight then

`y,c,a,x,b`

is already a `P5`. Otherwise `bxa` is tight; failure of `b y c a x` and `c x b y a` forces `cyb,ybx`, and then

`c,y,b,x,a`

is a `P5`.

For `M2(x),M2(y)`, if `xby` is tight, failure of `c x b y a` and then `b x c a y` forces `bxc,yac`, and

`x,b,y,a,c`

is a `P5`. The other orientation is symmetric.

For `P1(x),P1(y)`, if `xcy` is tight, failure of `a b x c y` forces `xba`, and

`x,b,a,c,y`

is a `P5`; otherwise swap `x,y`.

For `P1(x),P2(y)`, if `xya` is tight then

`x,y,a,c,b`

is a `P5`. Otherwise `ayx` is tight; failure of `b a c x y`, `a y x c b`, `b a y x c` forces `yxc,bcx,yab`, and

`y,a,b,c,x`

is a `P5`.

For `P2(x),P2(y)`, if `xay` is tight, failure of `x a c b y` forces `ybc`, and

`x,a,y,b,c`

is a `P5`; otherwise swap `x,y`.

Hence every bad pair has opposite signs. Moreover, a vertex carrying both signs cannot have a bad partner: every other endpoint of a bad pair carries at least one sign and would therefore share one of its signs. Thus three pairwise-bad exterior vertices would each carry a unique sign from a two-element set, so two of them would have the same sign, contradiction.

Therefore at least one of `P∪{x,y}`, `P∪{x,z}`, `P∪{y,z}` supports a Hamilton `P5`. QED.

## Theorem B — bad extension pairs form a triangle-free graph

Let `P` be a tight trimer in a Strong Level-(1) boundary tournament and let `X` be any set of `m>=3` vertices disjoint from `P`. Form a graph `G_bad` on `X` by joining `x,y` when the five-set `V(P)∪{x,y}` does not support a tight `P5`. Then `G_bad` is triangle-free. Consequently

`|E(G_bad)| <= floor(m^2/4)`,

so at least

`binom(m,2)-floor(m^2/4)`

pairs `{x,y}` extend `P` to a Hamiltonian five-support. Equality in the bad-pair bound forces the Mantel extremal structure: `G_bad` is a complete bipartite graph with part sizes `floor(m/2),ceil(m/2)`. Equivalently, in the equality case the outside vertices split into two nearly equal classes and every within-class pair extends `P` to a tight `P5`.

### Proof

For any three distinct `x,y,z` in `X`, Theorem A applied to `P,x,y,z` says at least one of `P∪{x,y}`, `P∪{x,z}`, `P∪{y,z}` supports a tight `P5`. Therefore not all three pairs `xy,xz,yz` can be edges of `G_bad`, so `G_bad` is triangle-free. Mantel's theorem gives

`|E(G_bad)|<=floor(m^2/4)`,

with equality exactly for the balanced complete bipartite graph `K_{floor(m/2),ceil(m/2)}`. The complementary good-pair count follows immediately. In the equality case every within-part pair is absent from `G_bad` and hence is a good `P5` extension of `P`. QED.

## Why this is reusable

The theorem is local, uses only Strong Level-(1) boundary antisymmetry, and converts Hamilton-five extension around a fixed tight trimer into ordinary graph theory. Failure pairs form a triangle-free graph, so Mantel's theorem and its equality case become immediately available. The result needs no smallest-counterexample hypothesis, deletion-cover structure, ancestry, or R24/R5 machinery.

## Scope and nonclaims

The theorem guarantees existence of a Hamilton `P5` on one fixed-trimer pair-extension. It does not prescribe the endpoints of that `P5`. Endpoint control for the parallel-source subconfiguration is supplied separately by S9022.

## Provenance

The statements were rescued from archived results `R146` and `R328`. The original durable proof of Theorem A was a finite SAT/DPLL certificate. The proof above is a later direct human reconstruction developed during the E8997 terminal composition and replaces that computational certificate without changing the theorem statement.
