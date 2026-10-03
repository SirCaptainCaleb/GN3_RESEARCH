# The remaining lemma

## Body

### Two-cut normal form

The defect-line formulation has an exact normalization for three-covers.

**Lemma 9 (two-cut normal form).** Let \(H\) be a minimum counterexample. Let
\[
C=P_1\mid P_2\mid P_3
\]
be any three-cover, and let \(\pi\) be the spanning ordering obtained by concatenating the three displayed path orders. If \(a<b\) are the two cuts between consecutive components, then
\[
\nu(L_\pi)=2,
\]
and \(\{a,b\}\) is a minimum vertex cover of \(L_\pi\).

Conversely, if \(\pi=(v_1,\ldots ,v_n)\) is any spanning ordering with \(\nu(L_\pi)=2\), then every minimum vertex cover \(\{a,b\}\), \(a<b\), of \(L_\pi\) cuts \(\pi\) into the three tight paths
\[
(v_1,\ldots ,v_a),\qquad
(v_{a+1},\ldots ,v_b),\qquad
(v_{b+1},\ldots ,v_n).
\]

**Proof.** The two component boundaries of \(C\) form a set of cuts whose removal partitions \(\pi\) into three tight intervals. Equivalently, the corresponding two vertices of the defect line meet every defect edge. Hence
\[
\tau(L_\pi)\le2.
\]
By the defect-line identity,
\[
\nu(L_\pi)=\tau(L_\pi)\le2.
\]
If \(\nu(L_\pi)\le1\), the same identity gives \(c(\pi)\le2\), so \(H\) has a two-cover, contrary to the choice of \(H\). Thus \(\nu(L_\pi)=2\), and the two displayed cuts form a minimum vertex cover.

Conversely, if \(\{a,b\}\) is a vertex cover of \(L_\pi\), then no defect center lies wholly inside any of the three intervals determined by the cuts after positions \(a\) and \(b\). Each interval is therefore a tight path. Since \(\tau(L_\pi)=\nu(L_\pi)=2\), every minimum vertex cover has exactly two vertices, giving the asserted three-cover. \(\square\)

This identifies the pairwise-repartition problem with a two-cut defect problem. Every three-cover state in a minimum counterexample carries two necessary defect-cover cuts; obtaining a two-cover is exactly the problem of finding a spanning ordering whose defect line can be covered by one cut. Thus the remaining compression step should be read as eliminating one of the two necessary cuts, rather than merely shortening the geometric span of the visible defects.

### Neutral end-edge reversal is a deletion-root exchange

The neutral residue of an end-edge reversal has additional structure when it starts from a singleton lift.

**Lemma 10 (root exchange).** Let
\[
H-x=P\mid Q
\]
be a deletion cover of a minimum counterexample, and suppose its singleton lift
\[
P\mid\{x\}\mid Q
\]
minimizes \(\Phi\) in its component of the pairwise-repartition graph. Let \(P\) have a Hamilton order
\[
R=(A,p_m,p_{m-1},B)
\]
containing the reversed terminal edge \((p_m,p_{m-1})\) of a displayed order of \(P\). Then either \(H\) has a two-cover, or \(|A|=1\). In the latter case, writing \(A=(a)\),
\[
H-a=(x,p_m,p_{m-1},B)\mid Q
\]
is a deletion cover at \(a\).

Moreover, after choosing \(R\) as the order of the first support in the deletion cover at \(x\), the deletion covers at \(x\) and \(a\) are compatible on their common domain. They share the support \(Q\), and on the other common support
\[
P-\{a\}=\{p_m,p_{m-1}\}\cup B
\]
they induce the same order \((p_m,p_{m-1},B)\). Equivalently, the omitted labels \(a\) and \(x\) occupy the same initial insertion slot of this common ordered support.

**Proof.** The displayed end-edge reversal lemma gives a two-cover, a strict decrease of \(\Phi\), or the neutral case \(|A|=1\). The strict-decrease alternative is impossible at the chosen minimum. In the neutral case boundary reversal gives
\[
(x,p_m,p_{m-1})
\]
tight, and the suffix \((p_m,p_{m-1},B)\) is inherited from the Hamilton order \(R\). Hence
\[
(x,p_m,p_{m-1},B)
\]
is a tight path. Together with \(Q\) it covers \(H-a\), proving the deletion-cover assertion.

For compatibility, restrict both deletion covers to \(H-\{x,a\}\). The fixed support \(Q\) is unchanged. The other support is \(P-\{a\}\) in both covers, and using the Hamilton order \(R\) at \(x\) gives exactly the order \((p_m,p_{m-1},B)\), which is also inherited from the deletion cover at \(a\). Thus the restricted covers are compatible. Both omitted labels are restored before \(p_m\), so their insertion slots coincide. \(\square\)

This identifies the neutral branch of defect compression with the support-compatible deletion-cover regime of Article I. Repeated neutral end-edge reversals therefore generate a family of deletion covers with a fixed support and a varying support, rather than an unconstrained family of three-cover states. Once three distinct deleted labels occur in such a compatible family, the localization machinery applies directly.

**Remaining Lemma.** Starting from a \(\Phi\)-minimum singleton lift, suppose the fixed-deletion transport reaches either
1. a displayed end-edge reversal; or
2. a Hamiltonian support of order four or five carrying a displayed endpoint, with two-coverable complement.

Then either \(H\) has a two-cover, or the resulting neutral root exchanges extend to a support-compatible family large enough for the deletion-cover compatibility machinery to force a spanning ordering \(\sigma\) with
\[
\nu(L_\sigma)\le1.
\]

In the two-cut normal form, the unresolved task is thus narrower than before: show that the endpoint-rooted bounded-support alternative either creates a third compatible deletion root or makes one of the two necessary defect-cover cuts redundant.

## Metadata

- ID: defect_lines_and_spanning_order_compression_the_remaining_lemma
- Kind: section
- Version: 3
- Math version: 3
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Subsection 1 — HOT, version 3: (untitled)
