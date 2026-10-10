# Exterior face charts and Fourier transport

# Exterior-face charts: exact root repair and its limits

In a legal physical ordered-three-face coloring, fixed exterior coordinates cannot be suppressed without proof. This subsection combines a general Boolean root-interpolation lemma, a seam triangularization mechanism, and a deliberately restricted computer-assisted higher-dimensional test. The restricted theorem is not claimed for arbitrary exterior dependence.

## Acyclic pivotal matching and root interpolation

Theorem (acyclic Boolean pivot matching). Fix any dimension n>=4, order p, rooted window colors w_i(x), and seam bits d_i=w_i+w_(i+1), i in [m], m=n-3. For a Boolean function f write Delta_j f(x)=f(x)+f(x+e_j). Select a set I of seam indices and injectively assign distinct root coordinates rho(i) to i in I. Assume Delta_(rho(i)) d_i = 1 at every root. Form a directed graph on I with arc j to i (j!=i) whenever d_i depends on x_(rho(j)); equivalently Delta_(rho(j))d_i is not identically zero. If this graph is acyclic, then for ANY target seam values t_i at i in I, exactly 2^(n-|I|) roots realize d_i=t_i simultaneously. In particular, min_root switches <= m-|I|. If |I|>=m-1, a full one-switch antipodal geodesic exists.

Proof. Choose the n-|I| unused root bits arbitrarily. Process seam indices in topological order of the directed graph. On processing i, every other pivotal coordinate influencing d_i has already been assigned, because a missing arc means the corresponding Boolean derivative vanishes identically. The pivotal coordinate rho(i) toggles d_i for every choice of other bits, hence there is exactly one value making d_i=t_i. Later choices preserve previous equations. Counting the free root bits gives 2^(n-|I|) roots.

Feedback-set corollary. If removing B from the pivotal dependency graph makes it acyclic, the same reasoning on I\B gives exactly 2^(n-|I|+|B|) roots satisfying all retained seam equations and at most m-|I|+|B| changes. Define alpha(p) as the maximum number of seams admitting an acyclic pivotal matching. Any putative NORI counterexample must obey alpha(p)<=n-5 for every full direction order p. The physical-face condition guarantees w_i are true faces; the proof needs no oddness assumption.

Extension: right-triangular seam interpolation (Item nori_order_local_boolean_seam_triangularization_dimension_independent_20261009) is the case rho(i)=p_(i+3), whose dependency arcs point forward. This result allows arbitrary pivotal coordinates and arbitrary nonlinear lower-order dependencies.

Abstract sharpness example: d_1=u+v and d_2=1+u+v have global unit derivatives in each variable. Assigning distinct pivots yields a directed two-cycle, and the equations d_1=d_2=0 are inconsistent; exactly one of them can vanish. This example is a statement about arbitrary Boolean seam systems and makes no claim of NORI realizability.

Open obligation: Find an all-but-one acyclic pivotal matching (or a fiberwise nonlinear substitute) in at least one genuine full direction order of each legal coloring.

## Local seam triangularization

# Dimension-independent nonlinear seam triangularization and exact root multiplicity

Let n>=4 and c be ANY binary coloring of physical ordered three-faces of Q_n (the NORI antipodal law may additionally hold). Fix a full direction order p=(p_1,...,p_n). Let w_i(x) denote its actual physical ordered-three-face color at starting cube root x, for 1<=i<=n-2. Put d_i(x)=w_i(x)+w_(i+1)(x) over F_2 for 1<=i<=m=n-3. For any Boolean function f of cube-root bits, define its Boolean difference Δ_j f(x)=f(x)+f(x+e_j).

Call seam i RIGHT-TRIANGULAR when BOTH identities hold at every cube root:
(1) Δ_(p_(i+3)) d_i ≡ 1;
(2) Δ_(p_j) d_i ≡ 0 for all j>i+3.
These hypotheses are physical-face local: (1) is exactly Δ_(p_(i+3)) w_i≡1, since p_(i+3) belongs to the second free triple; (2) says that the two adjacent actual faces have identical exterior-bit derivatives in every still-future direction p_j, j>i+3. Those common derivatives may be arbitrary nonlinear functions of other root coordinates.

