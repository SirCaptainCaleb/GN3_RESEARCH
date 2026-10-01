# Same-side double-clean swaps force a Hamiltonian five-window or a reverse cross-bridge

## Statement

In the setup of astra004corridordouble, write the middle exact deletion cover H-b=P|Q. Suppose the two clean endpoint replacements by b use the same side type on P and Q. If they are both terminal, write P=(...,u,c) and Q=(...,v,a), so P-c+b and Q-a+b are Hamiltonian in the adjacent deletion states. Then either the five-set {c,u,b,a,v} has tight Hamilton path (c,u,b,a,v), or (a,b,u) is tight. If they are both initial, write P=(c,u,...) and Q=(a,v,...). Then either {c,u,b,a,v} has tight Hamilton path (v,a,b,u,c), or (u,b,a) is tight. Consequently every clean four-support corridor produces either an explicit reverse cross-bridge through the middle omitted label, or a Hamiltonian five-vertex window W whose complement H-W is non-Hamiltonian of path-cover number exactly two.

## Body

# Proof

First suppose both clean replacements are terminal. Thus c is terminal in P=(...,u,c), a is terminal in Q=(...,v,a), and the adjacent odd-edge covers contain the replacement paths (...,u,b) and (...,v,b). Apply the standard deleted-vertex endpoint barrier to the exact cover H-b=P|Q. At the terminal end of P it gives (b,c,u) tight, hence by cyclic invariance (c,u,b) tight. At the terminal end of Q it gives (b,a,v) tight.

Exactly one of (u,b,a) and (a,b,u) is tight by boundary antisymmetry. If (u,b,a) is tight, then (c,u,b,a,v) is a tight path: its three consecutive triples are (c,u,b), (u,b,a), and (b,a,v). Otherwise (a,b,u) is tight, which is the asserted reverse cross-bridge.

Now suppose both replacements are initial: P=(c,u,...) and Q=(a,v,...). The initial endpoint barriers for omitted b give (u,c,b) and (v,a,b) tight. Cyclically, (b,u,c) is tight. If (a,b,u) is tight, then (v,a,b,u,c) is a tight path, using (v,a,b), (a,b,u), and (b,u,c). Otherwise boundary antisymmetry gives (u,b,a) tight, the asserted reverse cross-bridge.

In the Hamiltonian-five-window branch, W is proper in a minimum counterexample. Its complement cannot be Hamiltonian, since Hamilton paths on W and H-W would two-cover H. Minimality gives pc(H-W)<=2, so non-Hamiltonicity implies pc(H-W)=2. ∎
