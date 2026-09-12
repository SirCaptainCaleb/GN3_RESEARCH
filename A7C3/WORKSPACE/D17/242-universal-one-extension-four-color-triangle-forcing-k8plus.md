# Four-color pair-core multiplicity forces a triangle at |Y|>=13, so the k>=8 C4 is not terminal

**Workspace:** D17
**State:** established
**Key:** `universal-one-extension-four-color-triangle-forcing-k8plus`

**Summary:** For a universally one-extendable four-set S, let G_s on Y record pairs de for which (S-s)+{d,e} is Hamiltonian. R195 gives every exterior pair at least two good core colors. If all four G_s were triangle-free, choose for every pair exactly two good colors. Around any fixed exterior vertex v, each of the six two-color labels can occur on at most two incident edges: three neighbors with the same label A would force every edge among them to have the complementary label A^c, creating a monochromatic triangle in either color of A^c. Hence |Y|<=13. At equality |Y|=13, every label occurs exactly twice at every v. Any edge with a third good color would allow relabelling that edge to another good two-subset, producing a three-neighbor label class and contradiction; therefore every pair has exactly two good colors and every G_s is 6-regular. A 6-regular triangle-free graph on 13 vertices is impossible by a direct neighborhood count. Thus |Y|>=13 forces a pair-core triangle in some core color. In R927 Arm M with k>=8, |Y|=2k-3>=13, so any universal one-extension four-core can switch to a triangle color and invoke SV33654. Consequently a portal-only C4 cannot be the terminal local universal-core obstruction.

### 1. Four simultaneous core colors
Retain the universal one-extension four-set setup of SV26947. Thus S is a four-set, Y=V(H)-S, and for each core label s in S define the graph G_s on Y by

  de in E(G_s)  iff  (S-{s})+{d,e} is Hamiltonian.          (FC.1)

Accepted R195, exactly as used in SV26947, gives the multiplicity statement

  every exterior pair de belongs to at least two of the four graphs G_s.  (FC.2)

We prove a stronger global alternative than continuing one fixed portal C4.

### 2. A two-color coding bound
Assume for contradiction that all four graphs G_s are triangle-free. For every unordered exterior pair de choose arbitrarily a two-element subset

  c(de) subseteq S                                      (FC.3)

of good core colors for de. This is possible by (FC.2).

Fix v in Y and a two-subset A of S. Put

  N_A(v)={x in Y-{v}: c(vx)=A}.                          (FC.4)

We claim |N_A(v)|<=2. If x,y are both in N_A(v), then c(xy) must be disjoint from A. Indeed, if some color s lay in A intersect c(xy), then vx,vy,xy would all be edges of G_s, giving a triangle. Since both A and c(xy) have order two inside a four-set, disjointness forces

  c(xy)=S-A.                                             (FC.5)

If N_A(v) contained three vertices x,y,z, then all three edges xy,yz,zx would carry the same complementary two-color label S-A. Either color in S-A would therefore span the triangle xyz in its G_s, contradiction. Hence |N_A(v)|<=2.

There are exactly six two-subsets A of S, and the six classes N_A(v) partition Y-{v}. Therefore

  |Y|-1 <= 6*2 = 12,
  |Y| <= 13.                                             (FC.6)

Thus if |Y|>=14, some G_s already contains a triangle.

### 3. Equality |Y|=13 forces exact two-color multiplicity
Suppose |Y|=13. Equality in (FC.6) implies that for every v and every two-subset A of S,

  |N_A(v)|=2.                                            (FC.7)

We next show every exterior pair has EXACTLY two good core colors. Suppose uv were good in at least three colors. Starting from the chosen label c(uv)=A, choose a different two-subset B of the good colors and change only the label of uv from A to B. The new labeling still chooses two genuinely good colors on every exterior pair, so the argument of Section 2 still applies. But at u the A-class now has size one while the B-class has size three, contradicting the universal bound |N_B(u)|<=2. Therefore no pair has a third good color.

Consequently c(de) is not merely a choice: it is the full set of good core colors for de. For a fixed s in S and v in Y, exactly three of the six two-color labels contain s, and each occurs twice at v by (FC.7). Hence

  d_{G_s}(v)=6                                           (FC.8)

for every s and v. Under the standing triangle-free assumption, every G_s is therefore a 6-regular triangle-free graph on 13 vertices.

### 4. No 6-regular triangle-free graph has order 13
Let G be such a graph and fix v. Put A=N_G(v), so |A|=6. Triangle-freeness makes A independent. Let

  B=V(G)-({v} union A),

so |B|=6. Every a in A has degree six, has one neighbor v, and has no neighbor in A. Thus a has exactly five neighbors in B. Therefore there are exactly 30 A|B edges.

The six vertices of B have total degree 36. Subtracting the 30 cross incidences leaves total internal B-degree six, so

  e_G(B)=3.                                              (FC.9)

Now take any internal edge xy of B. No a in A can be adjacent to both x and y, else axy is a triangle. But every a has five neighbors among the six vertices of B, so every a has a unique nonneighbor in B. Therefore that unique nonneighbor must lie in {x,y}. It follows that every z in B-{x,y} is adjacent to all six vertices of A. Such a z already has degree six and hence has no neighbor in B. Thus every internal B-edge is forced to be xy itself, giving e_G(B)<=1, contradicting (FC.9).

Hence the equality case |Y|=13 is impossible as well. Combining with Section 2:

  if |Y|>=13, at least one core-color graph G_s contains a triangle.  (FC.10)

### 5. Arm-M consequence: C4 extinction by color-switch shortening
Now assume accepted R927 Arm M with |V(H)|=2k+1 and k>=8. For a universal one-extension four-set S,

  |Y|=|V(H)-S|=2k-3 >= 13.                              (FC.11)

By (FC.10), some core color s has a pair-core triangle. Choose that triangle; it is automatically a shortest cycle in G_s. The current triangle-extinction theorem SV33654 then exports it to explicit R435 reverse-trimer/proper-cycle geometry and hence to actual or closed maximum-three-forest dynamics.

Therefore a portal-only shortest C4 from another core color cannot be a terminal local universal-core obstruction in the k>=8 Arm-M range. One may switch core color and strictly shorten the pair-core support holonomy from length four to length three, after which the completed triangle consumer applies.

This is stronger than a direct Sigma>=12 portal calculation: the four-cut high-transition C4 may exist as a representative at one color, but it is bypassed by an unavoidable triangle at another color. No claim is made here that the resulting maximum-three-forest holonomy is globally extinct.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R195"
    },
    {
        "relation": "dependency",
        "revision_id": "R927"
    }
]
```