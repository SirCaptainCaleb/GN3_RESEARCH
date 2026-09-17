# Endpoint-endpoint reversal residue is an even alternating two-sheet holonomy

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-endpoint-reversal-two-sheet-parity`

**Summary:** In a fixed-complement critical block, consider an endpoint-return cycle y_i->y_{i+1} whose adjacent R435 outputs all lie in the endpoint-endpoint selected-reversal residue. Then P_i on Omega-y_i has endpoints {y_{i-1},y_{i+1}}. For one adjacent pair, if the exchanged labels y_{i+1} in P_i and y_i in P_{i+1} occupy opposite endpoint roles, non-Hamiltonicity of Omega reverses the two failed restoration seams into a literal tight P4 through y_i,y_{i+1} when the neighboring endpoints are distinct; if those neighbors coincide, one obtains a named tight trimer carrier. In either case R4 gives an ancestry-bearing maximum-three-forest recompletion. Hence a purely local survivor has the exchanged labels in the same endpoint role. Same-HEAD forces the physical edge y_i y_{i+1} to be a SINK of two endpoint spokes in the comparison orientation; same-TAIL forces it to be a SOURCE. Writing epsilon_i for the role of the matched successor y_{i+1} in P_i, the predecessor y_i has the opposite role in P_{i+1}; same-role survival therefore gives epsilon_{i+1}=opposite epsilon_i. Thus the endpoint-return cycle has even length and SOURCE/SINK fan polarity alternates around it. Moreover the same puncture paths expose both cycle neighbors, so switching every matched right core from the successor edge to the predecessor edge gives a second left-saturating endpoint-core matching whose functional cycle is the same physical cycle with reverse orientation. The last CBCA-local reversal residue is therefore a genuine two-sheet even holonomy, not an arbitrary collection of reversal cells.

### 1. Closed endpoint-return reversal residue
Retain a fixed-complement critical block

  V(H)=Omega disjoint_union V(Q)

in a hypothetical smallest Strong Level-(1) counterexample. Let

  y_0 -> y_1 -> ... -> y_{ell-1} -> y_0                 (EP.1)

be a directed cycle of an endpoint-core matching, and let P_i be the actual Hamilton path on Omega-y_i whose matched endpoint is y_{i+1}. Indices are modulo ell.

Assume that for every adjacent pair P_i,P_{i+1}, the relevant explicit R435 output has already reached the ENDPOINT-ENDPOINT selected-reversal residue of the pair-deletion currentization. In particular the exchanged label y_{i+1} is an endpoint of P_i and y_i is an endpoint of P_{i+1}.

Since P_i already has matched endpoint y_{i+1}, applying the preceding assertion at the pair P_{i-1},P_i shows that its other endpoint is y_{i-1}. Hence

  End(P_i)={y_{i-1},y_{i+1}}                             (EP.2)

for every i.

### 2. Opposite exchanged roles give an immediate tight carrier
Fix i. Let the role of y_{i+1} in P_i and the role of y_i in P_{i+1} be compared.

Suppose first that y_{i+1} is the HEAD of P_i and y_i is the TAIL of P_{i+1}. Write

  P_i=(y_{i+1},x,...),
  P_{i+1}=(...,z,y_i).

Because Omega is non-Hamiltonian, prepending the omitted y_i to P_i is impossible:

  (y_i,y_{i+1},x) bad,

so R3 gives

  (x,y_{i+1},y_i) tight.                                (EP.3)

Likewise appending the omitted y_{i+1} to P_{i+1} is impossible:

  (z,y_i,y_{i+1}) bad,

so

  (y_{i+1},y_i,z) tight.                                (EP.4)

If x!=z, (EP.3)-(EP.4) concatenate to the literal tight P4

  (x,y_{i+1},y_i,z).                                     (EP.5)

If x=z, retain instead the tight trimer (x,y_{i+1},y_i) together with its second ancestry turn (y_{i+1},y_i,x).

The opposite role pattern, y_{i+1} TAIL and y_i HEAD, is dual and yields

  (z,y_i,y_{i+1},x)                                      (EP.6)

when the two neighboring endpoints are distinct, or the analogous named tight trimer carrier when they coincide.

In every case choose the resulting vertex-simple tight carrier K of order three or four. K is proper because the disjoint fixed complement Q is nonempty. By accepted R4/P601, H-V(K) has an exact two-cover, and K together with that cover is an actual maximum spanning three-forest of H. Thus opposite endpoint roles already exit the static reversal residue into ancestry-bearing maximum-forest dynamics.

### 3. Same-HEAD is a comparison SINK fan
A purely local endpoint-endpoint reversal survivor must therefore have the exchanged labels in the same endpoint role.

Suppose y_{i+1} is the HEAD of P_i and y_i is the HEAD of P_{i+1}. Write

  P_i=(y_{i+1},x,...),
  P_{i+1}=(y_i,z,...).

The same failed-prepend argument gives

  (x,y_{i+1},y_i) tight,
  (z,y_i,y_{i+1}) tight.                                (EP.7)

Let e_i be the ordinary edge y_i y_{i+1}. In the comparison orientation, (EP.7) says that both incident endpoint spokes point INTO e_i:

  x y_{i+1} -> e_i,
  z y_i     -> e_i.                                      (EP.8)

Call this the SINK fan on e_i.

### 4. Same-TAIL is the SOURCE dual
If y_{i+1} is the TAIL of P_i and y_i is the TAIL of P_{i+1}, failed append of the omitted labels gives

  (y_i,y_{i+1},x) tight,
  (y_{i+1},y_i,z) tight,                                 (EP.9)

where x,z are the predecessor endpoints on the two paths. Hence

  e_i -> y_{i+1}x,
  e_i -> y_i z.                                          (EP.10)

This is the SOURCE fan on e_i.

### 5. Closed survival forces even parity
Let epsilon_i in {H,T} be the role of the matched successor y_{i+1} in P_i. By (EP.2), the predecessor y_i is the other endpoint of P_{i+1}, so its role in P_{i+1} is the opposite of epsilon_{i+1}.

Avoiding the opposite-role carrier of Section 2 means that the role of y_{i+1} in P_i equals the role of y_i in P_{i+1}. Therefore

  epsilon_i = opposite(epsilon_{i+1})                    (EP.11)

for every i. Thus the roles alternate around the cycle. In particular

  ell is even.                                            (EP.12)

By Sections 3-4 the comparison fan polarity also alternates SINK,SOURCE,SINK,SOURCE around the physical cycle edges.

### 6. The same puncture paths support the reverse endpoint-core matching
For each i, (EP.2) says P_i exposes not only the matched successor y_{i+1} but also the predecessor y_{i-1}. Therefore y_i is incident in the endpoint-core bipartite graph to both right cores

  Omega-{y_i,y_{i+1}},
  Omega-{y_i,y_{i-1}}.                                   (EP.13)

The first family is the set of right cores used by the original matching on the cycle. Reassign every cycle label y_i to the second core in (EP.13). This merely cyclically permutes the same set of right cores, so it remains a valid matching on those cycle labels and does not interfere with any matched right core outside the cycle. Keeping all outside matching edges unchanged gives another left-saturating endpoint-core matching.

Its functional cycle is

  y_0 -> y_{ell-1} -> ... -> y_1 -> y_0,                 (EP.14)

the same physical cycle with opposite orientation. The very same actual puncture paths realize both sheets, using their two opposite endpoint roles.

### 7. CBCA meaning
Hence the sole endpoint-endpoint reversal residue left by the parent CBCA reduction is not a bag of independent same-residue reversals. If it persists around a closed endpoint-return orbit without emitting a fresh carrier, it has the rigid form

  EVEN physical label cycle
  + alternating HEAD/TAIL matched roles
  + alternating SINK/SOURCE comparison fans
  + forward and backward endpoint-core matching sheets.  (EP.15)

This is the appropriate minimal holonomy object for the next contraction attempt. No claim is made here that the even two-sheet cycle closes H. The intended next consumer is to compare transfer/blocker states on the two matching sheets, or to show that one fan-polarity change under an admissible representative transition creates a directed comparison triangle and hence the G9 small extension core.

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
        "revision_id": "R945"
    }
]
```
