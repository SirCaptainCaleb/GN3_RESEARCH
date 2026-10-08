# Separated window outward loci are products and can be disconnected

## Composition

(none yet)

## Development

## The exact outward-locus product

Let F be protected at a fixed reflected span-two depth r, and suppose an ordered-block boundary separates its two determining windows. Write F=F_L times F_R by grouping the blocks on the two sides. Let D_L be the subcomplex of F_L consisting of faces on which the left occurrence is absent in every chamber; define D_R symmetrically. Then
\[
D_r(F)=X_{r+1}\cap F=D_L\times D_R.
\]
A product face is outward precisely when both occurrence indicators vanish on every pair of its chamber factors. Protection is automatic inside F. Thus block independence proves the product formula and nonemptiness when each factor has an absent occurrence. It does not prove that the factors are contractible.

## A family with nine disconnected outward chambers

For any n>=13, partition the vertices into a free first block A of order three, singleton middle blocks, and a free last block B of order three. This gives a proper face F=P_3 times P_3. Give each of A and B a cyclic three-vertex orientation: in an order a,b,c of its vertices, the tight orders are abc,bca,cab and the reverse orders are non-tight.

Prescribe mixed boundary triples so that every chamber of F has status word
\[
T_L\,11\,0^{\,n-6}\,T_R,
\]
where T_L and T_R are the internal statuses of its first and last triples. The displayed word has n-2 statuses. Such prescriptions are consistent: each variable or fixed status uses a distinct unordered triple support except for permutations at the free boundary blocks, and the mixed statuses can be fixed uniformly by choosing one representative of each reversal pair. For example, if the first two singleton vertices are u,v, set h(a,b,u)=h(a,u,v)=1 for distinct a,b in A; use the reversed construction for the last boundary. Assign all remaining reversal pairs arbitrarily.

The only possible positive witnesses are 011 at start 1, present when T_L=0, and 001 at start n-4, present when T_R=1. Every positive witness strictly between those reflected starts is absent in every chamber. Thus F is protected at that fixed depth.

Its outward chambers are exactly T_L=1,T_R=0. There are three choices for each factor, hence nine outward chambers. In the S_3 permutahedron the three cyclic orders are pairwise nonadjacent: an adjacent transposition changes parity and leaves the tight-order set. Therefore each single-sided outward subcomplex consists of three isolated vertices, and D_r(F) consists of nine isolated vertices. It is neither connected nor acyclic.

The word count above also verifies that no negative forbidden-word condition is being imported.

## Consequence for a natural carrier

Any sign convention retaining the forced signs of single-sided occurrences makes F mixed: it contains left-only and right-only chambers. Hence the separator face poset contains F and each of its outward chamber vertices. A D_r-carried continuous map would fix every outward chamber, because its point face has itself as the sole outward carrier. The barycentric edge from any such chamber to F would have to map into the discrete set D_r(F). It must therefore be constant, forcing the image of the barycenter of F to equal all nine different chambers. This is impossible.

This is a counterexample to a universal local claim that product-splicing implies outward-locus acyclicity or a natural D_r-carried extension. It is not a counterexample to the grand conjecture or to a theorem whose global counterexample hypothesis supplies additional, presently unspecified constraints.

A successful global construction must either use stronger hypotheses on the single-sided loci or permit larger outward carriers leaving the source face. The persistent-orientation theorem remains valid; the extra topology cannot be obtained from its product splice alone.
