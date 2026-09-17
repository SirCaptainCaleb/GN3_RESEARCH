# Every root crossing has dual K/exterior captures, and one side is forced current

**Workspace:** D17
**State:** established
**Key:** `closed-return-root-crossing-dual-capture-forced-current-fork`

**Summary:** Let d be a root of a retained carrier K and let an exact H-d two-cover select a K-d|E crossing k-e. Choose a third K-vertex w as the singleton-sign witness for d. Accepted R527 allows either physical marker endpoint k or e to be designated as the captured signed anchor. In either orientation R526 produces an opposite signed dimer with signed endpoint c, and R428 preserving singleton d pays, outside closure, exactly to floor {d,c}. Thus the same crossing lawfully yields both alternative floors {d,k} and {d,e}. Puncturing a chosen capture endpoint c from the same H-d cover gives an exact H-{d,c} two-cover if c is a rail endpoint, or a literal three-cover compared with an R429 exact two-cover and hence a current R159 component-drop interface if c is internal. The crossing endpoints k,e cannot both be rail endpoints: then their selected adjacency would be a dimer rail, and puncturing one would produce an exact pair-deletion cover with a singleton rail, forbidden by R429. Therefore at least one of the K-side and exterior-side capture choices is forced INTERNAL/current. In particular every END root-capture rim arc carries a dual exterior floor and current component-drop portal. The full legal capture family cannot be restricted to K-side anchors.

### 1. One physical root crossing has two lawful capture anchors
Let H be a hypothetical smallest Strong Level-(1) counterexample. Let K be a proper vertex-simple tight carrier path of order at least three, let d be one physical vertex of K, and put

  E=V(H)-V(K).

Retain one actual exact two-cover

  T_d=U|V

of H-d and one selected physical crossing state on it

  k e,    k in V(K)-{d},  e in E.                         (DC.1)

In the SV60333 P5 application such a crossing is forced by accepted R508.

Choose a third carrier vertex

  w in V(K)-{d,k}.                                        (DC.2)

Under the accepted singleton signed-support convention R444, use the automatic two-vertex path through w to regard singleton (d) as a signed support with exact witness w, choosing either polarity. The selected dimer marker {k,e} avoids w.

Accepted R527 is explicit that EITHER physical endpoint of a selected crossing marker may be designated as the captured signed anchor by orienting the two-vertex marker before R526 actualization. Therefore run the same-frame capture twice as alternative legal continuations:

- orient the marker to capture k;
- orient the marker to capture e.

For a chosen capture endpoint c in {k,e}, the R526 actualized opposite support is always a dimer whose displayed signed endpoint is exactly c: either the whole marker dimer is signed, or the failed terminal test gives the short witness-plus-c dimer. Thus together with singleton (d) we have a balanced singleton-plus-dimer pair with the dimer signed at c.

Apply accepted fixed-singleton descent R428, preserving singleton d. At order two its signed-end refund deletes the unsigned dimer endpoint and, outside closure, leaves precisely singleton c. Hence for BOTH choices c=k,e there is a lawful alternative continuation

  TWO-COVER,
  or ancestry-bearing floor {d,c}.                        (DC.3)

The two descendants are alternatives, not simultaneous current states. What coexists in the source is the one selected crossing DC.1 and the legal choice of either physical marker endpoint as capture anchor.

### 2. Same-pair currentization of each capture choice
Fix c in {k,e} and puncture c from the SAME source cover T_d.

If c is a rail endpoint, its selected crossing neighbor is still present, so deleting c leaves that rail nonempty; the other rail is unchanged and nonempty. Therefore T_d-c is a literal two-path cover of H-{d,c}. Accepted pair-deletion rigidity R429 says this residue has exact cover number two, so T_d-c is an exact pair-deletion cover.

If c is internal on its T_d rail, deleting c splits that rail into two nonempty intervals and leaves the other rail unchanged. Thus T_d-c is a literal THREE-cover of H-{d,c}. Accepted R429 supplies an exact two-cover F_c of the same residue. Some selected state of F_c crosses two components of T_d-c: otherwise every F_c rail would remain inside one component of the three-cover and could not span all three source components using only two rails. Retain such a selected crossing. Accepted R159 then supplies the corresponding graph-intrinsic component-drop pair certificate.

Call these alternatives

  END(c): exact same-pair two-cover,
  INTERNAL(c): literal 3-to-2 component-drop on H-{d,c}.  (DC.4)

Thus BOTH capture anchors in DC.3 have a same-pair currentization classification in the original source frame.

### 3. The two crossing endpoints cannot both be END
Suppose for contradiction that both k and e are rail endpoints of T_d. Since DC.1 is a selected adjacency, they lie on the same T_d rail and are adjacent. A path whose two adjacent vertices are both its endpoints is exactly the dimer rail

  (k,e) or (e,k).                                         (DC.5)

Delete k. Then T_d-k is a literal two-path cover of H-{d,k} whose former dimer rail has become the singleton (e). As in Section 2 it is exact, because R429 gives pair-deletion cover number two. But the nontriviality clause of R429 forbids a singleton rail in an exact pair-deletion cover. Contradiction.

Therefore

  at least one of k,e is INTERNAL in T_d.                 (DC.6)

Combining DC.3-DC.6 gives the DUAL-CAPTURE FORCED-CURRENT FORK:

  one selected K-d | E crossing
    => lawful floors {d,k} AND {d,e} as alternative captures,
    AND at least one of the two corresponding pair deletions
       H-{d,k}, H-{d,e}
       carries a literal current 3-to-2 component-drop interface.       (DC.7)

### 4. Portal-wheel consequence
In the G23 root-capture circuit, SV60333 deliberately chooses the K-side endpoint k. If that chosen rim arc is END-currentized, DC.6 forces the exterior crossing endpoint e to be INTERNAL. Hence the exact same source row simultaneously certifies the alternative exterior capture

  floor {d,e}

and a current component-drop interface on H-{d,e}. Dually, a K-side INTERNAL rim arc is already current on H-{d,k}.

Consequently every selected root crossing in the wheel family has at least one forced-current deleted-pair portal once BOTH legal capture anchors are retained. In particular, the support-coherent END-rim branch of SV61535/SV62430 is not a geometry-free closed family: every such END edge carries a dual exterior component-drop portal in the same ancestral singleton row.

### 5. Scope fence
A current component-drop portal is not by itself strict Phi, epsilon_*, or Morse descent, and the exterior floor {d,e} need not stay inside the original five-root P5 kernel. DC.7 therefore does not close the full wheel. Its gain is family-level completeness: the reconstruction-closed capture system cannot legitimately restrict marker actualization to the K-side endpoint. The full legal choice set always includes an exterior-root branch, and one side of the two-anchor fork is forced to expose current pair-deletion geometry.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R159"
    },
    {
        "relation": "dependency",
        "revision_id": "R428"
    },
    {
        "relation": "dependency",
        "revision_id": "R429"
    },
    {
        "relation": "dependency",
        "revision_id": "R444"
    },
    {
        "relation": "dependency",
        "revision_id": "R527"
    },
    {
        "relation": "dependency",
        "revision_id": "R508"
    }
]
```