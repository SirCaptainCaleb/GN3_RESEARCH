# Every G33 bad seam has a short active-spoke component and a rooted alternating exchange path

**Workspace:** D17
**State:** established
**Key:** `g33-short-active-component-rooted-exchange`

**Summary:** For the R540 one-hole proposal underlying SV103129, choose the cut edge inside the sole bad turn on the side adjacent to the omitted singleton partner whenever that turn contains the omitted spoke; otherwise use either cut. The omitted B-active source spoke s then lies in a J-component D_s of order at most two: source-side seams and extreme spectator seams give D_s=(s), while the only remaining near-end spectator cuts give a dimer containing s. Since s is internal in the old exact source cover F, at least one F-incidence at s leaves D_s. Moreover one physical in/out copy of s is unmatched in J, so an F-edge at that free copy is an endpoint of an alternating component C_s of M_F triangle M_J; hence delta(C_s) is 0 or +1, never -1. In the SV103932 dual-rigid branch, if C_s has positive transition weight then it must be +1 and is an F-heavy augmenting component. If it is balanced, w(C_s)<=0, so any retained old s-B transition lying on C_s must be canceled on that same alternating path by at least one J X|B transition. Thus the source-active discrepancy is rooted on a short physical component rather than anonymously distributed.

### 1. Input and the R540 singleton-partner geometry
Retain the direct G33 packet of SV103129 and either R540-style one-hole endpoint-cut proposal P on the top fiber G. Let s be its omitted B-active source spoke. In the literal R540 construction, s is exactly the singleton partner x of P616. Thus at a left cut through L=b_0 the second word is

  (s) followed by the K_s-suffix,

and at a right cut through R=b_m the first word is the K_s-prefix followed by

  (s).

The unique bad turn eta is one of the two P616 splice turns. Use the complete P616 seam ledger, not its pc(ambient)>2 conclusion.

### 2. A canonical cut leaves s on a component of order at most two
There are only four one-hole positions.

If the left cut has L in K-position 0, then eta=(s,k_1,k_2). Cut the selected edge s k_1. The resulting tight three-forest has singleton component (s). If L is in position 4, the singleton partner was already the separate word (s), so either cut inside the spectator-side eta leaves (s) untouched. If L is in position 3, the partner word is the literal dimer (s,k_4), so either cut leaves s on that dimer.

Dually, if the right cut has R in position 4, then eta=(k_2,k_3,s) and cutting k_3 s isolates s. If R is in position 0, s was already a singleton word. If R is in position 1, the partner word is the dimer (k_0,s).

Therefore one of the two defect forests from SV103530 may always be chosen so that the J-component D_s containing s has order one or two. Source-side holes and extreme spectator holes give |D_s|=1; only the near-end spectator positions give |D_s|=2.

### 3. Old source internality forces a rooted cross-component edge
In the actual old exact source cover F=U|V, the spoke s is internal, hence has one selected incoming and one selected outgoing F-edge. Since |D_s|<=2, those two old incidences cannot both remain inside D_s. Thus at least one selected F-edge incident with s leaves D_s and joins s to a different J-component. In particular, if the retained old active edge s-h with h in B is not the possible dimer edge of D_s, then s-h itself is such a component-crossing old edge. If s-h is the dimer edge, the other old F-incidence at s necessarily leaves D_s.

More precisely, D_s exposes a free matching copy of s. If D_s=(s), both s_in and s_out are unmatched in M_J. If D_s=(s,t), exactly the copy of s not used by the oriented dimer is unmatched. The corresponding copy is matched in M_F because s is F-internal. Hence an F-edge at that copy is an endpoint edge of a connected alternating path component C_s of M_F triangle M_J. Because that alternating component starts with an F-edge,

  delta(C_s)=|F cap C_s|-|J cap C_s| is 0 or +1.

It cannot be -1.

### 4. Transition-weight consequence in the SV103932 rigid branch
Retain the transition weight w(C) of SV103932. In its DUAL RIGIDITY branch every delta-zero component has w<=0. Therefore the rooted C_s has the exact alternative:

1. delta(C_s)=+1, so C_s is already one of the F-heavy augmenting components; or
2. delta(C_s)=0 and w(C_s)<=0.

In the second case, if the retained old s-B incidence lies on C_s, it contributes +1 to w(C_s). Consequently C_s must also contain at least one J-selected X|B transition, with enough total J-transition contribution to cancel that old source transition on the same alternating path. Since tau(J)<=2, only the two literal low-cut transitions are available for such cancellation.

Thus the active-spoke discrepancy is not diffuse in the rigid branch: it is either carried by a rooted augmenting path or paired on that same rooted path with one of the at-most-two physical J transitions.

### 5. Scope
This is a static localization theorem, not yet an augmentation theorem. It does not assert that C_s flips acyclically or without mixed-turn debt. It uses the exact P616 construction of R540, the old source internality retained in SV103129, and the elementary weighted-component conclusions of SV103932. R24, R5, payment, and replay are unused.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R540"
    }
]
```
