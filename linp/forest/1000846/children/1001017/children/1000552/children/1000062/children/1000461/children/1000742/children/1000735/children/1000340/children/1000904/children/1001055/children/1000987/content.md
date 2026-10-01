# The fixed-entrance conflict transfer extends to linear r-uniform paths

## Statement

Let r>=3 and let H be a finite linear r-uniform hypergraph. Define endpoint potentials and edge rank by longest linear paths. Suppose h has rank q>=4, has unique entrance x, satisfies phi(x)=q-1, and v is any other vertex of h. Put
J_q(v)={f in E(H): v in f and phi(f)<=q}.

Set a=r-2 and L=q-3. Define alpha_r(L) by
alpha_r(1)=a,
alpha_r(4k+2)=a+1+k(2a+1) for k>=0,
alpha_r(4k+3)=(k+1)(2a+1) for k>=0,
alpha_r(4k)=3a+1+(k-1)(2a+1) for k>=1,
alpha_r(4k+1)=3a+1+(k-1)(2a+1) for k>=1.
Then
|J_q(v)| <= 1+floor(((r-1)(q-1)+alpha_r(q-3))/2).
In particular
|J_q(v)| <= ((6r-7)/8)q+O_r(1).

For r=3 one has alpha_3(q-3)=ceil((3q-8)/4), and the bound becomes the exact inequality
|J_q(v)|<=floor((11q-5)/8).

## Body

Choose a q-edge path P=(g_1,...,g_q) ending in h=g_q at v, and let x=g_{q-1} intersect h. Put W=V(P) minus h. A linear r-uniform q-edge path has q(r-1)+1 vertices, so
|W|=(r-1)(q-1).

For f in J_q(v) minus {h}, let
C_f=(f minus {v}) intersect W.
If C_f were empty, P,f would be a (q+1)-edge path, contradicting phi(f)<=q. Since any two such f share v, linearity makes the C_f pairwise disjoint. Each has size between one and r-1.

There are two boundary families of vertices that cannot be singleton contact sets. Every vertex of g_1 minus g_2 is forbidden: a singleton there would give the q-edge path
f,g_1,...,g_{q-1}
ending at x, contrary to phi(x)=q-1. Every vertex of g_{q-2} minus g_{q-3} is also forbidden: a singleton there would give
g_1,...,g_{q-2},f,h,
a q-edge path ending in h through v rather than the unique entrance x. Each boundary family has r-1 vertices.

After deleting these 2(r-1) forbidden positions, organize the remaining possible singleton positions as follows. Cell C_1 consists only of the joint g_1 intersect g_2. For 2<=i<=L=q-3, cell C_i=g_i minus g_{i-1}; it has r-1 vertices, namely one forward joint and a=r-2 private vertices. The final endpoint set E consists of the r-2 private vertices of g_{q-1} outside g_{q-2} and h.

The same fixed-entrance splice as in the 3-uniform proof gives the full conflict rule. If cell C_i contains any singleton contact, then the forward joint in C_{i+1} cannot be singleton, and all a private vertices of C_{i+2} cannot be singleton. At the right boundary, occupancy of C_L forbids all a vertices of E. Indeed any forbidden pair of singleton contacts c,d would give
g_1,...,g_i,f,k,g_{i+2},...,g_{q-1},
a q-edge linear path ending at x.

Let A_i indicate whether C_i contains at least one singleton contact. For i>=1, if the previous state is (A_{i-1},A_i)=(u,v), then in C_{i+1} exactly a(1-u)+(1-v) vertices are available for singleton use. Thus the maximal-weight state transitions are
00->00 weight 0, 00->01 weight a+1,
01->10 weight 0, 01->11 weight a,
10->00 weight 0, 10->01 weight 1,
11->10 weight 0.
The initial values are F_1(00)=0 and F_1(01)=1. Four applications of this recurrence add 2a+1 to every finite state value once i>=2. The base vectors are
F_2=(0,a+1,1,a+1),
F_3=(1,a+1,a+1,2a+1),
F_4=(a+1,a+2,2a+1,2a+1),
F_5=(2a+1,2a+2,2a+1,2a+2)
in state order 00,01,10,11. The endpoint E contributes a precisely when A_L=0. Reading the four residue classes gives exactly alpha_r(L) as stated. Hence the number s of singleton contact sets satisfies
s<=alpha_r(q-3).

Let n_j be the number of contact sets of size j and let u be the number of unused vertices of W. Then
s+sum_{j>=2} j n_j+u=(r-1)(q-1).
Since every nonsingleton contact set consumes at least two vertices,
sum_{j>=2} n_j <= floor(((r-1)(q-1)-s)/2).
Therefore
|J_q(v)|
=1+s+sum_{j>=2}n_j
<=1+floor(((r-1)(q-1)+s)/2)
<=1+floor(((r-1)(q-1)+alpha_r(q-3))/2).

Because alpha_r(L)=((2r-3)/4)L+O_r(1), the leading coefficient is
(r-1)/2+(2r-3)/8=(6r-7)/8.
For r=3, a=1 and the residue table collapses to
alpha_3(L)=ceil((3L+1)/4),
which recovers eb40ddcc33ca.