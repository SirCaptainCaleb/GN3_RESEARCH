# Fiberwise six-cube geodesic forcing and global eight-cube SAT audit

- Stable ID: note_nori_q6_parity_fiber_sharp_q8_global_sat_r11510
- Author: unspecified; session provenance retained
- Primary home: subsection:obstruction_compatibility_and_a_programme_for_nori1_closure
- Labels: NORI1, paired-flat, Q6, Q8, parity-fiber, global-reachability, exhaustive, computer-assisted, independent-verification, witness-count
- Lifecycle: active
- Epistemic status: tested
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11510_3
- Updated session: session_nori_r11510_3
- Disposition: none
- Successor: none

## Related references

- note:note_nori_majority_static_and_seven_order_joint_forcing_r11510
- note:note_nori_cyclic_pair_gate_sensitivity_product_r11510

## Research note

# Fiberwise paired-flat six-cube forcing, sharpness, and eight-cube global reachability audit

**Theorem (finite exhaustive, Q6).** Let c be any legal antipodally odd paired-flat coloring of Q6 with paired directions P_i={2i,2i+1}, i=0,1,2. For EVERY prescribed pair-parity vector p_i=x_(2i)+x_(2i+1), some vertex of that parity fiber starts an all-zero full antipodal geodesic. This assertion is stronger than mere existence somewhere in Q6.

**Finite proof and independent checker.** Translating roots reduces to parity p=000. Reverse any red full geodesic to halve the root search, leaving representatives r=0,12,48,60 for its four antipodal root pairs. The three pair gates each have eight independent odd truth bits, total 24 independent coloring bits and 2^24 legal assignments. Admissible red pair-label words have length six, each of labels 0,1,2 appearing twice, with no equal consecutive labels. A twelve-word portfolio suffices:
 201012, 210102, 021201, 012120,
 210210, 010212, 021021, 202101,
 120201, 120120, 102102, 102021.
For every word enumerate its eight pair-member assignments and four representative roots: 12*8*4=384 red path patterns. Each pattern prescribes up to six of the 24 Boolean gate values. The standalone standard-C++ verifier q6_fiber_portfolio_independent.cpp generates those prescriptions independently of the preceding Z3 reachability solver and represents the union of their satisfaction subcubes as a bitset of size 2^24. It verifies that ZERO legal assignments are uncovered. Therefore every coloring has a red full geodesic rooted within the prescribed fiber. Translating proves all p.

**Portfolio irredundancy.** Removing the word families in the displayed order leaves, respectively, 3488,2976,384,7936,896,768,2112,1184,4128,1248,1248,3776 uncovered legal colorings. Irredundancy is relative to this twelve-word portfolio, not a claim of global minimum portfolio size.

**Sharpness of root-pair coverage.** The four antipodal root pairs in fiber p=000 are {0,63},{12,51},{48,15},{60,3}. For each pair a legal coloring exists having a red full path from that pair and none of the other three pairs. Truth-table masks (f0,f1,f2) indexed by outside-bit assignments 0..15 are:
 {0,63}: (0x5555,0xb2b2,0xff00);
 {12,51}: (0xeaa8,0xbf02,0xff00);
 {48,15}: (0xdf04,0xbf02,0xff00);
 {60,3}: (0xaaaa,0xb2b2,0xff00).
The independent subset-reachability verifier q6_fiber_witness_check.py checks all four certificates. A second complete bitset enumeration q6_fiber_root_sharpness.cpp finds 3584 legal coloring assignments with no red full path from any prescribed THREE of the four root pairs, and none excluding all four. The theorem is sharp with respect to universal selection of antipodal root pairs.

**Prior unpersisted finite Q8 result.** Every legal paired-flat antipodally odd Q8 coloring admits a red full antipodal geodesic, by two independently generated Boolean reachability encodings that return UNSAT. There are 128 independent coloring bits, 32768 root/subset states, and 131072 red transition implications in the first encoding. A nonodd constant-gate negative control returns SAT. Full mathematical audit nori_q8_pairedflat_global_closure.md and reproducible sources nori_q8_all_global_sat.py and nori_q8_global_alternate_sat.py. This Q8 statement is still solver-assisted, with no independently checked UNSAT log; it does NOT imply NORI1 for arbitrary Q8 colorings because arbitrary Q8 lift to paired-flat Q16.

**Scope and next mathematical challenge.** A prescribed-parity-fiber version of the paired-flat Q8 theorem was not determined; a specialized SAT attempt timed out and must not be read as evidence either way. The known Q8 nonlinear face-irreducible example has six successful starting roots in each parity fiber; a legal antipodal square-pair mutation changes some fiber counts to eight while others remain six, refuting uniformity of the counts. The Q6 argument shows how all four root-pair failures can be jointly inconsistent despite each three-root failure being realizable. A dimension-uniform version of this shared-assignment incompatibility is needed. Neither finite theorem settles unrestricted NORI1.

**Reproduction files.** /mnt/data/nori_q6_fiberwise_global_compatibility.md; /mnt/data/q6_fiber_portfolio_independent.cpp; /mnt/data/q6_fiber_root_sharpness.cpp; /mnt/data/q6_fiber_witness_check.py; /mnt/data/nori_q8_pairedflat_global_closure.md; /mnt/data/nori_q8_all_global_sat.py; /mnt/data/nori_q8_global_alternate_sat.py.

**COMPLETE Q6 ROOT-PAIR WITNESS DISTRIBUTION (additional independent full enumeration).** Let N_k be the number of legal paired-flat Q6 colorings for which, in any prescribed pair-parity fiber, precisely k of its four antipodal root pairs admit a red full antipodal geodesic. An independent C++ bitset computation over all 2^24 legal colorings gives
 N_0=0, N_1=14336, N_2=610944, N_3=2295552, N_4=13856384.
The sum is 16,777,216. Each of the four root pairs is uniquely successful in precisely 3,584 legal colorings. This strengthens the sharpness argument from four individual examples to an exhaustive distribution. The separate verifier q6_fiber_root_distribution.cpp builds four reachability witness coverage bitsets, one per root pair, and uses direct bitwise population counts. It does not use Z3. See the updated report nori_q6_fiberwise_global_compatibility.md, Section 6.
