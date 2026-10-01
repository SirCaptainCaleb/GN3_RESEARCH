# Maximin and balanced-cover compression

## Statement

Minimum counterexamples admit balanced three-covers and strong deletion-cover size control. The maximin parameter rho compresses to a non-Hamiltonian complement of order at most 2rho+1; sharpness has a unique (a,rho+1,rho) residue with a global complement-size ladder, with additional collapse for rho=3 and impossibility of the sharp rho=4 residue.

## Body

# Maximin and balanced-cover structural reductions

Let `H` be a minimum-order counterexample to the assertion that every boundary tournament has path-cover number at most two. Then `|V(H)|>10`.

## Theorem

For every vertex `v` and every exact two-path cover
`U|V`
of `H-v`, both `U` and `V` have order at least three.

Consequently, after naming a larger component
`U=(u_0,u_1,...,u_{r-1})`
with `r>=5`, both
`(u_1,u_0,v) | (u_2,...,u_{r-1}) | V`
and
`(u_0,...,u_{r-3}) | (v,u_{r-1},u_{r-2}) | V`
are spanning three-path covers of `H`. Every component in each cover has order at least three.

In particular, every vertex of a smallest counterexample belongs to a three-vertex component in a spanning three-path cover all of whose components are nontrivial of order at least three; indeed it has such covers arising from both ends of one component of any exact two-cover of its deletion.

## Proof

Fix `v` and an exact two-path cover `U|V` of `H-v`. Suppose, say, `|U|<=2`. Then the induced boundary tournament on `V(U) union {v}` has order at most three and is Hamiltonian. A Hamilton path on that set together with the path `V` would form a spanning two-path cover of `H`, contradiction. Hence both components have order at least three.

Since `|V(H)|>10`, the deletion `H-v` has at least ten vertices. Therefore one component, call it `U`, has order at least five. Write
`U=(u_0,u_1,...,u_{r-1})`, `r>=5`.

If `(v,u_0,u_1)` were tight, then
`(v,u_0,u_1,...,u_{r-1})`
would be a tight path on `V(U) union {v}`. Together with `V` this would two-cover `H`, impossible. Boundary antisymmetry therefore gives
`(u_1,u_0,v)`
tight.

Likewise, if `(u_{r-2},u_{r-1},v)` were tight, then
`(u_0,...,u_{r-1},v)`
together with `V` would two-cover `H`. Hence
`(v,u_{r-1},u_{r-2})`
is tight.

The two displayed triples are therefore tight three-vertex paths. Deleting the first two vertices from the displayed order of `U` leaves the tight suffix
`(u_2,...,u_{r-1})`,
and deleting the last two leaves the tight prefix
`(u_0,...,u_{r-3})`.
Each has order `r-2>=3`, while `V` has order at least three. The two asserted spanning three-path covers follow. ∎

This suggests replacing the singleton-sensitive lexicographic normalization by a balanced three-cover normalization when attacking the grand theorem: three-vertex components are universally available, not exceptional.

# Lexicographic deletion-cover control

# Vertex-deletion covers force a singleton-or-majority dichotomy

Let `H` be a minimum-order counterexample to the assertion that every boundary tournament has path-cover number at most two. Let
`A|B|C`
be a spanning three-path cover whose decreasing component-order triple is lexicographically maximal, and put
`a=|A|`, `b=|B|`, `c=|C|`,
with `a>=b>=c` and `n=a+b+c`.

## Theorem

For every vertex `v in V(H)` and every exact two-path cover
`U|V`
of `H-v`, if `x=max{|U|,|V|}` and `y=min{|U|,|V|}`, then `x<=a`.

If `x=a`, then necessarily `c=1` and `y=b`.

Consequently, if `c>=2`, then every exact two-path cover of every `H-v` satisfies
`b+c <= |U|,|V| <= a-1`.
In particular,
`a>=ceil((n+1)/2)`
and hence
`b+c<=a-1`.
Moreover, when `c>=2`, both components of every exact two-path cover of every `H-v` meet `V(A)`.

## Proof

