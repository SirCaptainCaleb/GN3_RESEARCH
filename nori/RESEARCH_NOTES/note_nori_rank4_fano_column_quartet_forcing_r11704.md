# Dimension-uniform rank-four peeling through complementary column pairs and Fano quartet compatibility

- Stable ID: note_nori_rank4_fano_column_quartet_forcing_r11704
- Author: unspecified; session provenance retained
- Primary home: subsection:obstruction_compatibility_and_a_programme_for_nori1_closure
- Labels: NORI1, affine-holonomy, dimension-uniform, rank-four, parity-peeling, Fano-plane, column-compatibility, zero-sum-quartet, computer-assisted, constructive-forcing
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11510_3
- Updated session: session_nori_r11510_3
- Disposition: none
- Successor: none

## Related references

- note:note_nori_m6_full_peeling_feedback_core_r11685
- note:note_nori_nested_core_phase_peeling_r11660

## Research note

# Column-compression and Fano-plane rank-four parity-peeling theorem

Let A be a zero-diagonal binary m-by-m matrix with A1=1. A deletion sequence i_1,...,i_k is legal when sum_(s<t) a_(i_t,i_s)=0 for every t. It succeeds if A[R,R] on the remaining labels is nonsingular.

**THEOREM A (column cancellation).** (1) Two equal columns can be legally deleted one after the other, with odd row sums retained in the residual matrix; the diagonal zero gives the required two-way entries zero. (2) A zero column can be deleted, again leaving odd row sums. (3) Two disjoint pairs of columns each summing to the all-one vector can always be deleted in some four-step legal order; the total of their four columns is zero, so all surviving row sums remain odd.

**Proof of (3).** Label the pairs (a0,a1), (b0,b1). Write c_t=A_(b_t,a0) and d_s=A_(a_s,b0), over F2. Complementarity makes A_(b_t,a_s)=c_t+s, A_(a_s,b_t)=d_s+t and the two within-pair cross-entries equal one. If c_0!=c_1 use the order (a_(c_0),b0,b1,a_(1-c_0)). If c_0=c_1=c put t=1+d_(1-c), and use (a_c,b_t,a_(1-c),b_(1-t)). The second and third choices have incoming parity zero, while the fourth is legal since the induced four rows have even total parity. QED.

**THEOREM B (bounded-rank compression).** Suppose rank(A)=r. Factor A=UV^T over F2 with U of full column rank, and normalize s=V^T1=e0, so U s=1. Each factor column v_i satisfies u_i dot v_i=0 whereas u_i dot s=1, hence v_i!=s. In a smallest unpeelable matrix the column-cancellation lemma excludes zero factors, repeated factors, and two complete pairs {v,v+s}. Modulo span(s), the nonzero factors occupy at most one representative of each of 2^(r-1)-1 nonzero quotient classes, plus at most one extra representative of one class. Consequently a smallest unpeelable matrix has at most 2^(r-1) labels.

For r<=3, at most four labels remain; this contradicts the previously fully checked odd six-label theorem. For r=4, at most eight remain. Eight is impossible: it would contain one doubled quotient class p and a singleton in each of the other six nonzero F2^3 classes; their quotient XOR is p!=0, whereas sum v_i=s projects to zero. At seven labels, one doubled class and five singleton classes similarly have nonzero quotient XOR p+q (q is the omitted class). Hence the only seven-label pattern chooses one representative of EVERY nonzero quotient class t in F2^3, the Fano-plane configuration.

**THEOREM C (rank at most four, every matrix size; computer-assisted finite base).** Every zero-diagonal A with A1=1 and rank(A)<=4 has a successful legal parity peel. For the rank-four seven-label normal form, normalize s=e0 and write each column factor as v_t=(epsilon_t,t), t=1,...,7, where sum_t epsilon_t=1. There are 64 lift patterns. Each row factor u_t=(1,z_t) satisfies u_t dot v_t=0, giving four choices for z_t. Thus there are 64*4^7=1,048,576 labeled Fano normal forms. A complete portable C++17 subset-DP verification checks every one. Zero failures occur, with minimum peeling counts k=3:920000, k=4:121184, k=5:7392. The earlier analytic reductions prepend legal deletions to these finite certificates, proving the theorem for ALL matrix sizes. Separately coded Python rank/reachability checked 20000 seeded configurations. Another independent canonical check exhausted 540 rank-at-most-three configurations.

**NORI1 CONSEQUENCE.** By the previously proved nested double-sweep theorem, every legal paired-flat Q_(2m) coloring with a parity-independent affine q-slope matrix of rank at most four and arbitrary nonlinear parity-phase functions has an all-red full antipodal geodesic rooted in EVERY prescribed pair-parity fiber, for all m. The pair word depends only on its slope matrix and gives 2^k red starting roots when k labels are peeled. This is a dimension-uniform theorem within this class, not unrestricted NORI1.

**THEOREM D (zero-sum four-column forcing).** Let four distinct columns of A sum to zero. The induced four-row restriction has zero diagonal and even row sums. Of the 256 such four-row patterns, 240 admit a legal deletion of all four labels. The remaining 16 patterns have a bidirected triangle among three labels, with these triangle rows not reading the fourth label. Four choices of the outside label times four even possibilities for its row give the 16. This is an exhaustive four-vertex Boolean lemma verified independently over all 256 cases and all 24 orders. Whenever a zero-sum quartet is not exceptional, its deletion preserves the odd-row property.

**FANO FOUR-COLUMN COVER.** In the rank-four Fano seven-label pattern, the complements of its seven projective lines are four-label sets. Because the lift parity sum is odd and each point belongs to three lines, at least one such quartet has zero column sum. An exhaustive local-only checker on ALL 1,048,576 normal forms shows at least one of these zero-sum quartets is nonexceptional. Thus it can be deleted, reducing to an odd-row three-label matrix. This provides a second finite proof certificate of rank-four success without seven-label reachability calculations.

**OUTLOOK AND STATUS.** The general parity-peeling conjecture remains open for unrestricted ranks. A minimal counterexample must now resist repeated columns, zero columns, complementary-column pairs and every nonexceptional zero-sum column quartet; each additive column parallelogram would have to support the exceptional bidirected-triangle obstruction. This is a common-matrix compatibility condition suitable for direct attack in higher ranks. Fully unrestricted NORI1 remains open.

**REPRODUCIBLE FILES.** nori_low_rank_peeling_and_zero_sum_quartets.md; nori_rank4_fano_enumeration.cpp; nori_rank4_quartet.cpp; nori_rank4_fano_independent_check.py; nori_rank3_column_compression_verifier.py; nori_zero_sum_quartet_verifier.py; nori_rank_four_column_peeling_bundle.zip.
