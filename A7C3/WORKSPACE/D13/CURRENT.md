# D13 — Absorber crossing, transition pressure, and unique-transition rigidity

Complete recompletion/absorber development: crossing existence, cut-indexed exchange, unique-transition words, pure-rail seam coupling, block pressure, anti-aligned bridge escape, current-trimer amplification, Hamilton-absorber wrap pressure, finite CS cells, and repaired right-split rigidity.

## Scope, notation, and status discipline

Let H be a finite tight-path system. A literal k-cover means k vertex-disjoint tight paths whose supports partition the indicated vertex set. For a partition W=S sqcup C and a chosen cover T of W, a selected S|C transition is an adjacent ordered state of a T-rail whose endpoints lie in different classes. A maximal C-block is a maximal contiguous C-subpath of a T-rail.

The development separates graph-intrinsic facts from facts about one selected cover. R508, R509, R511, R560, R567, R566, R570, R573 and the specialized consumers below are exact statements about the cover(s) named in their hypotheses. None identifies representatives chosen in different deletion residues. None manufactures a payment lineage. A tight P4 or witness packet created by a splice is a labelled output, not automatically a smaller cover.

Status ledger. R508/P523, R509/P524, R511/P526, R512/P539, R513/P528, R539/P615, R540/P616, R550/P628, R560/P651, R567/P642, R566/P641, R568/P643, R570/P645, R573/P648 and R833/P907 are accepted exact routes. R510/P525 is rejected and invalid as stated. R512 also has historical proof P527, which is stale/invalid through R297; P539 is the clean accepted replacement. The rejected/stale material is retained below only to localize what failed and what survived.

## Absorbable blocks force a recompletion crossing

R508 is the parent crossing theorem. Let D be a nonempty proper vertex set, W=V(H)\D, and let S be a nonempty proper subset of W. Suppose Q is a tight path whose support is exactly D union S and pc(H)>2. Then every literal two-cover T=T_1 sqcup T_2 of H-D selects an adjacency crossing S | C, where C=W\S.

Proof. Assume T selects no such crossing. If one rail T_i contained vertices from both S and C, traverse it from one end to the other and take the first adjacent pair at which membership changes. That adjacent ordered state is a selected S|C crossing, contradiction. Thus each T_i lies wholly in one class. Both S and C are nonempty and the two nonempty rails span W, so after relabelling V(T_1)=S and V(T_2)=C. Now Q and T_2 are disjoint tight paths and their supports partition V(H), giving a literal spanning two-cover of H. This contradicts pc(H)>2.

The strength of the lemma is its lack of geometry: it uses only literal path supports and the cover-number obstruction. Its conclusion is correspondingly modest. It forces at least one selected crossing in each named cover, but does not choose the crossing, synchronize crossings between covers, or control how many complement blocks occur.

## Cut-indexed outward-transition exchange and complete seam ledger

Keep the R508 packet and write Q=(q_0,...,q_m), C=W\S. R509 first proves that T has at least two maximal C-blocks. If there were exactly one block B, then B contains every vertex of C, and Q together with B is a literal spanning two-cover of H.

Now assume the C-blocks are exactly B=(b_0,...,b_r) and K=(c_0,...,c_s). Fix a cut -1 <= i <= m for which the selected T-incidences point outward from the two Q pieces: q_i b_0 when i>=0, and c_s q_{i+1} when i<m. Put L_i=Q[0,i] and R_i=Q[i+1,m], omitting an empty side. Define
U_i=L_i+B,   V_i=K+R_i.
Their supports are disjoint and span H.

Every turn internal to Q,B,K is certified. At L_i|B, the T-order q_i,b_0,b_1 certifies the second junction turn when it exists; the only possible uncertified turn is
alpha_i=(q_{i-1},q_i,b_0), present exactly for i>=1.
At K|R_i, the T-order c_{s-1},c_s,q_{i+1} certifies the first junction turn when it exists; the only possible uncertified turn is
beta_i=(c_s,q_{i+1},q_{i+2}), present exactly for i<=m-2.
Singleton blocks and endpoint cuts merely delete nonexistent triples. Therefore the complete hole set is
E_i={alpha_i : i>=1} union {beta_i : i<=m-2}.

