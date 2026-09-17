# Two-hole endpoint transfer forces a cyclic family of complementary Hamilton covers

**Workspace:** D17
**State:** working
**Key:** `middle-layer-two-hole-endpoint-transfer`

**Summary:** Let W have order 2k-1 and assume every k-set of W is Hamiltonian. Call a k-support S good when its (k-1)-complement also has a Hamilton path. Every good support has at least two distinct good Johnson neighbors. More precisely, if P is a Hamilton path on S and x is either physical endpoint, then W-S+x is a Hamilton k-set; choose any Hamilton path there and an endpoint y in W-S. Deleting y gives a Hamilton path on the complement of S-x+y, while uniformity Hamiltonizes S-x+y. Thus S -> S-x+y is realized through the actual cover sequence P|(W-S), (P-x)|(W-S+x), (S-x+y)|(W-S-y+x). The two endpoints of P yield distinct neighbors. Hence every nonempty good-support component has minimum degree at least two and contains a Johnson exchange cycle. In the near-maximal two-hole residue H-{p0,p{k-1}}, the three residual-pair covers supply initial good supports, so the family is nonempty. This is an amplification interface, not a Hamiltonicity theorem; cycle consumption remains open.

### Setup
Let W be a boundary tournament on 2k-1 vertices, k>=3, and assume every k-subset of W is Hamiltonian. Define a k-support S to be **good** when its complement C=W-S, of order k-1, has a Hamilton tight path. Since every k-set is Hamiltonian, a good support is exactly a support participating in an exact Hamilton k | Hamilton (k-1) cover of W.

Form the graph G_W whose vertices are good k-supports, with two supports adjacent when they differ by one Johnson exchange. The important point is not only that such neighbors exist, but that they can be reached by actual endpoint-transfer covers.

### Endpoint-transfer lemma
Fix a good support S. Retain an actual Hamilton path P on S and an actual Hamilton path B on C=W-S. Let x be either physical endpoint of P. Deleting x leaves the literal tight path P-x on S-x. The support C+x has order k, hence is Hamiltonian by the standing k-layer hypothesis. Choose any actual Hamilton path Q_x on C+x. At most one endpoint of Q_x is x, so at least one physical endpoint y of Q_x lies in C. Delete that endpoint y. Then Q_x-y is a literal Hamilton path on

  (C+x)-y = C-y+x.

Now put

  S' = S-x+y.

Its complement in W is exactly C-y+x, so Q_x-y certifies that S' is good. Uniformity independently supplies an actual Hamilton path on S'. Thus we have three actual exact covers of the same W:

  S | C,
  (S-x) | (C+x),
  (S-x+y) | (C-y+x),

where the first-to-second transition deletes a physical endpoint x of the displayed S-path and the second-to-third transition deletes a physical endpoint y of the displayed (C+x)-path. No path reversal or selected-state transport is used.

The support S' is a Johnson neighbor of S. Applying the construction to the two distinct physical endpoints x_1,x_2 of the same Hamilton path P produces two distinct neighbors S-x_1+y_1 and S-x_2+y_2: the first omits x_1 but contains x_2, while the second omits x_2 but contains x_1. Hence

  deg_{G_W}(S) >= 2

for every good support S. Consequently every nonempty connected component of G_W contains a support-exchange cycle.

### Near-maximal two-hole application
In the near-maximal uniform Arm-B frame, delete the two fixed P-endpoints d=p_0 and e=p_{k-1} and put W=H-{d,e}. The residual-triple construction gives exact covers M_{rs}|T_q of W, with |M_{rs}|=k and |T_q|=k-1, for the three residual choices q. Therefore G_W is nonempty and the endpoint-transfer lemma amplifies those three covers to a cyclic family of complementary Hamilton covers.

If W itself is Hamiltonian, H closes immediately as W | (d,e), since a dimer is vacuously tight. The remaining problem is therefore to consume a shortest good-support cycle into Hamiltonicity of W, a P_{k+1} in H, or an R561 boundary-reversed Hamilton dimer. The lemma alone does not do this. In particular, an abstract Johnson cycle is not by itself an order-compatible splice.

### Quiet-edge normal form
There is one further exact local restriction worth retaining. Suppose adjacent good supports have the form C+x and C+y, and retain a Hamilton order P_x on C+x in which x is the endpoint actually removed by the first transfer. If a Hamilton order P_y on C+y is R435-quiet relative to P_x, write the inherited C-order as (c_1,...,c_{k-1}) and assume the endpoint role is the head role, P_x=(x,c_1,...,c_{k-1}); the tail case is dual. R435-quiet contact monotonicity forces P_y to be obtained by inserting y into that same C-order. Since C+x+y has order k+1 and is non-Hamiltonian, y cannot occur after the first inherited edge: otherwise x prepends to P_y using the certified turn (x,c_1,c_2), Hamiltonizing C+x+y. Hence the only quiet forms are

  (y,c_1,...,c_{k-1})  or  (c_1,y,c_2,...,c_{k-1}).

Thus every quiet endpoint-transfer edge is an outer/inner near-end substitution at the physical endpoint that was transferred. This is a one-sided analogue of the R966 quiet forms, now attached to an actual complementary Hamilton cover. A cycle all of whose exchange edges are quiet therefore carries a coherent sequence of near-end substitutions; an R435-active edge remains explicitly cover-current. Consuming those two cycle types is the next target.

Status: complete symbolic working deduction from the stated 2k-1/k-layer hypotheses, with the near-maximal application conditional on the current two-hole residual-cover construction. It is not a reviewed conclusion and does not assert the speculative consecutive-layer incompatibility theorem.
