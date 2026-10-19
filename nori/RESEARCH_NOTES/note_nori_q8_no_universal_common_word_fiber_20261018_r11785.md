# Q8 counterexample to a single pair-word covering every parity fiber

- Stable ID: note_nori_q8_no_universal_common_word_fiber_20261018_r11785
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: NORI1, paired-flat, Q8, parity-fibers, common-word, obstruction, finite-exhaustive
- Lifecycle: active
- Epistemic status: tested
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11785_2
- Updated session: session_nori_r11785_2
- Disposition: none
- Successor: none

## Related references

- None

## Research note

# A four-pair counterexample to universal common-word parity support

Work on the legal paired-flat eight-cube with pair labels 0,1,2,3, represented by four pairs of original bits (a_i,b_i). Put q_i=x_(a_i) and p_i=x_(a_i)+x_(b_i) over F2. For gate i, pack the three bits of p excluding i into P in 0..7, and likewise the three bits of q excluding i into Q in 0..7, retaining the increasing label order. The selector gate f_i(P,Q) is bit number 8P+Q (least significant bit numbered zero) of the hexadecimal integer:

i=0: cc2bf0b2cce8e8aa
i=1: e8cc8e17f0d4aad4
i=2: 96b27155f0f0b2cc
i=3: 4d964df0558e71f0.

A red pair-i step flips original direction a_i if f_i=0, otherwise b_i. Every gate ignores its own pair and obeys f_i(P,Q+111)=1+f_i(P,Q); hence the undirected coloring is paired-flat and antipodally odd.

For a pair word w with every label occurring twice, let P(w) be the set of starting pair-parity fibers that contain a red full antipodal w-geodesic.

**Finite counterexample (exhaustively checked).** Every one of the 16 starting parity fibers admits some red full geodesic, while NO single pair word satisfies |P(w)|=16. Indeed, direct original-eight-bit enumeration over all 2520 multiset pair words and all 256 roots gives max_w |P(w)|=15. The number of pair words having support cardinality k is:
k=0:1656; k=3:2; k=4:24; k=5:34; k=6:44; k=7:120; k=8:128; k=9:148; k=10:104; k=11:108; k=12:76; k=13:50; k=14:16; k=15:10.
The counts sum to 2520. The union of P(w) over all words is all 16 parity fibers.

A direct checker enumerates original vertices 0..255, represents bits a_i,b_i at positions 2i and 2i+1, computes each red step by consulting the four masks, checks whether the endpoint equals root XOR 255, and records the initial parity vector. It independently verifies each gate's self-duality and the stated counts. Reproduction file: /mnt/data/nori_q8_common_word_parity_support_check.py, generated in session session_nori_r11785_2.

**Logical scope.** This disproves the proposed implication that fiberwise red antipodal reachability (possibly with a different pair word in each fiber) supplies a *single* pair word reaching an antipodal endpoint from some root in every fiber, already for m=4. It does not challenge the proved parity-cylinder theorem or single-slab robustness for colorings that DO admit a common word with full fiber support. In fact ten words in this example cover 15 fibers individually, so it does not refute the weaker five-fiber sufficient condition for single-square preservation in Q8. The unrestricted closure problem remains open.
