# Run counting replaces the contact transfer and extends the coefficient improvement to every uniformity

## Statement

For each integer r>=3, put c_r=1-(2r-1)/(8r(r-1)) and d_r=(4r^2-10r+1)/(4r(r-1)). Every finite linear r-graph with m edges, n_+ nonisolated vertices, and S=sum_v phi(v) satisfies m<=c_r S-d_r n_+. Hence ex_L(n,P_ell^(r)) <= [c_r(ell-1)-d_r]n for ell>=2. The underlying local bound is |J_q(v)|<=(6r-7)q/8+(7-2r)/4 at a terminal of an ascending rank-q edge. An elementary run decomposition proves singleton density (2r-3)/4 and replaces the four-state transfer. Leading coefficients for r=3,4,5 are 43/48,89/96,151/160.

## Body

For an r-uniform linear hypergraph, define phi(e), phi(v), and terminal incidences as in linear_paths.tex. Every edge has at least r-1 terminal vertices. It is special if all r are terminal; otherwise all longest paths ending in it have a unique entrance x. Call it ascending when phi(x)=phi(e)-1. Let r>=3.

RUN COUNTING LEMMA.
Suppose each of N ordered columns has r-2 private positions and one joint position. A selected position represents a singleton contact. Let A_i indicate that column i is nonempty. Assume that A_i=1 forbids the joint position of column i+1 and all private positions of column i+2. Then the number of selected positions is at most
 lambda(N+2), where lambda=(2r-3)/4.

Proof. Prepend two empty columns. There cannot be three consecutive nonempty columns: the first would forbid the private positions of the third, and the second would forbid its joint. Partition the columns into blocks consisting of an occupied run and all the empty columns immediately preceding it; trailing empties may be discarded. An occupied run has length one or two. If the preceding gap has length one, the previous occupied column forbids all private positions in the first column of the run. The four bounds are:
 run length 1, gap length 1: weight <=1, block length 2;
 run length 1, gap length >=2: weight <=r-1, block length >=3;
 run length 2, gap length 1: weight <=r-1, block length 3;
 run length 2, gap length >=2: weight <=2r-3, block length >=4.
In the two-column runs the joint of the second column is forbidden by the first. Since r>=3,
 1/2 <= lambda and (r-1)/3 <= lambda,
and (2r-3)/4=lambda. Each block has weight at most lambda times its length. Their total length is at most N+2, proving the claim.

FIXED-ENTRANCE CAPACITY.
Fix an ascending edge h of rank q and a terminal v at h. Define
 J_q(v)={f containing v: phi(f)<=q}.
Then
 |J_q(v)| <= alpha q+beta,
 alpha=(6r-7)/8, beta=(7-2r)/4.
For q=2,3 the stronger bounds are 1 and r-1, respectively.

Proof. Choose a longest path P=(g_1,...,g_q), with last edge h and last vertex v. Its entrance x=g_{q-1} cap h has phi(x)=q-1. Let W=V(P) minus h; |W|=(r-1)(q-1). For f in J_q(v) minus {h}, the contact set C_f=(f minus {v}) cap W is nonempty, or appending f to P contradicts phi(f)<=q. All C_f are pairwise disjoint.

For q=2, a second edge f through v would give a longest path (f,h) entering h through v, impossible. For q=3, C_f cannot lie entirely in g_1: linearity would make it a singleton and (g_1,f,h) would be a longest h-path with wrong entrance v. Thus all other f have distinct contacts in W minus g_1, a set of r-2 vertices. This gives |J_3(v)|<=r-1. Both bounds imply alpha q+beta.

Assume q>=4. Put z_i=g_i cap g_{i+1}; for 2<=i<=q-1 put B_i=g_i minus {z_{i-1},z_i}, of size r-2. Every vertex of g_1 minus {z_1} is forbidden as a singleton contact, since f,g_1,...,g_{q-1} would be a q-edge path ending at x. Every vertex of B_{q-2} union {z_{q-2}} is also forbidden as a singleton contact, since g_1,...,g_{q-2},f,h would be a longest h-path entering through v.

For 1<=i<=q-3, let the forward part of g_i be B_i union {z_i}, with g_1 itself used at i=1; let the backward part of g_{i+2} be B_{i+2} union {z_{i+1}}. A singleton contact c in the first part cannot coexist with a singleton contact d in the second part. Indeed, their edges f,k would give
 g_1,...,g_i,f,k,g_{i+2},...,g_{q-1}.
This has q edges and ends at x. The omitted g_{i+1} separates the retained prefix and suffix. Each of f,k has only its prescribed contact on W; they meet each other at v, which is absent from retained path edges. Neither contains another vertex of h, by linearity, so in particular neither contains x. The displayed sequence is therefore a linear path, contradicting phi(x)=q-1.

After removing the forbidden positions, group the internal positions into columns B_i union {z_i}, 2<=i<=q-3. There are N=q-4 columns. They obey the run counting lemma: a nonempty column i forbids z_{i+1} and every vertex of B_{i+2}. The remaining boundary positions are z_1 and B_{q-1}, at most r-1 vertices. Dropping their additional conflicts only enlarges the bound. Thus the number s of singleton contact sets satisfies
 s <= lambda(q-2)+(r-1) = lambda q+1/2.
This also holds when q=4 and there are no internal columns.

Every nonsingleton contact uses at least two W-vertices. Consequently
 |J_q(v)| <=1+s+(|W|-s)/2
           <=1+((r-1)(q-1)+lambda q+1/2)/2
           =alpha q+beta.

GLOBAL CONSEQUENCE.
Let n_+ count nonisolated vertices, S=sum_v phi(v), A count ascending edges, and m count all edges. If t(v)>0 counts ascending edges terminal at v, choose such an edge of maximum rank q. Every edge counted by t(v) belongs to J_q(v), and q<=phi(v). Hence
 t(v)<=alpha phi(v)+beta.
This also holds for t(v)=0, since alpha p+beta is increasing in p and its value at p=1 is (2r+7)/8>0. Each ascending edge has r-1 terminals, so
 (r-1)A <= alpha S+beta n_+.

For completeness, at a nonisolated vertex v of rank p, at most (r-1)(p-1)+1 incident edges have rank at most p: each except a possible last edge of a maximum v-path must have a distinct contact outside that last edge. Every edge contributes r such rank-admissible incidences except an ascending edge, which contributes r-1. Indeed a nonspecial rank-q edge has r-1 terminals, and deleting its last edge from a longest witness proves that its entrance has rank at least q-1; the entrance fails rank-admissibility exactly in the ascending case. Summation gives
 rm-A <=(r-1)S-(r-2)n_+.
Combining,
 m <= c_r S-d_r n_+,
 c_r=1-(2r-1)/(8r(r-1)),
 d_r=(4r^2-10r+1)/(4r(r-1)).

For a P_ell-free linear r-graph, ell>=2, S<=(ell-1)n_+, and therefore
 m <=[c_r(ell-1)-d_r]n.
The coefficient is positive for ell>=2: at ell=2 it equals (10r-1)/(8r(r-1)).
In particular the leading coefficients for r=3,4,5 are 43/48,89/96,151/160. For r=3 this gives m<=(43S-14n_+)/48; the already published exact endpoint transfer improves that additive term, but its leading coefficient now has an elementary four-case run proof.

This argument does not improve the 3-uniform leading coefficient below 43/48. It simplifies the proof of that coefficient and extends the mechanism to every uniformity r>=3. Double and larger contact sets are handled by their vertex cost, without assuming they are impossible.