Fix `v` and an exact two-path cover `U|V` of `H-v`, and order the two components so that `x>=y`. Then
`U|V|(v)`
is a spanning three-path cover of `H`. Its decreasing component-order triple is `(x,y,1)` because every component of an exact two-cover of `H-v` is nontrivial. Lexicographic maximality of `A|B|C` therefore gives `x<=a`.

Suppose `x=a`. Then
`y=n-1-a=b+c-1`.
Because the first coordinates of the two decreasing triples agree, lexicographic maximality also gives `y<=b`. Hence
`b+c-1<=b`,
so `c<=1`. Since `c>=1`, one has `c=1`, and then `y=b`.

Now assume `c>=2`. The previous paragraph rules out `x=a`, so `x<=a-1`. Since
`x+y=n-1`,
we obtain
`y=n-1-x >= n-1-(a-1)=n-a=b+c`.
Thus both component orders lie in the interval `[b+c,a-1]`. In particular
`n-1=x+y<=2(a-1)`,
so
`a>=ceil((n+1)/2)`.
Equivalently `b+c=n-a<=a-1`.

It remains to prove that both components meet `V(A)`. First note that `H[V(B) union V(C)]` is non-Hamiltonian: otherwise a Hamilton path on `V(B) union V(C)` together with the Hamilton path `A` would be a spanning two-path cover of `H`.

Suppose one component, say `U`, is disjoint from `V(A)`. If `v notin V(A)`, then
`|U|<=b+c-1`,
contradicting the already proved lower bound `|U|>=b+c`.

If `v in V(A)`, then `U` lies in `V(B) union V(C)`, which has exactly `b+c` vertices. Since `|U|>=b+c`, equality holds and `U` is a Hamilton path on all of `V(B) union V(C)`, contradicting the preceding non-Hamiltonicity.

Therefore both components meet `V(A)` for every vertex deletion. ∎

This gives a global dichotomy for the remaining augmentation problem: either a lexicographically maximal three-cover has a singleton smallest component, or its longest component is a strict majority path and every vertex-deletion exact two-cover necessarily splits that majority path between its two components.

# Balanced normalization

Let `H` be a minimum-order counterexample to the two-cover conjecture. By `the balanced-three-cover theorem above` there exists a spanning three-path cover all of whose components have order at least three. Among all such **balanced** spanning three-covers choose
`A|B|C`
with decreasing component-order triple lexicographically maximal, and write
`a=|A|>=b=|B|>=c=|C|>=3`.

Fix any vertex `v` and any exact two-path cover
`U|V`
of `H-v`. Write
`x=max{|U|,|V|}` and `y=min{|U|,|V|}`.
By `the balanced-three-cover theorem above`, `y>=3`.

## 1. Small deletion-cover side

Suppose first that `y=3` or `y=4`, and let `W` be the component of order `y`. The set
`F=V(W) union {v}`
cannot be Hamiltonian, because a Hamilton path on `F` together with the other component of `H-v` would be a spanning two-cover of `H`.

Hence:

- if `y=3`, then `F` is a non-Hamiltonian four-set whose complement is Hamiltonian;
- if `y=4`, then `F` is a non-Hamiltonian five-set whose complement is Hamiltonian.

Thus a 3-vertex deletion-cover side enters the codimension-four configuration directly, while a 4-vertex side enters the five-complement configuration directly. ∎

## 2. Deletion covers with both sides at least five

Assume now that `y>=5`. Let the smaller component be
`V=(v_0,...,v_{y-1})`.
If `(v,v_0,v_1)` were tight, then adjoining `v` to the beginning of `V` and keeping `U` would two-cover `H`, impossible. Hence boundary antisymmetry gives
`(v_1,v_0,v)`
tight. Therefore
`(v_1,v_0,v) | (v_2,...,v_{y-1}) | U`
is a balanced spanning three-cover of `H`, of component orders
`3,y-2,x`.
Since `x>=y>=5`, its largest component has order `x`. Balanced lexicographic maximality therefore gives
`x<=a`.

