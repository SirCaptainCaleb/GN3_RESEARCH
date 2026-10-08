# A persistent span-two occurrence permits a central three-position block — preserved pre-item development

## Development

## Audit: a persistent positive span-two occurrence need not have a fixed middle status

A positive span-two occurrence is the disjunction 001 or 011. Equivalently its first status is 0 and its third status is 1; its middle status is unrestricted. Thus the proof of Lemma 1 in [[double_persistent_faces_have_bounded_block_width_and_rank_one_span_boundaries]] does not establish its asserted bound of two positions for every block.

**Correct footprint statement.** A face block meeting a persistent five-position window in at least three positions can do so only in the central three positions. Consequently every such footprint has size at most three, and a block crossing either outer endpoint of the window has footprint at most two.

**Proof.** Write the window positions as 1,...,5. A block footprint is an interval. If it includes positions 1,2,3, reverse the endpoint labels of that triple while fixing all other orders; boundary antisymmetry flips the first status, contradicting its persistent value 0. If it includes 3,4,5, the same operation flips the third status, contradicting its persistent value 1. Any interval of length at least four contains one of these triples; the only surviving interval of length three is 2,3,4. An interval crossing an outer window endpoint cannot be that central interval. ∎

**The central-three exception is genuine, even for a protected double-persistent face.** Take n>=13 positions and a face with only positions 2,3,4 in one free three-vertex block; all other positions are singleton blocks. Prescribe, for every chamber, the status word
\[
0\,t\,1\,0^{n-8}\,001,
\]
where t is the status of the ordered triple of free vertices. This has length n-2. Prescribe the first status 0 for every ordered pair of free vertices following position 1, and the third status 1 for every ordered pair preceding position 5. Prescribe all remaining displayed statuses uniformly. These prescriptions concern distinct boundary-reversal orbits, so extend to a boundary tournament; the internal three-vertex orientations may be arbitrary.

The first window has word 001 or 011 according to t, and the last window has word 001. Both persist. No interior start has word 001 or 011, and no interior alternating word 0101 occurs. Therefore the face is protected at the reflected outer span-two depth while its left window contains a free central three-block. Reversal of the free triple changes t without destroying persistence.

This correction preserves the endpoint reservoir bound of two, the separate inward five-position bound, and the persistent-face sign construction. It does not license a fixed-word argument for the central three positions. No conclusion of grand closure is drawn.
