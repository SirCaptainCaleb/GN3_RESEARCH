# D5 — Comparison-orientation development: edge-orderability, barriers, and local-to-global fences

Complete connected development of the comparison-orientation representation and its historical edge-order fences. It proves the line-graph acyclicity criterion, canonical noninsertion barriers, the five-vertex nonHamilton integrability theorem, the vertex-minimal holonomy obstruction family, the elementary/asymptotic increasing-path fences, and the explicit port-preservation regression, while keeping the integrable two-cover statement explicitly conjectural.

## Boundary tournaments as line-graph comparison orientations

Let H be a finite boundary tournament on V, using exact reversal antisymmetry R3. Define Gamma(H) on vertex set E(K_V). If e={u,v} and f={v,w} are distinct incident ordinary edges, orient e->f exactly when (u,v,w) is tight. The reversed turn (w,v,u) corresponds to f->e, so R3 makes this a well-defined orientation of every edge of L(K_V).

For a vertex-simple sequence P=(v_0,...,v_k), put e_i={v_{i-1},v_i}. Then

    e_i -> e_{i+1} iff (v_{i-1},v_i,v_{i+1}) is tight.

Thus P is a tight path exactly when e_1->e_2->...->e_k is a directed comparison chain. Vertex-simplicity is essential: an arbitrary directed line-graph path can encode an ordinary trail with repeated original vertices.

If a total order < on E(K_V) realizes H by tight(u,v,w) iff {u,v}<{v,w}, every comparison arc points forward, so Gamma(H) is acyclic. Conversely, if Gamma(H) is acyclic, any topological total ordering of its vertices E(K_V) puts {u,v} before {v,w} exactly when Gamma(H) has {u,v}->{v,w}, hence exactly when (u,v,w) is tight. Therefore

    H is edge-orderable iff Gamma(H) is acyclic.

Now assume Gamma(H) is cyclic and choose a shortest directed cycle C=e_0->...->e_{r-1}->e_0. If two nonconsecutive vertices e_i,e_j of C were adjacent in L(K_V), whichever direction their chord has combines with one directed segment of C to form a shorter directed cycle. So C is chordless.

For r=3, three pairwise incident ordinary edges are either the three edges of one ordinary triangle or three edges sharing a common vertex. In the star case va,vb,vc, the cycle is exactly the local middle-v directed triangle (a,v,b),(b,v,c),(c,v,a). In the ordinary-triangle case, after cyclic naming a,b,c, it is (a,b,c),(b,c,a),(c,a,b).

For r>=4, chordlessness says nonconsecutive ordinary edges are disjoint while consecutive ones meet. Put v_i=e_{i-1} cap e_i cyclically. These v_i are distinct and e_i={v_i,v_{i+1}}, so the e_i are the edges of a simple ordinary r-cycle. The arc e_i->e_{i+1} is exactly the tight cyclic turn (v_i,v_{i+1},v_{i+2}). Hence every nonintegrable boundary tournament has a literal shortest holonomy certificate of the stated star/triangle/cycle type.

This proof uses only R3. No smallest-counterexample, deletion-cover, R24, gate, capture, payment, or finite-order hypothesis enters.



## Canonical insertion barriers in the edge-ordered branch

R895 is a pure edge-ordered graph lemma. Let Q=(q_0,...,q_m), m>=1, be increasing and write e_i=q_iq_{i+1}, so e_0<...<e_{m-1}. Let x be outside Q, adjacent to all q_i, and assume inserting x into no internal gap preserves the displayed increasing order.

Define L_0=true and, for i>=1,

    L_i : e_{i-1}<q_i x.

Define R_{m-1}=true and, for i<=m-2,

    R_i : xq_{i+1}<e_{i+1}.

Some gap has both L_i and R_i. Starting from L_0, if L_i holds but R_i fails for i<m-1, then e_{i+1}<xq_{i+1}; since e_i<e_{i+1}, we obtain e_i<xq_{i+1}, which is L_{i+1}. If no gap had both properties this would force L_{m-1}, contradicting the built-in truth of R_{m-1}.

At a gap with both properties, all comparisons needed to insert x are favorable except possibly q_i x versus xq_{i+1}. Since insertion fails, totality forces

    xq_{i+1}<q_i x.

Let beta(x) be the least right-feasible gap. Every earlier R_j fails, so the same propagation proves L_{beta(x)}. Therefore beta(x) is simultaneously feasible and carries the forced reverse-middle inequality.

If beta(x)<beta(y), put i=beta(x). Right feasibility of x gives xq_{i+1}<e_{i+1}, while minimality of beta(y) makes R_i(y) fail and gives e_{i+1}<yq_{i+1}. Hence

    xq_{i+1}<e_{i+1}<yq_{i+1},

which is exactly the tight cross turn (x,q_{i+1},y) in the induced boundary tournament. A family of noninsertable exterior vertices therefore carries a canonical barrier preorder, with every strict separation witnessed by an intrinsic cross turn.

Beta-values need not be distinct, and the lemma does not itself yield a two-cover. In an edge-orderable R24-failure application it does, however, replace a diffuse insertion-obstruction array by one scalar crossing-time coordinate per exterior vertex.



## Five-vertex nonHamilton systems are integrable

R902 states that a boundary tournament on five vertices with no tight Hamilton path has acyclic comparison orientation. By R887 it is enough to exclude every possible shortest directed comparison cycle.

Such a cycle is a star triangle, an ordinary triangle, or an ordinary simple cycle. On five vertices a simple comparison cycle has length at most five. A length-five ordinary cycle immediately supplies a Hamilton tight ordering: if its ordinary vertices are v_0,...,v_4 cyclically, the forward comparison arcs certify the three consecutive turns of (v_0,v_1,v_2,v_3,v_4). Thus a nonHamilton five-set can fail integrability only through an ordinary directed triangle, a directed star triangle, or an ordinary directed square.

The remaining exclusion is an exact finite propositional proof retained in P973. There are 60 ordered triples and 30 reversal pairs. Choose one Boolean variable for each pair, with reversing a triple negating its literal. For every permutation p=(p_0,...,p_4), the clause

    not tight(p_0,p_1,p_2) OR not tight(p_1,p_2,p_3) OR not tight(p_2,p_3,p_4)

says precisely that p is not a Hamilton tight path. All 120 permutation clauses therefore encode exactly nonHamiltonicity, without extra orientation hypotheses. For each of the three possible comparison-cycle roots, add unit clauses fixing its directed turns.

P973 stores an explicit binary case-split and unit-propagation refutation for each CNF, with a standard-library verifier. At each internal node the verifier checks both values of the split variable. Each propagation is checked against its indexed original clause: all other literals must already be false and the propagated literal must be the unique survivor. At each leaf an indexed original clause is checked to be false. The proof-tree statistics (split nodes, contradiction leaves, unit steps) are (29,30,331) for the ordinary triangle, (3,4,41) for the square, and (15,16,189) for the star triangle. Thus the certificate is an exhaustive propositional proof, not a trusted solver status. The complete certificate data and executable verifier are exactly retrievable as P973.

All three remaining roots are impossible, while the five-cycle root is Hamilton directly. Hence Gamma(H) is acyclic and R887 gives a realizing total edge order.

A useful consequence is order-free. In any boundary tournament with pc(H)>2, let a proper tight path have a five-vertex complement. If that complement were Hamiltonian, the two paths would form a spanning two-cover. So the complement is nonHamiltonian and R902 makes it edge-orderable.

This is only a five-vertex theorem. It does not imply that larger systems whose small induced subsystems are integrable are globally integrable.



## Two-cover conjecture for the edge-ordered subclass

R888 conjectures that every finite edge-ordered complete graph has its vertices partitionable into at most two vertex-disjoint increasing paths. Through R887 this is exactly the main two-cover statement restricted to acyclic comparison orientations. A stronger candidate asks that, for every prescribed vertex v, such a two-path partition can expose v as an endpoint of one path.

R888 has no proof route and is not a usable premise. Recorded MILP evidence is evidence only. Boolean pairwise comparisons encode a total order on the binomial(n,2) ordinary edges; directed-triangle inequalities enforce transitivity; for every ordered two-path vertex partition an inequality forbids all comparisons required by that candidate cover from holding simultaneously. The no-two-cover MILP was infeasible for n=5,6,7. At n=8 the recorded run reached a 35-second limit without either a feasible counterexample or an infeasibility certificate. Random edge orders had pc<=2 through n=10 in the tested sample, and random endpoint-flexibility tests passed through n=8. None of this proves n>=8 or endpoint flexibility.

Any proof must coexist with the long-path fences below. It cannot simply show that one increasing path is nearly spanning in every edge order.



## Local integrability does not imply global edge-orderability

R903 gives an explicit obstruction family. Fix n>=4 with vertices v_0,...,v_{n-1} cyclically and let e_i={v_i,v_{i+1}} be the edges of one ordinary Hamilton cycle. Let D be every other ordinary edge and choose any total order on D. Orient line-graph adjacencies within D according to this order, orient every mixed adjacency from D into the cycle-edge layer, and orient e_i->e_{i+1} cyclically.

This comparison orientation has exactly one directed simple cycle. A directed cycle cannot mix D and the cycle layer because no arc returns from the cycle layer to D. The orientation on D is acyclic. Among the e_i, the only line-graph adjacencies are consecutive ones of the chordless ordinary n-cycle, and these are oriented cyclically. Hence the displayed n-cycle is unique.

Every proper induced subsystem is edge-orderable: omitting any original vertex removes its two incident cycle edges and breaks the unique directed cycle, after which R887 topologically orders the restriction.

Every local middle-vertex tournament is also transitive. At v_i, its incident D-edges inherit the common total order and all precede the two cycle edges; those last two satisfy e_{i-1}->e_i. Yet the full system is nonintegrable because its comparison n-cycle survives.

Finally, e_i->e_{i+1} means every cyclic turn (v_i,v_{i+1},v_{i+2}) is tight, so (v_0,...,v_{n-1}) is a Hamilton tight path and pc(H_n)=1.

Thus for every fixed k there is a non-edge-orderable boundary tournament whose induced subsystems on at most k vertices are all edge-orderable, even with every local middle tournament transitive. These examples do not refute the two-cover conjecture because they are Hamiltonian. They do rule out bounded forbidden-induced-subsystem characterizations of edge-orderability and any promotion of R902 to an unsupported local-to-global theorem.



## Increasing-path length has strong independent obstructions

These are two distinct obstructions to forcing a single long tight path in the edge-order-induced subclass. Neither is a counterexample to the two-path-cover conjecture. For a total edge order, declare (u,v,w) tight exactly when {u,v}<{v,w}; this satisfies complete-reversal antisymmetry, and tight paths are precisely increasing graph paths.

Matching-layer construction (R823/P898; accepted, fully reconstructible). Let n=2m and partition the vertices into A and B of size m. Put all internal edges before all cross edges. Partition the cross edges into m perfect matchings M_1,...,M_m and order them in contiguous matching blocks. Such a partition can be obtained by labeling each part modulo m and putting a_i b_{i+j} in M_j.

An increasing path using no cross edge has at most m vertices. Otherwise its initial internal segment lies in one part, say A. After its first cross edge it can use only cross edges. Let p count vertices of the initial A segment and let c count cross edges. Matching-block indices are nondecreasing, and consecutive cross edges cannot belong to one matching because they share a vertex. Consequently c<=m. The alternating suffix consumes floor(c/2) further A vertices, so p+floor(c/2)<=m. Hence the number of path vertices is p+c<=m+ceil(c/2)<=m+ceil(m/2)=ceil(3n/4). For even n>=4 this excludes a spanning path.

Difference-class construction (R829/P903; accepted historical interface, external reconstruction gap retained). Let V=GF(2)^k and n=2^k. For each nonzero d, the edges {x,x+d} form a perfect matching M_d. Order these classes lexicographically by d, with arbitrary order within each class. For an increasing simple path (v_0,...,v_t), the differences d_i=v_{i-1}+v_i strictly increase lexicographically: consecutive edges cannot lie in the same matching, and an increasing path cannot return to an earlier matching block. Every consecutive block satisfies
  sum_{i=a}^b d_i = v_{a-1}+v_b != 0,
