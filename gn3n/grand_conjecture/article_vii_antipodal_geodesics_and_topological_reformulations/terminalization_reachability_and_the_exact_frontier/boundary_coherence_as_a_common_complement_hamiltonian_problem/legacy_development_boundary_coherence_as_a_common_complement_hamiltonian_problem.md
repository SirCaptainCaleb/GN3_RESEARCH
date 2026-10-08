# Boundary coherence as a common-complement Hamiltonian problem — preserved pre-item development

## Composition

(none yet)

## Development

## Boundary coherence reduces to a common complementary Hamiltonian pair problem

Consider the only nontrivial rank-two coherence situation left after terminal edge reduction: two bounded terminal supports differ by one boundary vertex. Write
[
S=Acup{x},qquad S'=Acup{y},
]
where the common core (A) has order nine (the smaller support sizes are analogous and easier).

A particularly clean sufficient compatibility condition is the existence of a five-set
[
Bsubset A
]
such that (H[B]) is Hamiltonian and, with
[
C=Asetminus B,qquad |C|=4,
]
both five-sets
[
Ccup{x},qquad Ccup{y}
]
are Hamiltonian.

Indeed, choose a Hamilton order on (B), and Hamilton orders on (C+x) and (C+y). Then the two adjacent terminal supports (S,S') admit two-covers sharing the entire Hamiltonian side (B). Their terminal surgeries can therefore be chosen with the same order on the common core side, while only the one boundary vertex changes. This supplies exactly the deletion-compatible local replacement needed to extend the edge assignment across the corresponding Coxeter residue.

Thus boundary coherence is implied by the following finite statement:

**Common-complement lemma.** For every boundary tournament on (Acup{x,y}), with (|A|=9), there is a Hamiltonian five-set (Bsubset A) such that both (Asetminus B+x) and (Asetminus B+y) are Hamiltonian.

The existing small-set density bounds nearly force this by counting. For each of (x,y), the family of bad four-sets (Csubset A) for which (C+x) (respectively (C+y)) is non-Hamiltonian is strongly sparse by the four-of-six/Johnson-density theory. The ten-vertex two-cover theorem also guarantees many complementary Hamiltonian (5|5) partitions. The remaining issue is an extremal-overlap question: rule out the possibility that every Hamiltonian (Bsubset A) has its complementary (C=Asetminus B) bad for at least one of (x,y).

This is a sharper finite target than arbitrary endpoint-compatible terminal surgery. It asks for one common Hamiltonian side across two one-vertex extensions of a nine-vertex core and is naturally suited to the existing Johnson-density/equality machinery in [[extremal01]].
