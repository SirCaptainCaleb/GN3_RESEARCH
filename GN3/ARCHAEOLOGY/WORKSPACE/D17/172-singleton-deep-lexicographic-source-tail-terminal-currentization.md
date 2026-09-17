# Lexicographic source/tail transport eliminates T+ into a two-sided current common shadow

**Workspace:** D17
**State:** established
**Key:** `singleton-deep-lexicographic-source-tail-terminal-currentization`

**Summary:** For any exact H-t row R|B selecting e0->e1 with (t,e0,e1) tight, source distance lambda>0 and tail count tau, successful source rotation or source-to-B transfer lowers lambda, while a terminal shave through any Hamilton B+q lowers tau at fixed lambda. Thus (lambda,tau) is a genuine finite lexicographic coordinate. A nonclosing motion-terminal is T0 (tau=0) or T+ (tau>0 and B+q non-Hamiltonian). T+ is not a true structural terminal: tau>0 and lambda>0 force |R|>=4, and the failed-wrap endpoint-transfer proof remains valid already at order four because R579 double-failure gives its reverse P4 for every order >=4 and all quiet replacement P4s remain vertex-simple there. Hence both endpoint deletion fibers are DIRECT outside labelled P4/R435. On X=H-{s,q,t} they share M|B. The q-end cannot be quiet because that would Hamiltonize B+s; the s-end cannot be quiet in T+ because its sole quiet form Hamiltonizes B+q. Therefore outside explicit P4/R435, T+ exports TWO forced-current endpoint fibers on one literal common shadow, each giving component drop or genuine support-partition disagreement with physical crossings retained. Only T0 remains a terminal of the lexicographic motion itself.


### 1. Exact lexicographic coordinate
Let

  R=(r_0,...,r_m) | B

be a literal exact two-cover of H-t. Suppose R selects the physical oriented state

  e_0 -> e_1 = r_a -> r_{a+1}

and the restoration turn (t,e_0,e_1) is tight. Put

  lambda=a,
  tau=m-a-1,
  s=r_0,
  q=r_m.

Assume lambda>0. The accepted R548 tail rotation, when its sole wrap seam

  (r_{m-1},r_m,r_0)

is tight, preserves the selected e_0->e_1 state and lowers lambda by exactly one. Independently, if B+s has any Hamilton order B_s, then

  (r_1,...,r_m) | B_s

is an exact H-t cover, preserves the same selected physical dimer, and lowers lambda by exactly one. These are genuine first-coordinate moves, even though the second move changes the support partition.

Now suppose the current tail wrap is bad and B+s is non-Hamiltonian. If tau>0 then q occurs strictly after e_1, so deleting q does not destroy the selected dimer. If B+q has any Hamilton order B_q, then

  (r_0,...,r_{m-1}) | B_q

is an exact H-t cover with the same lambda and with tau decreased by exactly one. This is a genuine second-coordinate move.

Therefore the ordered pair (lambda,tau), with lambda primary, strictly decreases under every displayed move. Source moves may increase tau after changing support, but they lower lambda; terminal shaves leave lambda fixed and lower tau. Since both coordinates are nonnegative integers, iteration is finite. If lambda reaches zero, prepending t using (t,e_0,e_1) closes H with B.

A nonclosing motion-terminal with lambda>0 therefore has a failed tail wrap, B+s non-Hamiltonian, and either

  T0: tau=0,

or

  T+: tau>0 and B+q is non-Hamiltonian.

The rest of this section proves that T+ is not a structural terminal.

### 2. The failed-wrap endpoint theorem is local already at order four
In T+ we have lambda>0 and tau>0, hence |R|=lambda+2+tau >=4. Write p=r_{m-1}. As in `singleton-deep-wrap-terminal-endpoint-transfer`, appending t to R would close H if (p,q,t) were tight, so

  (p,q,t) bad,
  (t,q,p) tight.

Let alpha=(q,s,r_1) be the opposite R579 wrap seam. The current tail seam (p,q,s) is bad. If alpha is also bad, accepted R579 is already in its double-failure branch; because |R|>=4, its reverse P4

  (r_1,s,q,p)

