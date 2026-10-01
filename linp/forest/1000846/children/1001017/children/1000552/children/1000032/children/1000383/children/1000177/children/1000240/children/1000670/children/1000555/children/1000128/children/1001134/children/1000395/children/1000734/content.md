# Retaining double contacts forces near-complete source-rail coverage and sixteen-elevenths overlap

## Statement

Let e_1,...,e_k be distinct ascending nonspecial edges terminal at the same vertex v in a finite linear 3-graph, ordered by ranks r_1<=...<=r_k=q, q>=4. Write e_i={v,x_i,u_i}, where x_i is the unique entrance. For each j choose any canonical source rail R_j of length r_j-1, so R_j,e_j is a longest path ending in e_j. Set alpha=ceil((3q-8)/4).

Fix h,m with h+m<=k, m>=2, and h>=alpha. Choose any m rails whose indices exceed h. Put U=union_{i<=h}{x_i,u_i}, L=2h-alpha and D=h-alpha. Then every chosen rail R satisfies
|V(R) intersect U|>=L,
|V(R) minus U|<=2q-1-L,
and its rank satisfies r(R)>=(L+1)/2.
Every pair of chosen rails shares at least 2h-2alpha vertices of U.
Some pair shares at least L(mL-2h)/(2h(m-1)) vertices of U.
Some (possibly different) pair contains both vertices of at least D(mD-h)/(h(m-1)) of the distinguished pairs {x_i,u_i} (a negative lower bound is vacuous).

In particular, if k=gamma(q)-o(q), where gamma(q)=floor((11q-5)/8), take m->infinity with m=o(q) and h=k-m. All final m rails have rank q-o(q) and all but o(q) of their vertices in U. Every pair shares at least (5/4-o(1))q distinguished vertices; some pair shares at least (16/11-o(1))q, and consequently contains at least (7/88-o(1))q entire distinguished pairs. Another pair contains at least (25/88-o(1))q entire distinguished pairs. These conclusions require no assumption phi(v)=q+1.

## Body

1. Retain both contacts. Fix a chosen rail R_j, j>h. Its anchor edge has rank r_j. Every earlier edge e_i, i<=h, meets R_j by downward-completeness. For completeness: if e_i avoided R_j, the path R_j,e_j,e_i would have length r_j+1>r_i, impossible. The rail avoids v and u_j and ends at x_j. Since different e_i through v have disjoint non-v pairs, none of the earlier pairs contains x_j. Thus its contacts with R_j are exactly its contacts with W_j=V(R_j) minus {x_j}, the precursor set of the r_j-edge anchor path R_j,e_j.

These h disjoint nonempty contact sets have size one or two. The exact singleton-conflict theorem bounds the number s_j of their singletons by ceil((3r_j-8)/4)<=alpha when r_j>=4. For r_j=2 there are no earlier contacts, since J_2 has size at most one; for r_j=3 there is at most one earlier edge, so s_j<=1<=alpha. Hence uniformly
s_j<=alpha,
d_j=h-s_j>=h-alpha=D,
|V(R_j) intersect U|=s_j+2d_j=2h-s_j>=L.
A rail of length r_j-1 has exactly 2r_j-1 vertices. This gives both the outside-U bound and r_j>=(L+1)/2.

2. Deterministic overlap. The universe U has exactly 2h vertices. Any two chosen rails contain at least L of them, so their intersection in U has size at least 2L-2h=2h-2alpha.

3. Averaged vertex overlap. For z in U let a_z be the number of chosen rails containing z, and let T=sum_z a_z. Then T>=mL and
sum_{rail pairs R,R'} |V(R) intersect V(R') intersect U|
=sum_z binom(a_z,2)
>= (T^2/(2h)-T)/2.
Here Cauchy-Schwarz gives the last inequality. Since h>=alpha, L>=h and m>=2; hence mL>=2h. The expression T^2/(2h)-T is increasing for T>=mL, so the sum is at least ((mL)^2/(2h)-mL)/2. Divide by binom(m,2) to obtain L(mL-2h)/(2h(m-1)).

4. Common double contacts. For each i<=h let b_i count the chosen rails containing both x_i and u_i. Each rail contains at least D whole pairs, so sum_i b_i>=mD. If mD>=h/2, the same Cauchy-Schwarz argument over h coordinates gives the asserted bound D(mD-h)/(h(m-1)). If mD<h/2 the displayed bound is nonpositive and is automatically true. (The intermediate case h/2<=mD<h also yields a nonpositive bound.) Thus no positivity assumption on D is needed beyond D>=0.

5. Near equality. Write k=gamma(q)-epsilon with epsilon=o(q), and choose m tending to infinity with m=o(q). Then
h=(11/8)q-o(q), alpha=(3/4)q+O(1),
L=2q-o(q), D=(5/8)q-o(q).
The first part immediately forces r_j=q-o(q) for EVERY final chosen rail and |V(R_j) minus U|=o(q). No separate rank-cutoff argument is needed. The deterministic overlap is (5/4-o(1))q. The average vertex overlap is
L^2/(2h)-o(q)=(16/11-o(1))q.
For the same pair, if B distinguished pairs have both vertices common, its common-vertex count is at most h+B. Hence B>=(16/11-11/8-o(1))q=(7/88-o(1))q.
The double-contact averaging bound tends to
D^2/h=(25/88-o(1))q.

Scope: this strengthens 58659c428983's (11/16-o(1))q overlap to (16/11-o(1))q by retaining contact multiplicity instead of choosing a single binary label per edge. It also replaces pair existence by a (5/4-o(1))q guarantee for EVERY pair of the final m rails, proves that those rails are almost contained in the same distinguished-vertex universe, and removes the gap-one hypothesis. It is a structural strengthening, not yet an unconditional improvement of the 43/48 global coefficient. The two averaged guarantees may be attained by different pairs. No simultaneous-switching or lens-cleanliness assumption is used.