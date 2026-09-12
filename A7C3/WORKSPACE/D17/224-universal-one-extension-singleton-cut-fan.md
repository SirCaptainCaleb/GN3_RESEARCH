# Universal one-extension forces an all-vertex R508 cut fan; a unique core crossing exports to fresh forest dynamics

**Workspace:** D17
**State:** established
**Key:** `universal-one-extension-singleton-cut-fan`

**Summary:** Let S be a universally one-extendable four-set, Y=V(H)-S, fix s in S and T=S-s. For every exterior w and every exact two-cover F of H-s, accepted R508 applied to the Hamilton support S+w forces F to cross (T+w)|(Y-w). Every exact F therefore has at least one selected T|Y state. Writing a=e_F(T), e=e_F(T,Y), b=e_F(Y), exact two-cover arithmetic gives a+e+b=|Y|+1 and b<=|Y|-2 because Y is non-Hamiltonian, hence a+e>=3. If e=1 then necessarily a=2 and b=|Y|-2: T is one contiguous tight trimer, Y splits into exactly two path blocks A|B, and the unique T|Y edge joins an endpoint t of the trimer to an endpoint u of A. The all-w cut for w=u forces A to have order at least two and makes the next A-edge at u the unique crossing of (T+u)|(Y-u), so the R573 unique-transition cell is available with Hamilton absorber S+u. If S itself is non-Hamiltonian, A|B is an exact two-cover of Y and accepted R157 applies at endpoint u, forcing u internal in every Hamilton S+u order and producing the fresh maximum three-forest P_u|(A-u)|B with B literally unchanged. Thus the one-core-crossing branch is nonterminal in the non-Hamilton-core case; the remaining unresolved branch has at least two T|Y transitions in every minimizing exact representative, or S Hamiltonian.

### 1. Universal one-extension setup
Retain the universal one-extension four-set setup of SV26947 in a hypothetical smallest Strong Level-(1) counterexample H. Thus S is a four-set such that S+w is Hamiltonian for every w in

  Y=V(H)-S,

and Y is non-Hamiltonian. Fix s in S and put

  T=S-s.

Then H-s is non-Hamiltonian and has exact path-cover number two by R4.

### 2. Every exterior label gives an R508 cut on every exact H-s representative
Fix w in Y. Since S+w is Hamiltonian, choose a Hamilton tight path on

  {s} union T union {w}.

Apply accepted R508 with deleted block D={s} and absorbable remainder block

  T union {w}

inside the exact deletion residue H-s. Therefore EVERY literal exact two-cover F of H-s selects at least one state crossing

  (T union {w}) | (Y-{w}).                                  (SC.1)

This holds simultaneously for every w in Y and for every exact representative F of H-s.

### 3. Every exact representative crosses T|Y
Let F be any exact two-cover of H-s. If F selected no T|Y state, each connected F-rail would lie wholly in T or wholly in Y. Since F has exactly two nonempty rails and spans the nonempty sets T and Y, one rail would have to span Y. That would Hamiltonize Y, contradiction. Hence

  e_F(T,Y)>=1.                                               (SC.2)

Write

  a=e_F(T),
  e=e_F(T,Y),
  b=e_F(Y),
  m=|Y|.

F has m+3 vertices and exactly m+1 selected states, so

  a+e+b=m+1.                                                (SC.3)

Because F[Y] is a path forest and Y is non-Hamiltonian, F[Y] cannot be connected spanning; hence

  b<=m-2.                                                   (SC.4)

Also a<=2 because T has three vertices and F[T] is a forest. Thus (SC.3)-(SC.4) give

  a+e>=3.                                                   (SC.5)

### 4. Exact normal form when there is one T|Y transition
Assume e=1. Then (SC.5) and a<=2 force

  a=2,
  b=m-2.                                                    (SC.6)

Therefore F[T] is a connected three-vertex path, and F[Y] has exactly two connected path components; write them A and B. The unique T|Y selected state must join an endpoint t of the T-path to an endpoint u of one Y-path, say A, because selected degree is at most two in a path cover.

Now use the universal cut (SC.1) at w=u. The unique T|Y edge t-u lies wholly inside T+u, so it does not cross

  (T+u)|(Y-u).

There is no other T|Y edge. Hence the required crossing must be a selected Y-edge incident with u. In particular A is nontrivial, u has exactly one selected neighbor v in A, and the state uv (or vu, according to the rail orientation) is the UNIQUE selected crossing of

  (T+u)|(Y-u).                                              (SC.7)

Thus accepted R573 applies with deleted block {s}, absorber-side block T+u, complement Y-u, and Hamilton absorber S+u. This is an exact unique-transition cell on the actual representative F. No endpoint-accessibility conclusion is asserted merely from R573.

### 5. Non-Hamilton S makes the one-crossing branch nonterminal
Assume additionally that S itself is non-Hamiltonian. Since Y is non-Hamiltonian and F[Y]=A|B is a spanning two-path cover, A|B is an exact two-cover of Y. The universal-extension hypothesis says every r in Y Hamilton-extends S. Accepted R157 therefore applies to this fixed residual cover A|B and the endpoint u of A.

Choose any Hamilton path P_u on S+u. R157 forces u to be internal in P_u and gives the literal spanning minimum three-cover

  P_u | (A-u) | B.                                         (SC.8)

The opposite residual rail B survives literally, and all selected states of A except its unique terminal state at u survive exactly as in R157. Because A is nontrivial by (SC.7), A-u is nonempty.

Hence, when S is non-Hamiltonian, a minimizing exact H-s representative with exactly one T|Y transition cannot be a terminal static crossing pattern: it emits an actual fresh maximum-three-forest representative with support moved from the singleton deletion coordinate s to the universal-extension coordinate u.

### 6. Remaining branch
The unresolved part of this cut-fan reduction is therefore concentrated in either

1. the Hamiltonian-S case; or
2. exact H-s representatives minimizing e_F(T,Y) with e_F(T,Y)>=2.

The all-w cut obligations (SC.1) remain available in both branches. No extinction of the resulting global holonomy is claimed here.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R4"
    },
    {
        "relation": "dependency",
        "revision_id": "R508"
    },
    {
        "relation": "dependency",
        "revision_id": "R573"
    },
    {
        "relation": "dependency",
        "revision_id": "R157"
    }
]
```
