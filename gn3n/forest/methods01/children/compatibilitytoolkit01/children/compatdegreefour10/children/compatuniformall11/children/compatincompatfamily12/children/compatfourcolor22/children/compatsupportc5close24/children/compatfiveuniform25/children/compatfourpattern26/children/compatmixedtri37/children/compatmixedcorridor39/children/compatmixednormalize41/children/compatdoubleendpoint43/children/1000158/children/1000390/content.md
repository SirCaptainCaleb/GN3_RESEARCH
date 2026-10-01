# The double-endpoint five-set branch gives a two-move strict quadratic descent

## Statement

Let H be a minimum counterexample and let H-b=P|Q be a deletion cover with p=|P|, q=|Q|>=3. In the same-slot double-endpoint replacement setting of compatdoubleendpoint43, if the reverse-cross-triple alternative does not occur, then the singleton lift P|Q|{b} reaches in two legal pairwise repartitions a spanning three-cover of component orders p-2, q-2, 5. Its quadratic potential is smaller by 4(p+q-8)=4(|V(H)|-9)>0. Hence at a quadratic-potential minimum of its pairwise-repartition component, the Hamiltonian-five branch is impossible: a reverse cross triple must occur.

## Body

By 31a72c1dd151, the Hamiltonian branch of compatdoubleendpoint43 has an explicit Hamilton path W on {a,u,b,c,v} which reverses both selected endpoint edges. Inspect the same four certified orders.

When a is terminal in P, the W-order begins with the tight 3-path S=(a,u,b); when a is initial, the W-order ends with the tight 3-path S=(b,u,a). In either case, deleting the endpoint a and its neighbor u from the displayed path P leaves an inherited tight path P' of order p-2. Therefore the pair P|{b} has a legal two-path repartition P'|S.

Now repartition S|Q. If c is terminal in Q, deleting c and its neighbor v leaves the inherited tight path Q' of order q-2, and the certified W-order contains the reversed pair c,v adjacent to S in exactly the displayed five-path. If c is initial, the certified W-order analogously contains v,c adjacent to S. Thus S|Q has the legal two-path repartition W|Q'. This is a second pairwise move.

Consequently
  P|Q|{b} -> P'|Q|S -> P'|Q'|W
lies in one pairwise-repartition component. The old component orders are p,q,1 and the final orders are p-2,q-2,5. Hence
  Phi_old-Phi_new
  = p^2+q^2+1 - [(p-2)^2+(q-2)^2+25]
  = 4p+4q-32
  = 4(p+q-8)
  = 4(|V(H)|-9).
Minimum-counterexample calculus gives |V(H)|>10, so the drop is strictly positive. Therefore a locally Phi-minimal trapped component cannot realize the Hamiltonian-five branch; only the explicit reverse cross triple remains.
