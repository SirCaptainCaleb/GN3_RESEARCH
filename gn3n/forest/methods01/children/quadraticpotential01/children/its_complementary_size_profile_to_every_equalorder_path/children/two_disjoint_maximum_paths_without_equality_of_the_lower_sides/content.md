# A largest-second size gap of two yields a cross-block edge or two disjoint maximum paths without equality of the lower sides

## Statement

Let H be a minimum counterexample and let A|B|C be a globally Phi-minimal three-cover with a=|A|>=b=|B|>=c=|C|. Assume A=(a_0,...,a_{b+1}) is globally longest and a=b+2. Put S=(a_1,...,a_b), x=a_0, y=a_{b+1}, and J=H-V(S). For every two-cover T=P|Q of J, labeled so |P|=a and |Q|=c, either one of x,y is internal in its T-component and every two-cover after deleting that label contains an ordinary edge joining two distinct inherited path blocks of T minus that label, or x,y are the two endpoints of Q and P is a globally longest path vertex-disjoint from A. In the latter case A and P contain distinct r,p,q with both (r,p,q) and (p,q,r) tight.

## Body

By 5ec26ec830d3, every two-cover of J has component orders {a,c}; fix T=P|Q with |P|=a and |Q|=c. Apply 203187bcc627 to the b-window S and its flanking labels x,y. For each z in {x,y}, either z is internal in its component of T or z is an endpoint of the c-vertex component Q. In the internal case the same theorem says that every two-cover after deleting z contains an ordinary edge whose endpoints lie in two different inherited path blocks of T-z.

Assume neither x nor y is internal. Then both are endpoints of Q. Since S is the interior of A, V(J)={x,y} union V(B) union V(C). Hence P contains neither x nor y and is contained in V(B) union V(C), so P is vertex-disjoint from A. It has order a=|A|, and A is globally longest, so P is also globally longest. The maximum-path splicing lemma in pathcalc01 applied to A and P gives distinct r,p,q in their union such that both (r,p,q) and (p,q,r) are tight. The proof never uses b=c.