# The tau=3 x/z pair-residue cell closes or hits a source-pinned P4/R523 packet

**Workspace:** D17
**State:** established
**Key:** `three-spoke-xz-pair-residue-tau3-root-attachment-collapse`

**Summary:** Retain the DR17.520 pair residue F of H-{x,z} with S={a,y,c}, exactly two W-blocks, and (p,tau)=(0,3). Contract each W-block. Since F has two path components, the contracted forest has five vertices and three edges. R429 forbids a singleton rail on any S-vertex, so the only support shape is S_i-W_1-S_j | S_k-W_2; in every case the outer source vertices a and c are endpoints of their F-rails. Test restoring x at the a-endpoint. If the attachment seam is tight, it gives an exact H-z row trimming back to F; if bad, R3 reverses it and the source turns (a,x,c) or (x,a,y) give a literal P4 or an R523 same-dimer collision, according to the endpoint role. Dually test restoring z at the c-endpoint, using source turns (a,z,c) and (y,c,z); success gives an exact H-x row trimming to F, failure gives P4/R523. If both attachments succeed, the two singleton rows trim to the identical common pair cover F, so DR17.519's endpoint-attachment theorem gives TWO-COVER; its same-end R407 branch is impossible because x and z attach at distinct base endpoints a and c. Hence tau=3 has no quiet residue.

### 1. The tau=3 pair-residue cell
Retain the G30 source packet

  K=(x,a,y,c,z),
  S={a,y,c},
  W=V(H)-V(K),

and one exact pair-deletion cover

  F of H-{x,z}

in the DR17.520 two-W-block branch. Assume

  p=0,  tau=3.                                             (T3.1)

Thus no selected F-state joins two vertices of S, while exactly three selected states join S to W.

### 2. Contracted forest shape and exposed outer source vertices
Contract each of the two maximal W-blocks to one labelled block-vertex W_1,W_2. Together with a,y,c this gives a five-vertex graph whose edges are exactly the three selected S|W transitions. Because F has two path components, this contracted graph is a two-component path forest with three edges and maximum degree two.

Accepted R429 says each physical rail of F has order at least two. Hence no S-vertex may be an isolated component of the contracted forest: an isolated S-vertex would be a singleton F-rail. With three S-vertices, two W-block vertices and no S-S edges, the only remaining forest shape is

  S_i - W_1 - S_j    |    S_k - W_2                      (T3.2)

up to exchange of W_1,W_2 and the two rails.

In every choice of {S_i,S_j,S_k}={a,y,c}, both outer source vertices a and c are endpoints of their physical F-rails. They may lie on the same rail or on different rails, and either may be the source or terminal endpoint.

### 3. Restore x at the physical a-endpoint
Let R_a be the F-rail containing a. Its neighbor next to a lies in W because p=0; call that physical W-neighbor u.

If a is the source endpoint, R_a=(a,u,...). Test (x,a,u). If it is tight, prepend x and obtain a tight extended rail; together with the untouched other F-rail this is an exact two-cover T_z of H-z. Trimming x from T_z recovers F literally. If (x,a,u) is bad, R3 gives

  (u,a,x) tight.                                           (T3.3)

The source spoke turn (a,x,c) is tight. On the tested dimer (a,x), (T3.3) is a head certificate with witness u and (a,x,c) is a tail certificate with witness c. Since u lies in W, u!=c. Accepted R523 therefore gives the literal P4

  (u,a,x,c).                                              (T3.4)

If instead a is the terminal endpoint, write R_a=(...,u,a). Test (u,a,x). Tightness appends x and again gives an exact H-z row trimming to F. If bad, R3 gives

  (x,a,u) tight.                                           (T3.5)

The source P5 K contains (x,a,y) tight. Thus the tested oriented dimer (x,a) has two distinct tail witnesses u and y, because u lies in W. Accepted R523 gives a same-oriented two-tail collision on (x,a).

Hence, outside source-pinned P4/R523 geometry, x restores at the physical a-endpoint and produces an exact H-z row whose x-trim is F.

### 4. Restore z at the physical c-endpoint
The c-side is dual but the exact source turns matter. Let v in W be the F-neighbor of c.

If c is the source endpoint, test (z,c,v). Tightness prepends z and gives an exact H-x row trimming to F. If bad, R3 gives (v,c,z). The source P5 contains (y,c,z), so the tested dimer (c,z) has two distinct head witnesses v and y; R523 gives a two-head collision.

If c is the terminal endpoint, test (v,c,z). Tightness appends z and gives an exact H-x row trimming to F. If bad, R3 gives (z,c,v). The source spoke turn (a,z,c) is tight, so on the tested dimer (z,c) the source gives a head certificate with witness a while (z,c,v) gives a tail certificate with witness v. Accepted R523 gives the literal P4

  (a,z,c,v).                                              (T3.6)

Thus, outside source-pinned P4/R523 geometry, z restores at the physical c-endpoint and produces an exact H-x row whose z-trim is F.

### 5. Simultaneous successful restoration closes
Assume neither side emitted P4/R523 geometry. Sections 3-4 then give exact singleton-deletion rows

  T_z of H-z, with x an endpoint and T_z-x=F,
  T_x of H-x, with z an endpoint and T_x-z=F.             (T3.7)

Apply SV93413 to these two rows. Their exchanged roots x,z are endpoints and their trims are literally the identical exact pair cover F. Moreover the attachments occur at the distinct physical base endpoints a and c. Hence they are either on different rails or at opposite ends of one rail; the same-end R407 residue of the general theorem is impossible here. The two attachments commute and give a spanning two-cover of H.

### 6. Conclusion
The (p,tau)=(0,3) pair-residue cell has no quiet survivor. Every such exact H-{x,z} cover yields

  TWO-COVER,
  a literal source-pinned P4,
  or an R523 same-oriented dimer collision.

No generic payment, birth generation, or return map is used. The conclusion is static in the one common-parent three-spoke packet. R24 and R5 are unused.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R429"
    },
    {
        "relation": "dependency",
        "revision_id": "R523"
    }
]
```