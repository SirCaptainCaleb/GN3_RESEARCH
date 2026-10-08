# Audit minimum counterexamplehood does not orient every proper block zero-to-one — preserved pre-item development

Audit of root 139 and every topological result depending on its all-proper-face zero-freeness.

Root 139 argues that for each block B_j of a proper permutahedron face, minimum-counterexamplehood supplies a spanning block order with one-change word
0^*1^*,
hence no internal 10 descent.

Minimum-counterexamplehood supplies only an order with AT MOST ONE color change. Its nonconstant word may instead be
1^p0^q.

For a reversal-odd ternary label, reversing the coordinate order sends a word
w_1,...,w_m
to
1-w_m,...,1-w_1.
Therefore
1^p0^q
under reversal becomes
1^q0^p,
which has the SAME 1-to-0 transition direction. Likewise 0^p1^q stays 0-to-1.

Thus reversal does not let one normalize the transition direction of an individual proper block. A global color complement would flip every block simultaneously, but cannot be chosen independently for the blocks of one face.

Consequently a proper block whose available chosen good order has word 1^*0^* may contain an internal 10 descent. Concatenating good orders of the blocks does not prove that every 10 descent crosses distinct face blocks.

Hence the step
'no crossing 10 root => concatenated full order has no 10 descent'
in root 139 is invalid without an additional SAME-DIRECTION block theorem.

Safe retained facts:
- root 42 gives boundary zero-freeness for faces whose blocks are small enough for its independent local rotation lemma;
- on any face, all actual roots crossing distinct ordered blocks are weakly/strictly cooriented by the block-rank functional;
- if one can independently produce a no-10 order inside every block of a particular face, the root-139 argument is valid for that face.

Not presently established:
- zero-freeness of the all-refinements carrier on EVERY proper face by minimum-counterexamplehood alone;
- the resulting claim that all carrier zeros lie in the top permutahedron cell;
- the nonzero global boundary degree asserted from that extension.

Therefore the center-replacement and one-root-per-face carrier results that use root 139 as their boundary-degree premise are CONDITIONAL on repairing this orientation issue. Their degree-to-monotone-path arguments remain valid if a zero-free nonzero-degree proper-boundary carrier is supplied by another theorem, but root 139 does not currently supply it.

A possible repair target is a synchronization theorem: on the blocks of every proper ordered partition, choose good restricted orders whose one-change directions agree globally; or replace 10-only roots by a signed descent/ascent carrier that treats both one-change directions symmetrically.
