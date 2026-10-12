# Rooted monochromatic reachability violates delta-matroid symmetric exchange

- Stable ID: note_nori_xi_rooted_monochromatic_family_not_delta_matroid
- Author: unspecified; session provenance retained
- Primary home: section:nori_matroid_generalizations_conjectures
- Labels: boundary-tournaments, delta-matroid, exchange-obstruction, rooted-reachability, finite-certificate
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6430_2
- Updated session: session_nori_r6430_2
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Research obstruction: rooted monochromatic reachable vertex-subset families need not be delta-matroids, even after forgetting the ordered penultimate endpoint. Work on n=5 original vertices V={0,1,2,3,4}. Reversal-orbit representatives (a,b,c) with a<c are ordered by increasing middle b and then ascending outer pair a<c. Put the representative-bit mask M=0x9c444a9 and reverse colors by b(c,b,a)=1-b(a,b,c). For root v=0 and epsilon=0, the complete family A_0^0 of subsets S⊂{1,2,3,4} represented by injective color-0 tight words ending at 0 is:
 ∅, {1}, {2}, {3}, {4}, {1,3}, {1,4}, {2,4}, {1,2,3}, {1,3,4}, {1,2,3,4}.
Choose feasible X={2,4}, witnessed by (4,2,0), whose sole triple has color 0, and feasible Y={3}, witnessed by (3,0) vacuously. Their symmetric difference is {2,3,4}. For u=3 in X Δ Y, symmetric-exchange feasibility would require at least one of X Δ {3}={2,3,4}, X Δ {3,2}={3,4}, X Δ {3,4}={2,3} to be feasible. All three are absent from the displayed complete rooted family. Hence Bouchet's delta-matroid symmetric-exchange axiom fails. Full family independently verified by enumerating all injective tight words of length 1..5 and testing every consecutive triple color. This does not contradict the rooted complementary pair theorem or the spanning one-turn conjecture. It blocks an argument that regards individual rooted monochromatic reachability families as delta-matroids, even though their underlying resources live in graphic matroids. An eventual exchange theorem must connect TWO arms, different roots, or additional ordered-terminal data.
