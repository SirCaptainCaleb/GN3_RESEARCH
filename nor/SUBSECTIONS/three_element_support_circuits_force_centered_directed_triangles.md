# Three-element support circuits force centered directed triangles

## Metadata

- ID: three_element_support_circuits_force_centered_directed_triangles
- Parent Section: directed_nor_union_closed_bridge
- Position: 25
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Three-element support circuits are blocked cycles with three centered triangles

Let h be a reversal-antisymmetric ternary coordinate coloring. Fix a tail F=(f_1,f_2) and color tau. Suppose U={a,b,c} is a minimal infeasible support in F_{tau,F}: every proper subset is feasible at F, while U is not. Put sigma=1-tau.

The three-element circuit theorem in Article II gives a cyclic labeling a,b,c such that
h(a,b,f_1)=h(b,c,f_1)=h(c,a,f_1)=tau,
h(b,a,f_1)=h(c,b,f_1)=h(a,c,f_1)=sigma,
and
h(a,b,c)=h(b,c,a)=h(c,a,b)=sigma.

### Theorem
At each y in U, let p,s be its predecessor and successor in the sigma-tight cyclic order (a,b,c). In the tournament whose color-sigma arcs are x->z iff h(x,y,z)=sigma, the triple {p,s,f_1} has the directed cycle
p -> s -> f_1 -> p.

Consequently a three-element minimal infeasible support cannot occur when every center tournament is transitive.

### Proof
The cyclic status gives h(p,y,s)=sigma. The absent reverse pair-witness arc gives h(s,y,f_1)=sigma. The forward pair-witness arc gives h(p,y,f_1)=tau, so reversal gives h(f_1,y,p)=sigma. These are precisely the three displayed arcs.

Changing from color-sigma orientation to color-0 orientation either retains or reverses every arc. A directed triangle remains a directed triangle, so the obstruction contradicts transitivity regardless of sigma.

### Connection to cycle absorption
The sigma-monochromatic circuit cycle cannot absorb f_1 by either endpoint extension at any y:
h(p,y,f_1)=tau,
h(f_1,y,s)=tau.
The one-vertex absorption lemma identifies this pair of failures with exactly the centered triangle above. Thus the circuit's polarity reversal and the cycle-extension obstruction are the same local mechanism.

This is not merely a support-frequency deficit. The support failure encodes a monochromatic cycle together with a specified outside vertex whose two possible attachments are blocked at every cycle center.

### Scope
The theorem rules out three-element minimal infeasible supports throughout the locally transitive class, for every tail and either color. It does not rule out two-element circuits; the sink-tail counterexample already realizes those with all centers transitive. It also does not rule out larger circuits, for which the present three-cycle classification supplies no automatic reduction.

For unrestricted directed NOR, the result supplies forced local triangles rather than closure. A possible continuation is to use these triangles as exchange data, or to classify how larger support circuits produce cycles and their corresponding attachment obstructions.

## Frontier

- Development version when composed: None
- Development version now: 1