If equality `x=a` holds, then the second component order of the new balanced cover is `y-2`, so balanced lexicographic maximality gives
`y-2<=b`.
But
`y=n-1-a=b+c-1`,
and hence
`b+c-3<=b`.
Thus `c<=3`, and since `c>=3`,
`c=3`
and
`y=b+2`.

Consequently, if `c>=4`, every exact two-cover of every vertex deletion whose smaller side has order at least five actually satisfies
`x<=a-1`.
If no vertex-deletion exact two-cover has a side of order three or four, this applies to every such cover. Then
`y=n-1-x>=b+c`,
so every component of every vertex-deletion exact two-cover lies in
`[b+c,a-1]`.
In particular
`a>=ceil((n+1)/2)`.

The same conclusion holds when `c=3` provided no deletion-cover has `x=a`. If some deletion-cover does have `x=a`, then necessarily its component orders are exactly
`a,b+2`.
Applying the same endpoint split at either end of its `b+2` component produces balanced spanning three-covers with component-order triple exactly
`(a,b,3)`. ∎

## 3. Both deletion-cover components meet the longest balanced component in the strict branch

Assume the strict branch: every exact two-cover of every `H-v` has component orders in
`[b+c,a-1]`.
Then both components of every such cover meet `V(A)`.

Indeed, if `v` lies outside `A`, a component disjoint from `A` has order at most `b+c-1`, contradicting the lower bound `b+c`. If `v in V(A)`, a component disjoint from `A` has order at most `b+c`; equality would make `H[V(B) union V(C)]` Hamiltonian, and that Hamilton path together with `A` would two-cover `H`. ∎

## 4. Arithmetic of the `c=3` residue

Assume no vertex-deletion exact two-cover has a side of order three or four, and `c=3`. For any exact two-cover of any `H-v`, write its component orders as `x>=y`. Section 2 gives
`y>=5`, `x<=a`, and
`x+y=n-1=a+b+2`.

Since both `x` and `y` are at most `a`,
`a+b+2<=2a`,
so
`a>=b+2`.

If `a=b+2`, then
`x+y=2a`
with `x,y<=a`, hence
`x=y=a`
for every vertex `v` and every exact two-cover of `H-v`. Thus
`n=2a+1`
and every vertex deletion has universal equal-split exact covers.

If `a=b+3`, then
`x+y=2a-1`.
Since `x<=a` and `x>=y`, one must have
`(x,y)=(a,a-1)`
for every vertex deletion and every exact two-cover.

More generally, if even one vertex-deletion exact two-cover lies in the strict case `x<=a-1`, then also `y<=a-1`, so
`a+b+2=x+y<=2a-2`,
and therefore
`a>=b+4`.

Hence the exceptional `c=3` branch has an exact numerical stratification:
- gap `a-b=2`: universal equal split `a|a`;
- gap `a-b=3`: universal near-equal split `a|(a-1)`;
- a genuinely strict deletion cover can occur only when `a-b>=4`. ∎

Hence the direct grand-conjecture search admits the following balanced normalization:

1. a vertex deletion exposes a 3-side, giving the codimension-four configuration;
2. a vertex deletion exposes a 4-side, giving the five-complement configuration;
3. every deletion-cover side has order at least five, and then either the `c=3` residue has the exact gap stratification above, or the balanced longest component is a strict majority and every deletion two-cover splits it between its two components.

This does not close the small-complement configurations, but it shows that they arise canonically from the global problem rather than as separate ad hoc cases.

# General maximin compression

Let `H` be a minimum-order counterexample to the two-cover conjecture. Define
`rho=max_F min{|P|: P is a component of F}`,
where `F` ranges over spanning exact three-path covers of `H`, and put `rho=r`.

Then there is a tight path `P` such that its complement
`F=V(H)-V(P)`
is non-Hamiltonian and satisfies
`4<=|F|<=2r+1`.

## Proof

Choose a spanning exact three-cover
`A|B|C`
whose minimum component order is `r`.
Since all three component orders are at least `r`,
`n=|V(H)|>=3r`.

### Case 1: `n=3r`

Then all three components have order exactly `r`. Take `P=A`. Its complement has order
`|F|=|B|+|C|=2r`.