E_i cannot be empty, because then U_i,V_i would be a spanning two-cover. If |E_i|=1, its unique member is bad and boundary antisymmetry R3 makes its complete reversal tight. If |E_i|=2, the two cannot both be tight, so at least one is bad and at least one physical reverse mate is tight.

This is a literal seam compiler, not a slogan about splicing. Its usefulness comes from the fact that every possible new turn has been enumerated, including endpoint and singleton degeneracies. The retained crossing orientation identifies which outward incidence is supplied, and its S-endpoint identifies the cut. R509 does not assert that the second outward incidence exists; that missing partner is precisely what becomes visible in the unique-transition obstruction.

## The unique-transition word and the sharp three-hole obstruction

Assume an R508 packet and an exact two-cover T with exactly one selected S|C transition. Since R508 forces at least one transition in every exact cover, this is globally transition-minimal among those covers. Splitting two nonempty rails at the unique transition produces three monochromatic blocks. R509 says at least two are C-blocks. Because S and C are both nonempty, the block types are exactly C,C,S. Hence one rail is pure C, call it K=(c_0,...,c_s), and the other is mixed, either A B (SC) or B A (CS), with A the unique S-block and B=(b_0,...,b_r) the other C-block.

SC case. Let q_i be the last S-vertex of A. When i=m the crossing is already an endpoint one-hole R509 cell. For i<m use
U=(q_0,...,q_i,b_0,...,b_r),
V=(c_0,...,c_s,q_{i+1},...,q_m).
The complete uncertified set is
E_SC = {(q_{i-1},q_i,b_0) if i>=1}
       union {(c_{s-1},c_s,q_{i+1}) if s>=1}
       union {(c_s,q_{i+1},q_{i+2}) if i<=m-2}.
It has three members exactly when s>=1 and 1<=i<=m-2.

CS case. Let q_j be the first S-vertex of A. When j=0 the crossing is the dual endpoint one-hole cell. For j>0 use
U=(q_0,...,q_{j-1},c_0,...,c_s),
V=(b_0,...,b_r,q_j,...,q_m).
The complete uncertified set is
E_CS = {(q_{j-2},q_{j-1},c_0) if j>=2}
       union {(q_{j-1},c_0,c_1) if s>=1}
       union {(b_r,q_j,q_{j+1}) if j<=m-1}.
It has three members exactly when s>=1 and 2<=j<=m-1. In particular j=m is a genuine endpoint degeneration with at most two holes.

Every displayed nonaligned hole set is nonempty and cannot consist entirely of tight turns, or the proposal would be a spanning two-cover. Boundary antisymmetry therefore reverses at least one displayed bad turn. The formal zero-hole cells (m=1,i=0,s=0) and (m=1,j=1,s=0) are impossible for the same literal reason.

Historical correction. Rejected R510/P525 contained essentially the same block count and seam inspection, but asserted that j>0 implied j<=m-1 in the CS branch. The endpoint j=m is possible, so that statement was false. R511/P526 repairs exactly this defect and also states the correct logical fence: tau(T)=1 is a conditional representative. Nothing here proves such a cover exists in the full graph class, and transition minimality alone does not create R509's missing partner crossing.

## Pure-rail seam coupling, reverse P4 substitution, and shallow cells

In a genuine three-hole R511 cell, two holes lie consecutively on the pure-C/Q seam and the third is isolated on the mixed seam. R512 couples the consecutive pair.

For CS set
e_0=(q_{j-2},q_{j-1},c_0), e_1=(q_{j-1},c_0,c_1), g=(b_r,q_j,q_{j+1}).
If e_0 and e_1 are both tight, the natural four-vertex seam is a tight P4 and the unchanged spanning proposal has sole hole g; hence g is bad and reverse(g) is tight. Otherwise choose a bad seam hole, reverse it by R3, and apply the corrected universal four-cell theorem R518 with the fourth seam vertex. In the no-P4 branch R518 certifies the adjacent seam hole, leaving exactly the chosen bad seam hole and g. In the P4 branch the chosen bad natural turn rules out the natural terminal-compatible order, so the P4 is terminal-incompatible. The SC calculation is dual with
f_0=(c_{s-1},c_s,q_{i+1}), f_1=(c_s,q_{i+1},q_{i+2}), h=(q_{i-1},q_i,b_0).
Historical proof P527 attempted this through invalid R297 and is stale; accepted P539 rederives R512 from R518.

