# Adjacent special-pair boundary caps absorb a missing vertex and complete endpoint ports

## Metadata

- ID: adjacent_special_pair_boundary_caps_absorb_a_missing_vertex_and_complete_endpoint_ports
- Parent Section: monochromatic_connector_blocks
- Position: 39
- Row version: 2
- Development version: 2
- Composition version: 1
- Composition stale: False

## Composition

In the fixed split, an empty or singleton shore cap next to adjacent x,z absorbs any omitted shore vertex while making both endpoint ports forward, provided the opposite port is already forward. Empty caps also absorb two omitted vertices as a forward ordered pair; singleton caps absorb two when their three shore vertices are transitive. One- or two-deletion witnesses of these types become whole-shore compatible connectors and close the ambient instance by homogeneous-cut composition. These legal boundary absorptions exclude explicit Hartman boundary classes and resolve their rank-two unions without general component union closure.

## Development

Combination of the monochromatic zero-path formulation, special-pair signatures, and Article IV's relaxed boundary-target state space.

Work in the fixed normalized split B→z→A→x. The signatures are α(a,x,z)=α(x,z,a)=0 for every shore coordinate a, and α(a,b,x)=α(z,a,b)=1−t(a,b), where t(a,b)=1 iff a→b. All port statements below refer to this fixed representative.

Left empty-cap absorption. Suppose C=(x,z,Q) is monochromatic zero and its final ordered pair is forward. For any omitted shore vertex a, C'=(a,x,z,Q) is monochromatic zero, because its sole additional ternary window is α(a,x,z)=0. Its first pair a→x and its unchanged final pair are forward. Thus one absorption simultaneously grows support and realizes both port targets.

Left singleton-cap absorption. Suppose C=(u,x,z,Q), u∈A, is monochromatic zero and its final pair is forward. For any omitted shore vertex a, orient the pair {a,u} forward, calling the resulting order (s,t). Set C'=(s,t,x,z,Q). The first new window has α(s,t,x)=0; the next is α(t,x,z)=0; the following special-pair and Q windows agree with old zero windows. The first pair s→t is forward, and the final port is unchanged. Therefore any such compatible singleton cap absorbs every individual omitted shore vertex.

The right-hand versions are equally exact. From C=(P,x,z), with a forward first pair, append a. From C=(P,x,z,u), replace the terminal singleton by the forward order of {u,a}. The identities α(x,z,s)=0 and α(z,s,t)=0 verify the new windows. The initial port is unchanged and the new final pair is forward.

Consequences. In an inclusion-minimal whole-shore obstruction, every one-vertex-deletion witness with an adjacent x,z pair avoids compatible singleton caps at both ends. A relaxed monochromatic one-deletion witness with an empty special-pair cap and the opposite port forward also closes immediately. More generally, any maximal compatible connector with an omitted shore vertex avoids singleton caps. These are explicit excluded boundary classes for a Hartman realization, established by legal absorptions rather than assumed boundary behavior.

If one-deletion witness of either type covers A minus {a}, the move constructs a compatible zero connector on all A∪{x,z}, and homogeneous-cut composition then gives a full NOR order. Thus the combination closes these ambient branches, with no union-closure, higher coherence, or incidence condition on a beyond the shore signature.

Rank-two boundary closure. The empty-cap state (x,z,Q) with its right port forward absorbs any two omitted shore vertices simultaneously: orient their pair (s,t) forward and prepend it to x,z,Q. The only new windows are α(s,t,x)=0 and α(t,x,z)=0; both final ports are forward. The right empty-cap case is symmetric. Thus every two-deletion state of this boundary class already gives whole-shore closure when those are its only omitted shore coordinates. A singleton cap also absorbs two omitted vertices if the three shore vertices form a transitive triple, by using its transitive order before x,z (or after x,z). The common boundary is released, so no arbitrary internal-pair gauge or outside left collar obstructs this rank-two union.