The path `A` is proper. By minimality, its complement has path-cover number at most two. It cannot be Hamiltonian, because a Hamilton path on `F` together with `A` would give a spanning two-path cover of `H`. Hence `H[F]` is non-Hamiltonian, and
`|F|=2r<=2r+1`.

### Case 2: `n>3r`

At least one component of the chosen maximin cover has order at least `r+1`. Take a contiguous tight subpath
`S`
of that component with exactly `r+1` vertices.

The complement `H-S` is proper and nonempty. By the minimum-counterexample complement lemma it has path-cover number exactly two. Choose an exact cover
`H-S=P|Q`
with
`|P|>=|Q|`.

If `|Q|>=r+1`, then
`S|P|Q`
would be a spanning exact three-path cover whose three component orders are all at least `r+1`, contradicting the definition of `rho=r`. Therefore
`|Q|<=r`.

Now take the larger complementary component `P` as the path in the conclusion. Its complement is
`F=V(S) union V(Q)`,
so
`|F|=(r+1)+|Q|<=2r+1`.

The path `P` is proper because `Q` and `S` are both nonempty. Again `H[F]` cannot be Hamiltonian, since a Hamilton path on `F` together with `P` would two-cover `H`. Thus `H[F]` is non-Hamiltonian.

Finally every tight path in a minimum counterexample leaves at least four vertices outside it, so `|F|>=4`. ∎

For `r=4` this recovers the bound `|F|<=9` from `the earlier rho-four complement bound`. For `r=3` it gives the coarse bound seven; the stronger theorem `the sharper rho-three small-complement theorem` improves that level all the way to the four- or five-complement frontier.

# Sharp maximin residue

Let `H` be a minimum-order counterexample to the two-cover conjecture, and let
`rho=r`.
Among spanning exact three-path covers whose minimum component order is `r`, choose
`A|B|C`
with decreasing component-order triple lexicographically maximal. Write
`a=|A|>=b=|B|>=|C|=r`.

## Theorem

Either there is a tight path whose complement is non-Hamiltonian of order at most `2r`, or all of the following hold:

1. `n>3r`;
2. `b=r+1`, so the maximin-lex cover has orders `a,r+1,r`;
3. for every contiguous tight subpath `S` of `A` with `|S|=r+1`, every exact two-cover of `H-S` has component-order multiset `{a,r}`.

Thus the general `2r+1` complement bound is sharp only in a unique two-small-tail geometry, and in that residue every `(r+1)`-window of the longest maximin component has a universal `a|r` complementary two-cover size pattern.

## Proof

If `n=3r`, then `a=b=r`. The complement of `A` has order `2r`, is two-covered by `B|C`, and is non-Hamiltonian, because a Hamilton path on it together with `A` would two-cover `H`. Hence the first alternative holds. We may therefore assume `n>3r`.

If `b=r`, the same argument with the complement `V(B) union V(C)` of `A` again gives a non-Hamiltonian complement of order exactly `2r`. Hence, under failure of the first alternative,
`b>=r+1`.

Now let `S` be any contiguous subpath of `A` of order `r+1`. Since `S` is a proper tight path, the minimum-counterexample complement lemma gives
`pc(H-S)=2`.
Choose any exact two-cover
`H-S=P|Q`
with
`p=|P|>=q=|Q|`.

If `q>=r+1`, then
`S|P|Q`
would be a spanning exact three-cover whose three component orders are all at least `r+1`, contradicting `rho=r`. Hence
`q<=r`.

If `q<=r-1`, the complement of the larger path `P` is
`V(S) union V(Q)`,
of order at most
`(r+1)+(r-1)=2r`.
It is non-Hamiltonian, since otherwise a Hamilton path on that complement together with `P` would two-cover `H`. This is the first alternative. Therefore, under failure of that alternative, every such exact cover has
`q=r`.

Then
`p=n-(r+1)-r=n-2r-1`.

Suppose `b>=r+2`. Since
`n=a+b+r`,
we have
`a=n-b-r<=n-2r-2=p-1`.
But `S|P|Q` is another spanning exact three-cover with minimum component order `r`, and its largest component has order at least `p>a`. This contradicts the lexicographic maximality of `A|B|C` among maximin covers. Hence
`b<=r+1`.