R513 resolves the residual case where both consecutive natural seam turns are bad. Write the natural seam as (a,b,c,d). R3 makes (c,b,a) and (d,c,b) tight, exactly the two turns of the reverse order K*=(d,c,b,a), so K* is a literal tight P4. Substitute K* into the spanning proposal and audit only its outer junctions.

CS: a=q_{j-2}, b=q_{j-1}, c=c_0, d=c_1. The reversed first rail has hole set {g} union L_CS(j) union R_CS(s), where
L_CS(2)=empty,
L_CS(3)={(q_0,c_1,c_0)},
L_CS(j>=4)={(q_{j-4},q_{j-3},c_1),(q_{j-3},c_1,c_0)},
and
R_CS(1)=empty,
R_CS(2)={(q_{j-1},q_{j-2},c_2)},
R_CS(s>=3)={(q_{j-1},q_{j-2},c_2),(q_{j-2},c_2,c_3)}.
Thus (j,s)=(2,1) is a one-hole cell, while (2,2) and (3,1) are two-hole cells.

SC: a=c_{s-1}, b=c_s, c=q_{i+1}, d=q_{i+2}. The reversed second rail has holes {h} union L_SC(s) union R_SC(i), with
L_SC(1)=empty,
L_SC(2)={(c_0,q_{i+2},q_{i+1})},
L_SC(s>=3)={(c_{s-3},c_{s-2},q_{i+2}),(c_{s-2},q_{i+2},q_{i+1})},
and
R_SC(i=m-2)=empty,
R_SC(i=m-3)={(c_s,c_{s-1},q_{i+3})},
R_SC(i<=m-4)={(c_s,c_{s-1},q_{i+3}),(c_{s-1},q_{i+3},q_{i+4})}.
So (s,i)=(1,m-2) is one-hole, and (2,m-2),(1,m-3) are two-hole.

All other parameter cells retain the isolated old hole plus at least two explicit outer holes for this exact substitution. This is an irreducibility statement about the displayed move, not a proof that no other move exists. Also, the seam P4 is a spanning-proposal device. Its Q-side vertices can lie in D, so it cannot automatically be substituted back into the deletion cover T.

## Order-free block inequalities and multi-absorber transition pressure

R560 extracts the counting heart from the two-rail normal form. Let pc(H)=p, let V(H)=D sqcup S sqcup C, let T be a literal k-cover of H-D, and suppose D union S has an a-path cover A. Split every T-rail at each selected S|C transition. The resulting maximal C-blocks are disjoint tight paths covering C. If their number is b_C(T), then A together with these blocks is a spanning cover of H by a+b_C(T) paths. Hence
p <= a+b_C(T), so b_C(T) >= p-a.
If a=1 and pc(H)>k, then p>=k+1 and b_C(T)>=k.

If T has exactly one selected transition, splitting k rails there creates exactly k+1 monochromatic blocks. With S,C nonempty, b_S>=1. The preceding bound gives b_C>=k, while b_S+b_C=k+1, so b_S=1 and b_C=k. Therefore exactly one rail is mixed, of type SC or CS, it contains the unique S-block and one C-block, and every other rail is pure C. There is no S-only rail. This is the k-rail parent of the block-word portion of R511.

R567 is the multi-absorber extension. Let W=V(H)\D be partitioned into r>=2 nonempty classes C_1,...,C_r. Let T be a k-cover of H-D, and let t(T) count selected T-adjacencies crossing between classes. For each i suppose H[D union (W\C_i)] has an a_i-path cover. Combining that cover with any cover of H[C_i] shows
pc(H[C_i]) >= p-a_i.
Let b_i(T) be the number of maximal C_i-blocks in T. Those blocks cover H[C_i], so b_i(T)>=pc(H[C_i])>=p-a_i. Splitting all k rails at every cross-class adjacency produces exactly k+t(T) monochromatic blocks, hence
sum_i b_i(T)=k+t(T).
Summing the lower bounds gives the transition-pressure inequality
t(T) >= r p - (a_1+...+a_r) - k.

In the two-class case, if D union S and D union C are both Hamiltonian, a_1=a_2=1 and t>=2p-2-k. Thus in the p=3,k=2 smallest-counterexample regime every such deletion cover has at least two transitions. For three classes with p=3,k=2 and a Hamilton complementary absorber for each class, t>=4.