by telescoping and vertex simplicity. Thus t<=f(k), where f(k) is the maximum length of a lex-increasing vector sequence with no zero-sum consecutive block.

P903 invokes the Calderbank–Chung–Sturtevant bound f(k)<=(1/2+o(1))2^k to obtain the asymptotic one-half path-length fence. The reduction above is explicit; the external bound itself has not been reconstructed in this development. Its use remains the recorded reconstruction gap, not a new internal proof. Here t counts edges; adding one gives the same asymptotic bound for vertices.

The matching-layer and difference-class constructions retain different mechanisms. Their exact historical statements and proof records remain R823/P898 and R829/P903. This section restores the substantive mathematical destination that had been replaced by a lone heading marker; it changes no canonical review status.

## Unresolved global use of the representation

The representation supplies an exact structural fork, not an alternative completed proof. In the acyclic branch we gain ordinary edge-order mathematics, the beta-barrier lemma, and the open target R888. In the cyclic branch we gain shortest holonomy certificates, but R903 shows that holonomy can be arbitrarily global while every bounded induced subsystem looks integrable.

Three fences must remain visible. R902 is local, not local-to-global. R823 and R829 prevent a generic nearly-spanning-path endgame. R888, including endpoint flexibility, is conjectural despite positive small-order evidence.

The live comparison-family problem is therefore crisp: prove the two-increasing-path theorem for all edge orders, or identify extra smallest-counterexample/deletion-cover hypotheses that interact globally with comparison holonomy. Until then this development is an orthogonal toolkit and fence collection, not a substitute for the R24/gate developments.



## Edge-order port-preservation regression

R177/P579 is an orthogonal negative result because its central mechanism is an explicit total edge order, not deletion-cover recompletion. On vertices {x,c,d,z,a,b,e}, order the ordinary edges

    ab < xa < be < zb < db < ae < za < cz < xz < cb < xd < dz < da < ze < xc < ce < xe < cd < de < ca < xb.

Declare (u,v,w) tight exactly when uv<vw. This is the standard edge-order-induced boundary tournament: reversing the turn reverses the comparison of the same two incident edges, so exactly one complete reversal is tight. Direct comparison gives xcd and abe tight, while cdz, zab, and dza are bad, realizing the historical crossed deletion-window pattern.

The point of the example is not failure of two-coverability. In fact (a,b,z,x,c,d,e) is a tight Hamilton path. What fails is the stronger **literal port-preservation** demand: there is no spanning ordered two-path partition in which one path begins with the prescribed port (x,c) and the other ends with the prescribed port (b,e). The preferred full proof P579 checks all literal candidates under those port constraints and finds none tight, while separately verifying the Hamilton ordering above.

The older compressed route P177 reports a different raw candidate count in its outline than P579. The preferred reconstructed proof P579 is the exact route used here; the count discrepancy is retained as provenance rather than harmonized by guesswork. The mathematical conclusion is unchanged: crossed local window data do not force a bounded reroute preserving both old ports, even inside an edge-orderable Hamiltonian system.

This fence belongs beside R823/R829: edge-orderable examples are a testing ground not only for path length, but also for overly rigid endpoint/port-preserving claims.

## Threshold-matching duality for increasing path covers

Let G=K_V be a complete graph with a strict total edge order, represented by distinct real labels lambda(uv). For a vector of real cut times tau=(tau_v)_{v in V}, define a bipartite graph B_tau with left copies v^out and right copies v^in of V. Put the bipartite edge

    u^out v^in in E(B_tau)

exactly when

    tau_u < lambda(uv) < tau_v.

(The reverse bipartite edge v^out u^in cannot occur simultaneously.) Let nu(B_tau) be the matching number.

**Threshold-matching characterization.** If n=|V|, then

    pc_inc(G) = n - max_tau nu(B_tau),

where pc_inc is the minimum number of vertex-disjoint increasing paths whose vertices partition V. Equivalently, by the bipartite deficiency form of Hall's theorem,

    pc_inc(G)
      = min_tau max_{X subseteq V} ( |X| - |N_{B_tau}(X)| ).

Proof. First fix tau and a matching M in B_tau. Interpret a matched edge u^out v^in as a directed ordinary edge u->v. Since M is a matching, every original vertex has outdegree at most one and indegree at most one in the resulting directed graph F. Moreover every directed edge u->v satisfies tau_u<lambda(uv)<tau_v. Hence tau strictly increases along directed edges, so F has no directed cycle. Its components are therefore vertex-simple directed paths and isolated vertices. At any two consecutive directed edges u->v and v->w we have

    lambda(uv) < tau_v < lambda(vw),

so each nontrivial component, read in its directed order, is an increasing path. As F has n vertices and |M| edges and is a disjoint union of paths, it has exactly n-|M| components. Thus

    pc_inc(G) <= n - nu(B_tau)

for every tau, and therefore pc_inc(G)<=n-max_tau nu(B_tau).

Conversely, let P_1,...,P_k be any increasing path cover. Orient each path in its increasing direction. For every vertex v choose tau_v strictly between the label of its incoming path edge and the label of its outgoing path edge. At an initial vertex only the upper inequality is required, so choose tau_v below its outgoing label; at a terminal vertex only the lower inequality is required, so choose tau_v above its incoming label; at a singleton choose tau_v arbitrarily. Such choices exist because the path labels strictly increase. If u->v is a path edge, then tau_u<lambda(uv)<tau_v. Hence all n-k path edges give a matching in B_tau: each vertex contributes to at most one selected outgoing edge and at most one selected incoming edge. Therefore max_tau nu(B_tau)>=n-k. Minimizing k gives

    max_tau nu(B_tau) >= n-pc_inc(G),

which combined with the first inequality proves equality.

For a balanced bipartite graph with n vertices on each side, Hall deficiency

    def(B)=max_{X subseteq V_out} (|X|-|N_B(X)|)

satisfies nu(B)=n-def(B). Substitution into the first identity yields the second.

**Consequences and exact open target.** A Hamilton increasing path is equivalent to some tau with Hall deficiency one. A spanning cover by at most two increasing paths is equivalent to some tau with Hall deficiency at most two. Thus the open integrable two-cover conjecture R888 is precisely the movable-threshold assertion

    min_tau def(B_tau) <= 2.

This is an exact reformulation, not a proof of R888. It isolates the remaining issue as a Hall-deficiency theorem for the straddling relation tau_u<lambda(uv)<tau_v, and it avoids any requirement that one individual increasing path be nearly spanning.

## Cyclic nonzero-block sequences generate two translated increasing rails

Retain the Calderbank–Chung–Sturtevant difference-class edge ordering from R829. Thus V=GF(2)^k, and every ordinary edge {x,y} receives difference label x+y. Difference classes are ordered lexicographically, with arbitrary order inside a class. Consecutive edges of a simple path can never have the same difference label because every fixed nonzero difference class is a perfect matching.

Call A=(a_1,...,a_t) an f*-sequence when it is lexicographically increasing and every nonempty cyclic consecutive block has nonzero sum in GF(2)^k. This is the CCS cyclic strengthening of an f-sequence. Put

    p_0=0,    p_j=a_1+...+a_j  (1<=j<=t),    c=p_t.

Because every ordinary consecutive block has nonzero sum, p_0,...,p_{t-1} are pairwise distinct. Because the full cyclic block has nonzero sum, c is nonzero.

Define two vertex sequences

    P=(p_0,p_1,...,p_{t-1}),
    Q=(c+p_0,c+p_1,...,c+p_{t-1}).

For 1<=j<=t-1, the difference of consecutive vertices of P is a_j, and the same is true for Q. Since a_1<...<a_{t-1} lexicographically, both P and Q are increasing simple paths in the CCS edge order.

It remains to prove disjointness. Suppose p_i=c+p_j for some 0<=i,j<=t-1. If i=j, then c=0, contrary to the full-block condition. If i<j, then

    0=c+p_i+p_j
      =(a_1+...+a_t)+(a_{i+1}+...+a_j),

which in characteristic two is exactly the sum of the complementary cyclic block

    a_{j+1},...,a_t,a_1,...,a_i.

That is a nonempty cyclic consecutive block, contradicting the f*-property. The case j<i is symmetric. Hence V(P) and V(Q) are disjoint and together contain exactly 2t vertices.

Therefore every f*-sequence of length t in GF(2)^k canonically produces two vertex-disjoint increasing paths covering 2t vertices in the CCS difference-class edge ordering. In particular, the general upper bound f*(k)<=2^{k-1} from CCS becomes a two-cover threshold: whenever equality f*(k)=2^{k-1} is attained by some sequence, these two translated paths partition all 2^k vertices.

The CCS displayed examples attain length 2^{k-1} for k=4 and k=5; the paper also states equality for k=1,2,3. Thus their canonical difference-class construction has a spanning two-increasing-path cover for k<=5, despite being the source of the asymptotic one-half longest-path fence.

For k>=6 their recursive theorem only guarantees f*(k)>=(23/48)2^k; this lemma does not assert equality, nor does it prove a spanning two-cover in those orders. It isolates the next question: whether the two translated rails obtained from a near-extremal f*-sequence can absorb the uncovered vertices by additional edges whose difference labels fit at the rail boundaries or by a different two-rail decomposition.

Tie-order invariance. The tight-path system, and hence its minimum path-cover number, is independent of the ordering of edges inside each fixed difference class. Indeed the two consecutive edges of any vertex-simple triple have distinct differences: u+v=v+w would imply u=w. Their comparison is therefore determined entirely by the order of the difference classes. Equivalently, any increasing simple path has strictly increasing difference labels; a repeated class cannot occur with intervening classes because the classes are contiguous in the total edge order. Thus resolving the two-cover question for one within-class tie order resolves it for all such tie orders of this same class ordering. This statement does not identify arbitrary increasing paths or two-covers with the translated f*-sequence construction; failure of that sufficient construction alone does not prove failure of a general two-cover.


## The CCS F(6) difference-class ordering has an explicit spanning two-path cover

Retain the Calderbank–Chung–Sturtevant difference-class ordering F(6): V=GF(2)^6 is identified with integers 0,...,63, and the class label of {x,y} is x xor y. Difference classes are ordered 1<...<63. Consecutive edges of a vertex-simple path have distinct difference labels, so within-class ordering is irrelevant.

The recursive length-31 sequence is

B=(1,4,6,7,9,10,12,13,15,16,17,18,20,25,29,31,37,38,39,41,42,44,45,47,48,49,50,52,57,61,63).

Its total xor is 32. The standard prefix-XOR construction using the first thirty differences gives the two translated increasing paths

P=(0,1,5,3,4,13,7,11,6,9,25,8,26,14,23,10,21,48,22,49,24,50,30,51,28,44,29,47,27,34,31),

Q=(32,33,37,35,36,45,39,43,38,41,57,40,58,46,55,42,53,16,54,17,56,18,62,19,60,12,61,15,59,2,63).

They are disjoint and cover 62 vertices; the omitted pair is {20,52}. Neither omitted vertex can be inserted, prepended, or appended individually to either displayed rail.

Nevertheless the pair inserts cooperatively into Q. Replace the single edge 42-53, whose difference label is 31, by

42-52-20-53.

The three new difference labels are

42 xor 52=30,
52 xor 20=32,
20 xor 53=33.

The neighboring Q labels are 29 before the old edge and 37 after it, so the local label string

29<31<37

is replaced by

29<30<32<33<37.

Thus

Q*=(32,33,37,35,36,45,39,43,38,41,57,40,58,46,55,42,52,20,53,16,54,17,56,18,62,19,60,12,61,15,59,2,63)

is increasing. P is unchanged. Since P and Q were disjoint and omitted exactly {20,52}, the paths P and Q* are disjoint and together cover all 64 vertices.

The direct algebra behind the bridge is general. If an XOR-ordered rail uses an odd label r on x-(x xor r), define

u=x xor (r-1),
v=u xor (r+1).

Then x-u, u-v, v-(x xor r) have labels r-1,r+1,r+2, because for odd r,

(r-1) xor r xor (r+1)=r+2.

Whenever the surrounding rail labels lie below r-1 and above r+2 and u,v are unused, this replaces one rail edge by a three-edge increasing bridge and absorbs two vertices.