Combined with `b>=r+1`, this gives
`b=r+1`.
Consequently
`n=a+2r+1`,
and the displayed value of `p` becomes
`p=a`.
Thus every exact two-cover of every `(r+1)`-vertex contiguous subpath deletion from `A` has component orders exactly `a` and `r`. ∎

# Moving globally longest paths

Let `H` be a minimum-order counterexample to the two-cover conjecture with maximin parameter
`rho=r`.
Assume that no tight path of `H` has a non-Hamiltonian complement of order at most
`2r`.

Let
`A|B|C`
be the maximin-lex cover from `the sharp maximin theorem above`. Thus
`|A|=a`,
`|B|=r+1`,
`|C|=r`,
`n=a+2r+1`,
and for every contiguous subpath
`S`
of `A` with
`|S|=r+1`,
every exact two-cover
`H-S=P|Q`
has component orders
`|P|=a`
and
`|Q|=r`.

Then:

1. `A` is a globally longest tight path of `H`.
2. For every such window `S` and every exact cover `H-S=P|Q`, the path `P` is also globally longest.
3. Consequently, if
   `P=(p_0,...,p_{a-1})`,
   then every vertex
   `x in V(H)-V(P)=V(S) union V(Q)`
   satisfies both endpoint barriers
   `(x,p_{a-1},p_{a-2})`
   and
   `(p_1,p_0,x)`
   tight.
4. Every globally longest tight path of `H` has order exactly `a` and therefore has a non-Hamiltonian complement of order exactly `2r+1`.

## Proof

Suppose there were a tight path `R` with
`|R|>=a+1`.
Its complement has order
`n-|R|<=a+2r+1-(a+1)=2r`.
The path `R` is proper, and in a minimum counterexample its complement has path-cover number exactly two and is non-Hamiltonian: Hamiltonicity of the complement together with `R` would give a spanning two-cover of `H`.
This contradicts the assumed absence of a non-Hamiltonian path complement of order at most `2r`.
Hence no tight path is longer than `A`, proving that `A` is globally longest.

For a window `S`, `the sharp maximin theorem above` gives
`|P|=a`.
Since `a` is the global maximum tight-path order, `P` is globally longest as well.

Now fix
`x outside V(P)`.
If
`(p_{a-2},p_{a-1},x)`
were tight, appending `x` to `P` would produce a tight path of order `a+1`, impossible. Boundary antisymmetry therefore gives
`(x,p_{a-1},p_{a-2})`
tight.
Similarly, if
`(x,p_0,p_1)`
were tight, prepending `x` would produce a longer path, so
`(p_1,p_0,x)`
is tight.

Finally any globally longest path has order `a`, so its complement has order
`n-a=2r+1`.
The complement is non-Hamiltonian by the minimum-counterexample complement lemma. ∎

Thus the unique `2r+1` residue is a moving-window family of globally longest paths with a fixed complement order and universal endpoint barriers, not merely a numerical exceptional case.

# Complement-size ladder

Let `H` be a minimum-order counterexample with maximin parameter `rho=r`. Assume the sharp residue of `the sharp maximin theorem above`: no tight path has a non-Hamiltonian complement of order at most `2r`. Thus
`n=a+2r+1`,
the maximum order of a tight path is `a`, and a maximin cover has orders
`a,r+1,r`.

## Theorem

Let `T` be any tight path of order
`|T|=r+k`,
where `k>=1` and `r+k<=a`.
Let
`H-V(T)=P|Q`
be any exact two-path cover, with
`p=|P|>=q=|Q|`.

Then
`max{1,r+1-k} <= q <= r`
and
`p=n-(r+k)-q <= a`.

In particular, for `k=1`, every tight path of order exactly `r+1` has the following universal complement structure:

- every exact two-cover of its complement has component orders exactly `a,r`;
- the `a`-vertex component is globally longest;
- its complement has order exactly `2r+1` and is non-Hamiltonian.

