# Complete-influence parity-class paired-root isolation and even-dimensional amplification

- Stable ID: note_nori_ordinary_paired_root_parity_isolation_r11435
- Author: unspecified; session provenance retained
- Primary home: subsection:dihedral_full_path_symmetry_and_the_root_gluing_obstruction
- Labels: NORI1, paired-root, ordinary-facets, root-transport, independent-paired-root-set, complete-influence, nonlinear, negative-result, Cartesian-product
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11435_4
- Updated session: session_nori_r11435_4
- Disposition: none
- Successor: none

## Related references

- note:note_nori_paired_gallery_separation_r11435

## Research note

# Parity-class isolation of paired roots in a fully interacting ordinary four-cube

**Theorem (dense nonlinear isolated paired roots).** There is an ordinary binary undirected-edge coloring f of Q4 with every ordered influence j->i (i != j) present, such that its paired-root set P(f)=A_0(f) intersection A_1(f) consists of ALL eight vertices of odd Hamming weight. Thus P(f) is nonempty and is an independent set in the cube's root-adjacency graph. Four of its paired roots admit NO monochromatic full path from that root.

An explicit coloring, with the labels x0,x1,x2,x3 and Boolean operations OR, AND, XOR, NOT, is
 f0 = x1 OR (x3 AND NOT x2),
 f1 = x0 OR (x2 XOR x3),
 f2 = x3 AND (x0 OR x1),
 f3 = (NOT x2) AND (x0 XOR x1).
Each f_i ignores x_i. Checking each other variable shows every one of the twelve directed influences is present.

**Finite certificate.** Fix the integer encoding x=sum_j 2^j x_j. Enumerating all 24 full direction orders at each root gives:
 A_0={0,1,2,4,5,6,7,8,11,12,13,14},
 A_1={1,2,3,4,7,8,9,10,11,13,14,15},
 P=A_0 intersection A_1={1,2,4,7,8,11,13,14},
 M={1,2,13,14},
where A_0 denotes starting roots with nondecreasing full-path color word, A_1 those with nonincreasing word, and M roots with a monochromatic full path. A_1 is obtained from A_0 by antipodal root complementation, via reversing each full path. In particular, the vertex x=4 is paired, supporting direction order (0,2,3,1) with word 0011 and (1,0,2,3) with word 1100, while 4 is not in M. Since every element of P has odd parity, P has no adjacent vertices.

**Uniform even-dimensional amplification.** For every k>=0 there is an ordinary coloring of Q_(4+2k) whose paired-root set is nonempty and independent, with paired roots admitting no monochromatic full path. Take the above Q4 coloring in one independent block and k copies of the Q2 coloring h0=y1, h1=y0 in other blocks. The Q2 paired set is {01,10}, which is independent. For independent Cartesian products, restricting a rising/falling full path to its direction blocks gives corresponding rising/falling full paths in each block; conversely concatenate the zero phases of block witnesses and then all one phases. Hence P(product)=Cartesian product of each block's P. A Cartesian product of independent vertex sets in the factors is an independent set of the product cube. The root with Q4 part 4 and Q2 parts 01 is paired but has no monochromatic full path, because any such full path would project to a monochromatic Q4 full path from 4. QED.

**Research implication.** A paired ordinary-facet root with no monochromatic geodesic need not have a paired root across ANY of its incident edges, even when every direction reads every other direction. Local one-step root transport of paired witnesses cannot serve as a universal mechanism to eliminate the internal-pivot bottleneck. This counterexample does not exclude nonlocal transport, and it is NOT a legal NORI1 counterexample: an ordinary facet need not satisfy antipodal oddness. The result is separate from the earlier order-gallery separation obstruction; here roots, not permutations, are isolated.

Full executable finite certificate: /mnt/data/nori_research/paired_root_parity_barrier.py.
