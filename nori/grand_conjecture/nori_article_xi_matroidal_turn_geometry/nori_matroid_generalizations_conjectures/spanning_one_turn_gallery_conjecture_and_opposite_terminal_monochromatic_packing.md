# Spanning one-turn gallery conjecture and opposite-terminal monochromatic packing

# Spanning one-turn galleries and opposite-terminal monochromatic packing

## 1. The strengthened target replaces the square-root resource bound

For a reversal-odd ordinary boundary 3-tournament, a vertex-simple tight path is an injective ordering \(v=(v_1,\ldots,v_n)\) of all original vertices with ordered triple-color word
\[
b(v_1,v_2,v_3),\ b(v_2,v_3,v_4),\ldots,\ b(v_{n-2},v_{n-1},v_n).
\]
Its **internal turn count** is
\[
s_b(v)=\sum_{i=1}^{n-3}[b(v_i,v_{i+1},v_{i+2})\ne b(v_{i+1},v_{i+2},v_{i+3})].
\tag{1}
\]

**Conjecture 1 (spanning one-turn boundary-tournament conjecture).** Every ordinary reversal-odd boundary 3-tournament on \(n\ge3\) vertices admits an injective ordering of all its vertices with
\[
\boxed{s_b(v)\le1.}
\tag{2}
\]
This is an open assertion, rather than a consequence of the earlier square-root resource-gallery conjecture. The latter would recover only a classical-scale \(\Omega(\sqrt n)\) monochromatic path, obtainable through elementary longest-path endpoint counting; thus it should not be the principal unification target.

For the cube, the corresponding spanning-gallery assertion is the existence of a complete antipodal geodesic whose edge colors change at most once. The antipodally odd cyclic closing seam turns this into the monochromatic NORI1 target. The two resulting quantitative targets are therefore both **spanning, at most one internal turn** (and in the cube equivalently zero internal turns).

## 2. Marked full-resource port intersection

Let \(D\) be the pointed binary matroid obtained from the connected reversal-overlap state cover, and \(X_b=\operatorname{supp}(d_b)\cup\{p\}\) its port cycle. The three-turn closing theorem for each injective full word \(v\), \(n\ge6\), yields a simple monodromy-one cycle \(C_v\) and cocircuit \(Y_v=C_v\cup\{p\}\). The **marking** is the ordered cyclic decomposition
\[
C_v=I_v\sqcup S_v
\]
into the \(n-3\) original internal turn edges \(I_v\) and the three ordered closing-seam edges \(S_v\). The unmarked cocircuit \(Y_v\) alone does not record which edges are internal.

**Proposition 2 (equivalent full-resource port criterion).** For \(n\ge6\), Conjecture 1 is equivalent, in the canonical boundary matroid, to the following statement:
\[
\boxed{
\forall X\in Z(D),\ p\in X,\quad
\exists\text{ a marked full-resource cocircuit }(Y_v,S_v):
\quad |X\cap(Y_v\setminus(\{p\}\cup S_v))|\le1.
}
\tag{3}
\]
If \(h_v=|X\cap S_v|\in\{0,1,2,3\}\), (3) is also equivalent to
\[
\boxed{|X\cap Y_v|\le h_v+2.}
\tag{4}
\]
For every marked full-resource cocircuit,
\[
|X\cap Y_v|=1+s_b(v)+h_v,\qquad
s_b(v)+h_v\equiv1\pmod2.
\tag{5}
\]
In particular, a witness to (3) automatically has \(|X\cap Y_v|\in\{2,4\}\). The four permitted pairs \((s_b(v),h_v)\) at most one internal turn are
\[
(0,1),\quad (0,3),\quad (1,0),\quad (1,2).
\tag{6}
\]
Conversely, mere unmarked intersection at most four is insufficient, since at intersection four it also permits \((s,h)=(2,1)\) or \((3,0)\).

*Proof.* The cochain \(d_b\) marks an internal turn precisely when two successive triple colors differ. Hence its support on \(I_v\) counts \(s_b(v)\). On the closing seam it counts \(h_v\). Adding the shared port yields (5), and monodromy-one parity makes the nonport weight odd. Equations (3), (4) and (6) follow by inspection. Every port-containing cycle corresponds to a reversal-odd coloring, up to global color complementation, by the covering reconstruction theorem. \(\square\)

