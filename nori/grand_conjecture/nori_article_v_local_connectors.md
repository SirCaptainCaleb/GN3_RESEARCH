# Article V — Local connectors and exchange geometry

# Certified connectors and extremal geodesic exchanges

Let c be a binary coloring of actual ordered three-faces of Q_n with c(bar F,rev pi)=1-c(F,pi). A k-edge direction-distinct cube geodesic has k-2 ordered-face window colors; call it good when there is at most one change. We study genuine local monochromatic connectors and global consequences of choosing a maximal good path.

## Dead edges force transverse monochromatic geometry

A physical cube edge is live if some monochromatic four-edge geodesic traverses it, and dead otherwise. Let e={z,z xor e_i} be dead. The dead-edge rigidity theorem asserts that every ordered physical three-face through either endpoint whose free directions avoid i has one common color q, independent of their direction order. Accordingly choose any k distinct directions avoiding i, with 3<=k<=min(n-1,6), and root their k-edge path so an endpoint of e lies in its central window overlap. Every length-three window then contains that vertex and has color q. This gives genuine monochromatic six-edge paths through dead-edge endpoints when n>=7.

For n>=8, each eight-dimensional coordinate facet containing e inherits a dead edge. The dimension-eight dead-edge bootstrap supplies a full good eight-edge path inside that facet. Appending the remaining n-8 unused coordinates creates at most n-8 additional color changes, giving a full n-edge path with at most n-7 changes. This is a global quantitative bound conditional on a dead edge.

## Bichromatic diamonds and the seam formula

Suppose two monochromatic four-edge geodesics of opposite colors run between the same roots along two distinct orders of a four-direction support. Appending a fresh direction e gives one new ordered three-face window for each candidate path. These cap windows may be different orders of the same physical face, so their colors are separately constrained rather than dictated by the original monochromatic runs. Under appropriate maximality the forbidden extensions yield precise opposite-color cap equations.

Now take two full antipodal geodesics rooted at x whose prefixes of length ell use the same set S. Both reach the physical vertex y=x xor S. Every choice of either prefix with either complementary suffix is a genuine full geodesic. If a prefix ends (u,v) and a suffix starts (w,t), their concatenation has exactly two new seam windows,
c(F_y({u,v,w});(u,v,w)) and c(F_y({v,w,t});(v,w,t)).
All other windows lie strictly inside the original prefix or suffix. Thus an attempted monochromatic two-tail splice reduces to two actual physical color checks. Connector abundance or a midpoint crossing is not sufficient until these checks are certified.

## Longest good paths have forced two-sided walls

Assume the grand conjecture fails and choose globally longest good partial geodesic P, length k<n, with ordered word q^s r^t, where q≠r. It must have exactly one change: appending any unused direction to a monochromatic P would still be good. Let its initial pair be (alpha,beta) and last pair (a,b). For each unused d, the physical appended cap (a,b,d) has color q, and the prepended cap (d,alpha,beta) has color r. Otherwise one extension remains good. Both extensions therefore have two changes, with words q^s r^t q and r q^s r^t. Antipodal reversal transfers these walls to the opposite cube roots.

A separate globally longest q-monochromatic path forces opposite-corner q-colored three-edge fans, indexed by all missing directions. Pairwise merged roots form a Johnson graph on two-subsets of missing directions. Their first-window colors can be prescribed independently in legal physical colorings, explaining why the root geometry alone gives no global merge. Nevertheless a seam direction with two certified q windows forces an entire row of monochromatic four-edge opposite-corner branches by maximality: otherwise a longer monochromatic path would exist.

Swapping adjacent travel directions preserves every physical three-face window except at most four consecutive positions. This sharply localizes the certificate check for exchanges. The missing global lemma is a terminating exchange rule or a connector selection theorem that forces one full good path from the two-sided walls and genuine cap geometry.
