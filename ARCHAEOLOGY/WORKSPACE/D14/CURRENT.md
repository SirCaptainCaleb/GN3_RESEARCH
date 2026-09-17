# D14 — Complete seam-window compilers for insertion, concatenation, and split-splice reconstruction

Generic complete-window development for block insertion, literal three-cover concatenation, split-splice reconstruction, four-complement insertion obstruction, and the exact failure modes caused by omitting a second junction turn.

## The width-two junction principle

If P=(p_0,...,p_r) and Q=(q_0,...,q_s) are tight paths on disjoint supports, the concatenation P+Q inherits all internal turns. The only possibly new consecutive triples are
  (p_{r-1},p_r,q_0) when r>=1,
and
  (p_r,q_0,q_1) when s>=1.
Thus a nontrivial junction can create two new turns. If one side is a singleton only one of these may exist; if both sides are singletons there is no turn at all.

This elementary observation is the audit rule for the whole development. Every insertion or split-splice must enumerate the complete set of consecutive triples crossing each physical junction. A theorem may delete one only when its nonexistence or tightness is separately certified.

## From endpoint blockers to the corrected block-insertion parent

R809/P885 recorded a useful endpoint intuition: if concatenating one exact-core rail with a Hamilton complement creates only one new boundary turn, that turn must be bad, otherwise the untouched second core rail completes a spanning two-cover. The revision was abandoned/invalidated as historical machinery and is not a current tool.

R811/P887 extended the same idea to inserting an exact-core rail A=(a_0,...,a_r) into every internal gap m_i|m_{i+1} of a Hamilton complement M. Its internal-gap audit is sound. For r=0 the complete new window is
  (m_{i-1},m_i,a_0) when i>=1,
  (m_i,a_0,m_{i+1}),
  (a_0,m_{i+1},m_{i+2}) when i+2<=t.
For r>=1 the complete window is
  (m_{i-1},m_i,a_0) when i>=1,
  (m_i,a_0,a_1),
  (a_{r-1},a_r,m_{i+1}),
  (a_r,m_{i+1},m_{i+2}) when i+2<=t.
If every present turn were tight, the inserted sequence plus untouched rail B would two-cover H, so some present turn is bad and its complete reversal is tight.

The defect in R811 was exterior insertion. BEFORE M, the concatenation A+M can have both
  (a_{r-1},a_r,m_0) when r>=1,
and
  (a_r,m_0,m_1) when t>=1.
AFTER M dually has
  (m_{t-1},m_t,a_0) when t>=1,
and
  (m_t,a_0,a_1) when r>=1.
R811 incorrectly collapsed these to the old one-turn endpoint viewpoint.

Accepted R844/P918 is the exact repair. It keeps the sound internal windows and replaces both exterior slots by the complete two-turn windows above. If r=t=0 the concatenation is an automatic dimer and already gives a two-cover with B, so that boundary case is impossible under pc(H)>2. R844 is now the canonical generic insertion compiler.

## Corrected generic split-splice theorem with complete seam windows

Let H satisfy pc(H)>2 and let
  V(H)=V(G) sqcup V(M),
where M=(m_0,...,m_t) is a nonempty tight path and G has a literal exact two-cover A sqcup B by nonempty tight paths,
  A=(a_0,...,a_r),  B=(b_0,...,b_s).
Fix an internal cut m_i|m_{i+1}, 0<=i<t.

Form the AB proposal
  P_AB=(m_0,...,m_i,a_0,...,a_r),
  Q_AB=(b_0,...,b_s,m_{i+1},...,m_t).
Its complete new seam set is
L_A(i)={ (m_{i-1},m_i,a_0) if i>=1,
         (m_i,a_0,a_1) if r>=1 }
and
R_B(i)={ (b_{s-1},b_s,m_{i+1}) if s>=1,
         (b_s,m_{i+1},m_{i+2}) if i+2<=t }.
All other turns are inherited from M,A,B. Therefore L_A(i) union R_B(i) is nonempty and cannot consist entirely of tight turns; otherwise P_AB,Q_AB would be a literal spanning two-cover of H. Hence at least one present turn in this union is bad, and boundary antisymmetry makes its complete reversal tight.

Similarly the BA proposal
  P_BA=(m_0,...,m_i,b_0,...,b_s),
  Q_BA=(a_0,...,a_r,m_{i+1},...,m_t)
has complete new seam set
  L_B(i) union R_A(i),
where the definitions exchange A and B. At least one present turn in that union is bad and its complete reversal is tight.

Thus every cut carries **two simultaneous complete-window obstruction clauses**:
  NOT(all turns in L_A(i) union R_B(i) are tight),
  NOT(all turns in L_B(i) union R_A(i) are tight).
Each clause has between one and four physical turns depending on singleton and endpoint degeneracies. No binary reduction is justified without additional tightness information.

Proof completeness. Each displayed proposal uses every vertex exactly once because the cut partitions M and A,B partition G. Every non-junction turn is inherited from one of the three tight source paths. The width-two junction principle lists all and only new triples. If all present new triples of one proposal were tight, its two sequences would be tight spanning paths, contradicting pc(H)>2. This proves both clauses independently.

This theorem is the exact salvage of the R812 idea. It preserves the coupling between the two core rails while refusing the false assumption that each concatenation has only one seam literal.

## Why R812 and R816 fail, and exactly what remains valid

R812/P888 claimed binary crossed clauses at every cut by assigning A to the left piece and B to the right, or vice versa. The spanning proposals themselves are legitimate. The proof fails only at seam accounting: prefix-to-A and B-to-suffix can each contribute two turns. Therefore the advertised two-literal clauses do not follow. The valid salvage is the complete-window theorem above.

