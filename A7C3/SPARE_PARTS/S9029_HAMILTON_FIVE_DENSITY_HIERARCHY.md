# S9029 — Hamilton-Five Density Hierarchy

## Theorem A — four of six deletions are Hamilton-five

Every six-vertex subset E of a Strong Level-(1) boundary tournament has at least four vertices e such that E\{e} supports a tight five-vertex path.

### Proof

Let M={e∈E : E\{e} supports a tight five-path}. Fix any three-subset T⊂E and put P=E\T. By boundary antisymmetry, every three-set admits a tight trimer orientation. The three vertices of T are distinct and exterior to P, so `S9023`, Theorem A implies that at least one of the three five-sets obtained by adjoining two vertices of T to P is Hamiltonian. Those three sets are exactly E\{t} for t∈T. Hence M∩T≠∅ for every three-subset T⊂E. If |E\M|≥3, choosing T⊂E\M of size three contradicts this. Therefore |E\M|≤2, so |M|≥4.

## Theorem B — fixed-subset density hierarchy

Let W be an r-vertex subset, r>=6, of a Strong Level-(1) boundary tournament, and let S subset W have size s in {0,1,2,3}. Let h_5(W;S) be the number of five-subsets F of W containing S that support a tight P5. Then h_5(W;S) >= ((4-s)/(6-s)) * binom(r-s,5-s). Explicitly: at least two-thirds of all five-subsets of W are Hamilton-five supports; every fixed vertex lies in at least three-fifths of its possible five-set supersets that are P5 supports; every fixed pair lies in at least one-half; and every fixed triple lies in at least one-third. In particular every physical triple in any six-or-larger vertex set has many Hamilton-five extensions.

### Proof

Fix S with |S|=s<=3. Consider all six-subsets U of W containing S. There are binom(r-s,6-s) of them. For any such U, Theorem A says at least four of the six five-subsets U-{u} support tight P5s. A five-subset U-{u} fails to contain all of S only when the omitted vertex u lies in S; there are exactly s such omissions. Hence among the at least four Hamilton five-subsets, at least 4-s contain S. Therefore the number N of incident pairs (U,F), where S subset F subset U, |F|=5, |U|=6 and F supports a P5, satisfies N >= (4-s) binom(r-s,6-s). On the other hand, each Hamilton five-subset F of W containing S lies in exactly r-5 six-subsets U of W, obtained by adjoining one vertex of W-F. Hence N=(r-5) h_5(W;S). Dividing and using binom(r-s,6-s)/(r-5)=binom(r-s,5-s)/(6-s) gives h_5(W;S) >= ((4-s)/(6-s)) binom(r-s,5-s). Substituting s=0,1,2,3 yields the stated fractions 2/3, 3/5, 1/2, 1/3.

## Why this is reusable

A local six-vertex Hamilton-five guarantee amplifies by double counting into uniform density through every fixed vertex, pair, and triple. This gives a ready-made supply of Hamilton five-supports around prescribed coordinates.

## Scope and nonclaims

The theorem counts supports, not Hamilton orders, and supplies no endpoint prescription on those paths.

## Provenance

Rescued from accepted archived results `R195`, `R228`.
