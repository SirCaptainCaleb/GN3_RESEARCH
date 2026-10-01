# A global four-side minimum forces a path longer than its displayed largest side

## Statement

Let H be a minimum counterexample and let X|P|Q be a globally quadratic-minimal spanning three-cover with |X|=4, |P|=m>=|Q|=r>=6. Let e be an endpoint of P and f an endpoint of Q. For either certified crossed Hamiltonian five-set F=(X-{x}) union {e,f} from 5e5806bd9b64, every two-cover U|V of H-F has a component of order at least m+1. Consequently the maximum tight-path order lambda of H satisfies lambda>=m+1; in particular the displayed largest component P is not globally longest.

## Body

Write d=m-r and delta=||U|-|V||. Certified theorem 5e5806bd9b64 gives
delta^2 >= d^2+2(m+r)-19.
Since m>=r, m+r-d=2r, so
[d^2+2(m+r)-19]-(d+1)^2
=2(m+r-d)-20
=4r-20
>=4.
Hence delta^2>(d+1)^2, so delta>d+1. The parity of delta agrees with |U|+|V|=m+r-1, whereas d=m-r has the parity of m+r. Thus delta and d have opposite parity, and therefore delta>=d+3. The larger component order is
(|U|+|V|+delta)/2=(m+r-1+delta)/2
>= (m+r-1+d+3)/2
= m+1.
This component is a tight path of H, so lambda>=m+1.
