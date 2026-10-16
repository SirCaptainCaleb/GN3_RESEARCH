# Hamming-layer barriers admit exponentially many paired-root repairs

- Stable ID: note_nori_hamming_layer_mass_paired_activations_20261015
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: counterexample, root-activation, extremal
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r9446_2
- Updated session: session_nori_r9446_2
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Let m>=3 and 1<=r<=m-2. Color a cube edge in Q_m one if and only if its endpoints have Hamming weights r and r+1, and color all remaining edges zero. Every full geodesic from 0^m to 1^m has color word 0^r 1 0^(m-r-1), and its reverse has word 0^(m-r-1) 1 0^r. Therefore neither antipodal endpoint belongs to A_0(g), the roots admitting a 0*1* full path. Yet for EVERY edge e joining these two Hamming layers, a full geodesic through e exists and has e as its sole one-colored edge. Recoloring e zero produces a monochromatic full antipodal geodesic from each endpoint and hence makes both previously empty roots favorable. There are (m-r) binomial(m,r) such distinct repairs, of order sqrt(m) 2^m when r is central. This proves that activation multiplicity and simultaneous root-pair repairs alone cannot force a previously favorable root. A closing proof must exploit the global requirement that no antipodal root pair is simultaneously favorable, rather than count restorations for an isolated root pair.
