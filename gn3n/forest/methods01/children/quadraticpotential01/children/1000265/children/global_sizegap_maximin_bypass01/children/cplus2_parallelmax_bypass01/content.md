# The c+2,c,c longest-path residue yields an inherited-block edge or two disjoint maximum paths

## Statement

Let H be a minimum counterexample and let A|B|C be a globally Phi-minimal spanning three-cover with |A|=c+2 and |B|=|C|=c. Assume A=(a_0,...,a_{c+1}) is globally longest. Put S=(a_1,...,a_c), x=a_0, y=a_{c+1}, and J=H-V(S). Then for every two-cover T=P|Q of J, with |P|=c+2 and |Q|=c, at least one of the following holds: (1) one of x,y is internal in its T-component, and for that label z every two-cover of J-z has an ordinary edge joining two distinct inherited path blocks of T-z; (2) x,y are the two displayed endpoints of Q, P is vertex-disjoint from A and is itself globally longest, and therefore A and P contain a two-sided extension witness: there exist distinct r,p,q in V(A) union V(P) such that both (r,p,q) and (p,q,r) are tight.

## Body

# Proof

Since A is globally longest and the displayed globally Phi-minimal profile is a=c+2, b=c, c=c, apply the certified profile-propagation theorem 5ec26ec830d3 to the tight c-path S. Every two-cover T=P|Q of J=H-V(S) has component-order multiset {c+2,c}; name the components so |P|=c+2 and |Q|=c.

The path S has displayed predecessor x=a_0 and successor y=a_{c+1} in A. Apply the certified adjacent-window theorem 203187bcc627. For each z in {x,y}, either z is internal in its T-component or z is an endpoint of the c-vertex component Q. If z is internal, that theorem states that every two-cover of J-z has an ordinary edge joining two distinct path blocks of the three-part partition induced by T-z. This is outcome (1).

Assume neither x nor y is internal. Then both are endpoints of Q. Consequently neither x nor y lies in P. But J has vertex set {x,y} union V(B) union V(C), because S is exactly the interior of A. Hence V(P) is contained in V(B) union V(C), so P is vertex-disjoint from A. Since |P|=c+2=|A| and A is globally longest, P is also globally longest.

Apply the certified maximum-path splicing lemma in pathcalc01 to the two vertex-disjoint globally maximum tight paths A and P. It yields distinct vertices r,p,q in V(A) union V(P) for which both (r,p,q) and (p,q,r) are tight. This is outcome (2). ∎
