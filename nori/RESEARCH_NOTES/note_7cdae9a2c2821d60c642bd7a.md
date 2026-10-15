# At least two factorial monochromatic paths in the cube threshold class

- Stable ID: note_7cdae9a2c2821d60c642bd7a
- Author: unspecified; session provenance retained
- Primary home: section:nori_type_a_rook_gallery_topology
- Labels: coxeter-cosets, threshold, quantitative
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r7547_3
- Updated session: session_nori_r7547_3
- Disposition: none
- Successor: none

## Related references

- subsection:linear_threshold_coset_colorings_admit_one_switch_full_paths

## Research note

**Theorem.** Let \(n\ge2\), and let \(c_\theta\) be the antipodally odd cube-edge coloring
\[
c_\theta(\{y,y\oplus e_i\})=
\mathbf1_{\{\sum_{j\ne i}(-1)^{y_j}\theta_j<0\}},
\]
where each threshold expression is nonzero. Then \(c_\theta\) has at least \(2n!\) distinct rooted-and-ordered monochromatic full antipodal geodesics.

*Proof.* Choose the root \(x\) with \((-1)^{x_i}\theta_i=|\theta_i|\), and let \(\pi\) run through all \(n!\) dimension orders. The linear-threshold theorem established in this Article shows that each corresponding full-geodesic word has at most one switch. Each Coxeter root-slide orbit has \(2n\) flags, and its color word is antiperiodic after \(n\) slides. Thus its cyclic derivative has one change in each run of \(n\) positions, and precisely two of the \(2n\) starting positions generate a monochromatic length-\(n\) word.

The \(n!\) flags \((x,\pi)\) occupy pairwise distinct root-slide orbits. Each nonidentity root-slide power \(t^k\), \(0<k<2n\), changes the initial root by a nonzero sum of distinct dimension vectors; hence no nonzero slide can take one flag based at \(x\) to another flag based at \(x\). Therefore there are at least \(n!\) different root-slide orbits of the required type, and each contains two monochromatic rooted geodesics. \(\square\)

The count distinguishes oriented rooted geodesics, including path reversals. It strengthens the threshold special case and does not assert the same quantitative bound for unrestricted NORI1 colorings.