Canonical barrier geometry explains why single insertion fails but is not needed for the certificate. For 20 against P and 52 against Q the least-right-feasible barrier is beta=9; for 52 against P and 20 against Q it is beta=15. The successful move bypasses the latter obstruction by using the two holes together. The earlier endpoint-transfer certificate recorded in R924/P996 is also valid but is redundant; no endpoint transfer is required.

Consequently F(6) has increasing path-cover number at most two. This finite result does not prove the general edge-ordered two-cover conjecture R888.

## Every recursive CCS difference-class obstruction F(k) has a spanning two-path cover

We prove that the entire recursive Calderbank–Chung–Sturtevant difference-class family is two-coverable, even though it is the classical source of the asymptotic one-half longest-monotone-path fence.

1. Difference-class order and the recursive sequences.

For k>=1 identify GF(2)^k with the integers 0,...,2^k-1 in binary. Give every ordinary edge {x,y} the nonzero difference label x xor y, and order the difference classes by their integer (equivalently lexicographic binary) order. Consecutive edges of a vertex-simple path cannot have the same difference because x xor y=y xor z would imply x=z. Therefore within-class tie order is irrelevant: a vertex sequence is increasing exactly when its consecutive XOR differences are strictly increasing.

The k=5 CCS sequence is

A_5=(1,4,6,7,9,10,12,13,15,16,17,18,20,25,29,31).

Its prefix-XOR path and its translate by the total XOR 21 are

P_5=(0,1,5,3,4,13,7,11,6,9,25,8,26,14,23,10),
Q_5=(21,20,16,22,17,24,18,30,19,28,12,29,15,27,2,31).

They are disjoint and together contain all 32 vertices, so F(5) is already two-covered.

For the induction it is convenient to start from the explicit k=6 sequence

A_6=(1,4,6,7,9,10,12,13,15,16,17,18,20,25,29,31,37,38,39,41,42,44,45,47,48,49,50,52,57,61,63).

For k>=6, write A_k=(a_1,...,a_t) and N=2^k. Define A_{k+1} by the CCS recursion

- if t is odd, A_{k+1}=(A_k, N+A_k);
- if t is even, put A_k^-=(a_1 xor a_2,a_3,...,a_t) and set A_{k+1}=(A_k,N+A_k^-).

Here N+A means add the new leading binary 1, so numerically each term is N+a. The first three terms remain 1,4,6, hence a_1 xor a_2=5<6 and A_k^- is increasing whenever it is used. Thus every A_k is strictly increasing. Also A_k ends in N-1 and its penultimate term is at most N-3; these facts hold at k=6 and are preserved by either lift.

Let t_k=|A_k|. Let

s_0=0,
 s_i=a_1 xor ... xor a_i  (1<=i<=t_k),
 c_k=s_{t_k}.

Define the canonical prefix rail

P_k=(s_0,s_1,...,s_{t_k-1})

and the translated rail Q_k=c_k+P_k, where + denotes XOR. Their consecutive difference labels are a_1,...,a_{t_k-1}, so whenever the vertex lists are simple and disjoint they are increasing paths.

At k=6, c_6=32. If c_k=2^{k-1}, then in either recursive branch the low-bit XOR of the two blocks cancels, while the second block has odd length (t_k in the odd branch, t_k-1 in the even branch), so its new leading bit survives. Hence

c_{k+1}=2^k.

Therefore for every k>=6,

c_k=2^{k-1}.

2. Exact hole recursion.

Let S_k={s_0,...,s_{t_k-1}} be the vertex set of P_k, let C_k=S_k union (c_k+S_k), and let

H_k=GF(2)^k \ C_k.

At k=6 the displayed rails are simple and disjoint and

H_6={20,52}.

We now derive H_{k+1} exactly and at the same time prove inductively that P_{k+1},Q_{k+1} remain simple and disjoint.

Fix k>=6, put N=2^k and c=c_k=N/2, and assume P_k,Q_k are disjoint. View GF(2)^{k+1} as two N-vertex layers according to the new leading bit.

If t=t_k is odd, the second block of A_{k+1} is N+A_k. Ignoring the new leading bit, its prefix states are c+S_k. Since Q_{k+1}=N+P_{k+1}, taking the union of the two new rails supplies both leading-bit copies of every low-bit state in

S_k union (c+S_k)=C_k.

Thus

H_{k+1}=H_k union (N+H_k).                                      (2.1)

If t is even, the prefix set of A_k^- is

S_k^-={0,s_2,s_3,...,s_{t-1}}=S_k\{s_1}.

Because s_1=a_1=1, the low-bit projections covered by the two new rails are

S_k union (c+S_k^-)
 = C_k \ {c+1}.

Hence

H_{k+1}=H_k union (N+H_k) union {c+1,N+c+1}.                    (2.2)

In the odd case the new covered set has 2|C_k| elements, exactly the total number of entries in P_{k+1},Q_{k+1}. In the even case it has 2(|C_k|-1) elements, again exactly the total number of entries in the two new rails. Therefore no repetitions or intersections are hidden in the set calculation: the new rails are simple and disjoint.

3. The universal odd-label two-hole bridge.

Suppose an increasing XOR rail contains an edge

x -> z=x xor r

with r odd. Define

u=x xor (r-1),
 v=u xor (r+1).

Then

x xor u=r-1,
 u xor v=r+1,
 v xor z=(r-1) xor (r+1) xor r=r+2,

where the last identity holds for every odd r. Therefore, if the preceding rail label is below r-1, the following rail label is above r+2, and u,v are unused, the one edge of label r may be replaced by

x -> u -> v -> z

with increasing labels

r-1 < r+1 < r+2.

We call this a safe r-bridge. It absorbs exactly two holes without changing the order of any old rail vertex.

4. A bridge graph on all holes.

We construct, for every k>=6, a multigraph Gamma_k whose vertex set is H_k. Every edge of Gamma_k is attached to one safe bridge position on P_k or Q_k, and its two endpoints are exactly the two holes absorbed by that bridge.

Base k=6. The P_6 edge 10-21 has label 31. Its bridge vertices are

10 xor 30=20,
20 xor 32=52.

The neighboring rail labels are 29 and 37, so this is safe. The translated Q_6 edge gives the same unordered hole pair. Thus Gamma_6 consists of two parallel edges on {20,52}, one P-edge and one Q-edge. It is a 2-regular even-cycle multigraph.

For bookkeeping, let R_k be the set of bridge labels used by Gamma_k. Initially R_6={31}. The induction below gives

R_{k+1}=R_k union (N+R_k)                         if t_k is odd,
R_{k+1}=R_k union {N-1} union (N+R_k)             if t_k is even.       (4.1)

Consequently every bridge label is odd, at least 31, distinct bridge labels differ by at least 32, and every r in R_k is at most 2^k-33. These properties are immediate at k=6 and preserved by (4.1). In particular no old bridge label is a_1 or a_2, and no bridge label is the final term of A_k.

Inductive lift of Gamma_k. Again put N=2^k and c=N/2. Write h^0=h and h^1=N+h for the two copies of an old hole h.

Take a P-colored bridge of Gamma_k at label r, with hole pair {u,v}. In A_{k+1}, the first-block occurrence of the same label r has the same old prefix state. Hence the corresponding P_{k+1} bridge is {u^0,v^0}, while translating the rail by the new total XOR N gives the Q_{k+1} bridge {u^1,v^1}. Thus a P-colored old bridge lifts to the two horizontal copies of that edge.

Now take a Q-colored old bridge at label r. If the old P-prefix immediately before r is x, then its Q-hole pair has the form

{c+u,c+v},

where u=x xor (r-1) and v=u xor (r+1). The second block of A_{k+1} contains the label N+r: in the odd branch this is immediate, and in the even branch r survives in A_k^- because r is neither a_1 nor a_2. Immediately before that high label, the low-bit part of the new prefix state is c+x; only its new leading bit depends on parity. Therefore the two bridge vertices for N+r are

(c+u)^{epsilon}, (c+v)^{1-epsilon}

for some epsilon in {0,1}. The Q_{k+1} translate supplies the complementary pair

(c+u)^{1-epsilon}, (c+v)^{epsilon}.

Thus a Q-colored old bridge lifts to the two crossed copies of that edge.

Ignoring the P/Q colors, these two rules say exactly that the old 2-regular multigraph Gamma_k is replaced by a 2-lift on the two copies of H_k. A cycle of length m in a 2-lift becomes either two m-cycles or one 2m-cycle. Since every old cycle is even, every lifted cycle is even.

There is one additional feature in the even-length branch. Formula (2.2) creates the two new holes

z=c+1,
 z^1=N+c+1.

The last first-block edge has label r=N-1. Its initial vertex is s_{t-1}=c xor (N-1), so its bridge vertices are

(c xor (N-1)) xor (N-2)=c+1=z

and

z xor N=N+c+1=z^1.

The translated rail gives the same unordered pair, so these two new holes form an additional two-cycle of parallel P/Q bridge edges. The bridge is safe: the preceding label is at most N-3<N-2, while the next used label is N+(a_1 xor a_2)=N+5>N+1.

Hence, in either parity branch,

Gamma_{k+1} is a disjoint union of even cycles.                 (4.2)

The bridge positions inherited from old edges remain safe because their local neighboring labels are unchanged in the first block and are shifted uniformly by N in the second block. In the even branch the only altered beginning of A_k^- is 5, while every inherited bridge label is at least 31. The special bridge was checked above. Finally, on each fixed rail, distinct bridge labels have disjoint ordered windows [r-1,r+2], because distinct labels in R_k differ by at least 32. The same bridge label may occur once on each of the two rails; those replacements are on disjoint vertex sequences and do not interact. Hence any collection of safe bridges selected on either rail may be performed simultaneously.

5. Perfect matching and spanning two-cover.

Every finite even cycle has a perfect matching; the same is true for a two-cycle of parallel edges. By (4.2), Gamma_k therefore has a perfect matching M_k.

For every matched edge of Gamma_k, perform the associated safe bridge replacement on its designated rail P_k or Q_k. Distinct matched bridge edges use disjoint hole pairs, so every hole is inserted exactly once and no inserted vertex is repeated. The original rails already partition GF(2)^k\H_k. Thus the two modified rails are vertex-disjoint and together contain every vertex of GF(2)^k.

Each modified rail remains increasing: every individual replacement substitutes r by r-1,r+1,r+2 inside its certified seam; on each rail the windows for distinct selected bridge labels are separated, while equal-label replacements can only occur on the two different rails and therefore do not interact. Therefore the two modified rails form a spanning cover by two increasing paths.

This proves that for every k>=6 the CCS difference-class ordering F(k) has increasing path-cover number at most two. Together with the explicit k=5 pair above, the conclusion holds for every k>=5.

The theorem is specific to the CCS XOR difference-class family. It does not prove R888 for arbitrary edge orders. Its significance is that the entire classical family giving the asymptotic (1/2+o(1)) upper fence for the longest single monotone path nevertheless has a spanning two-path cover, by a recursive cooperative-absorption mechanism rather than by one long path.

## Round-by-round compatible-edge abundance in ordered 1-factorizations

Let K_n, n even, have an ordered 1-factorization E(K_n)=M_1 disjoint-union ... disjoint-union M_{n-1}, where every edge of M_i precedes every edge of M_j for i<j. Let F be a spanning cover by k vertex-disjoint increasing paths. Orient each path in increasing order. For a vertex v define L(v) to be the matching-block label of its incoming F-edge, or 0 if v is a source, and U(v) the label of its outgoing F-edge, or n if v is a terminal. Thus L(v)<U(v).

Fix a round t in {1,...,n-1}. Call v active at t when L(v)<t<U(v). Let d_t be the number of F-edges belonging to M_t. Since M_t is a matching, each F-component contains at most one such edge. A component containing an F-edge of color t has no active vertex at t: the tail has U=t and the head has L=t. Every other F-component has exactly one active vertex, namely the unique vertex between its last used color below t and its first used color above t (with source/terminal conventions at the ends). Hence the number of active vertices is exactly k-d_t.

Call an oriented M_t-edge u->v interval-compatible with F when L(u)<t<U(v). Every selected F-edge of M_t is interval-compatible in its F orientation, giving d_t compatible ordinary edges.