Thus the moving family in `the moving-longest-path theorem above` extends from the contiguous `(r+1)`-windows of one distinguished path to every tight `(r+1)`-path in `H`.

## Proof

The path `T` is proper. By the minimum-counterexample complement lemma,
`pc(H-V(T))=2`,
so exact covers `P|Q` exist.

Because `a` is the global maximum tight-path order by `the moving-longest-path theorem above`,
`p<=a`.

If `q>=r+1`, then
`T|P|Q`
is a spanning exact three-path cover all of whose component orders are at least `r+1`, since
`|T|=r+k>=r+1`
and
`p>=q>=r+1`.
This contradicts the definition `rho=r`.
Hence
`q<=r`.

Using
`p+q=n-(r+k)=a+r+1-k`
and `p<=a`, we get
`q>=r+1-k`.
Of course `q>=1` because both components of an exact two-cover are nonempty. Therefore
`q>=max{1,r+1-k}`.

When `k=1`, the upper and lower bounds coincide:
`q=r`.
Then
`p=a+r+1-1-r=a`.
So every exact complementary two-cover has orders exactly `a,r`, and its `a`-path is globally longest.

Finally the complement of that globally longest `a`-path has order
`n-a=2r+1`
and is non-Hamiltonian, since Hamiltonicity together with the `a`-path would give a spanning two-cover of `H`. ∎

# The rho=3 refinement

Let `H` be a minimum-order counterexample to the two-cover conjecture.

## 1. Every vertex deletion produces a spanning three-cover with a four-vertex component

Fix a vertex `v` and an exact two-path cover
`H-v=U|W`,
where
`U=(u_0,...,u_{p-1})`,
`W=(w_0,...,w_{q-1})`.
By `the balanced-three-cover theorem above`, `p,q>=3`.

Because adjoining `v` to the beginning of `U` would otherwise two-cover `H` together with `W`,
`(v,u_0,u_1)`
is non-tight, so
`(u_1,u_0,v)`
is tight.
Similarly
`(w_1,w_0,v)`
is tight.

Exactly one of
`(u_0,v,w_0)`
and
`(w_0,v,u_0)`
is tight.

- In the first case,
  `(u_1,u_0,v,w_0)`
  is a tight four-vertex path, and
  `(u_2,...,u_{p-1}) | (w_1,...,w_{q-1})`
  are the two residual tight paths.
- In the second case,
  `(w_1,w_0,v,u_0)`
  is a tight four-vertex path, and
  `(u_1,...,u_{p-1}) | (w_2,...,w_{q-1})`
  are the two residual tight paths.

Thus every vertex `v`, and every exact two-cover of `H-v`, yields a spanning three-path cover of `H` having a component of order four. ∎

The symmetric construction at the terminal endpoints gives a second such four-tail cover.

## 2. Maximin reduction

Let
`rho`
be the maximum, over all spanning exact three-path covers of `H`, of the minimum component order.
By `the balanced-three-cover theorem above`,
`rho>=3`.

Assume
`rho=3`.

Fix any vertex `v` and exact two-cover
`H-v=U|W`,
and let
`p=max{|U|,|W|}`,
`q=min{|U|,|W|}`.
Again `q>=3`.

If `q=3`, then the three-vertex component together with `v` is a non-Hamiltonian four-set whose complement is the other Hamiltonian path. Indeed, Hamiltonicity of that four-set would two-cover `H`.

If `q=4`, the same argument gives a non-Hamiltonian five-set with Hamiltonian complement.

Suppose neither of these two small-complement configurations occurs. Then
`q>=5`.

If `q>=6`, apply the four-tail construction from Section 1. In either orientation its three component orders are
`4,p-2,q-1`
or
`4,p-1,q-2`.
Since `p>=q>=6`, all three orders are at least four. This contradicts `rho=3`.

Therefore, if `rho=3` and neither small-complement frontier occurs, then for every vertex `v` and every exact two-cover of `H-v`,
`min{|U|,|W|}=5`.

Equivalently every vertex deletion has universal component-order multiset
`{5,n-6}`. ∎

## 3. Forced endpoint orientation when n>=12

