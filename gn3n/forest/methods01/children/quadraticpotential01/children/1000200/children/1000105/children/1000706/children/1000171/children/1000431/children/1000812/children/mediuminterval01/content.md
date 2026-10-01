# An interval of Hamiltonian set sizes forces a globally longest complement path on the lambda equals 3c minus 3 boundary

## Statement

Let H be a minimum counterexample in the sharp half-order shell |V(H)|=2lambda+1. Among globally quadratic-minimal spanning three-covers choose X|P|Q with maximum minimum component order c, write |X|=c, |P|=m, |Q|=r with m>=r>=c, and put d=m-r. Suppose lambda=3c-3 and c>=4. Let h>=1, and let F be any Hamiltonian support of order c+h. If
(2h-c+1)^2 < 4c+d^2-8,
then every two-cover of H-F has component orders
{lambda, lambda+1-c-h}.
In particular it contains a globally longest tight path. Hence the same conclusion holds under the d-free sufficient condition
|h-(c-1)/2| < sqrt(c-2).

## Body

Put s=m+r. Since n=2lambda+1 and lambda=3c-3,
s=n-c=5c-5.

Let U|V be any two-cover of H-F, with p=|U|>=q=|V|, and put delta=p-q. Since lambda is the maximum order of a tight path, p<=lambda. Also
p+q=n-(c+h).
Therefore
delta=2p-(n-c-h)
     <=2lambda-(2lambda+1-c-h)
     =c+h-1.
Set L=c+h-1. The integers delta and L have the same parity, because
(n-c-h)-L=2lambda+2-2c-2h
is even.

Apply the complement-imbalance penalty 40c4a8aca820 to the globally quadratic-minimal cover X|P|Q and the Hamiltonian support F. It gives
delta^2 >= d^2+h(2s-4c-3h)
        = d^2+h(6c-10-3h).                         (1)

Suppose delta<=L-2. Since delta and L have the same parity,
L^2-delta^2 >= L^2-(L-2)^2=4L-4.                  (2)
On the other hand, (1) gives
L^2-delta^2
 <= L^2-d^2-h(6c-10-3h).
Subtracting 4L-4 from the right-hand side and simplifying gives
(2h-c+1)^2-(4c+d^2-8).
By hypothesis this is negative, contradicting (2). Hence delta=L.

Now
p=((p+q)+delta)/2
 =((2lambda+1-c-h)+(c+h-1))/2
 =lambda,
and consequently
q=lambda+1-c-h.
Thus every two-cover of H-F contains a globally longest component and has the asserted profile.

Finally,
|h-(c-1)/2|<sqrt(c-2)
is equivalent to
(2h-c+1)^2<4c-8,
which is stronger than the displayed hypothesis because d^2>=0. ∎
