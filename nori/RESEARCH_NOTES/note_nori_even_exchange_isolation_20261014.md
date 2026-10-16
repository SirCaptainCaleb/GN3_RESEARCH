# Isolated projective Petrie cycles under cyclic square exchanges

- Stable ID: note_nori_even_exchange_isolation_20261014
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: obstruction, counterexample, exchange
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r9311_2
- Updated session: session_nori_r9344_2
- Disposition: none
- Successor: none

## Related references

- subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths

## Research note

**Theorem (isolated projective Petrie cycles at every even rooted switch level).** Fix even \(t\ge2\) and \(n\ge3(t+1)\). Some antipodally odd binary coloring of \(E(Q_n)\) has both a monochromatic full antipodal geodesic and a projective Petrie cycle \(C\) of switch-orbit count \(q(C)=t+1\) such that every cyclic adjacent-direction square exchange produces a cycle \(C'\) with \(q(C')=t+3\). Here \(C\) is a full antipodal geodesic followed by its antipodal image, and \(q\) is half the number of cyclic color changes. Petrie root rotations preserve \(q\), so even allowing arbitrary such rotations there is no non-increasing exchange route from \(C\) to a monochromatic cycle.

*Proof.* Take the canonical geodesic \(P\) from \(0^n\), traversing dimensions \(1,\ldots,n\), and prescribe a binary word \(w\) with \(t+1\) alternating constant runs, each of length at least three, beginning and ending in zero. On the length-\(2n\) antipodal cycle \(C\), the word is \(w\bar w\) and the \(t+1\) switch orbits are separated by at least three edges.

For every one of the \(n\) cyclic consecutive direction pairs in \(C\), prescribe the two replacement edges of the associated square exchange. These \(2n\) replacement edges and the \(n\) original edges occupy distinct antipodal edge-pair orbits. Put \(S_k=\{1,\ldots,k\}\). In direction \(i\), the original lower endpoint has support \(S_{i-1}\), and the ordinary square replacements have supports \(S_{i-2}\) if \(i\ge2\), and \(S_{i-1}\cup\{i+1\}\) if \(i<n\). The wraparound square between dimensions \(n\) and \(1\) adds the support \(\{2,\ldots,n-1\}\) in directions \(1\) and \(n\). These supports are pairwise distinct within each direction, and none is antipodal to another when \(n\ge9\).

At any cyclic adjacent pair, let \(L,R\) be the unchanged outer neighboring colors. The old four-entry window has no switch if \(L=R\), and one switch otherwise, since run lengths are at least three. Give the two replacement edges colors \((1-L,L)\). The new window has respectively two or three switches, an increase of two. Its antipodal copy adds another two; hence \(q(C')=q(C)+2\). All these prescriptions are compatible by the orbit disjointness.

For a monochromatic witness, start instead at a vertex of Hamming weight three and traverse the dimensions in the same order. Its direction-\(i\) lower support differs from \(S_{i-1}\) in two or three bits. Each constrained support or its antipode differs from \(S_{i-1}\) in at most one or at least \(n-2\) bits, including the wraparound constraints. Thus the witness avoids every prescribed orbit. Color its edges zero, their antipodal mates one, and extend arbitrarily over remaining pairs. QED.

Every rooted half-cycle of \(C\) has at least \(q(C)-1=t\) switches, with equality for some root rotations. This rules out general non-increasing Petrie-exchange descent without refuting NORI1.