Now remove the endpoints of those d_t selected edges. The remaining active vertices are incident in M_t to edges disjoint from the selected ones. Every M_t-edge incident with at least one active vertex is interval-compatible in at least one orientation. Indeed, if u is active and its mate v is future at t (t<L(v)), then u->v is compatible because L(u)<t<U(v). If v is past at t (U(v)<t), then v->u is compatible because L(v)<t<U(u). If v is also active, either orientation is compatible.

A matching edge can contain at most two of the k-d_t active vertices, so at least ceil((k-d_t)/2) further edges of M_t are incident with an active vertex. Therefore M_t contains at least

    d_t + ceil((k-d_t)/2)

interval-compatible ordinary edges.

For k=3 this lower bound is always at least two; if d_t>=2 it is at least three.

This is only a round-abundance lemma. The interval-compatible relation uses the full open windows (L(v),U(v)); unlike the single-threshold graph of the threshold-matching duality, an arbitrary bipartite matching or alternating augmenting path in this wider relation need not compile to an increasing path cover if both the incoming and outgoing adjacency of one original vertex are changed simultaneously. Any use in a rotation argument must retain original-vertex consistency or a single separating threshold at each vertex.

## One-sided threshold graphs are exact endpoint-rotation systems

Let G be an edge-ordered complete graph with distinct real edge labels lambda, and let F be a spanning cover by k vertex-disjoint increasing paths. Orient every component in its increasing direction. For each vertex v let L(v) be the label of its incoming F-edge, with L(v)=-infinity at a source, and U(v) the label of its outgoing F-edge, with U(v)=+infinity at a terminal. Along every nontrivial component, L(v)<U(v).

TERMINAL-ROTATION THRESHOLDS. Choose one cut tau_v^- immediately after L(v): for a source choose it below every edge label, and otherwise choose L(v)<tau_v^- below the next larger edge label. The threshold graph B^- from the threshold-matching duality has

    u_out v_in in B^-  iff  L(u)<lambda(uv)<=L(v).

Every F-edge u->v lies in B^- because lambda(uv)=L(v)>L(u). Hence the n-k F-edges form a matching M_F in B^- saturating every right copy except the k source copies. A source right copy is isolated in B^-: its cut is below every edge label. Therefore every matching of size n-k in B^- leaves exactly the same k right copies unmatched, namely the original sources.

By the threshold-matching proof, any matching M of size n-k in B^- gives an acyclic directed linear forest on V with k components, and at every internal vertex the incoming selected label is below tau_v^- while the outgoing selected label is above tau_v^-. Thus every component is an increasing path. Consequently size-(n-k) matchings in B^- are genuine k-path covers with the same source set as F; there is no original-vertex collision issue.

The elementary alternating move has a direct path interpretation. Let t be a current terminal and let v be a nonsource with old predecessor p(v). If

    L(t)<lambda(tv)<=L(v),

then t_out v_in is an unmatched B^- edge and p(v)_out v_in is the matched old edge. Toggling those two edges deletes p(v)->v and adds t->v. Since t is terminal and the inequality gives

    last(t-path)=L(t)<lambda(tv)<=L(v)<U(v),

the path ending at t is concatenated to the old suffix beginning at v, while the old prefix ending at p(v) becomes a separate path. The source set is unchanged and the terminal t is replaced by p(v). Longer alternating paths are compositions of such source-preserving terminal rotations and remain valid automatically because they are matchings in one threshold graph.

SOURCE-ROTATION THRESHOLDS. Dually choose tau_v^+ immediately before U(v), above every edge label at a terminal. Then

    u_out v_in in B^+  iff  U(u)<=lambda(uv)<U(v).

The old F-matching again has size n-k. Every terminal left copy is isolated in B^+, so every size-(n-k) matching in B^+ yields an increasing k-path cover with exactly the same terminal set while the sources may rotate. This is the exact reverse-time analogue of the preceding construction.

These one-sided threshold graphs are deliberately narrower than the full interval-compatible relation L(u)<lambda(uv)<U(v). The latter is useful for identifying individual legal splice edges, but an arbitrary alternating path in that wider bipartite graph may change both incidences of the same original vertex and need not preserve increasing order. B^- and B^+ avoid that defect by using one fixed cut per vertex, so ordinary matching rotations in them are physically valid path-cover rotations.

## Minimum increasing covers contain large physical one-sided Hall-surplus barrier sets

### 1. Lower-cut alternating reachability
Let G be an edge-ordered complete graph with distinct real edge labels lambda, and let F be a spanning increasing k-path cover of minimum possible component count k=pc_inc(G). Orient every component increasingly. Write L(v) for the incoming selected-edge label, with L(v)=-infinity at a source, and U(v) for the outgoing selected-edge label, with U(v)=+infinity at a terminal.

Use the accepted one-sided threshold system of R936. Thus

  u_out v_in in B^-  iff  L(u)<lambda(uv)<=L(v),

and the selected F-edges form a matching M of size n-k in B^-. Every matching in B^- compiles to an increasing path cover, so minimality of k implies M is a MAXIMUM matching of B^-: a matching of size n-k+1 would compile to a spanning (k-1)-path cover.

Start the standard alternating-reachability search from the k unmatched LEFT copies of M, which are exactly the terminal out-copies of F. Traverse nonmatching edges from left to right and matching edges from right to left. Let X be the reachable left copies and Y the reachable right copies. Since M is maximum, no unmatched right copy is reachable. Moreover every neighbor of X lies in Y: for a nonmatching edge this is the search rule, while if an edge from x in X is the matching edge of x, then x was reached through its matched right copy unless x is an unmatched root. Hence

  Y=N_{B^-}(X).                                           (HB.1)

Every y in Y is matched, and its matched left copy lies in X. Conversely every nonroot left copy in X is reached from its matched right copy. Therefore matching gives a bijection between Y and X minus the k roots, so

  |X|-|Y|=k.                                              (HB.2)

### 2. Physical surplus vertices
For a physical vertex v compare its two bipartite copies. Define

  A_T={v : v_out in X and v_in notin Y},
  B_T={v : v_out notin X and v_in in Y}.                 (HB.3)

Summing the two copy-indicators over physical vertices gives

  |A_T|-|B_T|=|X|-|Y|=k.                                 (HB.4)

Hence

  |A_T|>=k.                                               (HB.5)

These are genuine physical vertices, not bipartite-copy artifacts.

There is also an endpoint interpretation. If v_out is in X, choose an alternating path from one unmatched terminal root to v_out and toggle it. Because both endpoints are left copies, the toggle preserves matching size and moves the unmatched left copy from the old terminal root to v_out. The new matching therefore has size n-k. R936 compiles it to an actual increasing k-path cover with the SAME source set as F and with v terminal. Thus every vertex of A_T is terminal-exposable inside the exact source-preserving rotation family.

### 3. Outside-interval clique barrier
Take distinct u,v in A_T and assume L(u)<L(v). Since u_out is in X while v_in is not in Y=N(X), the bipartite edge u_out v_in is ABSENT from B^-. By definition of B^- this says

  not( L(u)<lambda(uv)<=L(v) ).                           (HB.6)

Therefore lambda(uv)<=L(u) or lambda(uv)>L(v). Equality lambda(uv)=L(u) cannot occur under L(u)<L(v): edge labels are globally distinct, so equality would make uv the selected incoming edge of u, whose predecessor v necessarily satisfies L(v)<L(u) along the increasing F-rail. Hence

  lambda(uv)<L(u)  or  lambda(uv)>L(v).                  (HB.7)

Equivalently, for every distinct u,v in A_T,

  lambda(uv)<min{L(u),L(v)}
  OR
  lambda(uv)>max{L(u),L(v)}.                              (HB.8)

Thus Hall deficiency in the collision-free terminal-rotation system produces a physical clique of at least k vertices whose every internal edge label jumps completely outside the interval between the two incoming boundary labels.

### 4. Exact source-rotation dual
Use the upper-cut graph

  u_out v_in in B^+  iff  U(u)<=lambda(uv)<U(v).

Again the F-matching is maximum. Start alternating reachability from the k unmatched RIGHT copies, the source in-copies, traversing nonmatching edges right-to-left and matching edges left-to-right. Let X^+ be the reachable right copies and Y^+ their reachable left neighbors. Define

  A_S={v : v_in in X^+ and v_out notin Y^+}.              (HB.9)

The identical deficiency count gives |A_S|>=k. Toggling an even alternating path makes any v in A_S a source while preserving the old terminal set. And if U(u)<U(v) for u,v in A_S, absence of u_out v_in gives

  lambda(uv)<U(u)  or  lambda(uv)>U(v),

with equality excluded by the same selected-edge uniqueness/increasing-order argument. Hence

  lambda(uv)<min{U(u),U(v)}
  OR
  lambda(uv)>max{U(u),U(v)}                               (HB.10)

for every distinct u,v in A_S.

### 5. Minimum R888-counterexample specialization
In a minimum-order counterexample to R888, accepted R959 gives pc_inc(G)=3. Therefore every spanning minimum three-cover F has two simultaneous physical one-sided barrier sets

  |A_T|>=3,   |A_S|>=3,                                  (HB.11)

where every A_T vertex is terminal-exposable with the original source set fixed, every A_S vertex is source-exposable with the original terminal set fixed, and each induced complete graph obeys its exact outside-interval inequalities (HB.8) and (HB.10).

This is a structural Hall barrier, not a proof of R888. The remaining global problem is to couple the lower and upper surplus systems, or combine one with another extremal/fresh-edge construction, strongly enough to force a legal two-sided augmentation.

### 6. Scope fence
The theorem deliberately uses only B^- and B^+, where arbitrary alternating matching moves are physically valid by R936. It makes NO claim that a long alternating path in the wider broad interval relation L(u)<lambda(uv)<U(v) is valid. R956 gives one special three-component broad-interval augment, and R980 supplies the correct collision-poset treatment for general two-cover recombination. Those collision issues are not bypassed here.

## Every prescribed dimer admits an exact three-pole optimal threshold normalization

### 1. Prescribe one physical dimer rail
Let G be a minimum-order counterexample to R888. Fix any ordered pair of distinct physical vertices (x,y). Accepted R999 gives a spanning increasing three-cover

  F = (x,y) | U | V,

where the displayed dimer is literal. Accepted R1002 applied to the deleted pair {x,y} says every exact two-cover of G-{x,y} has both rails nontrivial, so we may and do retain

  |U|>=2,  |V|>=2.                                      (TP.1)

Thus all three rails of F are nontrivial. Orient U,V increasingly and retain the chosen orientation x->y of the dimer. Let S(F) be the three path sources and T(F) the three path terminals. Because there are no singleton rails,

  |S(F)|=|T(F)|=3,  S(F) cap T(F)=empty.                 (TP.2)

### 2. Push the six endpoint cuts to genuine poles
For each internal vertex v of a rail of F, let L(v) and U(v) be the labels of its selected incoming and outgoing edges and choose

  L(v) < tau_v < U(v).

For each source s in S(F), choose tau_s below every incident edge label. For each terminal t in T(F), choose tau_t above every incident edge label.

Every selected F-edge a->b then satisfies

  tau_a < lambda(ab) < tau_b.                            (TP.3)

Indeed this is immediate at internal vertices from the chosen interval, at a source from the lower-pole choice, and at a terminal from the upper-pole choice. Hence the n-3 selected edges of F form a matching M_F in the threshold graph B_tau of accepted R936.

Since pc_inc(G)=3, accepted threshold duality gives max_sigma nu(B_sigma)=n-3. Therefore

  nu(B_tau)=n-3,                                         (TP.4)

so tau is a globally optimal deficiency-three threshold vector.

### 3. The poles are exactly the path endpoints
A source s has tau_s below all incident labels, hence has no incoming threshold arc and its right copy s_in is isolated. Conversely every nonsource v has a selected incoming edge p->v satisfying lambda(pv)<tau_v, so v is not a threshold source.

Dually, every terminal t has tau_t above all incident labels and therefore no outgoing threshold arc, while every nonterminal v has a selected outgoing edge v->q satisfying tau_v<lambda(vq), so v is not a threshold sink.

Thus the physical threshold digraph has exactly

  Sources(D_tau)=S(F),  Sinks(D_tau)=T(F),               (TP.5)

