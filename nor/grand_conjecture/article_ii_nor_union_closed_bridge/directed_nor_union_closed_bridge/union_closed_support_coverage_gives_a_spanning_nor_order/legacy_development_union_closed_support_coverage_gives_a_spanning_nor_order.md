# Union-closed support coverage gives a spanning NOR order — preserved pre-item development

## Support coverage, rather than frequency, is sufficient under union closure

Fix a reversal-antisymmetric coordinate label h of arity r>=2 on a finite ground set V, with |V|>=r. This is the translation-invariant directed sector of N_{r+1}. Fix a color sigma and an ordered terminal tuple S of length r-1. Let W=V\setminus underlying(S), and let F_{sigma,S} consist of supports A subseteq W having a sigma-tight witness (an ordering of A followed by S).

### Theorem
Suppose F_{sigma,S} is union-closed. Put M=union_{A in F_{sigma,S}} A. Then M itself is feasible. If |W\setminus M|<=1, directed NOR holds on the entire ground set V.

### Proof
The support family is finite and contains the empty set. Repeated application of binary union closure gives M in F_{sigma,S}. Choose a tight witness P spanning M together with S.

If M=W, P is a monochromatic spanning order. Otherwise let W\setminus M={x}. The path P spans V\setminus{x} and is sigma-tight. Prepend x to P. All old r-windows retain color sigma, and there is only one new window, namely x followed by the first r-1 vertices of P. Whatever its color, the full color word has at most one change. This is a spanning order and proves the claim.

The hypothesis |V|>=r ensures that in the one-omitted case P has at least r-1 vertices, so the new window exists. When P has precisely r-1 vertices its tightness is vacuous and the spanning order has just one colored window.

### Counterexample consequence
In any directed NOR counterexample, every union-closed fixed-tail support family omits at least two coordinates from its union. Equivalently, if a fixed-tail family covers all but at most one outside coordinate through its feasible supports, it must fail union closure. By the accessible-family square-completion criterion developed in Article I, this produces a top-missing Boolean square.

This conclusion is stronger than applying Frankl to an antimatroid: no coordinate-frequency argument is needed once coverage is this high. It also avoids synchronizing chosen witnesses. Union closure supplies existence of one witness on the union; no claim is made that a particular support chain lifts by front extension.

### Singleton and near-sink corollaries
If all but at most one singleton {x}, x in W, are feasible and the family is union-closed, the theorem applies. The same conclusion holds if those coordinates occur in longer feasible supports, even without feasible singletons.

For ternary h, write T_u on V\setminus{u} with x->v if h(x,u,v)=0. If v has at most one out-neighbor in T_u, then all but at most one x outside (u,v) satisfy h(x,u,v)=0. Hence union closure of F_{0,(u,v)} proves directed N_4 on V.

In particular, a transitive T_u has a sink v. Union closure of F_{0,(u,v)} then yields a monochromatic spanning order, not merely a one-change order. Thus a center with transitive local neighborhoods, together with support union closure at its sink tail, is a sufficient condition for closure.

### Remaining obligation
Neighborhood union closure and fixed-tail support union closure are different conditions. The tournament theorem establishes only the former's equivalence with transitivity. It does not establish support union closure at a sink tail. Nor has high support coverage been proved for an arbitrary directed NOR coloring. The general conjecture remains open.

A useful next task is therefore to produce a tail with high support coverage and either union closure or a witness-preserving resolution of its first missing square. A frequency conclusion alone does not resolve the remaining case.
