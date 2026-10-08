# Featureless equality endpoints have distinct ordinary deletion labels — preserved pre-item development

## Featureless equality endpoints have distinct ordinary deletion labels

Retain the hard rooted five-component setup
\[
Y\mid P\mid Q,
\qquad
Y=\{x,y,r,s,t\},
\]
with distinguished holes \(x,y\), and suppose the threefold-core disturbance branch has been excluded.

For an exposed endpoint \(e\), call it a **featureless equality endpoint** if it is a four-of-six equality endpoint and, after applying [[equality_endpoints_reduce_to_a_hole_preserving_same_endpoint_extension_residue]], none of the first three disturbance outputs occurs. Thus there is a unique good ordinary deletion label
\[
\rho(e)\in Y-\{x,y\}
\]
such that, with
\[
C_e=Y-\{\rho(e)\},
\]
both
\[
C_e\cup\{\rho(e)\}=Y
\qquad\text{and}\qquad
C_e\cup\{e\}
\]
are Hamiltonian, and chosen compatible Hamilton orders place \(\rho(e)\) and \(e\) in the same endpoint gap of one common relative order on \(C_e\).

Then the map
\[
e\longmapsto \rho(e)
\]
is injective on the featureless equality endpoints.

Indeed, suppose two distinct exposed endpoints \(e,f\) satisfy
\[
\rho(e)=\rho(f)=r.
\]
Put
\[
C=Y-\{r\}.
\]
Then all three five-sets
\[
C\cup\{r\}=Y,\qquad
C\cup\{e\},\qquad
C\cup\{f\}
\]
are Hamiltonian. Apply Lemma 5 of [[endpoint_transport_and_small_support_gluing_compatible_one_vertex_extensions]] to the common four-set \(C\) and the three roots \(r,e,f\). It forces at least one of:

1. order disagreement on \(C\);
2. a Hamiltonian six-set \(C+\{u,v\}\) for two roots;
3. a Hamiltonian four-set;
4. a positioned reversing triple.

Each is already a bounded disturbance/output of the Article VII transport machinery, contradicting featurelessness.

Therefore distinct featureless equality endpoints use distinct ordinary deletion labels.

### Incidence consequence

There are only three ordinary labels in
\[
N=Y-\{x,y\}.
\]
Hence at most three of the four exposed endpoints of \(P\mid Q\) can be featureless equality endpoints. If all four endpoints are equality endpoints, some ordinary deletion label repeats and a bounded disturbance is forced immediately.

More generally, after excluding all bounded disturbances, the four-endpoint good-ordinary-deletion incidence pattern has:
- ordinary-label degree at most two (otherwise the threefold-core branch occurs);
- featureless singleton rows carrying pairwise distinct labels.

Thus the residual endpoint synchronization problem is finite already at the incidence level: at least one exposed endpoint must either have at least two good ordinary deletion labels or participate in a bounded disturbance.

This is the first constraint coupling the individual same-endpoint normal forms across different exposed endpoints.