R816/P891 made the same compression inside the synchronized R24 core. A typical proposed rail (q_2,...,q_j,z,R,s) has both new turns (q_{j-1},q_j,z) and (q_j,z,R), while its companion has both a core-to-q turn and, except at the terminal cut, a q-to-q_{j+2} turn. R816 was correctly rejected. Its source labels and intended pairing remain useful because accepted R818 reconstructs the same geometry without deleting holes.

This failure mode is local and general: one physical path junction is a two-turn window. It does not invalidate the spanning-proposal strategy itself.

## Accepted deep-cut specialization: four-hole and terminal three-hole clauses

Accepted R818/P893 is the R24 deep-cut implementation of complete seam accounting. In the synchronized R594/R619 frame, fix 3<=j<=m-3 and q=q_{j+1}. For each phase-labelled enlarged root, split N=Q[2,m-2] at q_j|q and assign one exact core rail to each side.

For the left root z, one proposal is
  (q_2,...,q_j,z,R,s)
and
  (u,L,a,c,b,q,q_{j+2},...,q_{m-2}).
The complete holes are
  (q_{j-1},q_j,z),
  (q_j,z,R),
  (c,b,q),
and, when j<=m-4,
  (b,q,q_{j+2}).
If all were tight these two paths would span H. Reversing one bad hole yields exactly
  A_j(z)=(z,q_j,q_{j-1}) OR (R,z,q_j) OR (q,b,c) OR C_j(b)=(q_{j+2},q,b),
with the C_j literal absent at j=m-3.

The other left root b and the two phase-dependent right roots give the five further clauses listed in R818. Every interior clause has four possible reverse literals; every terminal-deep clause has three. This is the exact repaired replacement for R816's binary system.

R818 does not choose a disjunct, convert the clauses to 2-SAT, or assert selected-state currentness. Its value is a complete physical seam ledger tied to the exact enlarged-root representatives.

## Specialized exact interfaces built from the generic windows

The generic theorem here is the complete seam-window calculation. R818/P893 specializes that calculation to the labelled deep-cut split-splice frame and retains every physical hole. R820 is a different, crossed-core consumer: P919 derives its deep-gap clauses directly from the four crossed core P4s and the complete internal insertion windows, so it does not depend on invalid R811. The crossed gate geometry needed to state and prove R820 is developed in D4. R816 remains a rejected R24-frame binary compression and its exact failure is recorded in D3. Their extra hypotheses and frame geometry are developed where those specializations are introduced.

## Complete two-turn seam fan of a literal three-cover

Let H=A ⊔ B ⊔ C be a literal spanning three-cover by nontrivial tight paths, with A=(a_0,...,a_p) and B=(b_0,...,b_q). The ordered concatenation A→B changes no old turn and creates exactly two new turns h_1=(a_{p-1},a_p,b_0) and h_2=(a_p,b_0,b_1). Because pc(H)>2, the proposal (A→B) ⊔ C cannot have both turns tight. Hence at least one is bad, and R3 gives the exact mate clause (b_0,a_p,a_{p-1}) OR (b_1,b_0,a_p). R453 repeats this for all six ordered component pairs and retains each literal proposal and its complete two-hole list.

The native fan has a sharp limitation. R457 checks component membership and exact order and proves that no native mate literal is the antisymmetric complement of a literal in another native clause. R459 strengthens this: every proposal obtained merely by permuting intact source components is already one of the same six, so any complementary sibling must cut or rewrite a component or import a genuinely different representative. R460 checks the twelve turn literals individually: they belong to twelve distinct antisymmetry pairs, so the six disjunctions admit 2^6 local exact-one choices and no resolution step exists among the native clauses alone. R461 identifies the necessary geometry of any true sibling: complementing either A→B seam literal requires abandoning both incident source endpoint adjacencies a_{p-1}a_p and b_0b_1. This is only a necessary two-cut condition, not an existence theorem.

## Four-vertex complement gives a synchronized complete insertion-obstruction array

Let Q=(q_0,...,q_m) be a vertex-simple tight path and let X=V(H)\\V(Q) have exactly four vertices. Fix x∈X. By boundary antisymmetry the other three vertices X\\{x} support a tight Hamilton trimer. If H[V(Q)∪{x}] had a Hamilton tight path, that path together with the trimer on X\\{x} would be a spanning two-cover of H. Thus Q∪{x} is non-Hamiltonian.

Insert x literally between q_i and q_{i+1}. Every old Q-turn outside the width-two insertion window remains tight. The only new turns are A_i(x)=(q_{i-1},q_i,x) when i≥1, B_i(x)=(q_i,x,q_{i+1}), and C_i(x)=(x,q_{i+1},q_{i+2}) when i+2≤m. Since the inserted order is not Hamiltonian, at least one present turn is bad. R3 therefore makes at least one exact reverse Abar_i(x)=(x,q_i,q_{i-1}), Bbar_i(x)=(q_{i+1},x,q_i), Cbar_i(x)=(q_{i+2},q_{i+1},x) tight. The clause holds independently for all four x on the same ordered Q.

For an internal gap, partition the four witnesses according to which reverse alternatives occur. If fewer than two witnesses realize the left alternative and fewer than two realize the right alternative, at least two witnesses realize the reverse-middle alternative. Hence every internal gap has either a two-witness packet on (q_i,q_{i-1}), a two-witness packet on (q_{i+2},q_{i+1}), or two distinct reverse-middle turns (q_{i+1},x,q_i). At the left endpoint only the middle and right alternatives exist; absent two right witnesses, at least three reverse-middle witnesses occur. The right endpoint is dual. No smallest-counterexample minimality, R24, transitive four-cell classification, or global-longest assumption is used.