with three physical sources and three physical sinks. The six forced unmatched copies of M_F are exactly the three source in-copies and the three terminal out-copies. There is no INTERNAL-DEFECT matching deficiency in this normalization.

Completeness also gives the full pole grid: for every s in S(F), t in T(F),

  tau_s < lambda(st) < tau_t,

so s_out t_in is an edge of B_tau. Hence the three sources and three sinks span a complete directed K_{3,3} threshold grid.

### 4. Prescribed-dimer three-pole normalization
Because (x,y) was arbitrary, every ordered physical edge may be installed as an entire source-to-sink dimer rail in some globally optimal exact THREE-POLE threshold cell:

  x in Sources(D_tau),  y in Sinks(D_tau),
  x->y selected in M_F.                                  (TP.6)

The reverse orientation (y,x) may likewise be prescribed in a different optimal three-pole cell.

Consequently, for an existential attack on R888, the INTERNAL-DEFECT side of SV59169 is not an unavoidable kernel. One may choose a clean exact three-source/three-sink optimal cell from the outset, while retaining an arbitrarily prescribed dimer as physical selected data. The remaining Hall obstruction can therefore be concentrated on extinction of the THREE-POLE residue.

### 5. Scope fence
This is a normalization/existence theorem, not an augmentation. It does not say every edge-maximal optimal cell is three-pole, does not connect two prescribed-dimer pole cells by an optimal threshold-cell path, and does not identify the cover-derived one-sided rotation graphs B^- or B^+ with B_tau. In particular, reversing the prescribed dimer between two optimal cells is not itself a contradiction. The gain is that no proof of R888 needs first to eliminate arbitrary INTERNAL-DEFECT cells before attacking a clean deficiency-three pole kernel.

## Every minimum cover carries an optimal threshold box; one-sided rotations glue these boxes

### 1. The selected-edge-preserving threshold box
Let G=K_V be a complete edge-ordered graph with distinct real labels lambda, and let

  F=P_1|...|P_k

be a spanning increasing path cover with the minimum possible number

  k=pc_inc(G).

Orient every component increasingly. Write L_F(v) for the incoming selected-edge label, with L_F(v)=-infinity at a source, and U_F(v) for the outgoing selected-edge label, with U_F(v)=+infinity at a terminal.

Define the open selected-edge-preserving threshold box

  T(F)={tau : L_F(v)<tau_v<U_F(v) for every physical vertex v}.   (TB.1)

Infinite endpoints have their evident meaning.

For every selected F-edge u->v of label e=lambda(uv),

  e=U_F(u)=L_F(v).

Hence every tau in T(F) satisfies

  tau_u < e < tau_v,

so u_out v_in belongs to B_tau. Therefore the F matching M_F of size n-k is contained in EVERY B_tau with tau in T(F):

  nu(B_tau)>=n-k.                                             (TB.2)

Accepted threshold duality R936 says

  max_tau nu(B_tau)=n-pc_inc(G)=n-k.                         (TB.3)

Combining TB.2-TB.3,

  nu(B_tau)=n-k for EVERY tau in T(F).                       (TB.4)

Thus the whole selected-edge-preserving threshold box of a minimum cover is globally optimal. Threshold hyperplanes may subdivide T(F) into many ordinary cells, but crossing them inside the box never changes the maximum matching value because M_F survives throughout.

### 2. The lower-cut graph B^- is literally a threshold graph in T(F)
For each non-source vertex v, choose tau^-_v immediately above L_F(v): more precisely choose

  L_F(v)<tau^-_v<U_F(v)

so that no v-incident edge label lies strictly between L_F(v) and tau^-_v. For a source v choose tau^-_v below every incident edge label. These choices are possible because the graph is finite and edge labels are distinct.

For any ordinary edge uv of label e,

  tau^-_u < e    iff    L_F(u)<e,                            (TB.5)

and

  e < tau^-_v    iff    e<=L_F(v).                           (TB.6)

The equality in TB.6 is allowed because tau^-_v is strictly above L_F(v), while no incident label lies in between. Hence

  u_out v_in in B_{tau^-}
    iff L_F(u)<lambda(uv)<=L_F(v).                           (TB.7)

The right side is exactly the accepted source-preserving one-sided graph B^- of R936. Therefore

  B_{tau^-}=B^-_F.                                          (TB.8)

In particular B^- is not merely analogous to a movable-threshold graph: it is one exact threshold graph at a canonical lower corner of the optimal box T(F).

### 3. The upper-cut graph B^+ is the opposite threshold corner
Dually, for each nonterminal v choose tau^+_v immediately below U_F(v), with no v-incident label strictly between tau^+_v and U_F(v). For a terminal choose tau^+_v above every incident edge label.

Then for every edge uv of label e,

  tau^+_u < e    iff    U_F(u)<=e,
  e < tau^+_v    iff    e<U_F(v).                           (TB.9)

Hence

  u_out v_in in B_{tau^+}
    iff U_F(u)<=lambda(uv)<U_F(v),                           (TB.10)

which is exactly B^+_F. Thus

  B_{tau^+}=B^+_F.                                          (TB.11)

The collision-free source- and terminal-rotation systems of R936 are therefore the two canonical threshold corners of one common optimal selected-edge box.

### 4. A one-sided rotation glues two optimal threshold boxes at an actual point
Let M' be any size-(n-k) matching in B^-_F. Accepted R936 compiles M' to a spanning minimum k-cover F' with the SAME source set as F.

Because B^-_F=B_{tau^-}, every selected edge u->v of F' satisfies

  tau^-_u < lambda(uv) < tau^-_v.                           (TB.12)

At a physical vertex v, the selected incoming F'-edge (if present) therefore has label below tau^-_v, while the selected outgoing F'-edge (if present) has label above tau^-_v. Equivalently

  L_{F'}(v)<tau^-_v<U_{F'}(v)                              (TB.13)

