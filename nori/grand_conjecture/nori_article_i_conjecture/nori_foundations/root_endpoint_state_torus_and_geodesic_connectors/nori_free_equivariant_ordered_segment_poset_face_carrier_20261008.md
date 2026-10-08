# Full NORI free antipodal ordered-segment poset with an exact barycentric face-carrier map

# Exact equivariant lift of the cubical face-label carrier by ordered geodesic segments

Let n>=5. Let c assign binary colors to ordered 3-faces (F,pi) of Q_n with c(bar F,rev pi)=1-c(F,pi). Define the finite poset P_n whose elements are all DIRECTED geodesic segments
P=(v_0,v_1,...,v_k), 0<=k<=n,
using k distinct directions. Order by CONTIGUOUS subsegment inclusion: P'<=P iff P'=(v_i,...,v_j) for some 0<=i<=j<=k, with the inherited orientation.

Let d_c(P) be the number of changes in its (k-2) consecutive ordered-three-face window colors, with d_c(P)=0 for k<=3. Let G_n(c) be the downward closed subposet consisting of all P with d_c(P)<=1, and let |G_n| be its order complex.

**Theorem 1 (free exact NORI involution).** Define
Theta(P)=(bar v_k,bar v_(k-1),...,bar v_0).
This is a poset involution, preserves G_n, and acts FREELY on |G_n| for n>=2.

Proof. Complemented reversal takes contiguous subsegments to contiguous subsegments and preserves rank k. The window color word of Theta(P) is the reversed complement of the word of P by the ordered-face axiom, so its change count is unchanged. If k<n, P=Theta(P) implies v_0=bar v_k and hence distance(v0,vk)=n, contradicting k<n. If k=n, the direction word would need equal its reversal, impossible because all n directions are distinct and n>=2. Thus no element is fixed. An invariant simplex in the order complex is a strictly ranked chain, so its vertices must all be individually fixed by any rank-preserving simplicial involution; none exists. QED.

**Theorem 2 (equivariant barycentric face-carrier map).** Define H(P) to be the UNIQUE smallest physical cube face containing every vertex of P: its free coordinate set is precisely the k used directions and its exterior bits equal those of v0. If P'<=P, then H(P') subseteq H(P). Therefore
Phi: |G_n| -> sd(Q_n),
mapping the vertex P to the barycenter b_(H(P)), is a simplicial map. Moreover H(Theta(P))=bar H(P), so
Phi(Theta u)=bar(Phi(u)).
In particular it is genuinely equivariant for the *correct* ordered-three-face involution, unlike the naive physical antipodal action on the unlifted one-switch rooted-flag subcomplex.

**Theorem 3 (exact central extraction and automatic low-rank surjectivity).** The following are equivalent:
(a) Some ordered-three-face antipodal geodesic has <=1 color change (the NORI grand conclusion);
(b) G_n contains a rank-n element;
(c) |G_n| has an n-dimensional simplex;
(d) the physical cube center b_(Q_n) lies in Phi(|G_n|).
Indeed H(P)=Q_n iff P uses all n directions; every such segment is a full antipodal geodesic, and a rank-n element admits a chain of prefixes P0<...<Pn. If every segment has rank<=n-1, every image face H(P) is proper and Phi(|G_n|) lies entirely in boundary Q_n, so center is excluded.

For all k<=4, EVERY rank-k directed segment is in G_n, independently of the coloring, because there are at most max(k-3,0)<=1 window transitions. Consequently Phi maps the rank<=4 subcomplex SURJECTIVELY onto the geometric cubical 4-skeleton of Q_n: each barycentric flag inside a physical face of dimension <=4 has a contiguous-prefix lift along a directed monotone geodesic in that face. Surjectivity by itself supplies no equivariant section and does not establish index four.

**Precise topological frontier.** Under a hypothetical counterexample, |G_n| is a free Z2 simplicial complex of dimension <=n-1, mapped equivariantly into boundary Q_n by Phi, with complete rank<=4 segment incidence. An equivariant-index lower bound >=n, or an equivariant extension of an antipodal S^n into |G_n|, would contradict that dimension. More concretely, seek a color-sensitive equivariant carrier section or multisection over a sufficiently high-index source whose simplices consist of ACTUAL mutually nested geodesic segments. The rank<=4 lifts fix the local face-incidence and involution obstacles, but an index/extension theorem is still open. This is a genuine full-NORI path-memory realization of the user's original reachable-face labeling program, not a proof of grand closure.