These are pure path-cover inequalities. They need neither Strong Level-(1) nor antisymmetry. They do not manufacture the absorber covers, identify which class pairs realize the forced transitions, or convert transition pressure into closure.

## A unique crossing inherits the absorber Hamilton boundary fan

R566 turns the unique-transition normal form into labelled witnesses. Let pc(H)>k, let X=H[D union S] be Hamiltonian, and let T be a k-cover of H-D with exactly one S|C transition. R560 writes T as one mixed rail plus k-1 pure C rails.

Suppose the transition is x y with x in S and y in C, so the mixed rail is A B with the unique S-block A ending at x and C-block B beginning at y. Let Q be any Hamilton path of X ending with ordered state (p,x). Replace A by Q, leave B and all pure-C rails in their literal T-orders. The resulting k sequences are disjoint and span H. Every turn is inherited from Q or T except possibly the single splice (p,x,y). If that turn were tight, the sequences would be a literal k-cover of H, contradicting pc(H)>k. Therefore (p,x,y) is bad, and R3 gives (y,x,p) tight.

Since Q was arbitrary, every Hamilton predecessor p of x in X is a tail witness on the same tested crossing dimer (y,x). Two distinct predecessors give a same-oriented two-tail collision, which can be consumed by R523. For the dual transition y x, choose any Hamilton path of X starting (x,p); the only possible hole is (y,x,p), so its reverse (p,x,y) is tight and every Hamilton successor p becomes a head witness on (x,y).

The physical selected crossing is retained throughout. This is stronger information than merely knowing that some witness exists, but it still depends on the actual Hamilton boundary multiplicity of X.

## Unique-transition rigidity and a direct two-rail alternative

R570 combines transition pressure, the boundary fan, and path comparison. In the two-rail unique-transition setting, if the complementary absorber H[D union C] were Hamiltonian as well as X=H[D union S], then R567 with p>=3 and k=2 would force at least two S|C transitions, contradicting tau(T)=1. Thus the complementary side is non-Hamiltonian.

Now suppose the unique transition is x y with x in S. If X has Hamilton paths Q_1,Q_2 ending at x with distinct penultimate vertices p_1,p_2, R566 gives tight turns (y,x,p_1) and (y,x,p_2), a same-support two-tail collision. If Q_1,Q_2 are distinct but share the same penultimate vertex, compare the two Hamilton orders with R435. The Reverse Ear Lemma produces an exact reversal of an old adjacent state, a tight reverse trimer, or a vertex-simple tight cycle. Therefore, in a tau=1 cell in which none of those explicit outputs occurs, there is at most one Hamilton order of X ending at x. Existence is not asserted. The dual statement holds for a y x transition and Hamilton paths beginning at x.

R573 is retained as a useful direct two-rail route with weaker machinery. For a CS crossing x y and a Hamilton Q of X ending (p,x), if (p,x,y) were tight then append to Q the C-block of T starting at y. If T has one C-block this produces a spanning path; if it has two, the other pure-C rail plus the concatenation gives a spanning two-cover. Both contradict pc(H)>2. Thus (p,x,y) is bad and (y,x,p) tight. Distinct Hamilton predecessors again give the R523 collision. The SC case is dual.

R573 is logically subsumed in many applications by R560+R566, but its proof is worth preserving: it needs only the literal two-rail block picture and directly exposes why the joined path count is one or two.

## Port-deficit, endpoint-cut, dimer-seam, and P4-puncture consumers

Several smaller results are genuine interfaces rather than duplicates.

R539 identifies a common extremal port-deficit cell with R511. If |S|=3, a two-cover F has c(F[C])=2 complement fragments and e_F(S)=2 internal S-edges, then the three S-vertices form one contiguous trimer block. The path-forest identity
c(F[C])=e_F(S)+delta_F(S)-1
becomes 2=2+delta-1, hence delta=1. Exactly one selected S|C adjacency occurs, and with two C-components one lies beside the S-block while the other is a pure C rail. Thus the rail word is exactly AB|K or BA|K.

