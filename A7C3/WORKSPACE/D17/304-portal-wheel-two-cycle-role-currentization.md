# Every root-capture 2-cycle is END-END or current component-drop geometry on its own rim pair

**Workspace:** D17
**State:** established
**Key:** `portal-wheel-two-cycle-role-currentization`

**Summary:** Complete the currentization-role split for a G23 root-capture 2-cycle d<->k. Each arc of SV60333 is END or INTERNAL according to whether its captured opposite root is an endpoint or internal in the source singleton cover. END-END is the separately classified SV61840 packet. In an END/INTERNAL cycle, puncturing the END-captured root gives an exact two-cover of H-{d,k}, while puncturing the INTERNAL-captured root gives a literal three-cover of the same residue; the exact rim cover therefore contains a current selected component-crossing for the opposite arc. In an INTERNAL/INTERNAL cycle, R429 supplies one exact two-cover of H-{d,k}; that single current representative must cross components of each of the two literal three-covers, giving a simultaneous double component-drop interface on one physical rim pair. Thus no non-END 2-cycle survives only as two paid-return arrows: its obstruction is already currentized on the common pair deletion.


### 1. Root-capture 2-cycle and the END/INTERNAL labels

Retain SV60333 and a directed rim 2-cycle on distinct roots \(d,k\in K\):

\[
 d\to k,\qquad k\to d.
\]

Let \(T_d\) be the actual exact singleton-deletion cover of \(H-d\) used to generate the first arc, and \(T_k\) the exact cover of \(H-k\) used for the second. By construction \(k\) is the captured \(K\)-endpoint of a selected \(K-d\mid(H-K)\) crossing in \(T_d\), while \(d\) is the captured \(K\)-endpoint of a selected crossing in \(T_k\).

Put

\[
 W=H-\{d,k\}.
\]

SV60333 gives the exact role split after puncturing the captured vertex:

- **END:** if \(k\) is an endpoint of its \(T_d\)-rail, then \(T_d-k\) is a literal exact two-cover of \(W\);
- **INTERNAL:** if \(k\) is internal, then \(T_d-k\) is a literal three-cover of \(W\).

The same dichotomy applies to the opposite arc \(k\to d\).

### 2. END-END is the bounded reciprocal-extension packet

If both arcs are END, the two endpoint punctures are exact two-covers of the same residue \(W\). This is exactly the scope of `portal-wheel-end-end-two-cycle-classification` SV61840.

Hence END-END already reduces to:

1. same-fiber support-partition disagreement and the accepted R410/R176 portal;
2. explicit R435 geometry;
3. a spanning two-cover; or
4. the shared-exterior R407 bidirectional rim-dimer interaction.

No claim beyond SV61840 is added in this branch.

### 3. Mixed END/INTERNAL: the opposite rim arc itself supplies the component-drop cover

Assume, without loss of generality, that \(d\to k\) is INTERNAL while \(k\to d\) is END.

Deleting \(k\) from \(T_d\) produces a literal three-cover

\[
 R_d=R_1\mid R_2\mid R_3
\]

of \(W\). Deleting endpoint \(d\) from \(T_k\) produces a literal exact two-cover

\[
 F_k=F_1\mid F_2
\]

of the SAME residue \(W\).

A two-path cover of \(W\) cannot have every selected adjacency contained inside one of the three \(R_d\)-components. If it did, each \(F_i\) would lie in one \(R_d\)-component, so two \(F\)-components could cover at most two nonempty \(R_d\)-components, contradiction. Therefore \(F_k\) selects at least one physical state

\[
 xy
\]

whose endpoints lie in two distinct \(R_d\)-components.

This is the elementary component-drop crossing underlying accepted R159/R176, but here its current representative is not an arbitrary recompletion: it is literally the END-punctured representative supplied by the OPPOSITE root-capture arc. Thus the crossing, both source singleton rows \(T_d,T_k\), the rim pair \(\{d,k\}\), and both capture ancestries are simultaneously retained before any payment.

The INTERNAL/END case is the exact dual.

### 4. INTERNAL-INTERNAL: one exact rim cover crosses both three-cover decompositions

Assume now both arcs are INTERNAL. Puncturing the captured vertices gives two literal three-covers of the same residue:

\[
 R_d=T_d-k,\qquad R_k=T_k-d.
\]

Accepted pair-deletion rigidity R429 supplies an exact two-cover

\[
 F=F_1\mid F_2
\]

of \(W\).

Apply the same component-counting argument to \(F\) versus \(R_d\). Some selected state of \(F\) crosses two \(R_d\)-components. Apply it again to the SAME current exact cover \(F\) versus \(R_k\). Some selected state of \(F\) crosses two \(R_k\)-components. The two selected states may coincide or may be different; no coincidence is asserted.

The important synchronization is that both component-drop obligations live in one actual exact pair-deletion representative \(F\) on the one physical rim pair \(\{d,k\}\), while the two three-cover decompositions retain their opposite root-capture ancestries. Accepted R159/R176 may be applied to either crossing if a pair birth is desired, but generic payment is not needed to state the current double-crossing interface.

### 5. Two-cycle role normal form

Every G23 root-capture 2-cycle therefore lies in exactly one of the following currentization regimes:

1. **END-END:** the bounded SV61840 reciprocal-extension classification;
2. **END-INTERNAL / INTERNAL-END:** one source-pinned current component-drop crossing, carried by the exact punctured representative of the opposite rim arc;
3. **INTERNAL-INTERNAL:** one common exact rim representative carrying component-drop crossings against BOTH opposite three-cover decompositions.

Thus a rim 2-cycle cannot hide solely in alternative paid-return descendants. As soon as either captured root is internal, the cycle already has current geometry on the common pair-deletion residue \(H-\{d,k\}\). The remaining G23 problem is to consume these current crossings together with the two spoke ancestries, or to show that their reconstruction forces a shorter/global-objective-decreasing return.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R159"
    },
    {
        "relation": "dependency",
        "revision_id": "R176"
    },
    {
        "relation": "dependency",
        "revision_id": "R429"
    }
]
```