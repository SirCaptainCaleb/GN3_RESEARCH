# Central two-layer switching Q8 and Q10 closures by physical root-profile cosets

# Physical central two-layer switching: Q8 and Q10 closure

Let n∈{8,10}, k=(n−4)/2, and c be an active NORI coloring of ordered three-faces. Assume that for every ordered triple π all physical faces on exterior weight k have color a(π), and all physical faces on weight k+1 have color 1−a(π). At all other exterior weights c is arbitrary, subject to NORI oddness. Oddness forces a(rev π)=a(π).

**Theorem.** In Q8, EVERY prescribed direction order admits a full antipodal geodesic with at most one color change. In Q10, every order p with a(p1,p2,p3)=a(p8,p9,p10) admits such a geodesic. Such an order always exists; hence this entire Q10 subclass satisfies NORI. In Q8 at least two actual central roots work for each order, and in Q10 at least four work for each equal-endpoint order.

**Proof.** For order p and starting bits x1,...,xn in that order, the exterior Hamming weight of window i is
K_i(x)=Σ_{j<i}(1−x_j)+Σ_{j>i+2}x_j, 1≤i≤n−2.
A central root has K_i∈{k,k+1} for all i; its profile t=(K_1−k,...,K_{n−2}−k) is binary. Write P_n for the finite set of these profiles. The actual face-color word along the full antipodal geodesic is a(p)_i+t_i. Let G_L be the set of binary words of length L with at most one change: 0^L, 1^L, 0^j1^(L−j), 1^j0^(L−j) for 1≤j<L. Therefore any order with a(p)∈P_n+G_(n−2) has the required physical witness.

For Q8, P_8 includes the 3-dimensional linear space H={(u,v,0,u,w,0):u,v,w∈F2}. Witness roots for (u,v,w)=000,001,010,011,100,101,110,111, respectively, are
00111000;10101001;01101010;01101001;10011010;10011001;01011010;01011001.
The quotient F2^6/H is parametrized by (z3,z6,z1+z4). Its eight cosets all meet G_6, as witnessed respectively by 000000,100000,111000,111100,000001,000111,001111,111111 (the quotient triples are all distinct). Thus H+G_6=F2^6 and every Q8 order succeeds.

For Q10, exact direct root-profile enumeration shows that P_10+G_8 contains EVERY 8-bit intercept word having equal first and last bits. The following fully reproducible finite certificate uses only integer arithmetic and the displayed physical-face formula, enumerating all cube roots and all intercept words:

```python
def verify(n):
    L=n-2; k=(n-4)//2
    root_count={}
    for mask in range(1<<n):
        x=[(mask>>j)&1 for j in range(n)]
        K=[sum(1-x[j] for j in range(i))+
           sum(x[j] for j in range(i+3,n)) for i in range(L)]
        if all(v==k or v==k+1 for v in K):
            p=sum((v-k)<<i for i,v in enumerate(K))
            root_count[p]=root_count.get(p,0)+1
    G={0,(1<<L)-1}
    for j in range(1,L):
        q=(1<<j)-1
        G.update((q,q^((1<<L)-1)))
    N={a:sum(root_count.get(a^g,0) for g in G)
       for a in range(1<<L)}
    if n==8:
        assert len(root_count)==34
        assert min(N.values())==2
    if n==10:
        assert len(root_count)==86
        E=[a for a in N if (a&1)==((a>>(L-1))&1)]
        assert len(E)==128 and min(N[a] for a in E)==4
        assert sum(v==0 for v in N.values())==24
verify(8)
verify(10)
```

To force an equal-endpoint order in Q10, partition any nine directions into three ordered triples. By pigeonhole, two of their a-values agree. Put those two triples at the beginning and end of a permutation, filling the four intervening places with the remaining directions. This proves the theorem.

**Exact frontier.** The Q10 central-profile method fails for precisely 24 of 256 possible intercept words for a fixed order; every one of those 24 has unequal first and last bits. Selecting the direction order removes that obstruction. This theorem covers a face-dependent NORI subclass, and establishes neither the unrestricted Q10 nor the all-dimensional grand conjecture.

## Stronger, entirely algebraic Q10 closure

The preceding finite Q10 certificate can be bypassed when proving existence of a suitable direction order. Read the all-even paired-root theorem Item nori_all_even_paired_root_linear_subspace_sparse_defect_two_start_geodesics_20261009.

For n=10 the paired-root defect vector is just (a_1+a_4,a_3+a_6,a_5+a_8). The paired-root theorem allows every defect vector EXCEPT 101 and 111. In particular, ANY direction order with a_1=a_4 guarantees at least TWO good genuine paired starting vertices, regardless of the other six intercept colors.

Take any NINE coordinates and partition them into THREE disjoint ordered triples. Two of the triples have equal a-color by pigeonhole. Put those two triples at positions 1,...,6 and put the four remaining coordinates at positions 7,...,10. Then a_1=a_4, so the paired-root theorem gives a full one-switch antipodal geodesic. This proves Q10 subclass closure by a pure pigeonhole-plus-cube-root argument.

At n=8 the paired-root defect vector has length two, and all four possible vectors are realizable by an at-most-one-switch word, recovering the every-order theorem algebraically. Together with the partition-parity argument at n=12, the closures n=8,10,12 now have entirely algebraic proofs; the finite profile verifier remains a separate exact check and gives the stronger fixed-order Q10 condition a_1=a_8.