**Proposition 3 (cube one-turn equals zero-turn).** In the canonical cube-edge representation, a complete antipodal geodesic with at most one internal change can be cyclically re-rooted to have zero internal changes.

*Proof.* Its cyclic turn word has the \(n-1\) internal transitions plus the unique closing turn, and its parity is odd by antipodal reversal. If at most one internal turn changes, at most two cyclic turns change; oddness forces one. Rotating the cyclic direction order and adjusting the root makes that unique changed turn the closing seam. The remaining complete geodesic is monochromatic. \(\square\)

This identifies one common *marked* invariant: full independent resource rank and at most one internal disagreement. The cube is the width-one, movable-seam case; boundary tournaments have a width-three fixed seam and need an additional endpoint compatibility mechanism.

## 3. An equivalent two-arm monochromatic packing theorem

For a color \(\varepsilon\in\{0,1\}\) and an ordered pair \(u\ne v\), let \(\mathcal P^\varepsilon_{uv}\) denote the family of vertex-simple \(\varepsilon\)-monochromatic tight paths whose last two vertices are \((u,v)\). We permit the two-vertex path \((u,v)\), on which the triple-color condition is vacuous.

**Theorem 4 (opposite-terminal packing equivalence).** A boundary 3-tournament on \(V\) admits a vertex-simple *spanning tight path with at most one color change* if and only if there exist distinct \(u,v\in V\), a color \(\varepsilon\), and paths
\[
P\in\mathcal P^\varepsilon_{uv},\qquad Q\in\mathcal P^\varepsilon_{vu}
\]
such that
\[
\boxed{V(P)\cap V(Q)=\{u,v\},\qquad V(P)\cup V(Q)=V.}
\tag{7}
\]
In the presence of a nondegenerate change, neither arm need be vacuous. If the spanning path is monochromatic, one may take one arm to be a two-vertex path. Thus the spanning one-turn conjecture is equivalent to a **spanning opposite-terminal monochromatic two-arm packing conjecture**.

*Proof.* Suppose \(W=(w_1,\ldots,w_n)\) is a one-turn spanning path, and its triple colors change between the windows beginning at positions \(i\) and \(i+1\). Put \(u=w_{i+1},v=w_{i+2}\), take \(P=(w_1,\ldots,w_{i+2})\), and let \(Q=(w_n,\ldots,w_{i+1})\), the reversal of the suffix starting at \(u\). If the original first color is \(\varepsilon\), the original suffix is monochromatic \(1-\varepsilon\), so reversal oddness makes \(Q\) monochromatic \(\varepsilon\). Their ends are \((u,v)\) and \((v,u)\), respectively, and injectivity gives (7).

If \(W\) is monochromatic of color \(\eta\), let \(Q\) be its full reversal (color \(1-\eta\)) and \(P=(w_1,w_2)\), a vacuous path declared to have color \(1-\eta\). Their terminal pairs are opposite, their vertex intersection is \(\{w_1,w_2\}\), and they cover \(V\).

Conversely, let \(P=(p_1,\ldots,p_r,u,v)\), \(Q=(q_1,\ldots,q_s,v,u)\) be as in (7), with possible empty prefixes. Reverse \(Q\), and concatenate with \(P\) along their common ordered pair \((u,v)\) to form
\[
W=(p_1,\ldots,p_r,u,v,q_s,\ldots,q_1).
\]
The vertex sets condition makes \(W\) a permutation of \(V\). All triples lying completely in its left portion have color \(\varepsilon\), while those in its right portion are reversals of the triples of \(Q\) and have color \(1-\varepsilon\). There is no additional triple outside these two windows, because the two portions share the full ordered pair. Thus \(W\) has at most one color change. \(\square\)

