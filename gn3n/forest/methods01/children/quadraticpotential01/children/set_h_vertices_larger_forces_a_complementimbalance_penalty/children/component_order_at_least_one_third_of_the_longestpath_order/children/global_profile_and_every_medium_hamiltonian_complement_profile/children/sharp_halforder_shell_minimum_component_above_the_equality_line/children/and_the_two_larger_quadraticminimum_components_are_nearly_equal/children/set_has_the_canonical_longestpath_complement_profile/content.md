# At lambda equals three c minus three every medium Hamiltonian set has the canonical longest-path complement profile

## Statement

Let H be a minimum counterexample in the sharp half-order shell |V(H)|=2lambda+1. Choose, among all globally Phi-minimal spanning three-covers, one with maximum minimum component order c, and suppose lambda=3c-3 with c>=4. Write its other component orders m>=r and let rho be the maximin minimum-component parameter. If c=2k, so lambda=6k-3 and rho=3k-1, every Hamiltonian set F of order rho has every two-cover of H-F of component orders {lambda,rho}. If c=2k+1, so lambda=6k and rho=3k, every Hamiltonian set F of order rho+1 has every two-cover of H-F of component orders {lambda,rho}. Thus in either parity every Hamiltonian set at the canonical medium order has a complementary two-cover whose larger component is globally longest, and the resulting spanning three-cover has exactly the canonical maximin profile.

## Body

Keep the notation of 86c6d5d44600. Thus the normalized globally quadratic-minimal cover has component orders m>=r>=c, put d=m-r, and suppose lambda=3c-3.

First suppose c=2k, so k>=2. Then
lambda=6k-3,
rho=3k-1,
m+r=10k-5,
and
d^2<4k-3.                                           (1)

Set h=k-1. Let F be any Hamiltonian set of order
c+h=3k-1=rho.
Because F is proper, minimum-counterexample calculus gives a two-cover U|V of H-F. Write p>=q for its component orders and delta=p-q.

The complement has order
p+q=(2lambda+1)-(3k-1)=9k-4.
Since no tight path has order more than lambda=6k-3,
delta=2p-(9k-4)<=3k-2.                              (2)

Apply 40c4a8aca820. Here s=m+r=10k-5 and h=k-1, so
delta^2 >= d^2+(k-1)(9k-7).                         (3)

Let L=3k-2. Then
L^2-(k-1)(9k-7)=4k-3.                               (4)
Combining (1), (3), and (4),
L^2-delta^2 <= (4k-3)-d^2 < 4k-3.                  (5)

The integers delta and L have the same parity. If delta<=L-2, then
L^2-delta^2 >= 4L-4 = 12k-12 > 4k-3,
contradicting (5). Hence delta=L=3k-2.

Therefore
p=6k-3=lambda,
q=3k-1=rho.

Now suppose c=2k+1>=5, so k>=2. Then
lambda=6k,
rho=3k,
m+r=10k,
and
d^2<4k.                                             (6)

Set h=k. Let F be any Hamiltonian set of order
c+h=3k+1=rho+1.
For any two-cover U|V of H-F, write p>=q and delta=p-q. The complement has order
p+q=9k,
and p<=lambda=6k, so
delta<=3k.                                          (7)

The complement-imbalance inequality gives
delta^2 >= d^2+k(20k-(8k+4)-3k)
        = d^2+9k^2-4k.                              (8)

Let L=3k. From (6) and (8),
L^2-delta^2 <= 4k-d^2<4k.                           (9)

Again delta and L have the same parity. If delta<=L-2, then
L^2-delta^2>=4L-4=12k-4>4k,
contradicting (9). Hence delta=L=3k.

Therefore
p=6k=lambda,
q=3k=rho.

So in either parity every two-cover of the complement of every Hamiltonian set at the indicated medium order has the exact profile {lambda,rho}. In the even-c case the resulting spanning three-cover profile is {lambda,rho,rho}; in the odd-c case it is {lambda,rho+1,rho}. In particular each resulting spanning three-cover is maximin, and its lambda-component is globally longest. ∎