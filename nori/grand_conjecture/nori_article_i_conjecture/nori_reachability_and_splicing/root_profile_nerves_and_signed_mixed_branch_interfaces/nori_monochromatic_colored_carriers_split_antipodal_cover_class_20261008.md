# Monochromatic colored-state carriers split the antipodal cover; connector parity survives independently

# Color-preserving path carriers have trivial antipodal cover class

Inputs: nori_window_shift_monochromatic_edges_universal_cohomology_class_20261008 and literature_fixed_point_theorems. This gives a precise transport constraint for the new window parity class.

## 1. The monochromatic-shift subgraph splits the double cover
Let H be the graph of actual ordered three-face windows, with shifts realized by genuine four-edge geodesics. Let tau(F,pi)=(bar F,rev pi), and let c(tau v)=1-c(v). Let H_mono be the spanning subgraph retaining exactly edges uv with c(u)=c(v).

Then c:|H_mono| -> {0,1} is continuous and equivariant (tau exchanges 0 and 1). The two color subgraphs are exchanged by tau. The quotient double cover
 H_mono -> H_mono/tau
is TRIVIAL: each quotient vertex and edge has a unique color-zero lift, and this defines a global continuous section. Thus its cover class w_mono vanishes, and all its positive powers vanish.

This holds even when the monochromatic shift graph has odd cycles and nonzero ordinary first cohomology.

## 2. The connector parity class is distinct from antipodal index
In the full quotient B=H/tau, the established classes satisfy
 alpha=[hbar]=[1_B]+w,
where hbar records same-color edges. Restrict to B_mono=H_mono/tau. Then
 w|B_mono=0,
 alpha|B_mono=[1_(B_mono)].
Hence an odd monochromatic cycle may detect alpha while detecting zero antipodal cover class.

The conclusion follows directly from the section in part 1 and the fact that hbar is one on every retained edge. In particular, the coloring-independent nonzero connector class provides genuine parity information; transporting it into a high-index carrier additionally requires the carrier's color-forgetting identifications or suitable edges between different colors.

## 3. General colored-state carrier theorem
Let Z be a finite simplicial complex whose vertices represent monochromatic path states, each with an actual binary witness color q(v). Suppose q is constant on every simplex and tau acts simplicially with q(tau v)=1-q(v). Then q extends to a continuous equivariant map |Z| -> S^0. Its quotient double cover has a global color-zero section. Consequently every positive power of its cover class vanishes.

Proof. Every simplex lies in one color class; the two resulting subcomplexes are disjoint and exchanged. The constant affine extension of q is continuous, and the section follows as above.

For r such carriers, their equivariant join maps to
 (S^0)^(join r)=S^(r-1),
by joining their color maps. Their product with the diagonal involution maps to S^0 by projecting to the first factor and then using its color map. Thus joins or products of separate color-preserving connector carriers have the stated index upper bounds, regardless of other ordinary cohomology classes.

## 4. Consequence for NORI's exact color-free carriers
The mixed root-profile interface and the initial/terminal physical witness-cone complexes forget witness color. Their points may identify states backed by distinct colored paths. Such identifications remove the hypothesis of part 3 and can carry nontrivial antipodal topology.

A proposed high-index construction should specify these identifications and verify that a face still retains a valid root/terminal-memory extraction. Keeping every monochromatic witness in a permanently separate colored component gives the explicit S^0 map above. The exact reversed-tail splice theorem allows either branch color, so color-free profile intersections are the appropriate extraction target.

No assertion of nonzero higher cover powers for the actual color-free interface is made here. Establishing such powers, or acyclicity of the interface, remains a forcing task toward grand closure.
