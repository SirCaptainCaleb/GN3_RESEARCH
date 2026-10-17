# Ten-path decision-tree certificate for four-cube internal critical-edge repair

- Stable ID: note_nori_q4_ten_path_critical_surgery_r11435
- Author: unspecified; session provenance retained
- Primary home: subsection:full_geodesic_color_profiles_span_the_entire_binary_space
- Labels: NORI1, critical-orbit, red-geodesic, Q4, constructive-certificate, proof-mining, orbit-recoloring, dimension-four
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11435_4
- Updated session: session_nori_r11435_4
- Disposition: none
- Successor: none

## Related references

- note:note_6f6b320f698318cecb8efd89
- note:note_143f396e6155ca89c587d00f

## Research note

# Ten-path constructive certificate for an internal red pivot in Q4

Let c be any legal antipodally odd undirected-edge coloring of Q4, and suppose it has an all-red full antipodal geodesic P containing red edge e strictly internally. Then there is an all-red full geodesic either avoiding the antipodal orbit {e,bar(e)} or using e as its first or last edge. Therefore orbit recoloring at {e,bar(e)} preserves all-red geodesic existence.

**Proof.** Reverse P if needed; translation and direction relabeling normalize e=(0,1), P rooted at integer vertex 2 with direction order (1,0,2,3). Represent the sixteen antipodal edge orbits by (i,min(a, (15 xor a) with i-th bit removed)), ordered by i, then by canonical base a. Let z_j denote the color on the canonical edge of orbit j. The four red edges of P fix four orbit bits and leave twelve free. The ten paths in the following table are red precisely under the indicated free-bit conditions (all omitted edge colors are already forced red):

Root; order; conditions:
0; (0,2,1,3); z7=0,z12=1.
0; (1,0,2,3); z1=0,z11=0,z12=1.
0; (1,0,3,2); z1=0,z8=1,z15=0.
1; (2,3,0,1); z1=1,z5=1.
3; (0,1,3,2); z1=0,z11=1,z12=0.
3; (1,2,3,0); z1=1,z5=0.
4; (2,1,0,3); z1=0,z8=0,z15=0.
4; (3,2,1,0); z2=1,z7=1,z11=1,z15=1.
5; (0,3,2,1); z2=0,z7=1,z11=1,z15=1.
7; (2,0,1,3); z1=0,z11=0,z12=0.

They cover all free-bit assignments by a short case distinction. If z1=1, use one of the two entries with z1=1 according to z5. If z1=0,z11=0, use one of the entries rooted at 0 and 7 according to z12. If z1=0,z11=1,z12=0, use the entry rooted at 3 with order (0,1,3,2). If z1=0,z11=1,z12=1,z7=0, use root 0 order (0,2,1,3). In the remaining z7=1 branch, if z15=1 choose the entries rooted at 4 or 5 according to z2, and if z15=0 choose the entries rooted at 0 or 4 according to z8. Each of the listed paths avoids e and bar(e) or traverses e as its first or last edge, as checked directly from its root and direction order. In the endpoint case cyclic root rotation replaces e by bar(e) while complementing just that edge color, so after orbit flipping the rotated path is red. QED.

**Computational provenance.** The ten paths were obtained from a minimum-set-cover search among the 104 distinct forbidden-red-path events after fixing P. The self-contained verifier q4_critical_ten_path_certificate.py checks the geometry, orbit sign conventions and coverage for all 2^12=4096 free assignments. The displayed case distinction proves the result independently of numerical optimization. Expanded derivation: q4_ten_path_internal_critical_certificate.md.

**Scope.** This is a concise constructive proof of the previously computationally known Q4 internal-pivot exclusion, not a new dimension-uniform NORI1 mechanism. It does not automatically lift to a four-dimensional face inside Qn: the antipodal mate of an edge in that face belongs to its globally opposite face when n>4. Transporting the ten candidates would require red entrance/exit arms simultaneously compatible with those two opposite faces, which is not established.
