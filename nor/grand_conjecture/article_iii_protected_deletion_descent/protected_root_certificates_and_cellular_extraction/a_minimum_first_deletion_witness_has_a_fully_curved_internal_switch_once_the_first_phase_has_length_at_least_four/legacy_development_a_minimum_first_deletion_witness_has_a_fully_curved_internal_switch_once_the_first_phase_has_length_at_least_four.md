# A minimum-first deletion witness has a fully curved internal switch once the first phase has length at least four — preserved pre-item development

## A minimum-first deletion witness has a fully curved internal switch once the first phase has length at least four

Work in the coboundary-flat alternating ternary sector of a minimum counterexample.

Choose a genuine one-change deletion witness

O=(v_1,...,v_m)

with normalized word

0^p 1^q,

where p is globally minimum over all one-change deletion witnesses after allowing reversal and global color complement.

Assume p>=4.

Let T be the unique internal transition between window ranks p and p+1. Its supporting ordered tetrahedron is

(v_p,v_{p+1},v_{p+2},v_{p+3}).

### Theorem

T is fully curved.

### Proof

Suppose T were flat. In the coboundary-flat ternary sector, a flat transition admits both endpoint repairs.

Use the LEFTWARD endpoint repair, swapping the first pair v_p,v_{p+1}. By the audited corrected transport law, a successful endpoint repair deletes the old transition and either:

1. creates the unique replacement transition two ranks to the left; or
2. creates it three ranks to the left;

unless it collides with an already existing transition and annihilates.

But O has exactly one transition. Hence no collision with another transition is possible.

Because p>=4, the entire target position p-2 or p-3 is a legitimate linear window boundary. Every transition bit outside the local affected packet is unchanged. Therefore the repaired deletion order O' again has exactly one transition.

The first and last untouched portions retain colors 0 and 1, so O' has normalized one-change word

0^{p-d}1^{q+d}

for d in {2,3}.

In particular p-d<p.

This contradicts the global minimality of p.

Hence T cannot be flat. Since every transition tetrahedron in the coboundary-flat sector is flat or fully curved, T is fully curved. QED.

### Endpoint consequence

Let x be the coordinate omitted by O. Prepending x produces a bad full order. Counterexamplehood forces the new first ternary window to have color 1; otherwise the full word would still be one-change. Thus the full order begins

1,0^p,1^q.

The initial 1->0 endpoint transition is the established fully-curved endpoint blocker, while the internal 0->1 transition of O is fully curved by the theorem above.

Therefore, for every globally minimum-first witness with p>=4, the prepended full order contains an isolated 0-band of length p bracketed by TWO fully-curved barriers, with no perfect-blocker scan hypothesis.

This supplies a canonical double-full isolated-band state in the arbitrary-scan endpoint regime. It is not the five-coordinate singleton gadget unless p=1; the remaining task is to exploit the two full boundaries of a long band or shorten the band while preserving minimum-first provenance.

The cases p<=3 require separate endpoint-clipped analysis and are not claimed here.
