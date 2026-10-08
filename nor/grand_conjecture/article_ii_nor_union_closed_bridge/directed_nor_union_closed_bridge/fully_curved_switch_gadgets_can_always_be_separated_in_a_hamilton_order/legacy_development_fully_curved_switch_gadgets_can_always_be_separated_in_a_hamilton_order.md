# Fully curved switch gadgets can always be separated in a Hamilton order — preserved pre-item development

## Composition

(none yet)

## Development


## Fully curved switch gadgets can always be separated in a Hamilton order

Let F be the family of fully curved four-sets of an alternating triangle orientation alpha.

From the five-set theorem, every five-set contains at most two members of F; more strongly, if two tetrahedral facets of one five-set are fully curved, the other three facets are not.

### Theorem
The vertices admit a linear ordering

v_1,...,v_n

such that no two consecutive four-windows

{v_i,v_{i+1},v_{i+2},v_{i+3}},
{v_{i+1},v_{i+2},v_{i+3},v_{i+4}}

are both fully curved.

Equivalently, the universal switch gadgets can be made pairwise nonconsecutive along a Hamilton order.

### Proof

For n<=4 the statement is immediate. Assume n>=5.

Choose any non-fully-curved four-set and order its vertices arbitrarily as the initial four vertices. Such a four-set exists: inside any five-set at least three of its five tetrahedral facets are not fully curved.

Maintain the invariant that the current final four-window is not fully curved whenever unplaced vertices remain.

Suppose the current last three vertices are a,b,c.

If only one vertex d remains, append it. The previous four-window is non-full by the invariant, so even if {a,b,c,d} is full there is no consecutive full pair.

Now suppose at least two vertices remain.

Choose any candidate d.

- If {a,b,c,d} is not fully curved, append d. The invariant continues.

- Suppose {a,b,c,d} is fully curved. If some other remaining e has {b,c,d,e} non-full, append d and then e. The two new windows are full followed by non-full, so no consecutive full pair is created and the invariant is restored.

- Finally suppose {a,b,c,d} is full and every other remaining e makes {b,c,d,e} full. Pick one such e. In the five-set {a,b,c,d,e}, the two facets {a,b,c,d} and {b,c,d,e} are fully curved. Hence all other tetrahedral facets are non-full, in particular {a,b,c,e}. Append e instead of d. The new final window is non-full, so the invariant is restored.

Proceed until all vertices are placed. QED.

### NOR interpretation

A fully-curved four-window forces a color change between its two consecutive alpha-statuses for every ordering of those four vertices. The theorem shows that these order-independent forced switches can always be globally isolated: there is an order in which no two forced switches occur at adjacent transition positions.

Therefore any residual high variation in a carefully chosen order must involve the flat or singly-curved tetrahedra between these isolated universal gadgets. This is the natural domain for the coboundary/Connector mechanism: the genuinely unavoidable switch gadgets themselves need not cluster.
