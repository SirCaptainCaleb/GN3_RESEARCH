# Equality endpoints reduce to a hole-preserving same-endpoint extension residue

## Metadata

- ID: equality_endpoints_reduce_to_a_hole_preserving_same_endpoint_extension_residue
- Parent Section: article_vii_synthesis_and_exact_frontier
- Position: 74
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Equality endpoints reduce to a hole-preserving same-endpoint extension residue

Let
\[
U=Y\cup\{e\},
\qquad
Y=\{x,y,r,s,t\},
\]
be a four-of-six equality endpoint as in [[four_endpoints_force_a_threefold_core_or_two_double_hole_equality_endpoints]]. Thus \(x,y\) are the distinguished hole labels, \(Y\) is Hamiltonian, \(U\) is non-Hamiltonian, and for the unique good ordinary deletion label \(r\),
\[
U-\{r\}=(Y-\{r\})\cup\{e\}
\]
is Hamiltonian.

Put
\[
C=Y-\{r\}=\{x,y,s,t\}.
\]
Then both
\[
C\cup\{r\}=Y
\qquad\text{and}\qquad
C\cup\{e\}=U-\{r\}
\]
are Hamiltonian, while
\[
C\cup\{r,e\}=U
\]
is non-Hamiltonian.

Choose Hamilton orders on \(C+r\) and \(C+e\).

If the two orders induce different relative orders on \(C\), we have an order-disagreement certificate on a four-label core containing both holes.

Assume instead that they induce the same relative order
\[
(c_1,c_2,c_3,c_4)
\]
on \(C\). Then each chosen Hamilton order is obtained by inserting its exceptional root, \(r\) or \(e\), into a gap of this common core order. Apply [[endpoint_transport_and_small_support_gluing_compatible_one_vertex_extensions]].

- If the two insertion gaps are separated, inserting both roots makes \(U\) Hamiltonian, impossible.
- If the gaps are adjacent, the simultaneous order is Hamiltonian unless the unique mixed triple through \(r,e\) and the intervening core vertex fails; because \(U\) is non-Hamiltonian, that boundary flip is forced and gives a positioned reversing triple.
- If the roots use one common internal gap, \(\{r,e,c_i,c_{i+1}\}\) is a Hamiltonian four-set.
- Therefore, if none of the preceding bounded disturbances occurs, \(r\) and \(e\) must occupy the **same endpoint gap** of the common order on \(C\).

Hence:

> **Hole-preserving equality reduction.** Every four-of-six equality endpoint has one of four outputs:
> 1. order disagreement on the common four-core \(C\) containing both holes;
> 2. a positioned reversing triple;
> 3. a Hamiltonian four-support;
> 4. a common-side endpoint normal form in which both the ordinary label \(r\) and exposed tail endpoint \(e\) Hamilton-extend the same endpoint gap of one common relative order on \(C=\{x,y,s,t\}\).

The fourth case is the only featureless residue, and it is precisely the same-side extension geometry isolated in the earlier endpoint-transport program. Unlike the older occurrence there, the common core here canonically contains the entire minimum pair \(\{x,y\}\).

Thus the equality branch of the rooted five-component frontier has been reduced to established bounded disturbances plus one hole-preserving same-endpoint extension state.

## Frontier

- Development version when composed: None
- Development version now: 1
