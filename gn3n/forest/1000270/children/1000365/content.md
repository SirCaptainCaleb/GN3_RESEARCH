# Current proof composition: bounded obstruction to defect compression

## Statement

A minimum counterexample has an exact one-vertex deletion two-cover P|Q. The omitted vertex cannot be inserted into either displayed component, so the certified bounded-obstruction theorem supplies local obstruction windows immediately. The sole unsupported inference is to consume such a window to obtain a spanning two-cover or defect span at most two.

## Body

# Current composition

Assume the grand conjecture is false and let H be a minimum counterexample.

1. **Take one deletion state.** Fix any vertex x. By the minimum-counterexample calculus, H-x has an exact two-path cover P|Q, and both components are nontrivial.

2. **Insertion fails on both components.** The omitted vertex x cannot be inserted anywhere into the displayed order of P: if it could, the resulting tight path on V(P) union {x}, together with Q, would be a spanning two-cover of H. The same argument applies to Q.

3. **Localize the obstruction.** The bounded insertion-obstruction theorem in the endpoint-transport module applies separately to P and Q. Therefore this single deletion state already contains two bounded local obstruction windows, each supported on x and at most four consecutive vertices of one component.

4. **Missing step.** Prove the endpoint-transport / defect-compression bridge: consume one or both bounded obstruction windows to obtain either a spanning two-cover directly, an absorbable endpoint reversal after valid transport, or a spanning ordering of defect span at most two.

5. **Close from defect span.** If the bridge returns an ordering of defect span at most two, the defect-span theorem converts it to a spanning cover by at most two tight paths.

Thus the first unsupported inference in the shortest current proof attempt is exactly the endpoint-transport / defect-compression bridge.

The compatibility, common-gap, and richer deletion-state machinery remain useful alternative producers of transport data and remain live mathematics, but they are not required as top-level premises of this shortest proof organization.
