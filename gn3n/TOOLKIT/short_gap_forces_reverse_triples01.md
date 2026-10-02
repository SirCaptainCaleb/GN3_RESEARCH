# Short gaps force reversed endpoint triples without a minimum-counterexample hypothesis

**Summary:** Short gaps force reversed endpoint triples without a minimum-counterexample hypothesis.

## Statement

Let B=(b_1,...,b_r) be a tight path in a boundary tournament H, and let L be a set of exterior vertices. Assign each x in L a distinct second-type obstruction gap g(x) in {1,...,r-1}. Assume that for adjacent assigned gaps i=g(u), i+1=g(w), the triple (u,b_{i+1},w) is tight. If no Hamiltonian four- or five-support meets both L and V(B), then for any distinct u,v,w in L with 0<g(w)-g(u)<=2, (w,v,u) is tight. Equivalently, every tight triple (u,v,w) on L with g(u)<g(w) has g(w)-g(u)>=3. In particular, for any displayed tight four-path (x_0,x_1,x_2,x_3) on L, each of g(x_2)-g(x_0) and g(x_3)-g(x_1) is either negative or at least three. If its label gaps are increasing, its second-neighbor gaps are at least three, its total span is at least four, and r>=6. These conclusions do not require a cycle claim, an endpoint-extension hypothesis, a cover, or global quadratic minimality.

## Body

Fix distinct u,v,w in L and let i=g(u)<g(w)=j. Suppose (u,v,w) is tight. If j=i+1, the assumed adjacent-gap cross triple gives the second tight path (u,b_{i+1},w). The parallel-middle four-path lemma in localextend01 therefore makes {u,v,w,b_{i+1}} Hamiltonian, contradicting the mixed-support exclusion. If j=i+2, the separated-gap case of 36fccff06d48 gives (u,b_{i+1},b_{i+2},w) tight. This four-vertex path and (u,v,w) are internally disjoint corridors with the same ordered endpoints. By 53d257fcf0a8 their five-vertex union is Hamiltonian, again a contradiction. Boundary antisymmetry now forces (w,v,u) whenever j-i is one or two. Apply this to the two consecutive triples of a displayed four-path for the stated inequalities. If its gaps increase, g(x_2)-g(x_0)>=3 and g(x_3)-g(x_1)>=3. Distinct integer gaps then give g(x_3)-g(x_0)>=4. Since assigned indices lie in {1,...,r-1}, r-2>=4 and r>=6. This is a direct local statement on arbitrary H. The second-type gap network in four_side_endpoint_lock_gap_network01 provides its assumptions in its unresolved branch. No step concatenates paths around a cycle or assumes the gap order agrees with a preexisting path order.

## Metadata

- ID: short_gap_forces_reverse_triples01
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
