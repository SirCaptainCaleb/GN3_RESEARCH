# Global quadratic minima reduce to adjacent size gaps or a standard obstruction interface

## Statement

Let H be a minimum counterexample and let X|P|Q be a spanning three-cover minimizing Phi among all spanning three-covers, with p=|P|>=q=|Q|>=c=|X| and p,q>=2. Then at least one of the following holds: (1) for every displayed endpoint e of P and f of Q, H[V(X) union {e,f}] is non-Hamiltonian with path-cover number two; (2) H has a proper Hamiltonian induced set W of order four or five whose complement is non-Hamiltonian with path-cover number two; (3) for one endpoint e of P there are y in V(Q) and z in V(X) such that both (z,y,e) and (y,z,e) are tight; or (4) p-q<=1 and q-c<=1. Thus outside the three standard obstruction interfaces, every globally quadratic-minimal three-cover has consecutive component sizes.

## Body

Apply eb50bf03ddf1. If its endpoint-square alternative holds, we are in (1). Otherwise (p-c)+(q-c)<=3. If p>=q+2, then the globally Phi-minimal cover is in particular Phi-minimal in its pairwise-repartition component; since H is a counterexample, that component contains no two-cover. Apply 4e06a72b9f64 to the ordered components P,Q,X. It gives either a proper Hamiltonian induced set W of order four or five with non-Hamiltonian pc-two complement, which is (2), or a doubled cross barrier through an endpoint e of P and vertices y in Q, z in X, which is (3). It remains that p-q<=1. If q-c>=2, then p>=q gives (p-c)+(q-c)>=2+2=4, contradicting the bound at most three. Hence q-c<=1, giving (4).