# Equal endpoint support partitions force same-support restoration and an opposite-end bridge

## Statement

Let G_x and G_y be opposite endpoint deletion covers whose induced covers of H-{x,y} have the same unordered two-support partition. Then x and y must restore to the same common support; restoring them to opposite supports would itself give a spanning two-cover. In the longest-path endpoint orientation, with y terminal on one restoration and x initial on the other, the common support S satisfies H[S+x+y] non-Hamiltonian and endpoint barriers force (p,x,y) and (x,y,q) tight, where p is the initial vertex of the x-restored Hamilton order and q the terminal vertex of the y-restored order. Thus p!=q gives a tight four-path (p,x,y,q), while p=q gives the corresponding degenerate cyclic bridge.

## Body

# Equal support partitions force same-support restoration and an opposite-end bridge

Let (H) be a boundary tournament with (pc(H)>2), and let (x,y) be distinct vertices. Let (G_x) be an exact two-path cover of (H-x) in which (y) is an endpoint of its component, and let (G_y) be an exact two-path cover of (H-y) in which (x) is an endpoint of its component.

Delete the displayed endpoints and write
[
T_x=G_x-y,qquad T_y=G_y-x,
]
so (T_x,T_y) are exact two-path covers of (H-{x,y}).

Assume their unordered support partitions agree, say
[
{S,T}.
]

Then (x) and (y) must restore to the same one of the two common supports.

Indeed, suppose after naming the supports that (y) restores to (S) in (G_x), while (x) restores to (T) in (G_y). The (Scup{y})-component of (G_x) and the (Tcup{x})-component of (G_y) are disjoint tight paths whose supports partition (V(H)). They would form a spanning two-path cover of (H), contradiction.

Hence, after relabeling, both omitted vertices restore to (S). In particular (H[T]) is Hamiltonian, as is each of
[
H[Scup{x}],qquad H[Scup{y}].
]
The set (Scup{x,y}) is non-Hamiltonian, since otherwise a Hamilton path on it together with a Hamilton path on (T) would two-cover (H).

Now impose the opposite-end orientation arising from the longest-path endpoint situation: suppose the (Scup{y})-component of (G_x) has the form
[
P,y,qquad P=(p_0,ldots,p_k),
]
while the (Scup{x})-component of (G_y) has the form
[
x,P',qquad P'=(p'_0,ldots,p'_k).
]

Apply the exterior endpoint barriers inside the non-Hamiltonian induced tournament (H[Scup{x,y}]).

From the Hamilton path (xP') on (Scup{x}), failure to prepend (y) gives
[
(p'_0,x,y)
]
tight.

From the Hamilton path (Py) on (Scup{y}), failure to append (x) gives
[
(x,y,p_k)
]
tight.

Therefore, if (p'_0
e p_k), then
[
(p'_0,x,y,p_k)
]
is a tight four-vertex path.

If (p'_0=p_k=p), the two tight triples
[
(p,x,y),qquad (x,y,p)
]
remain as a degenerate cyclic bridge on the three vertices ({p,x,y}).

The other two endpoint barriers are also forced:
[
(p_1,p_0,x),qquad (y,p'_k,p'_{k-1})
]
when the displayed indices exist.

Thus equal support partitions do not leave arbitrary order disagreement: opposite-end restorations synchronize onto one support and force explicit two-ended bridge data there.
