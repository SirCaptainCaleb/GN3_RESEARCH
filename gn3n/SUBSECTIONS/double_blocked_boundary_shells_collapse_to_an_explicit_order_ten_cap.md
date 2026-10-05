# Double blocked boundary shells collapse to an explicit order-ten cap

## Metadata

- ID: double_blocked_boundary_shells_collapse_to_an_explicit_order_ten_cap
- Parent Section: article_vii_synthesis_and_exact_frontier
- Position: 31
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Cold composition

(none yet)

## Development

## Double blocked boundary shells collapse to an explicit order-ten cap

Let G be a genuine two-deletion state. Suppose G-{x,y}=P|Q, where P=(p_1,...,p_s) and Q=(q_1,...,q_t), with s,t at least 4. Assume x,y have the same initial fixed-pair signature and the same terminal fixed-pair signature. Then K_I={x,y,p_1,q_1} and K_T={x,y,p_s,q_t} are Hamiltonian four-supports.

At the initial boundary consider U_I=K_I union {p_2,q_2}. If either K_I union {p_2} or K_I union {q_2} is Hamiltonian, then G already has a Hamiltonian five-component whose complement is the inherited two-cover P[3,s]|Q[2,t] or P[2,s]|Q[3,t], respectively. Thus this branch enters the five-component endpoint-handoff interface.

Assume instead that both five-extensions are non-Hamiltonian. By the theorem that two non-Hamiltonian five-extensions of a Hamiltonian four-set force all four opposite five-deletions Hamiltonian, for every z in K_I the set U_I-{z} is Hamiltonian. In particular A={y,p_1,q_1,p_2,q_2} is Hamiltonian.

Apply the same argument at the terminal boundary. Put U_T=K_T union {p_{s-1},q_{t-1}}. If either terminal five-extension is Hamiltonian, again one obtains a five-component state with inherited two-cover complement. Otherwise every opposite five-deletion is Hamiltonian, and in particular B={x,p_s,q_t,p_{s-1},q_{t-1}} is Hamiltonian.

When both boundaries are blocked, A and B are disjoint and A union B is exactly the ten-label endpoint shell
E={x,y,p_1,p_2,p_{s-1},p_s,q_1,q_2,q_{t-1},q_t}.
Hence E=A|B is an explicit 5|5 two-cover.

Therefore every bidirectionally compatible genuine two-deletion core satisfies the following dichotomy.

(1) One boundary admits a hole-preserving Hamiltonian five-support whose complement is the inherited two-cover, so the problem enters the five-component handoff machinery.

(2) Both boundaries are blocked, and all unbounded data lie in the untouched interiors P[3,s-2] and Q[3,t-2], while the entire interaction with the hole is compressed to an explicitly two-coverable ten-vertex endpoint cap E.

The second alternative is stronger than a generic small-order reduction: its 5|5 cover is forced directly by the two six-shell equality relations, with one hole vertex on each five-side.

The remaining obligation is anchored routing, not Hamiltonicity of the cap. One must repartition or order the two Hamiltonian five-sides so that the two neutral interiors can be threaded through them using the inherited oriented boundary edges. Four-end synchronization points those boundary edges in the reversing direction, so an arbitrary 5|5 cover of E is insufficient. Thus the blocked-blocked frontier is precisely a bounded order-ten endpoint-routing problem.