R540 is an endpoint-cut recompletion compiler for a deletion cover R=(r_0,...,r_t) sqcup (x), t>=2, together with a Hamilton absorber K on D union {r_0,r_t}. If r_0=k_i, use U=K[0,i]+R^o and V=(x)+K[i+1,m], where R^o removes the endpoints. The complete hole set is
{(k_{i-1},r_0,r_1) if i>=1} union {(x,k_{i+1},k_{i+2}) if i<=m-2}.
The right-end construction is dual, with holes
{(k_{j-2},k_{j-1},x) if j>=2} union {(r_{t-1},r_t,k_{j+1}) if j<=m-1}.
A zero-hole cell is impossible and a nonempty set cannot be all tight.

R550 and R568 refine the both-bad R513 seam when the pure C rail is a dimer. In CS with s=1, write a=q_{j-2}, b=q_{j-1}, c=c_0, d=c_1. The bad natural order kills (a,b,c,d); the only prefix-(a,b) Hamilton alternative is P_L=(a,b,d,c). If P_L is tight, the rewritten spanning proposal has sole inherited mixed hole g, so reverse(g) is tight. If turn abd is bad, its reverse dba together with inherited cba gives a two-head collision on dimer (b,a); if bdc is bad, cdb is tight. R568 is the exact SC dual: the only suffix-preserving alternative is P_R=(c_1,c_0,q_{i+1},q_{i+2}); if tight, the proposal has sole hole h, otherwise the failed P_R turn reverses. These refinements preserve physical seam labels and do not modify the deletion cover.

R833 is a two-block puncture normal form for a tight P4 K=(x,p,q,y), D={p,q}, S={x,y}, and an exact nontrivial-rail two-cover T of H-D. R508 gives at least two C-blocks. If epsilon records whether xy is a T-edge, deleting x,y from the two-component path forest gives the exact identity
b_T(x,y)=deg_T(x)+deg_T(y)-epsilon.
When b_T=2 and xy is absent, both x,y have degree one. A C->x incidence triggers the endpoint R509 cell and forces the reverse seam (p,x,c); a y->C incidence forces (c,y,q). If neither occurs, x is an outward initial endpoint and y an inward terminal endpoint on nonadjacent rails, the ANTI-ENDS alternative. If xy is present, the degree sum is three. Orientation y->x is a REVERSE-CHORD. For x->y, whichever endpoint has degree two has the additional C incidence in the one-hole direction, forcing X-REVERSE or Y-REVERSE. These alternatives are exhaustive for b_T=2.

## What this development does not prove, and why the failed routes matter

The exchange machinery is deliberately representative-specific.

1. R508 forces a crossing in each named cover, but different covers need not realize the same crossing.
2. R509 compiles a pair of C-blocks only when the required outward incidences are physically present. A transition-minimal cover need not provide the missing partner.
3. R511 classifies a hypothetical tau=1 cover. It does not establish realizability of such a packet.
4. R512/R513 modify spanning proposals, not the deletion cover. A seam P4 whose Q-side vertices include D cannot simply be inserted into T.
5. R560/R567 are counting inequalities. They force block or transition quantity, not labels, witness collisions, capture, payment, or closure.
6. R566 creates witnesses only from Hamilton paths with the specified boundary state. R570 explicitly allows there to be zero such Hamilton paths.
7. R833 classifies the b_T=2 puncture cell and preserves an ANTI-ENDS alternative; it is not by itself a two-cover contradiction.

Historical failures sharpen these fences. R510 shows that one omitted endpoint parameter can change a three-hole claim into a two-hole degeneration. The stale P527 route for R512 shows why corrected local four-cell dependencies must be cited exactly. More broadly, every splice in this development is audited by listing all consecutive triples crossing the physical junction. This is the same discipline needed in the later insertion/split-splice family, where older one-turn seam compilers failed because a nontrivial path junction can create two new turns.

## Anti-aligned bridges: forks, reversals, and the cross-state escape

The R485-to-R505 line studies an anti-aligned spanning three-cover built from ancestral rails A,B and a bridge P joining a_0 to b_q. The side compiler strengthens through R493/R494/R495 to R501. Its durable alternatives are a double ancestral-end reversal, a Hamilton P4 in a fork cell, or a rigid same-polarity bidirectional chord packet. R486 first places the ancestral bridge chord into a lawful reverse-dimer shadow. R487/R488 test the reverse-chord cell against the immediate ancestral neighbors: absent the old head/tail collision, two explicit Hamilton P4 forks are forced. R489 then exposes the bridge-neighbor state in an exact deletion cover; one literal R453 clause has its sibling killed by the already-tight bridge trimer, so the state either collides or reverses the first/last old bridge order. R490 rules out a quiet side-locked endpoint-universal residue, while R491/R492 turn the reversed endpoint shift into a collision-decorated double splice fan.

