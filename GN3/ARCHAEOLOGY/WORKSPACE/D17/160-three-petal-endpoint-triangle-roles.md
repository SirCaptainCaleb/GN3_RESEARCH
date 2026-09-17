# A two-triangle endpoint-perfect assignment has constant or alternating endpoint roles

**Workspace:** D17
**State:** established
**Key:** `three-petal-endpoint-triangle-roles`

**Summary:** In the surviving two-triangle endpoint-perfect R953 branch, orient each pair-union Hamilton path and record source/terminal roles on the two endpoint triangles. Around either endpoint triangle the three roles are either all equal or not. A nonconstant role triangle yields an adjacent opposite-role pair; the third pair-union path supplies the disjoint Hamilton complement, and one R3 test on the omitted-petal endpoint triangle gives either a spanning two-cover or an R933 two-ended absorber packet. Hence outside closure/R933 every endpoint triangle is constant-role. The two endpoint triangles must have opposite constant roles on each pair-union path, so one is all-source and the other all-terminal. This yields a canonical source triangle and terminal triangle across the three pair unions.

### Setup and role notation
Retain the Type-II endpoint-perfect branch of `three-petal-endpoint-perfect-triangle`. Label the two endpoint triangles

  T_S?={l_0,b_0,z_0},
  T_T?={l_1,b_1,z_1}

without yet assigning source/terminal meaning. Choose actual orientations of the three pair-union Hamilton paths:

  P_{LB} on L+B,
  P_{LZ} on L+Z,
  P_{BZ} on B+Z.

By the two-triangle endpoint assignment, each path has one endpoint in each triangle or, after the exact switched labelling, the three edges alternate so that each triangle still supplies one endpoint to each pair-union path. Thus every triangle vertex carries a role bit: source or terminal of the unique pair-union path in which it appears as endpoint.

Because each pair-union path has one source and one terminal, the role bits of its two triangle endpoints are opposite.

### A nonconstant endpoint triangle exposes an opposite-role adjacent pair
Suppose one endpoint triangle, say T_0={l,b,z}, does not have all three role bits equal. Then among its three vertices there exist two, say l and b, with opposite roles. These two are endpoints of the same pair-union path P_{LB} or of two adjacent paths depending on the exact Type-II incidence orientation. In either case the third petal endpoint z belongs to the remaining pair-union path that is disjoint from the support containing l,b after deleting the common petal endpoint pair.

Choose the pair-union path for which l is a source and b a terminal after orienting names accordingly. Consider the physical triple {l,z,b}. Exactly one of

  (l,z,b), (b,z,l)

is tight by R3. If the role-correct orientation (l,z,b) is tight, inserting z between the source l and terminal b gives a literal Hamilton bridge across the pair-union support plus z. The complementary punctured petal rail supplied by the third R953 cover remains Hamiltonian, yielding a spanning two-cover of H. If instead the role-correct orientation is bad, R3 gives the reverse connector (b,z,l) tight. This is exactly the graph-intrinsic reverse middle connector required by the two-ended absorber alternative in accepted R933, with z as the singleton absorber and l,b as the opposite-role endpoints.

Thus a nonconstant role triangle yields either closure or an R933 packet with all endpoint identities retained.

### Outside R933, each endpoint triangle is constant-role
Assume no spanning two-cover and no R933 output. Then every endpoint triangle has all three role bits equal. Since each pair-union Hamilton path takes one endpoint from each of the two triangles and its two endpoints have opposite roles, the two triangles have opposite constant roles. After renaming,

  T_src={l_s,b_s,z_s}

consists entirely of source endpoints of the three pair-union paths, while

  T_term={l_t,b_t,z_t}

consists entirely of terminal endpoints.

This gives a canonical SOURCE TRIANGLE and TERMINAL TRIANGLE across the three Hamilton pair unions. No claim is made that either physical triangle is tight in cyclic order. The retained solo petal paths connect l_s to l_t, b_s to b_t, z_s to z_t in some actual orientations which may or may not agree with the pair-union role assignment.

### Next interface
The role-rigid endpoint-perfect branch is now a six-endpoint two-triangle packet:

- every pair-union Hamilton path runs from its source-triangle vertex to its terminal-triangle vertex;
- every solo petal has one endpoint in each triangle;
- the three source vertices and three terminal vertices are pairwise on disjoint petals.

A natural next test compares the solo petal endpoint roles with these pair-union roles. If a solo petal runs terminal-to-source relative to the global triangles, trimming one endpoint from the corresponding pair-union cover may create a fixed-support reversed boundary dimer. If all solo petals run source-to-terminal, the three pair-union paths form a coherent directed endpoint prism and should be attacked by a cross-petal splice. No such consumer is claimed here.

Status: working symbolic role reduction. The R933 application is at theorem-interface level and should be audited with exact endpoint-support bookkeeping before canonical use.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R933"
    }
]
```
