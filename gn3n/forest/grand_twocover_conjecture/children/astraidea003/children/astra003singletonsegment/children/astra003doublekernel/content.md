# Singleton-transfer hooks synchronize two endpoint matching-block kernels

## Statement

In the reciprocal-one-crossing first form, write B=(b,r,...) and Q=(...,s,q). Let X_L={b,x,m,y} and X_R={m,y,s,q}. Each is either Hamiltonian or a non-Hamiltonian edge-orderable K4 with matching-block structure. If X_L is non-Hamiltonian then its block order is uniquely {bx,my}<{bm,xy}<{by,xm}. If X_R is non-Hamiltonian then {my,sq} is its bottom matching block. Hence in the double-non-Hamiltonian residue the transfer edge my lies in the bottom block at both ends, and the left matching-block order is completely determined.

## Body


# Two endpoint kernels sharing the transfer edge

Assume the reciprocal-one-crossing first form from f6cdd6346980:

G_x=(m,B)|(Q,y),
G_y=(x,B)|(Q,m),
G_m=(x,B)|(Q,y),

where B and Q have order lambda-1. Write

B=(b,r,...),    Q=(...,s,q).

Because lambda>=5 in this shell, all displayed vertices are defined and distinct.

Apply endpoint-hook forcing to G_y and G_m.

For the common path (x,B), with omitted vertices y and m respectively, the left endpoint hooks give

(b,x,y), (r,y,x),
(b,x,m), (r,m,x)

tight.

For the paths (Q,m) in G_y and (Q,y) in G_m, the right endpoint hooks give

(y,m,q), (m,y,s),
(m,y,q), (y,m,s)

tight.

Also, the first-form theorem itself gives (b,m,x) tight.

Consider first

X_L={b,x,m,y}.

The two triples

(b,x,m), (b,x,y)

have the same first ordered pair. By the certified four-vertex common-first-pair classification, either H[X_L] is Hamiltonian, or it is edge-orderable and non-Hamiltonian with matching-block form. In the latter case, put

M_0={bx,my},
M_1={bm,xy},
M_2={by,xm}.

The common-first-pair classification leaves exactly the two block orders

M_0<M_1<M_2
or
M_0<M_2<M_1,

and distinguishes them by the reversal pair (b,m,x) versus (x,m,b). Since (b,m,x) is tight in the first form, only

M_0<M_1<M_2

is possible. Thus the left matching-block order is unique.

Now consider

X_R={m,y,q,s}.

The two triples

(m,y,q), (m,y,s)

again have the same first ordered pair. Hence either H[X_R] is Hamiltonian, or it is edge-orderable and non-Hamiltonian with matching-block form. In the latter case, with

N_0={my,qs},
N_1={mq,ys},
N_2={ms,yq},

the same classification forces N_0 to be the bottom block; the two possible block orders differ only in the order of N_1,N_2.

Therefore, if neither endpoint four-set is Hamiltonian, the ordinary edge my belongs to the bottom matching block in both local edge-order representations. On the left it is paired with the first edge bx of the common longest path (x,B), and the full local order is

{bx,my}<{bm,xy}<{by,xm}.

On the right my is paired with the last edge sq of Q and lies in the bottom matching block.

Thus the no-Hamiltonian-window residue is a pair of rigid matching-block kernels synchronized by one common lowest-block transfer edge, with the left kernel completely ordered at the matching-block level. This is strictly more structured than two unrelated failed-insertion obstructions and is the natural residual configuration for trying to escape the Astra 003 equality plateau.