Continue in the universal five-side residue and assume
`n>=12`.
Let
`H-v=U|W`
with
`|U|=n-6>=6`,
`|W|=5`,
and write
`U=(u_0,...,u_{p-1})`,
`W=(w_0,...,w_4)`.

At the initial endpoints, if
`(u_0,v,w_0)`
were tight, then the first alternative of Section 1 would give a spanning three-cover with component orders
`4,p-2,4`,
all at least four, contradicting `rho=3`.
Hence
`(w_0,v,u_0)`
is tight.

At the terminal endpoints, the noninsertability barriers give
`(v,u_{p-1},u_{p-2})`
and
`(v,w_4,w_3)`
tight.
If
`(w_4,v,u_{p-1})`
were tight, then
`(w_4,v,u_{p-1},u_{p-2})`
would be a four-tail whose residual components have orders
`4` and `p-2>=4`, again contradicting `rho=3`.
Therefore
`(u_{p-1},v,w_4)`
is tight.

Thus every universal `5|(n-6)` deletion cover satisfies the cross-endpoint constraints
`(w_0,v,u_0)`,
`(u_{p-1},v,w_4)`
tight, in addition to the ordinary noninsertability barriers
`(u_1,u_0,v)`,
`(w_1,w_0,v)`,
`(v,u_{p-1},u_{p-2})`,
`(v,w_4,w_3)`.

So the only maximin-three residue outside the codimension-four and five-complement frontiers is not merely a size condition: every deletion is forced into the same five-side geometry with opposite-end cross barriers. ∎

Let `H` be a minimum-order counterexample to the two-cover conjecture, and let
`rho=max_F min{|P|: P is a component of F}`,
where `F` ranges over spanning exact three-path covers of `H`.

Assume `rho=3`, and assume that no vertex deletion exposes either
- a non-Hamiltonian four-set with Hamiltonian complement, or
- a non-Hamiltonian five-set with Hamiltonian complement.

Then `|V(H)|<=12`.

Equivalently, if `|V(H)|>=13`, the hypotheses above force `rho>=4`.

## Proof

By `the rho=3 four-tail theorem above`, under `rho=3` and the exclusion of the two small-complement frontiers, every vertex `v` and every exact two-cover of `H-v` has component-order multiset
`{5,n-6}`.

Assume for contradiction that `n>=13`. Fix `v` and write one such exact cover as
`H-v=U|W`,
where
`U=(u_0,...,u_{p-1})`, `p=n-6>=7`,
and
`W=(w_0,w_1,w_2,w_3,w_4)`.

Again by `the rho=3 four-tail theorem above`, the initial-end cross orientation is forced:
`(w_1,w_0,v)` and `(w_0,v,u_0)`
are tight. Hence
`P_0=(w_1,w_0,v,u_0)`
is a tight four-vertex path.

Put
`T=(w_2,w_3,w_4)`.
This is a tight three-vertex path.

We claim that both four-sets
`V(T) union {u_1}`
and
`V(T) union {u_{p-1}}`
are non-Hamiltonian.

Indeed, if `V(T) union {u_1}` had a Hamilton path `D`, then
`P_0 | D | (u_2,...,u_{p-1})`
would be a spanning three-path cover of `H` with component orders
`4,4,p-2`.
Since `p>=7`, all three orders are at least four, contradicting `rho=3`.

Likewise, if `V(T) union {u_{p-1}}` had a Hamilton path `D'`, then
`P_0 | D' | (u_1,...,u_{p-2})`
would be a spanning three-path cover with component orders
`4,4,p-2`,
again contradicting `rho=3`.

Now consider the five-set
`Z=V(T) union {u_1,u_{p-1}}`.
We show that `H[Z]` is Hamiltonian.

Suppose instead that `H[Z]` were non-Hamiltonian. The five-set theorem says that every non-Hamiltonian five-set is edge-orderable. In such an edge-order representation, `T` is an increasing three-vertex path, while the two four-sets
`V(T) union {u_1}` and `V(T) union {u_{p-1}}`
are both non-Hamiltonian. The two-bad-four-sets theorem then forces the whole five-set `Z` to have an increasing Hamilton path, contradiction. Therefore `H[Z]` is Hamiltonian.