**Corollary 5 (graphic-matroid interpretation).** Under (7), the union of the underlying \(K_n\)-edges of the two arms, with the common edge \(\{u,v\}\) counted once, forms a Hamiltonian graph path. It is an independent set of rank \(n-1\), hence a *basis* of the graphic matroid \(M(K_n)\), and its graph degree is at most two. Conversely, a same-color opposite-terminal pair of tight paths whose underlying edges form a Hamiltonian path and satisfy (7) decodes to a spanning at-most-one-turn tight path.

The basis condition alone is not sufficient without the oriented terminal compatibility and path-language requirements. Those are precisely the extra decorations absent from an undecorated binary cycle–cocircuit intersection conjecture.

## 4. An explicit obstruction to nearly monochromatic cyclic Hamiltonian words

We exhibit an ordinary reversal-odd boundary tournament with a spanning one-turn word but no cyclic Hamiltonian word with at most two changes. This rules out the stronger approach of first finding a nearly monochromatic cyclic ordering and cutting it.

Let \(V=\{0,1,2,3,4,5\}\). Index the 60 representatives of reversal classes of ordered triples by increasing middle vertex, followed by lexicographically increasing unordered outer pair \(a<c\) disjoint from the middle vertex. Define the representative color by its indexed bit of
\[
\boxed{M=\mathrm{0x1418d63f482ff8d},}
\tag{8}
\]
and give the reverse triple the complementary color.

**Proposition 6 (cyclic Hamiltonian obstruction).** Among all \(6!=720\) spanning linear words \(v\), the histogram of internal color-change counts is
\[
\boxed{\#(0)=0,\quad \#(1)=108,\quad\#(2)=360,\quad\#(3)=252.}
\tag{9}
\]
For cyclic triple words \(\bigl(b(v_i,v_{i+1},v_{i+2})\bigr)_{i\in\mathbb Z/6\mathbb Z}\), the cyclic change-count histogram is
\[
\boxed{\#(0)=0,\quad\#(2)=0,\quad\#(4)=576,\quad\#(6)=144.}
\tag{10}
\]
In particular, a spanning one-turn path exists, but no cyclic Hamiltonian triple word has at most two changes.

*Proof (finite certificate).* The following Python 3 code visits every permutation and computes both histograms using the 60-bit indexing:
\`\`\`python
from collections import Counter
from itertools import permutations, combinations

V=range(6)
reps=[(a,b,c) for b in V for a,c in
      combinations([x for x in V if x!=b],2)]
assert len(reps)==60
idx={t:i for i,t in enumerate(reps)}
M=0x1418d63f482ff8d
def col(a,b,c):
    rep=(a,b,c) if a<c else (c,b,a)
    return ((M>>idx[rep])&1)^int(a>c)
linear=Counter()
cyclic=Counter()
for v in permutations(V):
    w=[col(*v[i:i+3]) for i in range(4)]
    linear[sum(w[i]!=w[i+1] for i in range(3))]+=1
    z=[col(v[i],v[(i+1)%6],v[(i+2)%6]) for i in range(6)]
    cyclic[sum(z[i]!=z[(i+1)%6] for i in range(6))]+=1
assert linear==Counter({1:108,2:360,3:252})
assert cyclic==Counter({4:576,6:144})
\`\`\`
The enumeration covers all ordered spanning paths and all cyclic orders (with multiplicity six). Reversal oddness is enforced by the color definition, and the assertions reproduce (9)–(10). \(\square\)

## 5. Revised research program

The principal **proposed unification** should now be the spanning one-internal-turn assertion (3), equivalently the boundary opposite-terminal packing (7) coupled with cube root rotation. The earlier \(m\ge\sqrt n\), \(|X\cap Y|\le4\) marked-gallery conjecture is a strictly weaker auxiliary statement, since its boundary consequences only recover the classical \(\Omega(\sqrt n)\) monochromatic scale. A stronger bare cyclic Hamiltonian assertion is refuted by Proposition 6.

The key missing step is not controlling total cyclic switch weight but aligning two long same-colored *oppositely oriented* terminal arms without repeated original vertices. Any matroidal route must preserve both graphic independence and ordered-pair compatibility; replacing them by cographic port parity or unmarked cocircuit intersection forfeits the spanning problem. The proof objective is an independence-preserving terminal-pair splice that grows the two disjoint arms to total resource rank \(n-1\).