The fork obstructions are part of the mathematics, not failed bookkeeping. R496 shows a fork mate makes a_0 internal with a unique successor and therefore cannot simultaneously preserve either old source exit. R497 proves the bridge-interior prong is native-clause isolated without a second cross-arm cut, and R498 shows the two fork prongs cannot themselves be the complete holes of another spanning two-path proposal because their mate turns are already tight. Thus the escape is cross-state comparison, not sibling-clause resolution.

R499/R500 delete the reversal cell and compare a literal three-cover with an exact two-cover of the same residue, producing a balanced cross-state pair. R502 gives the general form: every exact two-cover of the bridge-dimer deletion must cross the bridge interior P^o to one ancestral side, hence births a bridge-interior cross-state pair. The capture genealogy requires precise wording. R503 is an historically accepted retired interface, but its deposited internal-interaction branch over-specialized the capture witness. R504 isolates what is actually witness-blind: by R3, any residue vertex avoiding the deleted bridge dimer can sign that dimer. That generic sign manufacture alone does not identify the selected crossing interaction. R531 is the corrected capture route for the false R503 internal-interaction branch: it retains the actual selected crossing and a genuine adjacency in P^o before invoking the historical capture/mirror machinery. R505 separately records when a fork witness coincides with the forced crossing state and when it instead exposes an avoiding mate certificate.

Consequently the anti-aligned bridge program has a clean logical arc: local fork/reversal geometry, exact negative fences against naive sibling resolution, a forced cross-state pair birth, then a representative-safe capture that keeps the actual bridge-interior crossing. None of the P4, reversal, or balanced-pair outputs is asserted to close H by itself.

## Current-trimer recompletion and local amplification

R506 is the order-free recompletion core. If H=J sqcup U sqcup V with J=(p,x,z), then after deleting p every exact two-cover must cross the surviving boundary dimer {x,z} to U union V, and after deleting z the dual crossing is forced. R507 consumes a chosen crossing by one antisymmetry test against the natural J witness: depending on which dimer endpoint is touched, one gets a same-tested-order collision, a literal P4, or the exact reverse contact. The later local amplification tools clarify how much such four-vertex geometry buys. R522 classifies two no-P4 extensions of one trimer: both fourth vertices must have the same exact R516 signature because the two core turns determine the signature bits, and the two matching no-P4 cells splice to a Hamilton P5. R524 proves a more abstract insertion theorem under prepend/append plus reversal symmetry: every outside vertex has at least two legal insertion slots in any tight path, yielding at least 2^(n-1) spanning paths; R525 shows why PA without reversal symmetry is weaker, reducing each triple to one of nine minimal never-position patterns and identifying the literal insertion barrier. R535 supplies the exact four-marker fragmentation identity c_x=p+q-d_Y(x)-1 and sum c_x=4p+3q-4; when X has no selected Hamilton P4 and all c_x>=4, only the four high-interleaving parameter pairs survive. These identities are reusable independently of R24.

## Hamilton absorbers, wrap states, and unique-transition pressure

R548 gives the universal wrap selection-or-reversal dichotomy for a path component. Reversing a dimer is free; for longer paths, a cyclic wrap succeeds in one direction or both wrap seams fail and R3 supplies their reverse terminal turns, producing opposite-polarity terminal signs and, once the path is long enough, a reverse P4. R579 refines a Hamilton path into four exclusive wrap branches: double wrap, the two single-wrap branches, or double failure. Double wrap is exactly a directed Hamilton cycle.

R561 isolates the strongest reusable absorber object: a boundary-reversed Hamilton dimer, meaning Hamilton paths on the same support beginning with (u,v) and ending with (v,u). For every exterior d, antisymmetry makes exactly one of (d,u,v) and (v,u,d) tight, so one of the two Hamilton representatives absorbs d. R581 combines this with universal-extension rigidity to forbid singleton residual rails in exact covers of the complement.