is vertex-simple and tight. Thus outside labelled-P4 output, alpha is tight.

This is the only point in the earlier q2-specific proof where a rail-size floor was invoked. Its written q2 floor |R|>=5 is stronger than needed: the accepted R579 P4 clause requires only |R|>=4. The quiet fixed-hub replacement analysis also remains literal at order four. Indeed, after deleting s there are at least three old R-vertices. Outside R435 order activity, a support-copy Hamilton replacement can place t only in one of the first two slots; otherwise its first two old vertices are r_1,r_2 and prepending s Hamiltonizes R+t. The two surviving orders are

  (t,r_1,r_2,...,q),
  (r_1,t,r_2,...,q),

and the same tests used in WT.14-WT.17 give a labelled P4. When |R|=4 these are respectively P4s on the four distinct vertices q,t,r_1,r_2 or q,t,r_1,s (with the dual bad-seam alternative again using r_2=p), so no degeneracy occurs.

Dually, after deleting q, outside R435 a support-copy Hamilton replacement can place t only in one of the last two slots. The two orders

  (s,r_1,...,p,t),
  (s,r_1,...,r_{m-2},t,p)

give the same WT.22/WT.24/WT.25 labelled P4s. For |R|=4, r_{m-2}=r_1 and p=r_2, so all displayed P4s still have four distinct vertices.

Consequently the fixed-hub dichotomy used in SV14039 extends verbatim to every current T+ row: outside explicit labelled P4 and exact R435 geometry, BOTH endpoint deletion fibers are END-DIRECT. Namely, some exact H-s cover selects an actual adjacency crossing (R-s)|B, and some exact H-q cover selects an actual adjacency crossing (R-q)|B. No q2-specific order-five hypothesis remains.

### 3. T+ forces both endpoint fibers current on one common shadow
Put

  M=(r_1,...,p),
  X=H-{s,q,t}.

The two ancestral pair-deletion covers

  (M,q)|B on H-{s,t},
  (s,M)|B on H-{q,t}

both restrict to the same literal exact two-cover

  M | B

of X. Exactness is immediate: if X were Hamiltonian, the deleted three-set {s,q,t} has a tight Hamilton order by R3 and the two paths would cover H.

Apply the exact currentization argument of `singleton-deep-end-direct-pair-deletion-currentization` separately to the two END-DIRECT fibers. Trimming t and then the opposite endpoint yields, on X, either an ancestry-bearing component drop with an actual M|B crossing, or a genuine support-partition disagreement with bidirectional selected crossings, unless the mixing localizes entirely at the trimmed endpoint.

For the q-end, such a quiet localization would Hamiltonize B+s. But T+ inherits the failed-source-transfer condition that B+s is non-Hamiltonian. Hence the q-end is forced current.

For the s-end, SV14503 identified the unique quiet localization exactly: it is an endpoint transfer whose mixed rail Hamiltonizes B+q. T+ assumes B+q is non-Hamiltonian. Hence the s-end is forced current as well.

Thus every T+ state has the exact alternative:

1. an explicit labelled P4 or exact R435 geometry produced while currentizing an endpoint fiber; or
2. on the single residue X=H-{s,q,t}, TWO endpoint-derived current representations against the literal ancestral cover M|B, each furnishing either a component-drop crossing or genuine support-partition disagreement with physical selected crossings retained.

In particular T+ is eliminated as a terminal species of the restoration program. It is a two-sided current common-shadow output. No generic R159/R176/R523 payment is taken, and no claim is made that the two endpoint-derived crossings already coincide or close H.

### 4. Remaining terminal
The only terminal of the lexicographic source/tail motion not consumed above is T0, where tau=0 and the tracked state e_0->e_1 itself is terminal on R. Any q2/lower-lift ancestry, including the lambda=1 neighboring-fiber switch when available, remains attached to that T0 row and should be consumed there rather than converted into anonymous packet currency.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    },
    {
        "relation": "dependency",
        "revision_id": "R548"
    },
    {
        "relation": "dependency",
        "revision_id": "R579"
    },
    {
        "relation": "dependency",
        "revision_id": "R159"
    },
    {
        "relation": "dependency",
        "revision_id": "R410"
    }
]
```
