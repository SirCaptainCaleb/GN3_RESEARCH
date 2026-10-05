# Three bridge candidates join two tails and absorb a six-vertex packet

## Metadata

- ID: three_bridge_candidates_join_two_tails_and_absorb_a_six_vertex_packet
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 59
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Lemma. Let S be a six-vertex set and let T=(t_1,...,t_k), U=(u_1,...,u_l), k,l>=2, be vertex-disjoint tight paths disjoint from S. Call v in S a bridge candidate if either (T,v,U) or (U,v,T) is tight. These conditions are tested respectively by
h(t_{k-1},t_k,v)=h(t_k,v,u_1)=h(v,u_1,u_2)=1,
or by the symmetric three triples with T,U exchanged.

If at least three vertices of S are bridge candidates, then S union V(T) union V(U) has a two-path cover, of orders 5,k+l+1.

Proof. The four-of-six theorem in [[smallset01]] gives at least four vertices v in S for which S-v is Hamiltonian. At most two vertices fail this deletion test. Therefore one of the at least three bridge candidates has S-v Hamiltonian. Use a Hamilton order on S-v as one component and the actual tight concatenation (T,v,U) or (U,v,T) as the other. They partition the whole vertex set. QED.

The exact sufficient test is weaker than the cardinality condition: any single bridge candidate with Hamiltonian deletion suffices. If the test fails, every bridge candidate is one of the at most two non-Hamiltonian deletion labels. Thus three candidates are sufficient, not asserted necessary.

Application to a mixed positive span-two double. Write its corridor paths P=(p_1,...,p_s), Q=(q_1,...,q_t) in their tight orientations and its exterior vertices x,y. If s,t>=4, choose
S={x,y,p_1,p_2,q_1,q_2},
T=(p_3,...,p_s), U=(q_3,...,q_t).
Both tails are tight. The preceding lemma gives a two-cover of the complete determining span whenever the bridge/deletion test succeeds. Testing all candidates uses only S, the initial and terminal ordered pairs of T and U, at most fourteen distinct vertices. The tails themselves can be arbitrarily long. The five-set Hamiltonicity test is bounded and is supported by the audited six-set theorem.

This is a bounded certificate for a successful repair, not an exhaustive finite reduction: the reversed initial hooks of the original double do not by themselves guarantee three bridge candidates, or even one candidate with a good deletion. In particular the conditions h(p_2,p_1,x)=h(q_2,q_1,y)=1 cannot be substituted for any of the three bridge triples unless the actual labels and positions agree.

Unlike the failed simultaneous two-tail attachment target in [[protected_mixed_doubles_can_forbid_simultaneous_preservation_of_both_tail_pairs]], this construction places both old tails in the same final component. The other component uses the five packet vertices. It therefore changes the assignment of tails to final paths and does not require both final paths to end in old corridor pairs.

The resulting two-cover can be normalized on the full determining span J and gives an outward positive-word order. Frozen inherited-mask carriers on a fixed ambient face remain available. Shorter corridor paths, failure of the bridge/deletion test, and compatibility of choices across ambient faces remain separate obligations.
