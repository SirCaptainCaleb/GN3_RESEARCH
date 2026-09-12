# A same-support maximum-forest reversal transports to R561 or a current wrap shield with both complement rails frozen

**Workspace:** D17
**State:** established
**Key:** `compatible-forest-selected-reversal-two-rail-transport`

**Summary:** Let P|U|V and Q|U|V be literal maximum spanning three-forests with identical three support sets and identical complementary rails U,V, while Hamilton paths P,Q on the common active support X select one physical dimer in opposite directions. Define the same boundary-distance discrepancy used in the fixed-complement two-cover transport. Directed R548 rotations on P and Q preserve U,V and the named reversed dimer; every successful rotation decreases the discrepancy by exactly one, while a failed rotation yields the exact graph-intrinsic reverse-wrap shield trimer. Hence finite transport reaches either an R561 boundary-reversed Hamilton dimer on X or one/two named wrap shields. At R561 every exterior vertex Hamilton-extends X; absorbing an endpoint of U (or V) either gives a spanning two-cover when that rail is a singleton or an actual support-changing maximum three-forest X+d | (U-d) | V. A wrap shield is a proper tight trimer and R4 currentizes it into an actual maximum three-forest. Thus same-support selected reversal is not an unstructured terminal global holonomy species: with the two spectator rails literally frozen it has strict finite transport to R561 support escape/closure or to named current reverse-wrap geometry.

### 1. Three-forest reversal setup
Let H be a hypothetical smallest counterexample, so pc(H)=3 by accepted R4. Retain two literal maximum spanning three-forests

  F^+ = P | U | V,
  F^- = Q | U | V,                                      (TR.1)

with the SAME unordered support partition and the SAME literal complementary path words U,V. Write

  P=(p_0,p_1,...,p_r),
  Q=(q_0,q_1,...,q_r)                                   (TR.2)

on one common active support X. Suppose one physical dimer {u,v} is selected in opposite directions:

  (p_a,p_{a+1})=(u,v),
  (q_b,q_{b+1})=(v,u).                                  (TR.3)

Define

  delta(P,Q;u,v)=a+(r-b-1).                             (TR.4)

Thus delta=0 exactly when P begins with (u,v) and Q ends with (v,u), the fixed-support boundary-reversal configuration of accepted R561.

The difference from `fixed-complement-selected-reversal-normal-form` is that the exterior of X need not be Hamiltonian as one path: here it is retained as TWO literal spectator rails U,V. The transport itself uses no property of the exterior except that these two rails remain unchanged.

### 2. Left transport freezes both spectator rails
Assume a>0. Consider the tail rotation

  P_T=(p_1,...,p_r,p_0).                                (TR.5)

Its only new turn is

  beta_P=(p_{r-1},p_r,p_0).                             (TR.6)

If beta_P is tight, accepted R548 makes P_T a Hamilton tight path on X. Because a>0, the selected state (u,v) is not cut by this rotation and remains selected, now one position closer to the left boundary. Therefore

  P_T | U | V                                            (TR.7)

is another literal maximum spanning three-forest and

  delta(P_T,Q;u,v)=delta(P,Q;u,v)-1.                    (TR.8)

Both spectator rails, including their literal path words and every retained datum not involving the changed active boundary, are unchanged.

If beta_P is bad, R3 gives the exact reverse-wrap shield

  (p_0,p_r,p_{r-1}) tight.                              (TR.9)

The original forest F^+ and the named selected orientation (u,v) remain current; the shield is additional graph-intrinsic geometry.

### 3. Right transport is dual
Assume b<r-1. Consider the head rotation

  Q_H=(q_r,q_0,...,q_{r-1}).                            (TR.10)

Its only new turn is

  alpha_Q=(q_r,q_0,q_1).                               (TR.11)

If alpha_Q is tight, accepted R548 makes Q_H Hamiltonian on X. The selected reverse state (v,u) is not cut and moves one position toward the right boundary. Hence

  Q_H | U | V                                            (TR.12)

is a literal maximum three-forest with

  delta(P,Q_H;u,v)=delta(P,Q;u,v)-1.                    (TR.13)

If alpha_Q is bad, R3 gives the exact reverse-wrap shield

  (q_1,q_0,q_r) tight.                                 (TR.14)

Again U,V are untouched.

### 4. Finite terminal normal form
Apply the two directed rotations whenever the corresponding distance coordinate is positive and the required wrap seam is tight. Every successful step decreases the nonnegative integer delta by exactly one and preserves the SAME physical discrepancy {u,v} with its two opposite selected orientations. Hence the process terminates.

At termination, independently on the two sides, either the relevant boundary-distance coordinate is zero or the corresponding named reverse-wrap shield (TR.9) or (TR.14) is present.

Thus there are only two parent terminal species:

  (R561) delta=0;
  (SHIELD) at least one still-positive side is blocked by its exact reverse-wrap trimer.  (TR.15)

No anonymous R435 disagreement or changed complement is introduced during the transport.

### 5. R561 gives closure or genuine support escape
Suppose delta=0. Then P begins with (u,v) and Q ends with (v,u). Accepted R561 says that EVERY vertex d outside X Hamilton-extends X.

Choose a physical endpoint d of U. If U is the singleton {d}, then a Hamilton path on X+d together with V is a spanning two-cover of H, contradiction.

If |U|>=2, deleting the endpoint d leaves the inherited tight path U-d. Therefore

  H(X+d) | (U-d) | V                                    (TR.16)

is a literal spanning three-path cover of H, hence another maximum three-forest. Its support partition differs from X|U|V: one physical vertex has moved from U into X. Thus R561 is a genuine support-changing exit in the three-forest space unless it closes H immediately. The same statement holds using an endpoint of V.

### 6. A failed wrap is already current graph-intrinsic geometry
A shield in (TR.9) or (TR.14) is a proper tight trimer of H because U and V are nonempty spectator components. By accepted R4, its complement has an exact two-cover. Hence the shield occurs literally as one rail of an actual maximum spanning three-forest.

This currentization does NOT assert that the shield representative has a different support partition from (TR.1), and it does not silently transport the selected reversal into that new representative. What is proved is the exact finite alternative: same-support reversal transport either reaches R561 support escape/closure or emits named graph-intrinsic reverse-wrap geometry already current in maximum-forest space.

### 7. Global holonomy consequence
The selected-reversal species therefore cannot remain as unstructured same-support order debt in the marked-holonomy program of SV35882. Along the successful transport the two spectator rails are literally fixed and the named physical reversal is retained while a strict integer discrepancy decreases. The only failures are explicit shields.

Accordingly a shortest marked-holonomy extinction argument may replace any same-support selected-reversal packet by the finite terminal interface (TR.15):

  R561 support escape / two-cover,
  or a named current reverse-wrap trimer.

The remaining global work is to consume the wrap-shield branch when it lies on a shortest support-changing marked loop.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R4"
    },
    {
        "relation": "dependency",
        "revision_id": "R548"
    },
    {
        "relation": "dependency",
        "revision_id": "R561"
    }
]
```