Let `Q` be a Hamilton path on `Z`. Then
`P_0 | Q | (u_2,...,u_{p-2})`
is a spanning three-path cover of `H`. Its component orders are
`4,5,p-3`.
Because `p>=7`, one has `p-3>=4`. Thus every component has order at least four, contradicting `rho=3`.

This contradiction proves `n<=12`. ∎

The point is that the universal five-side residue is not a genuine large-order obstruction: once the long side has order at least seven, the forced endpoint geometry plus the five-vertex Hamiltonicity machinery automatically raises the minimum component size from three to four.

# The rho=4 sharp residue is impossible

Let `H` be a minimum-order counterexample to the two-cover conjecture with maximin parameter
`rho=4`.

Then some tight path of `H` has a non-Hamiltonian complement of order at most eight.

Equivalently, the sharp `2rho+1=9` residue of `the sharp maximin theorem above` cannot occur when `rho=4`.

## Proof

Assume for contradiction that no tight path has a non-Hamiltonian complement of order at most eight.

By the sharp alternative of `the sharp maximin theorem above`, a maximin-lex spanning three-cover has orders
`a,5,4`
and
`n=|V(H)|=a+9`.

Moreover `a` is the global maximum order of a tight path. Indeed, a tight path of order at least
`a+1`
would leave at most
`n-(a+1)=8`
vertices outside it, and that complement is non-Hamiltonian in a minimum counterexample, contradicting the assumption.

Fix any vertex `v` and any exact two-path cover
`H-v=U|W`,
with
`U=(u_0,...,u_{p-1})`,
`W=(w_0,...,w_{q-1})`,
and
`p>=q`.

Since
`p+q=n-1=a+8`
and every tight path has order at most `a`,
one has
`p<=a`
and therefore
`q>=8`.
Thus also `p>=8`.

Consider the six-set
`E={v,u_0,u_1,u_{p-1},w_0,w_{q-1}}`.

We show that four distinct five-subsets of `E` are non-Hamiltonian.

### 1. Delete `u_1` from `E`

Suppose
`F_1=E-{u_1}`
were Hamiltonian.
After using a Hamilton path on `F_1`, the residual displayed paths are
`(u_1,...,u_{p-2})`
and
`(w_1,...,w_{q-2})`,
of orders
`p-2>=6`
and
`q-2>=6`.
Together with the Hamilton five-path on `F_1`, these give a spanning three-cover of `H` whose minimum component order is at least five, contradicting `rho=4`.
Hence `F_1` is non-Hamiltonian.

### 2. Delete `u_{p-1}` from `E`

If
`F_2=E-{u_{p-1}}`
were Hamiltonian, the residual paths would be
`(u_2,...,u_{p-1})`
and
`(w_1,...,w_{q-2})`,
again of orders at least six.
Thus `F_2` is non-Hamiltonian.

### 3. Delete `w_0` from `E`

If
`F_3=E-{w_0}`
were Hamiltonian, the residual paths would be
`(u_2,...,u_{p-2})`
and
`(w_0,...,w_{q-2})`,
of orders
`p-3>=5`
and
`q-1>=7`.
Thus `F_3` is non-Hamiltonian.

### 4. Delete `w_{q-1}` from `E`

If
`F_4=E-{w_{q-1}}`
were Hamiltonian, the residual paths would be
`(u_2,...,u_{p-2})`
and
`(w_1,...,w_{q-1})`,
of orders
`p-3>=5`
and
`q-1>=7`.
Thus `F_4` is non-Hamiltonian.

The four sets `F_1,F_2,F_3,F_4` are distinct five-subsets of the same six-set `E`.
But the four-of-six theorem says that every six-set has at least four Hamiltonian five-subsets, equivalently at most two non-Hamiltonian five-subsets.
This is a contradiction.

Therefore the sharp nine-vertex-complement residue is impossible, and some tight path has a non-Hamiltonian complement of order at most eight. ∎

This improves the general maximin bound `2rho+1` to `2rho` at `rho=4`.
