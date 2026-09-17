# The universal one-extension pair-core holonomy has length three or four

**Workspace:** D17
**State:** established
**Key:** `universal-one-extension-four-set-girth-four-compression`

**Summary:** In the SV26947 universal one-extension four-set setup, one color graph G_s on the exterior Y has m>=7 vertices and at least m(m-1)/4 edges. If G_s had girth at least five, then every unordered vertex pair would have at most one common neighbor, so sum C(d(v),2)<=C(m,2). Cauchy gives sum C(d(v),2)>=2e^2/m-e, hence e<=m(1+sqrt(4m-3))/4. This contradicts e>=m(m-1)/4 for m>=8, and at m=7 integrality gives e>=11 versus e<=10. Therefore the shortest pair-core cycle has length 3 or 4. The universal one-extension absorber is thus reduced at arbitrary order to a bounded triangle or quadrilateral nucleus, each retaining the donor/crossing-portal data of SV26947.

### 1. Setup from the pair-core cycle
Retain the working universal one-extension four-set setup of `universal-one-extension-four-set-pair-core-cycle` SV26947. Thus S is a four-set, Y=V(H)-S has order m>=7, and for one core label s in S the graph G_s on Y satisfies

  |E(G_s)| >= m(m-1)/4.                                  (GF.1)

A shortest cycle in G_s is the pair-core support holonomy used there.

### 2. Girth at least five is impossible
Assume for contradiction that G_s has girth at least five. Then it has no triangles and no 4-cycles. In particular any unordered pair of vertices has at most one common neighbor: two distinct common neighbors would form a 4-cycle. Therefore the number of unordered length-two paths satisfies

  sum_v C(d(v),2) <= C(m,2).                             (GF.2)

Write e=|E(G_s)|. By Cauchy,

  sum_v d(v)^2 >= (sum_v d(v))^2/m = 4e^2/m.

Hence

  sum_v C(d(v),2)
    = (sum_v d(v)^2 - 2e)/2
    >= 2e^2/m - e.                                      (GF.3)

Combining (GF.2)-(GF.3) gives

  2e^2/m - e <= m(m-1)/2,

so solving the quadratic inequality yields

  e <= m(1+sqrt(4m-3))/4.                               (GF.4)

For m>=8, (GF.1) is strictly larger than the right side of (GF.4), because

  m-1 > 1+sqrt(4m-3)

is equivalent to (m-1)(m-7)>0. For m=7, (GF.1) gives the integer bound e>=11, while (GF.4) gives e<=10.5 and hence e<=10. Contradiction in every case m>=7.

### 3. Bounded holonomy consequence
Therefore G_s has girth at most four. Since the pair-core construction already chooses a shortest cycle, its length r satisfies

  r in {3,4}.                                             (GF.5)

Thus a universally one-extendable four-set never exports to an arbitrarily long support cycle. It exports immediately to one of two bounded nuclei on a fixed trimer T=S-s:

  TRIANGLE: T+{a,b}, T+{b,c}, T+{c,a} are Hamiltonian;

  QUADRILATERAL: T+{a,b}, T+{b,c}, T+{c,d}, T+{d,a} are Hamiltonian while the two diagonals T+{a,c}, T+{b,d} are non-Hamiltonian by shortestness.

Each perimeter edge retains the donor-or-crossing-portal data of SV26947. No claim is made that either bounded nucleus already closes H. The significance is that the arbitrary-order universal-core absorption problem has been reduced to consuming a triangle or quadrilateral of actual five-support representatives; long pair-core holonomy is impossible by elementary graph theory.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R195"
    }
]
```
