# Audit: pair insertion cancellation requires local tetrahedral flatness — preserved pre-item development

## Scope correction and a local pair-extension lemma

This audits subsection 103. Work with an alternating ternary orientation alpha, not an arbitrary reversal-odd h. Let O=(v_1,...,v_m) have word 0^p 1^q and let s_i^x=alpha(x,v_i,v_{i+1}), c_i=alpha(x,y,v_i). Define
kappa_i=delta alpha({x,y,v_i,v_{i+1}}).
The four-face parity identity gives
c_i xor c_{i+1}=s_i^x xor s_i^y xor kappa_i.
Thus identical scans imply c_i xor c_{i+1}=kappa_i, rather than constant c_i in general. A tournament switching-class representative exists in the coboundary-flat sector; using it for all alternating orientations silently assumes the missing flatness.

A useful repaired theorem requires only local flatness. Suppose both omitted vertices have scan B=1^(p+1)0^q, with p,q>=2, and kappa_p=0. Orient the pair so c_p=c_{p+1}=1 and insert it between v_p and v_{p+1}. The four new statuses are s_{p-1}^x,c_p,c_{p+1},s_{p+1}^y=1,1,1,1. The untouched prefix is 0^(p-2), and the untouched suffix is 1^q. This is a spanning one-change extension on O union {x,y}. Global coboundary flatness is unnecessary; flatness of this one tetrahedron suffices.

The unrestricted assertion has a small symbolic obstruction. Take O=(v_1,...,v_6), with alpha-word 0011. Prescribe both scans to be 11100 and prescribe c_2=0,c_3=1; choose other c_i arbitrarily. These prescriptions concern disjoint underlying triples, so they extend to an alternating orientation on eight vertices by assigning all remaining triples arbitrarily and extending by permutation parity. They give kappa_2=1.

Each single vertex blocks every insertion: prepend and append produce respectively 10011 and 00110; the five internal gaps produce 01011,10111,01001,00110,00101. Every word has at least two changes. For consecutive pair insertion, either pair order fails in all seven gaps:
- before v_1, the unchanged tail contains the pattern 1,0,1;
- after v_1, the fixed tail statuses include 1,0,1;
- after v_2, the local packet is 1,c_2,c_3,1 or its pair-reversed version, and hence contains 1,0,1;
- after v_3, fixed statuses include 0,1,0,1;
- after v_4, fixed statuses include 0,1,0;
- after v_5, fixed statuses include 0,1,0;
- after v_6, the unchanged old word followed by scan value 0 includes 0,1,0.
Patterns here may be subsequences, which already certify at least two changes.

This is a counterexample to universal cancellation by consecutive insertion into a prescribed carrier, not a counterexample to NOR: other orders remain available.

There is also a boundary improvement. A genuinely perfect insertion blocker cannot occur when p=1 or q=1. If p=1, failure of prepend forces s_1=1, and insertion after v_1 gives (1-s_1),s_2 followed only by old 1's, hence a one-change word. If q=1, failure of append forces s_{m-1}=0, and insertion just before v_m gives an old all-0 prefix followed by s_{m-2},1-s_{m-1}, again one-change. Therefore any surviving pure-orientation one-vertex insertion obstruction has both runs of length at least two.

Consequently the valid combination of subsections 99,102,95,103 is: choose a tournament representative inside a switching class in the flat sector; use bidirectional flat endpoint repairs and audited two-or-three-position switch transport; invoke pair extension when the switch tetrahedron is flat. The missing global statement is termination or escape from closed components of the repair graph. No monotonic termination principle has yet been proved.