THEOREM (nonlinear seam-defect bound and exact multiplicity). Let B be ANY set of seam indices containing every seam that is not right-triangular. For every assignment of the first three root bits and every requested t_i∈F_2 for i∉B, there are EXACTLY 2^|B| completions of the remaining root bits satisfying d_i(x)=t_i at every i∉B. Consequently an actual antipodal full geodesic of direction order p exists with at most |B| changes. More precisely, among the 2^n possible initial roots, exactly 2^(3+|B|) satisfy d_i=0 for all i∉B. If B=∅, every seam word in F_2^(n-3) occurs at exactly eight roots and there are eight monochromatic full geodesics of this fixed direction order. If |B|=1, at least sixteen starting roots yield a full one-change geodesic.

PROOF. Choose x_(p_1),x_(p_2),x_(p_3) arbitrarily, and process i=1,...,m. If i∈B, choose x_(p_(i+3)) freely. If i∉B, condition (2) says d_i is independent of every as-yet-unassigned bit x_(p_j), j>i+3. Condition (1) says toggling the current bit x_(p_(i+3)) toggles d_i, for every setting of already fixed bits. Exactly one choice attains d_i=t_i. Subsequent choices cannot modify a previously solved nonexceptional seam by (2). Conversely each permissible assignment must choose these same forced pivot bits. Hence there are precisely 2^|B| completions per initial triple and 2^(3+|B|) total. Setting all prescribed t_i=0 leaves changes only at seams in B. QED.

COROLLARY (counterexample obstruction). Any counterexample to full NORI must have at least TWO non-right-triangular seams for EVERY full direction order p. Thus every order must encounter at least two failures of pointwise entering-direction flip or two-face future-derivative agreement, counted jointly.

NONLINEAR, NO-GLOBAL-FLIPPER EXAMPLES. For an arbitrary order p and arbitrary Boolean maps G_i on i-1 variables, prescribe on ordered triple (p_i,p_(i+1),p_(i+2)) the face color c_i(z)=Σ_(j=i+3)^n z_(p_j)+G_i(z_(p_1),...,z_(p_(i-1))), with z denoting its fixed exterior coordinates. Prescribe reversed triples by the antipodal-reversal-odd law, and all other ordered triple types arbitrarily subject to that law. Along the genuine rooted full path of order p, the prefix exterior coordinates have been toggled and the suffix exterior coordinates have not; therefore w_i(x)=Σ_(j=i+3)^n x_(p_j)+G_i(1+x_(p_1),...,1+x_(p_(i-1))). It follows that d_i(x)=x_(p_(i+3))+G_i(prefix_(i-1))+G_(i+1)(prefix_i). Every seam is right-triangular regardless of the Boolean degrees of G_i. For n>=7, the unused triple types can be colored independently of a selected exterior coordinate for each direction, so this family can be chosen with NO universal exterior flipper. The result therefore supplies an all-dimensional, genuinely nonlinear, order-local root-control criterion strictly broader than relying on globally uniform exterior flippers.

LIMIT. The right-triangular hypotheses are sufficient local certificates, not consequences of antipodal oddness. The unrestricted grand conjecture remains open. The new closure target is to force an order with at most one defective seam, or find a weaker global replacement for the pointwise future-derivative agreement.

## Exact Q8 one-sentinel physical-face theorem (computer-assisted)

THEOREM (complete Q8 closure with one genuine exterior coordinate; computer-assisted). Let c color the PHYSICAL ORDERED three-faces of Q8, obeying c(bar F,reverse pi)=1-c(F,pi). Fix one distinguished direction t. Assume that for each ordered free triple pi the face color depends on its exterior fixed bits only through the bit x_t when t is NOT in pi; when t is free, its color depends on no exterior bit. Then some full antipodal eight-geodesic has a window-color word with at most one change. The assumption allows genuine face-position dependence, so this strictly extends coordinate-only Q8 closure.

MATHEMATICAL REDUCTION. Relabel t=7 and V={0,...,6}. For all ordered triples pi on V let H(pi)=c(F,pi) at t-exterior bit 0 (the other exterior bits are immaterial). The antipodal-reversal law forces color at t-bit 1 to equal 1-H(reverse pi). H is an ARBITRARY 210-bit ordered-triple coloring; NO reversal-oddness of H is assumed. For ordered triples pi containing 7, denote their position-independent labels by G(pi); then G(reverse pi)=1-G(pi), contributing exactly 63 Boolean variables. There are 210+63=273 independent Boolean variables.

