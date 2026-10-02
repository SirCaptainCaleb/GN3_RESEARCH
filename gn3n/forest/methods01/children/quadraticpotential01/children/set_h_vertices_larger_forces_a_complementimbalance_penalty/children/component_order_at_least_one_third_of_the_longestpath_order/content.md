# Sharp half-order quadratic minima have minimum component order at least one third of the longest-path order

## Statement

Let H be a minimum counterexample in the sharp half-order shell |V(H)|=2lambda+1, where lambda is the maximum tight-path order. Let X|P|Q be a spanning three-cover minimizing Phi=sum |C_i|^2 among all spanning three-covers, and write c=min{|X|,|P|,|Q|}. Then lambda<=3c-2. Equivalently c>=ceil((lambda+2)/3).

## Body

Order the component sizes as m>=r>=c, with X the c-vertex component.

First dispose of c=1. Since |V(H)|=2lambda+1>10 by minimum-counterexample calculus, lambda>=5. Take any two-vertex set F; it is Hamiltonian, has order c+1, and is proper. Its complement has a two-cover U|V. Put d=|m-r| and delta=||U|-|V||. Here s=m+r=2lambda. Since every tight path has order at most lambda while |U|+|V|=2lambda-1, we have delta<=1. Applying 40c4a8aca820 with h=1 gives
delta^2 >= d^2+2s-4c-3 = d^2+4lambda-7 >= 13,
contradicting delta^2<=1. Hence c>=2.

Now put h=floor(c/2), so h>=1, and suppose for contradiction that lambda>=3c-1. Since m+r=2lambda+1-c and m>=r,
m>=ceil((2lambda+1-c)/2).
Under lambda>=3c-1 this is larger than c+h, so P contains a contiguous tight subpath F of order c+h.

Because F is a proper Hamiltonian set in a minimum counterexample, H-F has path-cover number two. Choose a two-cover U|V and put delta=||U|-|V||. Every tight path of H has order at most lambda, while |U|+|V|=2lambda+1-c-h. Therefore max{|U|,|V|}<=lambda and delta<=c+h-1.

Apply 40c4a8aca820 to the globally Phi-minimal cover X|P|Q and the Hamiltonian set F. Writing d=|m-r| and s=m+r=2lambda+1-c gives
delta^2 >= d^2 + h(2s-4c-3h)
= d^2 + h(4lambda+2-6c-3h).

Discarding d^2>=0 and using delta<=c+h-1,
(c+h-1)^2 >= h(4lambda+2-6c-3h).

Now substitute lambda>=3c-1. If c=2k is even, h=k and at lambda=3c-1 the right side minus the left side equals 4k-1>0. If c=2k+1 is odd, then c>=3, so k>=1; h=k and the difference equals 4k>0. Increasing lambda only enlarges the difference. This contradiction proves lambda<=3c-2. Rearranging gives c>=ceil((lambda+2)/3). ∎