The transition-count layer is R571. If W=S disjoint-union C is covered by k paths with t selected S|C transitions and b_S,b_C maximal class-block counts, then b_S+b_C=k+t. Hamilton or low-cover absorbers on D union S and D union C give the lower bound t>=2p-a_S-a_C-k. R572 is the constructive dual: if X union {x,y} has a Hamilton path from y to x and a two-rail cover of Y exposes x and y at suitable ends, trimming those endpoints and inserting the Hamilton bridge creates at most two new turns, a literal two-hole spanning splice.

The tau=1 wrap descendants record exact access information. R575 and R577 are valid abandoned wrap-success consumers: a wrap cycle makes the unique crossing S-endpoint Hamilton-accessible and therefore forces the R566 crossing collision in their stated scopes. R578 handles the singleton mixed C-block directly. R580, also abandoned rather than false, records exact one-in/one-out access and the canonical crossing sign in double-wrap geometry. These historical interfaces were retired because later consumers organize the same pressure more cleanly, not because their local conclusions failed.

R586 applies the architecture to a longest path punctured at a terminal dimer: the surviving carrier is a Hamilton absorber and every exact deletion cover has tau>=1. R587 closes the three-vertex-absorber wrap subcases. This section stops at absorber/transition pressure. The separate four-vertex-complement insertion array and its R24 consumer are developed in `r24-four-complement-pressure`, because their hypotheses and mechanism are genuinely different.

## Small pure-rail CS cells and finite seam menus

Several finite cells survive because they encode exact seam arithmetic. R563 treats the trimer pure-rail both-bad CS cell at j=2: the two bad seam holes reverse to a tight four-segment, and adjoining the third pure-rail vertex creates a spanning proposal with one explicitly named residual hole. R565 performs the j=3 analogue and records the complete three-seam menu. R545 is a valid abandoned reduction for the dimer pure-rail s=1 unique-transition cell: the isolated parent mixed seam g is coupled to the two forced reverse seams, and the retained Hamilton-boundary P4 candidate localizes the remaining three-hole residue. R538 gives a separate absorber fence: complementary prefix absorbers covering H minus T and one of c,d force both one-witness tails T+c and T+d to be non-Hamiltonian, or else the Hamilton tail plus the complementary prefix absorber closes H. R552 is the exact 2+2 equal-rail amplification: two disjoint P4s can be re-covered as 5+3 by extending one rail and leaving the complementary three-set, a useful finite-base maneuver. R558 proposed the corresponding near-equal augmentation but remains needs-more-work and is retained as such rather than silently used.

R557 belongs to the same finite-cell archaeology: in the minimum R24 seam cell it gives two explicit endpoint-capture pair births on the two ends. Its scope is narrower than the generic absorber and bridge machinery above, so the exact labels are retained here rather than promoted as a universal interface.

## Right-split and unique-transition repair history

Two early deposits in this family are worth retaining only through their repaired forms.

**Right-split order one.** R562 contains a visibly corrupted statement: its drafting text repeatedly corrects the order of the final triple and even contains impossible repeated-vertex triples. The proof idea, however, was elementary and sound once stated correctly. Accepted R564 is the authoritative repair. Let P=(v_0,...,v_{m-1}) be tight, let x lie outside P, and assume Q=(v_0,...,v_{m-2},x) is tight. Test the append turn (v_{m-2},v_{m-1},x). If it is tight, P followed by x is Hamiltonian on P union {x}. If it is bad, exact reversal/cyclic completion gives the two specified cyclic mates (v_{m-1},x,v_{m-2}) and (x,v_{m-2},v_{m-1}) tight. In this bad-append branch, if the additional middle-insertion turn (v_{m-3},x,v_{m-2}) is tight, then (v_0,...,v_{m-3},x,v_{m-2},v_{m-1}) is Hamiltonian. Only simultaneous failure of the append and middle-insertion turns remains. Nothing from the malformed wording of R562 beyond this corrected content is retained.

**Unique-transition rigidity.** R569 already contained the main idea but overstated uniqueness by failing to allow the relevant Hamilton boundary family to be empty. Accepted R570 gives the exact statement. Partition V(H)=D sqcup S sqcup C, suppose H[D union S] is Hamiltonian, and let T be an exact two-cover of H-D with exactly one selected S|C transition at x. The opposite augmented side H[D union C] cannot also be Hamiltonian, because R567 would force at least two transitions. If two Hamilton paths of H[D union S] realize the crossing boundary x with distinct neighboring vertices, R566 gives a same-oriented collision on the actual crossing dimer. If two distinct Hamilton orders share the same boundary neighbor, R435 gives its reverse-order output. Therefore, outside those explicit outputs, the relevant Hamilton boundary family has **at most one** member, not necessarily exactly one.

