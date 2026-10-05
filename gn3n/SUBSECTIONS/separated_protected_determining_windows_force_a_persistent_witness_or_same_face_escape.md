# Separated protected determining windows force a persistent witness or same face escape

## Metadata

- ID: separated_protected_determining_windows_force_a_persistent_witness_or_same_face_escape
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 96
- Row version: 2
- Development version: 1
- Composition version: 1
- Composition stale: False

## Cold composition

### Persistence-or-escape on separated windows

Suppose the two protected determining windows of a reflected span are separated far enough that a face-block boundary lies between them. Then the chamber choices on the two sides factor. If both a left-only and a right-only chamber occur, the product face contains a chamber in which the selected witness has moved strictly outward. Otherwise one of the two reflected occurrences persists throughout the face. Thus every separated protected carrier has either a same-face outward chamber or a persistent reflected witness orientation.

## Development

## Elevating the five-position obstruction to the separator step

Work with the positive witness language {001,011,0101}. Fix a noncentral reflected span-two depth r with starts a<b, whose determining vertex intervals are
\[
I_L=[a,a+4],\qquad I_R=[b,b+4].
\]
For a chamber pi in a protected ordered-partition face F, let L(pi),R(pi) indicate positive span-two occurrences at those two starts. Protection excludes all positive witnesses strictly inward of this reflected pair. At depth r there are exactly these two possible occurrences.

**Lemma.** If b-a>=8, F has an ordered-block boundary after some position j with
\[
a+4\le j\le b-1.
\]

**Proof.** Otherwise all positions a+4,...,b lie in one block. There are at least five such positions. Choose five consecutive positions inside that interval. All three internal status positions have starts strictly between a and b. The words 001 and 011 there would be strictly inward witnesses and are forbidden in every chamber of F. Every order of the five chosen block vertices is available, contrary to the five-position obstruction in [[verified_five_position_obstruction_and_ordered_tuple_compression]]. ∎

**Theorem (persistent orientation or same-face escape).** Under these hypotheses, at least one of the following holds:
1. some chamber of F has neither depth-r occurrence and is therefore outward;
2. every chamber of F has the left occurrence;
3. every chamber of F has the right occurrence.

**Proof.** The block boundary supplied by the lemma separates the complete determining windows. Consequently F is a product of its prefix and suffix block-order choices, and L depends only on the prefix factor while R depends only on the suffix factor.

If L vanishes in some chamber and R vanishes in some chamber, combine the former chamber's prefix block orders with the latter chamber's suffix block orders. The resulting chamber belongs to F and has L=R=0. Protection is retained because every chamber of F is protected. This gives outcome 1.

If no such combination is possible, L never vanishes or R never vanishes, giving outcome 2 or 3. ∎

Equivalently, if F has no outward chamber then
\[
\bigcap_{\pi\in\mathcal V(F)}
\bigl(\{+:L(\pi)=1\}\cup\{-:R(\pi)=1\}\bigr)
\ne\varnothing.
\]
Thus a long reflected double is not, by itself, a forced signed separator. On this fixed face one may assign every depth-r chamber the same available orientation. Intrinsically single-sided chambers receive their forced sign; chambers with both occurrences receive the persistent sign. Reverse the assignment on the antipodal face. This removes all depth-r sign-flip edges inside that face without repairing its long determining span.

The quantitative consequence is precise: a protected face with no outward chamber and no persistent orientation can have full determining span of at most twelve vertices, since its length is b-a+5. This is a bound on the obstruction to a local sign choice, not a two-cover theorem for twelve vertices.

Independent choices on different ambient faces may disagree on their common chambers, especially where both occurrences persist. The theorem proves the local statement only. Global equivariant compatibility must be supplied before using these relabelings in a genus iteration.
