# Complementary-arm counting potential and centerwise comparison sensitivities

- Stable ID: note_nori_xi_complementary_arm_count_and_sensitivities
- Author: Astra
- Primary home: section:nori_matroid_generalizations_conjectures
- Labels: proved, boundary-tournament, two-arm-packing, counting, research-tool, open-positivity
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6661_1
- Updated session: session_nori_r6661_1
- Disposition: none
- Successor: none

## Related references

- subsection:antipodal_boolean_lattice_terminal_polarity_and_spanning_one_turn_paths
- subsection:spanning_one_turn_gallery_conjecture_and_opposite_terminal_monochromatic_packing

## Research note

# Complementary-arm counting and comparison sensitivities

For an ordinary reversal-odd boundary coloring b on V, let F_epsilon(A,u,v) count vertex-simple epsilon-monochromatic words on A ending in (u,v). Set F_epsilon({u,v},u,v)=1. For |A|>=3,
F_epsilon(A,u,v)=sum_{x in A\{u,v}} [b(x,u,v)=epsilon] F_epsilon(A\{v},x,u).
Write J(A,u,v)=((V\A) union {u,v},v,u) and define
Z(b)=sum_{epsilon,A,u!=v in A} F_epsilon(A,u,v) F_epsilon(J(A,u,v)).

## Counting theorem

If H_0,H_1 count ordered spanning words with zero and one internal color changes, respectively, then for n>=3
Z(b)=2 H_0(b)+H_1(b).

Proof. Each product counts same-colored arms with opposite terminal pairs, disjoint outside that pair. Reverse the second arm and concatenate along the pair. Their ordinary K_n edges form a graphic-matroid basis of maximum degree two. For a word with one change, the change position uniquely determines its shared pair and arm color, giving one representation. A monochromatic word has two representations, one at each end using a vacuous two-vertex arm. An interior split would give opposite arm colors after reversal. Conversely these constructions account for every counted word.

Consequently Z(b)>0 is equivalent to the spanning one-turn assertion for b.

## Centerwise affinity

Let x_j be the representative bit for a reversal pair of triples. Replace color indicators by x_j or 1-x_j. This extends Z to a polynomial which is affine in the ENTIRE block of comparisons having any fixed middle vertex. Its total degree is at most n-2.

Proof. Each spanning word uses its n-2 internal vertices once each as triple middles. In a complementary arm pair the internal-vertex sets are disjoint: one shared terminal vertex is internal to the first arm, and the other to the second. Thus no monomial uses two comparisons with the same middle vertex.

It follows that flipping bit j changes the potential by
Delta_j Z=(1-2x_j) partial_j Z.
Derivatives associated with a fixed middle vertex are independent of all comparison bits at that vertex. Reorienting several comparisons at that middle vertex changes Z by the sum of their separate flip changes.

Conditional on every other local tournament, minimization at the remaining middle vertex therefore consists of independent pair choices. In a hypothetical zero-potential coloring, the local orientations preserving zero form a subcube: positive flip costs force the corresponding orientations, and zero-cost comparisons may be changed in any combination at that middle vertex. This does not assert transitivity of an optimizing local tournament.

## Full-gradient recurrence

The value and all representative-bit derivatives can be computed together using O(n^3 2^n) arithmetic operations and O(n^2 2^n) storage. Integer bit complexity additionally depends on the sizes of the path counts.

After the forward recurrence, initialize adjoints by
G_epsilon(A,u,v)=2 F_epsilon(J(A,u,v)).
Process states in decreasing |A|. For every predecessor (A\{v},x,u), put c=b(x,u,v), and add G_c(A,u,v) to G_c(A\{v},x,u). For j=(min(x,v),u,max(x,v)), add
(-1)^[x>v] (G_1(A,u,v) F_1(A\{v},x,u)
             -G_0(A,u,v) F_0(A\{v},x,u))
to partial_j Z.
The adjoints used include contributions propagated from larger states.

This is reverse differentiation of the forward recurrence. The initialization differentiates the symmetric complementary-arm product. The flip-change identity was checked against the recomputed potential after every flip during the search runs.

## Reproducible stress test

Exploratory searches in orders 8,9,10,12 produced no zero potential. These searches supply no exhaustive assertion in any of those orders.

For an order-twelve test use increasing middle vertex followed by lexicographic increasing outer pair to index representative bits, and take
M=0x2d1ef2449ffa4843abf74a0fb7dbedfe1f70b4ba5b03b1bf886f7fb2bd5efaf7543a3e7fa4012200f3da0d80976d2804436600c9bdfc00ff018c200cfc2447bbdf401ebffc10016fcf8b8086f1d00001ffc0c.
Independent complementary-arm and direct switch-state recurrences give H_0=0, H_1=770, and Z=770. The longest monochromatic word has ten vertices. The nonzero arm-size contributions are
(4,10):2, (5,9):33, (6,8):190, (7,7):320,
(8,6):190, (9,5):33, (10,4):2.

The following direct recurrence independently verifies the spanning counts.

~~~python
from itertools import combinations
n=12
M=int("2d1ef2449ffa4843abf74a0fb7dbedfe1f70b4ba5b03b1bf886f7fb2bd5efaf7543a3e7fa4012200f3da0d80976d2804436600c9bdfc00ff018c200cfc2447bbdf401ebffc10016fcf8b8086f1d00001ffc0c",16)
R=[(a,b,c) for b in range(n)
   for a,c in combinations([x for x in range(n) if x!=b],2)]
index={t:i for i,t in enumerate(R)}
def color(a,b,c):
    return ((M>>index[min(a,c),b,max(a,c)])&1) ^ (a>c)
F=[{} for _ in range(1<<n)]
for A in range(1<<n):
    vertices=[x for x in range(n) if A>>x&1]
    if len(vertices)<3:
        continue
    if len(vertices)==3:
        for u in vertices:
            for v in vertices:
                if u==v:
                    continue
                x=next(x for x in vertices if x not in (u,v))
                F[A][u,v,color(x,u,v),0]=1
        continue
    for v in vertices:
        for (x,u,c,s),count in F[A^(1<<v)].items():
            d=color(x,u,v)
            t=s+(c!=d)
            if t<=1:
                key=(u,v,d,t)
                F[A][key]=F[A].get(key,0)+count
hist={s:sum(count for (u,v,c,t),count in F[-1].items() if t==s)
      for s in (0,1)}
assert hist=={0:0,1:770}
~~~

Uniform positivity of Z remains open. The counting identity, centerwise affinity, and gradient recurrence provide tools for analyzing a hypothetical zero and carrying out reproducible adversarial search.
