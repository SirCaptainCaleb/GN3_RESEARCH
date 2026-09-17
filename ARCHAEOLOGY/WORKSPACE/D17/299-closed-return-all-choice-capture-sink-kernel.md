# The all-choice P5 capture graph has a sink kernel; every two-root sink is mutually internal

**Workspace:** D17
**State:** established
**Key:** `closed-return-all-choice-capture-sink-kernel`

**Summary:** Strengthen SV60333 from one arbitrarily selected root map to the digraph of all nonclosing root-capture choices on the Hamilton P5 K. Outside closure, every root has an outgoing capture arc and no loop, so a sink strongly connected component S exists with 2<=|S|<=5. Every selected K-d|E crossing in any exact H-d representative has its K-endpoint inside S whenever d lies in S. If S={a,b}, this forces a sharp endpoint exclusion: b is internal in every exact H-a two-cover and a is internal in every exact H-b two-cover. Indeed, if b were an endpoint in some H-a cover, puncturing b gives an exact H-{a,b} cover; R508 applied to the surviving Hamilton trimer K-{a,b} forces a selected crossing to E at a third K-vertex c, which already survives in the original H-a cover and therefore gives a nonclosing capture arc a->c leaving S, contradiction. Thus any reconstruction-closed two-cycle kernel is necessarily mutually internal; every END-currentized two-cycle shortens to a larger capture choice or closes H. This is genuine bounded-kernel reduction, not extinction of the remaining mutual-internal two-root cell.

### 1. Replace one chosen root map by the all-choice capture digraph
Retain the Hamilton P5 K and exterior E=V(H)-V(K) of SV60333. Work in a hypothetical nonclosing reconstruction-closed family; if any capture/actualization/payment branch below gives a spanning two-cover, stop.

Define a directed graph C_K on the five physical vertices of K. Put an arc d->k when there exists a literal exact two-cover T of H-d and a selected R508 crossing of T between K-d and E whose K-endpoint is k, and the SV60333 capture/payment continuation from that crossing is nonclosing. By the proof of SV60333, every such crossing can be oriented through R527 so that k is the captured signed endpoint, and R428 preserving d pays exactly to the ancestry-bearing floor {d,k}. In particular k!=d.

For every d in K, accepted R508 forces every exact H-d cover to contain at least one K-d|E crossing. Under the standing nonclosure assumption at least one such crossing therefore gives an outgoing arc of C_K. Hence every vertex has outdegree at least one and C_K has no loops.

Choose a sink strongly connected component S of C_K. Since every vertex of S has an outgoing arc and no arc may leave a sink component, while loops are impossible,

  2 <= |S| <= 5.                                           (AC.1)

This is canonical family-level compression: unlike the one-edge-per-root function of SV60333, S is defined using ALL available nonclosing root-capture choices.

### 2. Sink closure forces every current K/E crossing to stay inside S
Fix d in S and any exact two-cover T of H-d. Let ke be any selected crossing of T with k in K-d and e in E. The SV60333 construction may use this very crossing as its marker: choose w in K-{d,k}, sign the singleton d with witness w, orient the marker to capture k, and apply R527 followed by R428. Under the standing nonclosure assumption this produces the arc d->k in C_K. Since S is a sink, k must lie in S. Thus

  every selected K-d|E crossing in every exact H-d cover has its K-endpoint in S.   (AC.2)

The assertion is simultaneous over all exact representatives because C_K contains all choices, not one selected representative per root.

### 3. A two-root sink is mutually internal in every singleton fiber
Suppose now S={a,b}. Then AC.2 says every selected K-a|E crossing in every exact H-a cover is incident with b on the K side, and symmetrically every K-b|E crossing in every exact H-b cover is incident with a.

We claim b is internal in every exact H-a two-cover. Suppose instead that some exact cover

  T=P|Q of H-a

has b as a physical rail endpoint. Delete b. Both T rails are nonempty after the deletion: accepted pair-deletion rigidity R429 says every exact H-{a,b} cover has two nontrivial rails, and the punctured endpoint cover cannot collapse to one spanning path because that would contradict pc(H-{a,b})=2. Hence

  T-b

is itself a literal exact two-cover of H-{a,b}.

Apply accepted R508 to this pair-deletion residue with deleted set D={a,b}, absorbable block

  S_0=K-{a,b},

and carrier Q_K=K. Since K is a Hamilton path on D union S_0, every exact cover of H-{a,b}, in particular T-b, selects a physical crossing

  ce,   c in K-{a,b}, e in E.                             (AC.3)

The selected state ce survives literally in the original T because it avoids b. Therefore T, regarded again as an exact H-a cover, contains a K-a|E crossing whose K-endpoint is c. By Section 2 this gives the capture arc a->c in C_K. But c is not in {a,b}=S, contradicting that S is a sink.

Thus b is internal in every exact H-a cover. Interchanging a and b gives

  b internal in every exact H-a cover,
  a internal in every exact H-b cover.                    (AC.4)

### 4. Kernel-shortening consequence
A directed two-cycle a<->b extracted from one arbitrary root map need not by itself be rigid. The all-choice sink quotient is stronger. If either direction admits even one END-currentized source representative, puncturing that endpoint exposes by R508 a third-root crossing and therefore an outgoing capture choice to K-{a,b}; the pair is not a closed sink. Consequently every reconstruction-closed two-root capture kernel is forced into the fully mutual-INTERNAL cell AC.4.

Equivalently, the shortest wheel rim has the dichotomy

  END somewhere => TWO-COVER or an escaping third-root capture,
  closed two-root sink => both roots internal in every opposite singleton fiber.   (AC.5)

This is a genuine shortening/extremalization of the G23 wheel kernel: all endpoint-currentized 2-cycles are eliminated from a closed sink.

### 5. Scope fence
The mutual-internal cell is not extinguished here. Puncturing a or b from the opposite singleton fiber gives a literal three-cover of H-{a,b} and hence the existing R159 component-drop packet against an exact pair-deletion cover, but paying that packet anonymously would lose the current Johnson-triangle geometry and is not counted as progress. The next target is to combine AC.4 with the two hub spokes {x,a},{x,b} on the common triple-deletion residue, or otherwise show that the mutual-internal cell forces a strict global Phi/epsilon improvement. Alternative current representatives remain alternatives unless explicitly constructed simultaneously.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R508"
    },
    {
        "relation": "dependency",
        "revision_id": "R429"
    },
    {
        "relation": "dependency",
        "revision_id": "R527"
    },
    {
        "relation": "dependency",
        "revision_id": "R428"
    }
]
```