These repair histories are mathematically useful scope fences. R562 is preserved as a malformed historical record rather than normalized silently; R569 is preserved as the predecessor of the zero-or-one correction. New use should cite R564 and R570.

## Directed-state rigidity modulo same-support collision

Suppose two tight paths contain the directed state (u,v) and have distinct immediate successors a and b. Then (u,v,a) and (u,v,b) are both tight, so the same physical dimer (u,v) is tail-signed by the distinct witnesses a,b with the same polarity. R38 gives the same-support two-witness interaction. Therefore outside R38 interaction the successor is unique. Dually, if distinct immediate predecessors a,b occur then (a,u,v) and (b,u,v) are tight, so (u,v) is head-signed by two distinct witnesses and R38 applies; hence the predecessor is unique outside interaction. Now let P,Q contain (u,v) in the same orientation and have the same ordered head and tail. If no R38 interaction occurs, repeatedly apply successor uniqueness from (u,v): the next vertex agrees, then the next directed state agrees, so induction forces the entire suffix through the common tail to agree. Vertex-simplicity prevents one path from passing the common tail and later returning to it. Applying predecessor uniqueness backward forces the prefixes through the common head to agree. Hence P=Q literally. The one-sided endpoint version is the same induction in one direction.

## Selected path-forest deletion and partition identities

Let F be a finite selected path forest (the undirected linear forest underlying a chosen tight-path cover), with k nonempty components. For K subseteq V(F), write h=|K|, p=e_F(K) for the number of selected edges with both endpoints in K, and
  delta_F(K)=sum_{x in K}(2-deg_F(x)).
All degrees and edges refer to this same selected forest, not to the ambient boundary tournament. Set c(empty)=0.

Then the number of surviving components is exactly
  c(F-K)=k+h-p-delta_F(K).
In particular c(F-K)<=k+h. Singleton components contribute two endpoint slots, so delta_F(K) counts the original path-end slots lying in K; sum_{x in V(F)}(2-deg_F(x))=2k.

Proof. Put n=|V(F)| and q=e_F(K,V(F)-K). Since F is a forest with k components, |E(F)|=n-k. Degree summation over K gives 2p+q=2h-delta_F(K). Deleting K removes exactly p+q edges. The induced forest F-K therefore has n-h vertices and n-k-p-q edges, so
  c(F-K)=(n-h)-(n-k-p-q)=k-h+p+q
        =k+h-p-delta_F(K).
The argument includes K=empty, K=V(F), singleton rails, and an empty initial forest.

Related partition identity. If V(F) is partitioned into classes C_i, let b_i=c(F[C_i]) and let t count selected edges whose endpoints belong to different classes. Removing those t edges increases the forest component count by exactly t, hence
  sum_i b_i=k+t.
Here b_i counts blocks of the selected representative. It is not the minimum tight-path-cover number of the ambient induced subsystem on C_i. If that minimum is a_i, then b_i>=a_i; writing sigma=sum_i(b_i-a_i) gives t=sum_i a_i-k+sigma. This is fragmentation excess, not an assertion that F contains cycles.

Specializations and scope.
- D2/fixed-cover: F is its selected two-cover T, so k=2. D2 uses its symbol k for h=|K|, giving r=2+|K|-e_T(K)-delta_T(K), the block-count input to boundary compression.
- D1/conservation: F=T, k=2 and K=X has four vertices. With Y=V(T)-X, this becomes r_Y+p+delta_X=6. The LOW/MAX interpretation additionally needs the geometric hypotheses in that section.
- D13/block-pressure: the partition identity supplies the block total; absorber hypotheses supply the separate lower bounds on individual block counts.

These identities use only the selected linear forest. No boundary antisymmetry, minimality, gate geometry, payment ancestry, or existence of a specially arranged cover is needed. They count components in the inherited selected paths; they neither assert that this is a minimum cover after deletion nor synchronize different representatives.

This is an elementary generalization of the counting proof already exposed in D2 and its D1 specialization. It is recorded as internal mathematical exposition, not as a newly accepted standalone theorem.