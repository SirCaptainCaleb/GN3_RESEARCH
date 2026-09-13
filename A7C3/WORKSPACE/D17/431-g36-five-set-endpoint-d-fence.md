# The G36 five-set does not force a Hamilton P5 with endpoint d

**Workspace:** D17
**State:** established fence
**Key:** `g36-five-set-endpoint-d-fence`

**Summary:** The local five-set geometry occurring around the G36 source wall does not, by itself, force a tight Hamilton P5 that starts or ends at the far wall vertex `d`. An explicit five-vertex boundary tournament satisfies the retained G36 seams `(d,b,t)`, `(b,t,A)`, `(A,t,C)`, `(C,t,b)` but has no Hamilton P5 with endpoint `d`. Exhaustive enumeration gives exactly four Hamilton P5 orders, all with `d` internal. Therefore any endpoint-controlled splice at `d` needs additional information beyond these local seams.

## 1. Convention
On the vertex set

`Z={A,C,t,b,d}`,

for a fixed middle vertex `v` write `x ->_v y` when `(x,v,y)` is tight. Specifying one tournament on `Z\{v}` for every middle `v` specifies a boundary 3-tournament, with reversal antisymmetry built in.

## 2. Explicit boundary tournament
Take the following star tournaments.

- At middle `A`, use the transitive order `C -> b -> d -> t`.
- At middle `C`, use the transitive order `b -> A -> d -> t`.
- At middle `b`, use the transitive order `A -> C -> d -> t`.
- At middle `d`, use the transitive order `t -> b -> C -> A`.
- At middle `t`, let `d` dominate `A,C,b`, and orient the remaining triangle `A -> C -> b -> A`.

The four retained G36 turns are then all tight:

`(d,b,t)`, `(b,t,A)`, `(A,t,C)`, `(C,t,b)`.

Thus this model contains exactly the local seams one might try to use for an endpoint-`d` splice.

## 3. Exhaustive Hamilton check
Checking all `5!=120` vertex orders against the three consecutive tight-turn conditions gives exactly four Hamilton P5 orders:

1. `(A,b,d,C,t)`;
2. `(C,b,d,A,t)`;
3. `(b,C,d,A,t)`;
4. `(b,d,A,t,C)`.

In every one, `d` is internal. Reversal of any displayed order is not automatically a tight path because tightness reverses at each middle vertex under R3 rather than preserving directed path orientation.

Hence there is no tight Hamilton P5 on this five-set with `d` as either endpoint.

## 4. Consequence and scope
The local seam packet

`(d,b,t)`, `(b,t,A)`, `(A,t,C)`, `(C,t,b)`

cannot justify an endpoint-controlled Hamilton splice through `d`. In particular, a proof step of the form “the five-set is Hamiltonian, therefore choose a Hamilton P5 ending at `d`” is invalid without an additional endpoint-forcing hypothesis.

This fence does **not** say the five-set is non-Hamiltonian. In fact the model above has the four Hamilton P5s listed in Section 3. It also does not contradict R902 or D17.430: those results assert existence of a Hamilton P5 in the relevant nonintegrable five-set, not control of its endpoint.

The purpose of this unit is purely architectural: prevent reuse of an invalid endpoint-forcing shortcut in the G36/G37 source-gate absorber.