For a full eight-direction order p and a starting sentinel bit b, let j=position of 7 in p. For window index i with ordered triple pi=p[i:i+3]: if 7 lies inside pi its color is G(pi); otherwise its color is H(pi) for b XOR [j<i]=0, and 1-H(reverse pi) for b XOR [j<i]=1. Every other starting-root bit is immaterial. The full window word has six bits. Forbid each of the twelve binary words with zero or one color change by one six-literal clause OR_i(window_i != target_i). Reversing p at the SAME root sends its word to the complement of the reversed word by the physical NORI law; hence it suffices to inspect half of all 8-permutations, for both sentinel-root bits, giving (8!/2)*2*12=483840 clauses.

A DICHOTOMY ON THE CHART H is exhaustive.
Case I. H has a monochromatic tight directed five-path on five distinct vertices of V. By relabeling V and globally flipping all colors, normalize H(012)=H(123)=H(234)=0. Add these three unit clauses. The full 273-variable CNF with the 483840 badness clauses is UNSAT (libz3.so.4).
Case II. H has NO monochromatic tight directed five-path. For each ordered five-tuple q in V, forbid both H(q0q1q2)=H(q1q2q3)=H(q2q3q4)=0 and the analogous all-1 assignment. These are 2*7P5=5040 three-literal clauses. With the same full 483840 badness clauses the 273-variable CNF is UNSAT (libz3.so.4).
Thus a hypothetical coloring with no good full Q8 geodesic lies in neither exhaustive case; contradiction.

REPRODUCIBLE REFERENCE CHECKER (Python 3 with z3-solver):
from itertools import permutations
from z3 import Bool,Not,Or,Solver,unsat
V=range(8); t=7; W=list(permutations(V,3))
H={q:Bool('H'+''.join(map(str,q))) for q in W if t not in q}
G={}
for q in W:
    if t in q and q not in G:
        a=Bool('G'+''.join(map(str,q)))
        G[q]=a; G[q[::-1]]=Not(a)
assert len(H)==210 and len(G)==126
def h(q,b):
    if t in q:return G[q]
    return H[q] if b==0 else Not(H[q[::-1]])
good={tuple([a]*j+[1-a]*(6-j)) for a in (0,1) for j in range(7)}
assert len(good)==12
for case in (0,1):
    S=Solver()
    if case==0:
        for i in range(3):S.add(Not(H[tuple(range(i,i+3))]))
    else:
        for q in permutations(range(7),5):
            w=[H[q[i:i+3]] for i in range(3)]
            S.add(Or(*w));S.add(Or(*(Not(a) for a in w)))
    for p in permutations(V):
        if p>p[::-1]:continue
        loc=p.index(t)
        for b in (0,1):
            w=[h(p[i:i+3],b^(loc<i)) for i in range(6)]
            for g in good:
                S.add(Or(*(w[i] if g[i]==0 else Not(w[i]) for i in range(6))))
    assert S.check()==unsat
Executed with direct ctypes calls to the system Z3 C library on 2026-10-09: Case I UNSAT in 9.84 s; Case II UNSAT in 7.87 s, each with 273 variables and 483840 six-literal no-good clauses. A separate SAT tactic independently rechecked Case I UNSAT (~10.35 s).

IMPORTANT SCOPE. The theorem is a special FACE-DEPENDENT rank-eight case and therefore a strictly stronger bridge than coordinate-only Q8. It does not establish full physical Q8 or all-dimensional NORI, because a generic ordered-face color can depend on five independent exterior bits. Any all-dimension upgrade must control multiple exterior coordinates simultaneously. A two-sentinel extension was formulated with 438 variables and 967680 no-good clauses; initial SAT solving did not finish. This identifies a natural next bridge between coordinate-only combinatorics and the full physical geometry. Request independent certificate audit before elevating to a publication composition.

## Interpretation and remaining obligation

The Boolean matching and seam arguments permit local control where their exact pivot and support hypotheses hold. The Q8 SAT statement assumes a single globally distinguished exterior coordinate; it is **not** unrestricted dimension-eight closure and supplies no induction by itself. Extending these constructions would require a dimension-uniform choice of compatible physical roots and seam windows despite general nonlinear dependence on all exterior coordinates.
