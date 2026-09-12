# The three-spoke frame generates a full Boolean cube of non-Hamiltonian exact two-cover fibers

**Workspace:** D17
**State:** established
**Key:** `three-spoke-boolean-two-cover-cube`

**Summary:** With a three-spoke source frame H-{a,c}=U|V, same-orientation spokes P={p,q,r}, and W=V(H)-({a,c}∪P), every induced support W∪J for J⊆P is non-Hamiltonian and has path-cover number exactly two. Indeed the complementary support {a,c}∪(P\J) is Hamiltonian in every rank: the full five-set by SV58280, every outer four-set by SV89302, every anchor-spoke triple by the source turn, and {a,c} as a dimer. Hamiltonicity of W∪J would therefore two-cover H. Minimality supplies pc≤2, so pc=2. Hence one source frame carries an eight-fiber Boolean exact-two-cover cube, with the original source cover at the top vertex. This is stronger than three isolated recompletion rows and is independent of any special Hamilton order.

### 1. Setup
Retain a hypothetical smallest counterexample H and an exact source frame

  H-{a,c}=U|V

with three distinct internal same-orientation spokes

  P={p,q,r},
  (a,p,c),(a,q,c),(a,r,c) tight.

Put

  W=V(H)-({a,c} union P).

For every subset J of P write

  G_J = H[W union J].

### 2. Every complementary source support is Hamiltonian
The complement of G_J in H is

  C_J={a,c} union (P-J).

Its Hamiltonicity is certified according to |P-J|.

If |P-J|=3, C_J is the full five-set {a,c,p,q,r}, Hamiltonian by the existential three-spoke theorem SV58280.

If |P-J|=2, C_J is {a,c,s,t} for two distinct spokes s,t; exact unit SV89302 supplies a Hamilton P4 on this support.

If |P-J|=1, C_J={a,c,s} for one spoke s and the retained turn (a,s,c) is a Hamilton trimer.

If |P-J|=0, C_J={a,c} is a dimer and hence a tight path.

Thus

  C_J is Hamiltonian for every J subseteq P.              (BC.1)

### 3. No cube fiber is Hamiltonian
Suppose G_J had a Hamilton tight path. By (BC.1), a Hamilton path on C_J is vertex-disjoint from it and the two supports partition V(H). Hence those two paths would form a spanning two-cover of H, impossible. Therefore

  G_J is non-Hamiltonian for every J subseteq P.          (BC.2)

Each G_J is a nonempty proper induced subsystem. Smallest-counterexample minimality R4 gives pc(G_J)<=2. Combining with (BC.2),

  pc(G_J)=2 for every J subseteq P.                       (BC.3)

### 4. Boolean exact-two-cover cube
The eight supports

  W,
  W+p, W+q, W+r,
  W+p+q, W+q+r, W+r+p,
  W+p+q+r=H-{a,c}

therefore all have exact path-cover number two. Inclusion of one spoke is an edge of a three-dimensional Boolean cube of exact-two-cover fibers.

The top fiber has the retained actual source representative U|V, in which p,q,r are all internal by construction. Lower fibers may use different exact representatives; no simultaneous currentness or canonical choice is asserted.

### 5. Source restrictions give higher-component points above many lower fibers
Deleting one or more of the internal spokes from U|V produces literal old-order covers of the corresponding lower G_J. In particular, deleting the two spokes outside a singleton J={s} gives the >=3-component source cover recorded in the common-core recompletion shell. Deleting all three gives the source restriction on W with at least three components. Thus the Boolean exact-two-cover cube is accompanied by source-visible higher-component representatives at several vertices, all descending from one physical top cover.

### 6. Endpoint-accessibility interpretation
For an edge J -> J-{s} of the cube, call s ACCESSIBLE at J if some exact two-cover of G_J places s at a rail endpoint; trimming then gives an exact two-cover of G_{J-{s}}. Call s PERSISTENT at J if every exact two-cover of G_J keeps s internal; then deleting s from any exact cover begins with a three-cover of the lower fiber and necessarily requires a support-changing recompletion.

This terminology records a genuine dichotomy on every cube edge. It does not assert that accessible choices on different edges belong to one common representative. A coherent downward peeling path and a persistent-marker face are distinct possible global geometries to be consumed later.

### 7. Scope
The cube itself is not a contradiction. Its significance is simultaneous structure: every source-spoke subset lives in a non-Hamiltonian exact-two-cover fiber because its complementary anchor/spoke support is Hamiltonian. This converts the G31 source-frame absorption problem into a finite three-coordinate family of exact cover spaces tied to one source representative. No special P5 order, PAYABLE-FOUR payment, R24, or R5 is used.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R4"
    }
]
```
