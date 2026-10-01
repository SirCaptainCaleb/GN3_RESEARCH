# Every prescribed pair lies in an alternating Hamiltonian five-set with a stable three-label complement family

## Statement

Let H be a minimum counterexample and let L,R be distinct vertices. Then there exist distinct x,y,z outside {L,R} such that (y,L,x,R,z) or (y,R,x,L,z) is a tight Hamilton path. Writing T={x,y,z} and G=H-{L,R}, one may choose x,y,z from one orientation class so that G, G-t for every t in T, and G-{s,t} for every distinct s,t in T are all non-Hamiltonian with path-cover number two. Moreover H-{L,R,x,y,z} is non-Hamiltonian with path-cover number two.

## Body

Apply fixedpair_halfstable01 and choose the larger orientation class C among C_+={w:(L,w,R) is tight} and C_-={w:(R,w,L) is tight}. A minimum counterexample has order greater than ten, so |C|>=ceil((n-2)/2)>=5. If C=C_+, then (L,w,R) is tight for every w in C. Apply the certified five-parallel-middle theorem 837aaea0f9fd with a=L, b=R and W=C. It gives distinct y,x,z in C such that (y,L,x,R,z) is a tight five-vertex path. If C=C_-, apply the same theorem with a=R,b=L to obtain (y,R,x,L,z). Put T={x,y,z}. Because T is contained in C, fixedpair_halfstable01 gives that G, every G-t, and every G-{s,t} with s,t distinct in T are non-Hamiltonian with path-cover number two. Finally W={L,R,x,y,z} is a proper Hamiltonian five-set. If H-W were Hamiltonian, Hamilton paths on W and H-W would form a spanning two-cover of H. Hence H-W is non-Hamiltonian, and minimality gives path-cover number two.