with the usual infinite endpoint conventions. Thus

  tau^- in T(F) intersect T(F').                            (TB.14)

By Section 1 both boxes are globally optimal. Therefore every legal source-preserving one-sided rotation moves from F to a new minimum cover F' whose selected-edge threshold box OVERLAPS the old box at the literal common threshold vector tau^-.

The B^+ statement is exact dual: every terminal-preserving rotation F'' compiled from a size-(n-k) matching in B^+ satisfies

  tau^+ in T(F) intersect T(F'').                           (TB.15)

This is the explicit transport missing from any argument that merely juxtaposes B_tau with B^-/B^+.

### 5. Exact-three-pole normalization lies in the same box
Now specialize to a minimum-order counterexample to R888 and use SV60353. Fix any ordered physical edge (x,y). Accepted R999 gives a spanning minimum three-cover

  F=(x,y)|U|V,                                              (TB.16)

and accepted R1002 makes U,V nontrivial. Thus all three F-components are nontrivial and the three path sources S and three path terminals T are disjoint physical sets.

Inside the same box T(F), choose a threshold vector tau^pole as follows:

- for each source s, put tau^pole_s below every s-incident edge label;
- for each terminal t, put tau^pole_t above every t-incident edge label;
- for every internal vertex v, choose any L_F(v)<tau^pole_v<U_F(v).

This remains inside T(F). Every internal vertex has its selected incoming edge below the cut and selected outgoing edge above the cut, so it is neither a physical threshold source nor sink. A path source has its cut below every incident label and hence is a threshold source; a path terminal has its cut above every incident label and hence is a threshold sink. Therefore tau^pole is an exact THREE-SOURCE / THREE-SINK optimal threshold normalization with pole sets exactly S,T. This recovers SV60353 as one distinguished region of the same optimal box whose lower and upper corners are B^- and B^+.

### 6. One-sided exposure gives legal pole mobility when it avoids a singleton
Retain the prescribed-dimer cover F of Section 5. Apply SV58872 in B^-_F. If a physical vertex v is terminal-exposable by an alternating path and v is NOT one of the three fixed sources S, toggling that path changes only the unmatched left endpoint: one old terminal ceases to be terminal and v becomes terminal, while the source set stays S. Since the original three components are nontrivial and v is not a source, no physical source becomes terminal, so the new minimum cover F_v has no singleton component.

By Section 4,

  tau^- in T(F) intersect T(F_v).                           (TB.17)

Apply the Section-5 pole normalization inside T(F_v). This gives another exact three-source/three-sink optimal cell with the SAME physical source set S and the new terminal set of F_v, in particular with v as a physical threshold sink.

Thus every terminal-exposable v outside S is not merely a cover-theoretic endpoint rotation: it is a lawful S-fixed mobility of an exact three-pole optimal threshold state through overlapping optimal boxes.

Dually, every source-exposable v outside the fixed terminal set T gives a T-fixed exact-three-pole mobility through the common point tau^+.

This is the precise bridge between SV58872 and SV60353. No identification of distinct threshold graphs is assumed; the common threshold vectors TB.14-TB.15 are explicit.

### 7. Strategic consequence and R987 fence
The exact-three-pole Hall kernel should therefore be viewed as living in a CONNECTED OVERLAP COMPLEX of optimal selected-edge boxes rather than in one isolated threshold cell. One-sided alternating rotations move between boxes by literal common threshold points, and non-singleton rotated covers may be re-normalized to exact three-pole states inside their new boxes.

R987 remains an important fence. It exhibits a two-coverable K9 where one selected-edge-preserving threshold box contains no deficiency-two threshold even though a two-cover exists outside that box. The present theorem does not contradict it. In a hypothetical R888 counterexample, every minimum-cover box is optimal by TB.4, and progress must come from the way many such optimal boxes overlap under legal neutral rotations, not from asserting that one box alone contains an augmentation.

No deficiency-two threshold is produced here. The remaining G24 Hall target is to prove that the exact-three-pole overlap complex cannot be globally stable: some legal sequence of pole mobility / overlapping-box transport must leave the deficiency-three region, or else the resulting rigid overlap pattern must itself be impossible.

## Exact three-pole Hall mobility yields a fresh pole, a singleton escape, or two stationary pole barriers

### 1. Non-singleton exact-three-pole state and full reachable sets
Let G be a minimum-order counterexample to R888 and let

  F=P_1|P_2|P_3                                             (PM.1)

be a spanning minimum three-cover whose three rails are all nontrivial. Write

  S={s_1,s_2,s_3}

for its three physical sources and

  T={t_1,t_2,t_3}

for its three physical terminals. Nontriviality makes S and T disjoint.

By SV65511 the selected-edge threshold box T(F) is globally optimal and contains an exact-three-pole normalization whose physical threshold source and sink sets are exactly S and T.

Use the lower one-sided graph B^-_F and its standard alternating-reachability search from the three unmatched LEFT copies, the terminal out-copies. Let X be the reachable left-copy set and Y=N(X) the reachable right-copy set as in SV58872. Define the FULL physical terminal-reachability set

  R_T={v : v_out in X}.                                     (PM.2)

Every current terminal t lies in R_T because t_out is an alternating root. Moreover the proof of SV58872 applies to every v_out in X, not only to copy-mismatch vertices: an alternating path from a terminal root to v_out may be toggled to a size-(n-3) matching, and R936 compiles it to a minimum three-cover with the SAME source set S and with v terminal. Hence

  every v in R_T is terminal-exposable preserving S.       (PM.3)

Dually, in B^+_F start from the three unmatched RIGHT source in-copies and let X^+ be the reachable right-copy set. Define

  R_S={v : v_in in X^+}.                                    (PM.4)

Then S subseteq R_S and every v in R_S is source-exposable while preserving the terminal set T.

The surplus mismatch sets A_T,A_S of SV58872 remain available, but the exhaustive mobility analysis below uses the larger full reachable sets R_T,R_S.

### 2. Fresh terminal and source poles
Suppose

  v in R_T - (S union T).                                   (PM.5)

Toggle an alternating path exposing v as a terminal. Accepted R936 gives a new minimum three-cover F_v with the SAME source set S and with v among its terminals.

Since v is not a source and the source set remains S, no source is forced to become a terminal. The old terminal at the root of the toggled path ceases to be terminal. Thus F_v still has three nontrivial components.

By the overlap theorem SV65511, the canonical lower threshold point tau^- belongs to

  T(F) intersect T(F_v).                                    (PM.6)

Inside T(F_v), perform the exact pole normalization. This yields a globally optimal exact-three-pole cell with source set S and a sink set containing the genuinely new physical vertex v.

Therefore PM.5 gives FRESH SINK MOBILITY through overlapping optimal boxes.

The exact dual holds:

  v in R_S-(S union T)                                      (PM.7)

produces an overlapping-box exact-three-pole state with the same terminal set T and a genuinely new physical source v.

### 3. Pole-crossing reachability gives a singleton escape
Suppose

  s in R_T cap S.                                           (PM.8)

The B^- alternating path exposing s as a terminal preserves the entire source set S. Hence s remains a source and becomes a terminal in the compiled minimum three-cover. Its component is therefore the singleton (s). Thus PM.8 gives a legal minimum three-cover with one singleton rail and an exact two-cover of G-s on the remaining vertices.

Accepted R959 says every exact two-cover of G-s has both rails of order at least three, so this singleton escape retains substantial nontrivial geometry on the complement.

Dually,

  t in R_S cap T                                             (PM.9)

produces a minimum three-cover with singleton component (t), while the complementary exact two-cover has both rails of order at least three.

We call PM.8-PM.9 SINGLETON MOBILITY. The present section does not claim that the singleton cover itself admits an exact three-pole normalization.

### 4. Exact characterization of one-sided immobility
Assume the lower system has neither fresh-sink mobility nor singleton mobility. Then by PM.5 and PM.8,

  R_T subseteq T.                                           (PM.10)

But T subseteq R_T because the terminal out-copies are the alternating roots. Therefore

  R_T=T.                                                    (PM.11)

We now recover the precise mismatch set A_T of SV58872. Fix t in T. Its right copy t_in is matched because the F-component containing t is nontrivial. Suppose t_in were reachable, i.e. t_in in Y. Alternating reachability would then traverse its matching edge backward to the matched predecessor left copy p_out. The predecessor p is not a terminal of its F-component, so p is not in T. But p_out would lie in X, giving p in R_T, contradicting PM.11. Hence

  t_in notin Y for every t in T.                            (PM.12)

Since t_out in X for every terminal root, PM.12 says T subseteq A_T. Conversely A_T subseteq R_T=T by definition. Thus

  A_T=T.                                                    (PM.13)

The source dual is exact. If the upper system has neither fresh-source mobility nor singleton mobility, then

  R_S=S,
  A_S=S.                                                    (PM.14)

Thus complete one-sided immobility is much stronger than a cardinality statement: the ENTIRE physical alternating-reachable set on each side is exactly its current pole triple.

### 5. Stationary pole barriers
Apply the exact outside-interval inequalities of SV58872 to PM.13-PM.14.

For every two distinct terminals t_i,t_j,

  lambda(t_i t_j)<min{L(t_i),L(t_j)}
  OR
  lambda(t_i t_j)>max{L(t_i),L(t_j)}.                       (PM.15)

For every two distinct sources s_i,s_j,

  lambda(s_i s_j)<min{U(s_i),U(s_j)}
  OR
  lambda(s_i s_j)>max{U(s_i),U(s_j)}.                       (PM.16)

Hence a completely immobile residue consists of two physical three-vertex pole cliques, each of whose three internal edge labels jumps completely outside the corresponding selected-boundary interval, and no nonpole physical vertex is alternating-reachable in either one-sided system.

We call PM.11-PM.16 the STATIONARY POLE-BARRIER normal form.

### 6. G24 exact-three-pole mobility quotient
Combining Sections 2-5, every non-singleton exact-three-pole minimum cover has at least one of the following outcomes:

1. FRESH-POLE: the lower or upper one-sided system exposes a physical vertex outside S union T, and an overlapping optimal box yields an exact-three-pole state with a genuinely new source or sink;
2. SINGLETON: the lower system reaches a source, or the upper system reaches a terminal, producing a legal minimum three-cover with one singleton rail and two long complementary rails;
3. STATIONARY BARRIER: R_T=T and R_S=S, equivalently no nonpole or opposite-pole physical vertex is one-sided reachable, and A_T=T,A_S=S satisfy the exact pole-clique barriers PM.15-PM.16.         (PM.17)

This is an exhaustive one-sided mobility quotient for the G24 Hall program. It does not prove deficiency two. The fresh-pole branch may continue through many minimum covers unless a finite global objective is imposed, the singleton branch still needs a consumer, and the stationary barrier must be contradicted or combined with a two-sided augmentation. The gain is that a genuinely immobile exact-three-pole kernel is supported on only the six physical poles and the six pole-internal barrier edges.

R24 and R5 are not used.

## Exact Phi calculus and the lower/upper/active remainder trichotomy

Let K_n, n even, have ordered 1-factorization M_1<...<M_{n-1}. Let F be a spanning increasing cover by c paths, oriented increasingly. Put L(v)=0 at a source and otherwise the color of its incoming F-edge; put U(v)=n at a terminal and otherwise the color of its outgoing F-edge. Thus L(v)<U(v). Define

    Phi(F)=sum_{sources s} U(s) - sum_{terminals t} L(t).

A singleton x has L(x)=0,U(x)=n and contributes n to Phi. A nontrivial component with first color f and last color ell contributes f-ell.

SINGLETON BOOKKEEPING. A minimum-component cover has at most one singleton, since two singleton components can be replaced by their dimer. If n is even and a c-component cover has exactly one singleton x, then some other component has order at least three: otherwise the total order would be 1+2(c-1), odd. If P=(v_0,...,v_r), r>=2, is such a component, then replacing {x},P by the dimer (x,v_0) and the inherited suffix (v_1,...,v_r) gives a singleton-free c-component cover. This shows that singleton-free minimum covers exist, but it does not justify restricting a global Phi maximum to them: the singleton contributes n and the normalization can lower Phi.

EXACT TERMINAL-ROTATION CHANGE. Let x be a current terminal, let v be a nonsource in a different component, and write p=pred(v), b=L(v)=color(pv), r=color(xv). Suppose

    L(x)<r<=b.

Deleting p->v and adding x->v is the elementary source-preserving terminal rotation from the lower threshold graph. It keeps c components and replaces terminal x by p. Its exact Phi change is

    Delta^- = L(x)-L(p)
              + 1_{x singleton}(r-n)
              + 1_{p source}(n-b)
              + 1_{v terminal}(b-r).

Proof: the terminal contribution changes by +L(x)-L(p), with L(p)=0 when p is a source. If x was singleton, its source first-edge value changes from n to r. If p was a source, cutting p->v makes p singleton and changes its source value from b to n. If v was the old terminal of its component, its incoming terminal label changes from b to r, adding b-r. No other source or terminal datum changes.

In particular, when x is singleton, every such elementary terminal rotation has Delta^-<=0; equality occurs only when the target component is a dimer. When x is non-singleton and p is a source while v is not terminal, Delta^-=L(x)+n-b>0. Thus a global Phi-maximal cover forbids that boundary rotation.

EXACT SOURCE-ROTATION CHANGE. Dually, let y be a current source, let u be a nonterminal in a different component, write q=succ(u), b=U(u)=color(uq), a=U(y), and r=color(uy). Suppose

    b<=r<a.

Deleting u->q and adding u->y is the elementary terminal-preserving source rotation from the upper threshold graph. It replaces source y by q and has exact change

    Delta^+ = U(q)-U(y)
              - 1_{y singleton} r
              + 1_{q terminal} b
              + 1_{u source}(r-b).

The terms have the dual meanings: if y was singleton it acquires incoming edge r, changing its terminal contribution by -r; if q was terminal it becomes singleton, changing its terminal label from b to 0; if u was a source, its first selected edge changes from b to r. Again no other endpoint datum changes. For singleton y one always has Delta^+<=0, with equality only against a dimer. If y is non-singleton and q is terminal while u is not a source, then Delta^+=n-U(y)+b>0, so a Phi maximum forbids that boundary rotation.

INTERVAL-COMPATIBLE CLASSIFICATION. Let u->v have color t and satisfy the broad interval condition

    L(u)<t<U(v).

Then exactly one of the following descriptions applies, except that the first two may overlap on a selected/current boundary edge:

(LOWER) t<=L(v). Then u_out v_in belongs to the lower-cut graph B^- defined by cuts immediately after incoming labels.

(UPPER) U(u)<=t. Then u_out v_in belongs to the upper-cut graph B^+ defined by cuts immediately before outgoing labels.

(REMAINDER) t>L(v) and t<U(u). Then

    L(u)<t<U(u),   L(v)<t<U(v),

so both u and v are active at round t. A current path component has at most one active vertex in a fixed round, hence u and v lie in different current components. This two-active remainder is precisely the part of the broad interval relation not certified by either one-sided threshold graph.

The broad interval graph is not itself a safe matching object: changing both incidences of one original vertex can reverse the two new labels. The lower and upper pieces are safe separately by the one-threshold theorem; the two-active remainder must be handled by a simultaneous rotation or cooperative splice argument.

## Phi as internal waiting and parity-forced one-sided edges

Let K_n, n even, have ordered 1-factorization M_1<...<M_{n-1}, and let F be a spanning increasing cover by c paths. Use L(v)=0 at a source, U(v)=n at a terminal, and otherwise the incoming/outgoing matching colors. Let sigma be the number of singleton components. A minimum-component cover has sigma in {0,1}.

PHI AS TOTAL INTERNAL WAITING. For round t, call a component internally active when its unique active vertex v satisfies L(v)<t<U(v) and v is neither the source nor the terminal of its component. Let I_t be the number of internally active components. Then

    Phi(F)=2c-n + sigma(n-1) - sum_{t=1}^{n-1} I_t.                (1)

Proof. A nontrivial component with edge colors e_1<...<e_r contributes e_1-e_r to Phi. Its internal-active incidences occur precisely in the skipped integer rounds strictly between consecutive used colors, so their number is

    sum_{i=1}^{r-1}(e_{i+1}-e_i-1)
      = e_r-e_1-(r-1).

Summing over all nontrivial components, the total number of selected cover edges is n-c, while the number of nontrivial components is c-sigma. Hence

    sum_t I_t
      = -(Phi-sigma n) - [(n-c)-(c-sigma)]
      = -Phi + sigma n - n + 2c - sigma,

which rearranges to (1). Thus, with c and sigma fixed, maximizing Phi is exactly minimizing total internal waiting.

A second equivalent form is useful when sigma=0. If component i has first and last colors f_i,ell_i, then its span contains ell_i-f_i+1 rounds and

    -Phi = sum_i(ell_i-f_i).

At each round t let m_t be the number of component color-spans containing t. Since a span contains t either through a selected color-t edge or through one internal active vertex,

    m_t=d_t+I_t,

where d_t is the number of selected F-edges in M_t.

STRICT TEMPORAL STATE PARTITION. Fix a round t and remove from M_t the d_t selected cover edges and their 2d_t endpoints. Every remaining vertex is in exactly one of three strict states relative to F:

    P_t-state: U(v)<t   (strict past),
    A_t-state: L(v)<t<U(v)   (active),
    Q_t-state: L(v)>t   (strict future).

The class sizes are determined only by the multiplicities d_s:

    P_t = sum_{s<t} d_s,
    A_t = c-d_t,
    Q_t = sum_{s>t} d_s.                                      (2)

Indeed every selected edge of color s<t contributes exactly its head/tail history so that one vertex has already departed by t; equivalently, among the n-c selected path edges, exactly sum_{s<t}d_s tails lie strictly in the past and sum_{s>t}d_s heads lie strictly in the future, while each component not using color t contributes one active vertex. The identity P_t+A_t+Q_t=n-2d_t follows.

Every residual M_t-edge joining two different state classes is a noncurrent interval-compatible edge belonging to at least one safe one-sided threshold relation:

- past--future: orient past->future; it belongs to both lower and upper pieces;
- past--active: orient past->active; it belongs to the upper piece;
- active--future: orient active->future; it belongs to the lower piece.

An active--active edge is exactly the two-active remainder. Past--past and future--future edges are not interval-compatible.

PARITY FORCING. The residual edges of M_t form a perfect matching on the P_t-,A_t-,Q_t-state vertices. If at least two of the three class sizes are odd, no perfect matching can stay entirely within the three classes, so M_t contains a noncurrent cross-state edge and therefore a noncurrent lower/upper-safe edge. Since P_t+A_t+Q_t is even, the number of odd classes is either zero or two. Consequently a round can avoid this parity-forced safe edge only if P_t,A_t,Q_t are all even.

Writing p_t=sum_{s<t}d_s, this all-even condition is equivalent to

    p_t even  and  d_t congruent c (mod 2),                    (3)

because A_t=c-d_t and Q_t=(n-c)-p_t-d_t, with n even.

ODD-c CONSEQUENCE. Assume c is odd and let r be the number of rounds with d_t odd. Since sum_t d_t=n-c is odd, r is odd. Among the odd-d_t rounds, the prefix parity p_t alternates: before the first odd round it is even, before the second it is odd, and so on. Hence exactly (r+1)/2 odd-d_t rounds satisfy the all-even escape condition (3); every even-d_t round is parity-forced. Therefore the number F_safe of rounds containing a noncurrent one-sided-safe edge satisfies

    F_safe >= (n-1-r) + (r-1)/2
           = n-1-(r+1)/2.

Because each odd-d_t round contributes at least one selected edge, r<=sum_t d_t=n-c. Thus

    F_safe >= (n+c-3)/2.                                      (4)

For c=3 this gives at least n/2 rounds with a noncurrent lower/upper-safe edge. No claim is made here that these safe edges lie in one simultaneously realizable rotation closure; that is the remaining global problem. For even c the parity argument alone can be silent, for example when every d_t is even.

## Two-active remainder edges admit a cooperative suffix switch or an extreme diagonal

Let F be a spanning increasing path cover in an edge-ordered complete graph; in the ordered-1-factorization application all labels below are matching-block colors. Let u and v lie on distinct F-components and suppose their joining edge has label t with

    L(u)<t<U(u),    L(v)<t<U(v).

Thus u and v are simultaneously active at t. Assume u is nonterminal and v is nonsource. Put

    q=succ_F(u),   p=pred_F(v),
    a=U(u)=lambda(uq),   b=L(v)=lambda(pv),
    s=lambda(pq).

If

    L(p)<s<U(q),                                              (1)

then delete the two old path edges u->q and p->v and add

    u->v   and   p->q.                                        (2)

This produces another spanning increasing cover with the same number of components.

Proof. Write the two old components as

    A=A^- u q A^+,
    B=B^- p v B^+,

where the displayed boundary pieces may degenerate to single vertices but q and p exist by hypothesis. After (2), use the two sequences

    A^- u v B^+,
    B^- p q A^+.

They are vertex-disjoint and together use exactly the old vertices of A union B. At the first new seam, the preceding selected label is L(u)<t and the following selected label is U(v)>t. At the second new seam, (1) is exactly the pair of required inequalities L(p)<s<U(q). Every other adjacency is inherited. Hence both new sequences are increasing. Two old edges were replaced by two new edges, so the component count is unchanged. The source set and terminal set are unchanged as vertex sets, although the first or last selected colors can change when a cut is adjacent to an endpoint.

The exact Phi change is

    Delta Phi = 1_{u source}(t-a)
                + 1_{p source}(s-b)
                + 1_{v terminal}(b-t)
                + 1_{q terminal}(a-s).                        (3)

Indeed these are precisely the possible changes to the first selected edge at the two preserved sources and the last selected edge at the two preserved terminals. In particular, if u and p are not sources and v and q are not terminals, then Delta Phi=0. Thus every fully internal two-active switch is Phi-neutral and may be included in a Phi-maximal neutral rotation closure.

If (1) fails, totality of the edge order gives the exact obstruction

    s<=L(p)  or  s>=U(q).                                     (4)

Hence the companion diagonal p q lies completely before the predecessor p becomes available, or completely after the successor q ceases to be available. We call these the early-diagonal and late-diagonal obstructions.

There is a symmetric candidate obtained by orienting the remainder edge as v->u. If v is nonterminal and u nonsource, put q'=succ(v), p'=pred(u). The same theorem applies with companion diagonal p'q'. Therefore a two-active remainder edge is locally non-switchable in both orientations only when each existing companion diagonal is forced to one of its two extreme sides.

This theorem is a physical two-component splice, not a matching shortcut. It does not assert that every two-active remainder edge is switchable: ordered 1-factorizations can realize double extreme-diagonal obstructions. The remaining global problem is to show that a minimum-component Phi-maximal cover cannot keep all compulsory remainder edges trapped in such obstructions throughout the legitimate one-sided and neutral-switch rotation closures.

## Lexicographic color minimality sharpens internal remainder barriers

Let F be a spanning increasing cover in an ordered 1-factorization. First minimize its number c of components, then maximize Phi, and among all covers with those two optimal values choose F so that the selected-color multiplicity vector

    d(F)=(d_1,...,d_{n-1})

is lexicographically minimum, where d_t is the number of F-edges in matching block M_t.

Let u and v be simultaneously active internal vertices on distinct components at the color

    t=color(uv),

and orient the remainder edge as u->v. Assume the cut positions are fully internal in the sense that u is not a source, q=succ(u) is not a terminal, p=pred(v) is not a source, and v is not a terminal. Put

    a=U(u)=color(uq),
    b=L(v)=color(pv),
    s=color(pq).

Then

    b<t<a.

If L(p)<s<U(q), the cooperative two-active suffix switch from section ordered-factorization-two-active-switch is physically valid and, because all four cut positions are internal, has Delta Phi=0. It removes selected colors a and b and adds selected colors t and s.

Suppose in addition that s>b. No selected-color multiplicity below b changes, while d_b decreases by one: neither new color equals b, because t>b and s>b, and a>b is the other removed color. Therefore the new cover has the same component count and the same Phi but a lexicographically smaller color-multiplicity vector, contradicting the choice of F.

Consequently, if the companion diagonal is interval-compatible, it must satisfy s<b. If it is not interval-compatible, the exact obstruction from the two-active switch theorem is s<=L(p) or s>=U(q); the first alternative also implies s<b because L(p)<b. Thus every fully internal oriented remainder edge satisfies the canonical dichotomy

    color(pred(v),succ(u)) < L(v)
        or
    color(pred(v),succ(u)) >= U(succ(u)).                       (1)

The reverse orientation v->u gives the symmetric dichotomy

    color(pred(u),succ(v)) < L(u)
        or
    color(pred(u),succ(v)) >= U(succ(v)).                       (2)

This is stronger than the raw early/late diagonal obstruction: lexicographic color minimality rules out the entire compatible interval from L(v) upward. It does not claim that the early alternative is itself switchable. If the early diagonal color lies strictly between L(pred(v)) and L(v), it is a legitimate lower one-sided edge from pred(v) toward succ(u); if it lies at or before L(pred(v)), the obstruction has propagated one step farther toward the source side. The late alternative is the corresponding upper-side barrier. These propagated barriers are the next object for the simultaneous rotation-closure argument.

## Existential longest-complement conjecture and minimal-counterexample three-rail reduction

Proposed theorem (not accepted). Every finite edge-ordered complete graph G has some globally longest increasing path P such that the induced edge-ordered graph G-V(P) has an increasing Hamilton path; the empty complement is allowed. This would imply R888 immediately.

Minimal-counterexample reduction. Suppose the proposed theorem is false and let G be a counterexample of minimum order n. Let P be any globally longest increasing path of G and put H=G-V(P). Because G is a counterexample, H is not Hamiltonian: otherwise this P itself witnesses the theorem.

But H has fewer than n vertices, so the proposed theorem holds for H by minimality. Hence H has a globally longest increasing path A whose complement in H is Hamiltonian; call one such complementary Hamilton path B. Therefore H is covered by at most two increasing paths. Since H is not Hamiltonian, its increasing path-cover number is exactly two.

Thus in a smallest counterexample the complement of every globally longest P has pc_inc(H)=2. Choosing A as above gives a literal partition

    V(G)=V(P) disjoint-union V(A) disjoint-union V(B)

into three increasing paths, where P is globally longest in G, A is globally longest in H=G-P, and B is Hamilton on H-A. In particular

    |P| >= |A| >= |B| >= 1.

So the existential longest-complement theorem reduces inductively to ruling out this hierarchical three-rail configuration. No reduction from deleting vertices of an ordered 1-factorization is involved; this is a statement for arbitrary edge-ordered complete graphs.

Exact finite fence. Pending R947/P1019 shows why the existential quantifier is essential: an explicit matching-layer K_16 has a globally longest 12-vertex path with non-Hamiltonian four-vertex complement, but a one-vertex-swapped globally longest path has Hamiltonian complement. Thus a smallest counterexample must obstruct every globally longest support, not merely contain one bad support.

## Minimum R888 counterexamples have critical port universes; trimer rails force a degree-four port

Let G be a minimum-order counterexample to R888. By accepted R959, for every vertex z, every exact two-path cover of G-z has both rails of order at least three; in particular one may choose a complete singleton-deletion cover family and apply the current accepted rail-incidence parent R965 (strengthening R926). Retain its root and port universes Omega_P.

PORT-UNIVERSE CRITICALITY. Let P be a root vertex and let x=PQ be any incident physical edge. The P-side rail of C_x is exactly Omega_P-{x}, hence Omega_P-{x} has an increasing Hamilton path. On the other hand Omega_P itself is non-Hamiltonian. Indeed, if Omega_P had an increasing Hamilton path, then together with the Q-side rail Omega_Q-{x} of C_x it would give two disjoint increasing paths whose vertex sets cover V(G), because Omega_P union Omega_Q=V(G) and Omega_P intersect Omega_Q={x}. This contradicts pc_inc(G)>2. Thus every port universe is non-Hamiltonian while deletion of every physical vertex incident with that port leaves a Hamiltonian induced subgraph.

TRIMER-RAIL SATURATION. Suppose for some z a chosen exact cover has a three-vertex rail A={a,b,c} and opposite Hamilton rail B. Put X=A union {z}. Every edge-ordered triangle has an increasing Hamilton path: among its three edge labels, the smallest and largest edges share a vertex, and traversing smallest then largest gives an increasing two-edge path. Hence for every r in X, the triangle X-{r} is Hamiltonian. Therefore G-r has the exact two-cover (X-{r})|B, and we may choose these four covers simultaneously for r in X.

For r,z in X these support partitions agree after deleting r and z, because both restrict to (X-{r,z})|B. Thus all four physical vertices in X are pairwise compatible through the same rail port. In the rail-incidence root they are exactly the four edges incident with one root vertex P, and Omega_P=X: using C_z, its P-side support is X-{z}, so adjoining z gives X; any further physical edge incident with P would itself belong to Omega_P=X, so there are no others. Consequently deg(P)=4. By accepted R965 the entire component of this saturated degree-four port has depth at most two, with every same-component external label represented by a unique one-for-one exchange behind one spoke.

The opposite rail B is literally the same support in all four covers. For every r in X, B union {r} is non-Hamiltonian: otherwise a Hamilton path on B union {r} together with the Hamilton triangle X-{r} would form a spanning two-cover of G. Also X itself is non-Hamiltonian by the preceding port-universe argument. This is accepted R962's critical four-set setup.

GLOBAL HAMILTON-DELETION EXCHANGE BLOCKING. Accepted R967 strengthens the earlier root-dependent R964 conclusion. Let b in B be any vertex such that B-b is Hamiltonian. Then for every x in X, the exchanged support B-b+x is non-Hamiltonian. Otherwise B-b+x would be Hamiltonian. Its complementary four-set X-x+b must then be non-Hamiltonian, else those two supports already two-cover G. But X is non-Hamiltonian too, and X and X-x+b share the triangle X-x. Accepted R963 therefore Hamiltonizes their union X+b. Together with Hamilton B-b this gives the forbidden spanning two-cover (X+b)|(B-b). Thus every Hamilton-deletable b in B has all four one-for-one exchanges blocked, with no root-component hypothesis.

In particular, each endpoint of every Hamilton order on B is Hamilton-deletable, so both physical endpoints of every such order carry four simultaneous blocked exchanges. R967 does not assert that every interior vertex of B is Hamilton-deletable, and it does not by itself synchronize the different Hamilton orders.

UNIVERSAL SINGLETON MIGRATION ON A TRIMER. More generally, whenever a displayed cover contains an increasing trimer (x,y,w) and a singleton {z}, exactly one of the two sequences (x,z,w) and (w,z,x) is increasing, because they use the same two edges xz and zw in opposite orders and one of lambda(xz)<lambda(zw) or lambda(zw)<lambda(xz) holds. Hence one may replace (x,y,w)|{z} by an increasing trimer on {x,z,w} together with singleton {y}, preserving all other cover components. This is a component-preserving rotation, not by itself an absorption theorem.

The trimer branch therefore has a precise current shell: one critical non-Hamiltonian four-set X; one fixed Hamilton rail B blocked from all one-vertex extensions by X; a saturated depth-two R965 port component; and, for every Hamilton-deletable b of B, four additional blocked exchanged supports B-b+x. The remaining problem is to consume these simultaneous failures through total edge order, threshold/rotation structure, or cooperative multi-cut surgery. Further root classification alone is no longer the main bottleneck.

TWO-ENDED GATE-TO-ONE-HOLE REDUCTION. Accepted R969 strengthens the long opposite-rail case without introducing new local taxonomy. Choose any Hamilton order B=(q_0,...,q_m). If |B|>=4, then X is the transitive matching-height bad four-cell. The endpoint five-sets X+q_0 and X+q_m are P5-free because B-q_0 and B-q_m are Hamiltonian complements. Moreover B+x is non-Hamiltonian for every x in X, so prepending or appending x to B must fail; in edge-order language this gives the universal reverse endpoint stars (q_1,q_0,x) and (x,q_m,q_{m-1}). These are exactly the hypotheses of accepted R541, so the two endpoints carry one global ALIGNED/CROSSED middle-gate polarity and its associated one-witness non-Hamiltonicity statements.

Accepted R582 then supplies some x in X and an endpoint-favorable Hamilton P5 K_x on (X-x)+{q_0,q_m}. Put D=X-x. The residue G-D has the literal two-cover B|{x}, and K_x has exactly the support D+{q_0,q_m} required by accepted R540. Endpoint favorability makes one of the q_0/q_m cut ledgers contain at most one possible hole; R540 guarantees the ledger is nonempty, hence it contains exactly one bad seam and its exact reverse mate. Thus every surviving trimer fiber with |B|>=4 now comes with a literal spanning two-path proposal having one labelled seam hole, plus retained R541 polarity and R967 exchange blocking. The seam is not automatically repaired.

The only trimer case outside this long-rail reduction is |B|=3, the order-seven trimer/trimer residue. R718 remains the fence against replacing the long-rail consumer by generic two-fifth-vertex gate propagation: two P5-free fifth vertices over one transitive four-cell can remain P6-free with differing middle-gate bits under additional universal-star data.


EXACT NORMALIZED ONE-HOLE COORDINATES. The finite proof P660 of R582 gives more information than the abstract endpoint-favorable conclusion when inserted into the R540 ledger. Normalize the transitive cell as in R582, with the left outgoing middle edge {b,z} and write L=q_0, R=q_m.

In the CROSSED gate case P660's final favorable path is
  K=(z,c,a,L,R),
omitting b. Use the R endpoint cut in R540. Since R is in K-position 4, the only possible hole is (a,L,b). Therefore (a,L,b) is bad and its exact reverse (b,L,a) is tight. The resulting literal proposal is (z,c,a,L,b) together with the B-suffix (q_1,...,q_m).

In the ALIGNED gate case P660's final favorable path is
  K=(b,a,R,L,c),
omitting z. Use the L endpoint cut in R540. Since L is in K-position 3, the only possible hole is (R,L,q_1). Therefore (R,L,q_1) is bad and (q_1,L,R) is tight. The literal proposal is the K-prefix through L followed by the B-interior, together with the residual dimer (z,c).

These coordinates are direct specializations of accepted P660 and P616; they are recorded here to prevent future consumers from treating the R969 seam as anonymous. They do not themselves close either gate branch. In particular, R958 requires additional cross-cut interval inequalities not supplied automatically by these turns.


## The trimer shell reproduces the universal first-inward portal geometry

Retain the accepted R962/R967 trimer setup and a Hamilton order B=(q_0,...,q_m), m>=3. Write L=q_0,u=q_1,v=q_2,d=q_{m-2},s=q_{m-1},R=q_m. The endpoint-exchange blocking of R967 immediately propagates one step inward, independently of the R541 ALIGNED/CROSSED gate split.

UNIVERSAL FIRST-INWARD STARS FROM R967. For x in X, endpoint L is Hamilton-deletable and R967 makes (B-L)+x non-Hamiltonian. If xq_1<q_1q_2, then (x,q_1,...,q_m) Hamiltonizes that support, contradiction. Hence q_1q_2<q_1x, equivalently (v,u,x) is tight for every x. Dually R967 at R gives xq_{m-1}<q_{m-2}q_{m-1}, equivalently (x,s,d) tight for every x. Thus every Hamilton order of B carries two four-witness first-inward stars.

PURE PATH AND SIGN GEOMETRY. Test the middle turn (u,x,s). A forward winner gives the tight P4 (v,u,x,s); when m>=5 the distinct last coordinate d extends it to P5 (v,u,x,s,d). At m=4 one has v=d=q_2, so only the P4 is valid. If every forward middle loses, R3 gives (s,x,u) for all x, and every unordered X-pair gives a cross-depth P4 through s,u. Also (v,u) is tail-signed and (s,d) head-signed by any chosen common x. R425/R547 therefore give the static opposite-sign singleton pair {u},{s} with all four X witness certificates. The old R775 statement overclaimed the m=4 P5; pending R976 is its explicit correction, and D20 records the hinge issue.

SAME-FRAME CAPTURE PORTALS. Fix any exact two-cover T_L of G-{u,v}; minimum-order R888 induction supplies one. The old Q turn (u,v,q_3) signs S_L=(u,v). For each x, the carrier K_x=(v,u,x) and R508 force a selected x-to-exterior crossing in the same T_L. At most two of the four crossings can use q_3 as their exterior endpoint because a vertex has selected degree at most two in a two-path forest. Hence at least two distinct X anchors have witness-avoiding crossings, and local R527 may capture each of those anchors in that same deletion frame. The right pair deletion G-{d,s} gives the exact dual. Therefore the two fixed portal sets A_L,A_R each have size at least two. Set-theoretically, either A_L and A_R meet at a common physical X anchor, or they are complementary two-sets and hence exactly one of the three perfect-matching layers of the transitive bad K4 X. This common-versus-matching-split compression is safe; the stronger historical R757 attempt to couple coincident actualized supports is not, because its tested orientations reverse on the same unordered support.

CRITICAL FIVE-CELL SIBLING FIBERS. For either Hamilton endpoint b in {L,R}, X+b is non-Hamiltonian because B-b is Hamiltonian. If (X-x)+b were also non-Hamiltonian, accepted R963 applied to X and (X-x)+b would Hamiltonize X+b. Hence (X-x)+b is Hamiltonian for every x. In particular, after deleting {u,x}, any Hamilton P4 P_x^L on (X-x)+L together with Q[2,m] is an exact mixed-sibling two-cover. This replaces the R24-specific shallow sibling fibers used in the old first-inward program.

PENDING GENERALIZED CONSUMERS. R974/P1045 packages the corrected literal-star path/sign geometry and the two same-frame capture portals per side without an R24 hypothesis. R977/P1048 goes one step farther: for two left good anchors x,y, tight (u,x,y) gives P4 (v,u,x,y) and a second capture of y in the mixed sibling G-{u,x}; tight (y,v,u) independently gives P4 (y,v,u,x); joint failure forces the exact R518/R516 no-P4 four-cell on {v,u,x,y}. The right side is dual. Both revisions are pending independent review and are not current premises.

PENDING FLOOR STRENGTHENING. R972/P1043 monotonically merges R969 with the verified interior-barrier argument: every R895 beta_B(x) is strictly interior and |B|>=5. Until R972 is independently reviewed, the accepted current theorem remains R969; the first-inward derivation above is already valid whenever |B|>=4.

LIVE CONSUMER FRONTIER. The trimer problem is no longer a search for more endpoint gate types. One must consume one of the concrete simultaneous objects now available: a common two-sided captured X anchor; a named matching-layer split of the portal sets; the R977 mixed-sibling double-capture/P4/no-P4 trigger; the R969 normalized ALIGNED/CROSSED one-hole seam; or the four interior R895 barriers if R972 is accepted. The orientation-invalid coincident-support argument of R757 must not be reused.

## Stationary three-pole mobility isolates every terminal root in B^- and every source root in B^+

### 1. Stationary lower reachability
Retain the STATIONARY BARRIER branch of SV66184 for a minimum non-singleton three-cover F. Thus the source and terminal sets S,T have order three and, in the lower one-sided graph B^-_F, the full physical alternating-reachable set from the three unmatched terminal left roots is exactly

  R_T=T.                                                    (RI.1)

Let X be the reachable left-copy set and Y=N(X) the reachable right-copy set.

Fix a terminal t in T. Its left copy t_out is one of the alternating roots, hence belongs to X. We claim

  deg_{B^-}(t_out)=0.                                       (RI.2)

Suppose instead that t_out v_in is an edge of B^-.

If v_in were unmatched by the selected F matching, then v would be a source of F and the one-edge alternating walk from the unmatched left root t_out to the unmatched right root v_in would augment the matching. That would give a matching of size n-2 in B^- and, by R936, a spanning two-cover, impossible in a counterexample.

Therefore v_in is matched. Let p_out v_in be its selected matching edge, so p->v is a selected F adjacency. Alternating reachability traverses t_out v_in from left to right and then the matching edge backward from v_in to p_out. Hence p_out belongs to X, so p belongs to R_T.

But p has the selected outgoing edge p->v and therefore is not a terminal of F. Thus p is not in T, contradicting RI.1. This proves RI.2.

By the definition of B^- we obtain the global terminal-root exclusion

  NOT( L(t)<lambda(tv)<=L(v) )                              (RI.3)

for every terminal t and every v != t.

Equivalently, whenever

  lambda(tv)>L(t),                                          (RI.4)

one necessarily has

  lambda(tv)>L(v).                                          (RI.5)

For a source v the conclusion is automatic because L(v)=-infinity; for every nonsource it is a genuine boundary dominance relation.

### 2. Stationary upper reachability
The source dual is exact. In B^+_F start alternating reachability from the three unmatched source right roots. In the stationary branch the full physical reachable set is

  R_S=S.                                                    (RI.6)

Fix s in S. Then its right copy s_in has no B^+ neighbor:

  deg_{B^+}(s_in)=0.                                        (RI.7)

Indeed if u_out s_in were a B^+ edge and u_out were unmatched, u would be a terminal and the edge would be an augmenting path from unmatched right source root s_in to unmatched left terminal root u_out. If u_out were matched, alternating reachability would traverse its selected matching edge to a right copy v_in whose physical vertex v is not a source, contradicting R_S=S.

Therefore

  NOT( U(u)<=lambda(us)<U(s) )                              (RI.8)

for every source s and every u != s. Equivalently, whenever

  lambda(us)<U(s),                                          (RI.9)

one necessarily has

  lambda(us)<U(u).                                          (RI.10)

### 3. Global endpoint-dominance normal form
The stationary exact-three-pole kernel therefore satisfies simultaneous global inequalities

  terminal t:  lambda(tv)<=L(t) OR lambda(tv)>L(v),         (RI.11)
  source s:    lambda(us)<U(u) OR lambda(us)>=U(s),         (RI.12)

for every physical partner vertex.

The source/source and terminal/terminal outside-interval clique barriers of SV66184 are immediate finite shadows of this stronger root-isolation statement, but RI.11-RI.12 also constrain all internal vertices of the three rails.

These relations identify exactly where a two-sided augmentation must fail. For example, if a terminal t and an internal vertex v satisfy the lower broad seam inequality L(t)<lambda(tv), then stationarity forces lambda(tv)>L(v); the only remaining obstruction to inserting t before v is the upper boundary U(v). Dually, if an internal u and source s satisfy lambda(us)<U(s), stationarity forces lambda(us)<U(u), leaving only the lower boundary L(u). This is the natural interface with the cooperative splice theorem R956 and the isolated-gain endpoint blockers R995.

No assertion is made that suitable simultaneous broad seams must exist. The section is a structural sharpening of the stationary branch, not a deficiency-two proof. R24 and R5 are not used.