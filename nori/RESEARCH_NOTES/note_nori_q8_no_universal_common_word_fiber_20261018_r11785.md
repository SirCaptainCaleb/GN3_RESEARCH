# Q8 parity-support ceiling and tensor scarcity of common words

- Stable ID: note_nori_q8_no_universal_common_word_fiber_20261018_r11785
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: NORI1, paired-flat, Q8, parity-fibers, common-word, obstruction, finite-exhaustive
- Lifecycle: active
- Epistemic status: tested
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11785_2
- Updated session: session_nori_r11974_2
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


## Strengthening: exponential scarcity of common-word parity support despite every-root success

**Theorem (base Q8 and products).** There is a legal nonlinear paired-flat coloring c of Q8 in which all 256 roots support a red full original-direction-simple antipodal geodesic, but every pair-label word w with each of four labels occurring twice has a successful starting-parity support P_c(w) of cardinality at most 12 of the 16 parity fibers. The value 12 is attained. Its k-fold independent Cartesian product c^(boxplus k), on Q_(8k), retains red full success from every root and satisfies

max_w |P_(c^(boxplus k))(w)| / 16^k = (12/16)^k = (3/4)^k.

For any additional r=1,2,3 direction pairs, add gates f_j=x_0 with all old gates independent of added bits. Then every root still starts a red full geodesic, and for m=4k+r pairs the maximum support fraction is at most (3/4)^k. Thus no positive dimension-independent fraction of successful starting parity fibers can be guaranteed for one common pair word, even under universal rooted red success.

**Base gate certificate.** Pair original directions as (0,1),(2,3),(4,5),(6,7). For gate i, form a six-bit integer z_i from its exterior original direction bits in increasing direction order, put t_i=min(z_i,63-z_i), and set
f_i(x)=bit_(t_i)(M_i) xor [z_i>=32].
The four unsigned 32-bit masks are
M=(0xDBBD4B24, 0x90099FF9, 0x096000F0, 0xFD990F1F).
Every f_i ignores its own pair. Since complementation replaces z_i by 63-z_i, the indexed bit is unchanged and the final indicator reverses; therefore every f_i is antipodally odd and the coloring is legal.

**Finite verification.** Enumerate the 864 pair words of length eight with each label used twice and no adjacent equal labels. For each word and each of 256 cube roots, apply the unique red pair matching and test whether the endpoint is the vertex antipode. The histogram of |P_c(w)| for cardinalities 0,1,...,16 is
(26,28,136,108,188,84,134,40,66,14,18,10,12,0,0,0,0).
Consequently max_w |P_c(w)|=12. There are 14712 rooted red full paths, and every root supports between 30 and 93 of these paths, so all 256 roots succeed. As one witness, root zero has the red original-direction word (0,4,3,6,2,1,7,5) with visited vertices (0,1,17,25,89,93,95,223,255). A second independent enumeration loops over original roots and the reduced pair words, separately checking the gates' invariances and every selected red step, and reproduces all counts.

Words with adjacent equal pair labels cannot be successful: their two uses of that pair become consecutive after removal of independent-block steps and the red pair matching is involutive, so those two steps cancel and cannot make the pair's original bits antipodal.

**Tensor proof.** For independent paired-flat c and d and a global doubled pair word w, let w_c,w_d be its subsequences belonging to the two factors. All cross-factor red matchings commute, and success at a product root is equivalent to success of each factor projection. Thus
P_(c boxplus d)(w)=P_c(w_c) times P_d(w_d)
as a Cartesian product of starting pair-parity supports, including empty supports for words with consecutive equal projected pair labels. Taking maxima over all global words gives multiplicativity of maximum support cardinality: any chosen factor words can be interleaved to form a global word, and no interleaving affects the factor endpoints. Hence the k-fold product maximum is 12^k. Every product root succeeds by concatenating a red full geodesic from each of its factor roots.

For added feed-forward pairs with selector x_0, project any successful enlarged full word onto the old pairs. The projection remains a red full original-direction-simple antipodal path, so the enlarged support has size at most 2^r times the old maximum. Conversely every successful old rooted path has direction 0 once; insert each new pair's even/odd red steps on opposite sides of that step according to its root's initial x_0. This gives a fully red enlarged original-direction-simple antipodal path from every extended root, establishing the rooted-success assertion.

**Scope and research implication.** The original Q8 note already refuted universal full-parity common-word support with an example reaching 15 fibers; the new certificate strengthens the ceiling to 12 while ensuring every root succeeds, and tensor amplification forces the maximum *fraction* for every word toward zero. The stronger claim needed to eliminate one strict critical square is only the existence of some successful word on more than four starting parity fibers. This construction does not refute that claim: the base has words with support 12 and its products have maximum support 12^k. A proof of unrestricted NORI1 may still use absolute, rather than positive-density, parity support.
