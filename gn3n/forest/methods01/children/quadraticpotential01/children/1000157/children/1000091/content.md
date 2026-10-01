# Adjacent moving windows force a two-label internal-or-small-endpoint core

## Statement

Let H be a counterexample minimal by order and let A|B|C be a globally Phi-minimal spanning three-cover with a=|A|>=b=|B|>=c=|C|. Assume A=(a_0,...,a_{a-1}) is globally longest and a>=b+2. Let S=(a_i,...,a_{i+b-1}) be a contiguous b-vertex subpath with a displayed predecessor ell=a_{i-1} and successor r=a_{i+b}. Put J=H-V(S). Then every exact two-cover T=P|Q of J has component orders |P|=a, |Q|=c, and for each z in {ell,r}, either z is internal in its component of T or z is an endpoint of Q. If z is internal, every exact two-cover of J-z contains an ordinary edge joining two distinct path blocks of T-z. Consequently, if neither ell nor r is internal in T, then they are the two endpoints of the c-vertex component Q, giving a tight ell-to-r connector of order c.

## Body

By the equal-order profile propagation theorem 5ec26ec830d3, since S is a tight b-path, every exact two-cover of
J=H-V(S)
has component-order multiset {a,c}. Fix one and name it
T=P|Q
with |P|=a and |Q|=c.

The two adjacent enlargements
F_ell=(ell,S)
and
F_r=(S,r)
are contiguous subpaths of A and therefore are tight paths of order b+1. By the one-step moving longest-path theorem 3167845f1601, every exact two-cover of
J-ell = H-V(F_ell)
and of
J-r = H-V(F_r)
has component-order multiset {a,c-1}.

Fix z in {ell,r}. Suppose first that z is an endpoint of the a-vertex component P. Deleting z from its displayed path leaves a tight path of order a-1, while Q remains a tight path of order c. Thus T-z is an exact two-cover of J-z with component orders {a-1,c}. But a>=b+2>=c+2, so
{a-1,c} != {a,c-1},
contradicting the forced profile of every exact two-cover of J-z. Hence z cannot be an endpoint of P.

Therefore, if z is not internal in its T-component, it must be an endpoint of Q. This proves the first assertion.

Now suppose z is internal in its component of T. Deleting z splits that component into two nonempty contiguous tight subpaths; the other component of T remains nonempty. Thus T-z is a three-path cover of J-z with three nonempty path supports. Let R|W be any exact two-cover of J-z; such covers exist and have orders {a,c-1} by 3167845f1601. If no ordinary edge of R|W joined two distinct members of the three-part support partition induced by T-z, then each connected path R and W would lie wholly inside one part. Two paths cannot cover all three nonempty parts. Hence some ordinary edge of R|W crosses that three-part partition.

Finally, if neither ell nor r is internal in T, the first assertion puts both at endpoints of Q. Since Q is one path, ell and r are its two displayed endpoints. Hence Q itself is a tight connector from one of ell,r to the other, of order c.

The conclusion is scale-free: adjacent moving windows convert the family of longest complementary paths into a fixed two-label dichotomy—three-block crossing under deletion, or a small endpoint-to-endpoint connector.