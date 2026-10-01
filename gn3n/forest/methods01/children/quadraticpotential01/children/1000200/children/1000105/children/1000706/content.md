# Equality in the sharp half-order quadratic bound fixes the global profile and every medium Hamiltonian complement profile

## Statement

Let H be a minimum counterexample in the sharp half-order shell |V(H)|=2lambda+1, where lambda is the maximum tight-path order. Let X|P|Q be a globally Phi-minimal spanning three-cover, with component orders m>=r>=c, and suppose lambda=3c-2. Put h=floor(c/2). Then the component orders and all complements of Hamiltonian (c+h)-sets are rigid as follows. If c=2k, then lambda=6k-2, {m,r,c}={5k-1,5k-2,2k}, and every Hamiltonian set F of order 3k has every two-cover of H-F of component orders {6k-2,3k-1}. If c=2k+1, then lambda=6k+1, {m,r,c}={5k+1,5k+1,2k+1}, and every Hamiltonian set F of order 3k+1 has every two-cover of H-F of component orders {6k+1,3k+1}. In particular, in either parity every such complement two-cover contains a globally longest tight path.

## Body

Put h=floor(c/2), s=m+r=2lambda+1-c, d=m-r>=0. Let F be any Hamiltonian set of order c+h. Since F is proper, minimum-counterexample calculus gives a two-cover U|V of H-F; write p>=q for its component orders and delta=p-q. Because lambda is the maximum tight-path order, p<=lambda. Since p+q=2lambda+1-c-h, this gives delta=2p-(2lambda+1-c-h)<=c+h-1.

By the general complement-imbalance penalty 40c4a8aca820,
 delta^2 >= d^2+h(4lambda+2-6c-3h).                 (1)
We now impose lambda=3c-2.

First suppose c=2k. Then h=k, lambda=6k-2, s=10k-3, and (1) becomes
 delta^2 >= d^2+9k^2-6k.
The path-order cap gives delta<=3k-1, hence
 delta^2 <= (3k-1)^2=9k^2-6k+1.
Thus d^2<=1. Since d=m-r has the same parity as s=m+r, and s is odd, d is odd. Therefore d=1. The lower bound in (1) is now exactly (3k-1)^2, so delta=3k-1. Consequently
 m=(s+d)/2=5k-1,   r=(s-d)/2=5k-2.
Also p+q=2lambda+1-c-h=9k-3 and p-q=3k-1, whence
 p=6k-2=lambda,   q=3k-1.
Since F was arbitrary, this profile holds for every Hamiltonian 3k-set and every two-cover of its complement.

Now suppose c=2k+1. Then h=k, lambda=6k+1, s=10k+2, and (1) becomes
 delta^2 >= d^2+9k^2.
The path-order cap gives delta<=3k, hence delta^2<=9k^2. Therefore d=0 and delta=3k. Thus
 m=r=s/2=5k+1,
and because p+q=2lambda+1-c-h=9k+2,
 p=6k+1=lambda,   q=3k+1.
Again F was arbitrary, so every Hamiltonian (3k+1)-set has every complementary two-cover of that profile.

In both cases the larger complementary component has order lambda, so it is globally longest. ∎