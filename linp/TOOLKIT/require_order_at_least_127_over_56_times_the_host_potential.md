# Cheap switching states require order at least 127 over 56 times the host potential

**Summary:** Cheap switching states require order at least 127 over 56 times the host potential.

## Statement

Let H be a finite linear 3-graph on n vertices and let v be an active misaligned vertex with p=phi(v). Suppose v is low-defect and its switching-family source-potential mass is within o(p^2) of the generic 185/512 p^2 floor, in the asymptotic regime p->infinity.

Then
  n >= (127/56-o(1))p.

More explicitly, if U_v is the terminal-retained part of a switching family and k=|U_v|, then
  n >= 2p+1+k.
Hence any estimate k>=(15/56-epsilon)p gives
  n >= (127/56-epsilon)p+1.

Therefore for every fixed epsilon>0, a sequence with
  n <= (127/56-epsilon)p
cannot realize the locally cheap post-43/48 switching state at a p-center; such a center must instead pay a fixed positive quadratic gain in switching-source potential over the generic 185/512 floor.

## Body

Let P be the chosen maximum p-edge path ending at v. A linear 3-uniform p-edge path has exactly
  |V(P)|=2p+1
vertices.

Every terminal-retained switcher e={x,v,u} has its unique entrance x omitted from P by definition. Distinct switchers through v have distinct entrances: two distinct hyperedges already share v, so sharing an entrance x would violate linearity. Thus the k terminal-retained switchers supply k distinct vertices outside V(P). Consequently
  n>=|V(P)|+k=2p+1+k.                                  (1)

Now assume the local switching-source mass is within o(p^2) of the generic 185/512 p^2 floor. By 1bab77ec4e49,
  k >= (15/56-o(1))p.                                  (2)
Substituting (2) into (1),
  n >= 2p+1+(15/56-o(1))p
    = (127/56-o(1))p.

For the final contrapositive, fix epsilon>0. If n<=(127/56-epsilon)p for all sufficiently large p, then (1) implies
  k <= (15/56-epsilon)p+O(1).
Since the total switching size is (5/8-o(1))p at a low-defect center, this places k a fixed positive fraction below the three-sevenths threshold of 1bab77ec4e49. That theorem then gives a fixed positive quadratic source-potential gain over 185/512 p^2.

## Metadata

- ID: require_order_at_least_127_over_56_times_the_host_potential
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
