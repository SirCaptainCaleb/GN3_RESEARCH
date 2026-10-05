# Two-cover status words avoid three local patterns

**Summary:** A binary status word satisfies the exact two-cover condition q<=p+1 iff it contains none of 001, 011, or 0101 as a consecutive subword. Equivalently, every bad word has a local witness on at most four consecutive status positions.

## Statement

Let epsilon_1...epsilon_m be a binary status word, with p the first 0 and q the last 1 using the usual conventions. Then q<=p+1 iff the word avoids the consecutive patterns 001, 011, and 0101. Equivalently, if q>=p+2, there is a minimal inversion pair i<j with epsilon_i=0, epsilon_j=1 and j-i>=2; its span is 2 or 3, yielding 001/011 or 0101.

## Body

# Two-cover status words avoid three local patterns

Let

`epsilon_1...epsilon_m`

be a binary status word. Put `p` for the first zero and `q` for the last one, with the usual endpoint conventions. The exact inversion-window criterion says that the corresponding spanning order yields a two-cover exactly when

`q<=p+1`.

This condition has a purely local forbidden-pattern form.

## Proposition

The following are equivalent:

1. `q<=p+1`;
2. there are no indices `i<j` with `epsilon_i=0`, `epsilon_j=1`, and `j-i>=2`;
3. the word contains none of the consecutive subwords

`001`, `011`, `0101`.

**Proof.** The equivalence of (1) and (2) is immediate from the definitions of the first zero and last one.

Assume (2) fails and choose an inversion pair `i<j` with `epsilon_i=0`, `epsilon_j=1`, `j-i>=2` having minimum span.

If `j-i=2`, the three-position subword is either `001` or `011`.

Suppose `j-i>=3`. Minimality implies that every position `k` with `i<k<=j-2` must have `epsilon_k=1`, since a zero there would give the shorter inversion `(k,j)`. Likewise every `k` with `i+2<=k<j` must have `epsilon_k=0`, since a one there would give the shorter inversion `(i,k)`. If `j-i>=4`, these two ranges overlap, a contradiction. Hence `j-i=3`. The two interior bits are then forced to be `1,0`, so the four-position subword is `0101`.

Conversely each of `001`, `011`, and `0101` visibly contains a zero followed at distance at least two by a one, so (2) fails. ∎

Thus badness of a spanning order is always witnessed on at most four consecutive status positions, equivalently on at most six consecutive vertices of the order.

Under reversal-complement, `001` and `011` are exchanged, while `0101` is fixed. This local symmetry is useful for antipodal labeling arguments.

## Metadata

- ID: two_cover_words_avoid_three_local_patterns
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: passed
- Refutation: unrefuted
- Toolkit status: Limbo
