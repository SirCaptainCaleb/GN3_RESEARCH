# Reciprocal unique support crossing reduces to a singleton transfer

## Statement

In the opposite-end common two-deletion comparison, suppose the induced exact two-covers have different support partitions and each has exactly one ordinary edge crossing the other partition. Then either one of the comparison blocks already has relative-order disagreement, or the support change is a one-vertex transfer. More precisely, in the no-order-disagreement branch the unique-crossing block decomposition transfers a block M between components, and every case with |M|>=2 yields either a spanning two-cover of H or a Hamilton path of H-{x,y}; hence |M|=1.

## Body

# Reciprocal unique support crossing reduces to a singleton transfer

Let (H) be a minimum-order counterexample and let (x,y) be distinct vertices. Suppose
[
G_xquad	ext{is an exact two-cover of }H-x
]
in which (y) is the terminal vertex of its component, and
[
G_yquad	ext{is an exact two-cover of }H-y
]
in which (x) is the initial vertex of its component.

Delete those endpoints and put
[
T_x=G_x-y,qquad T_y=G_y-x.
]
These are exact two-covers of (H-{x,y}).

Assume their unordered support partitions differ, and that each cover has exactly one ordinary edge crossing the two support classes of the other cover.

Then at least one of the following holds:

1. a path block of one cover orders two vertices of a support block differently from the inherited order of the other cover, hence the path-intersection calculus gives explicit order-disagreement data; or
2. the support change from (T_x) to (T_y) is a transfer of a single vertex from one component to the other.

## The unique-crossing support form

Assume there is no relative-order disagreement on any block occurring in the comparison.

Write
[
T_x=Pmid Q.
]
Since (T_y) has exactly one (Pmid Q) crossing, cutting that edge produces three nonempty blocks. Thus one of (P,Q) occurs as one whole block of (T_y), while the other is split into two nonempty blocks.

Because (T_x) also has exactly one crossing across the support partition of (T_y), the two pieces of the split (T_x)-component occur as two consecutive support intervals in its displayed path order. Hence, after naming the split component (P), there are nonempty paths (B,M,Q) such that
[
P=BMquad	ext{or}quad P=MB,
]
and (T_y) has support partition
[
Bmid (Mcup Q).
]
In the no-order-disagreement branch, the (B)-, (M)-, and (Q)-blocks in (T_y) use exactly their inherited orders from (T_x), while the mixed component is either (MQ) or (QM).

We show that (|M|ge2) is impossible.

## The endpoint-restoration constraints

First (y) must restore to the split support (P) in (G_x).

Indeed, suppose instead that (y) restores to the unsplit support (Q), so (Qy) is tight. If (x) restores to the mixed component of (T_y), then:
- when that component is (MQ), the path (xMQy) is tight because (|Q|ge2);
- when it is (QM), the path (xQy) is tight because (|Q|ge2), and the original path (P) covers the remaining support.

Either way one obtains a spanning two-cover.

If (x) restores to the pure component (B), then (xB) is tight and (|B|ge2). If (P=BM), the path (xBM=xP) is tight because (|B|ge2), and together with (Qy) gives a spanning two-cover. Suppose instead that (P=MB). If the mixed component is (MQ), then (MQy) is tight because (|Q|ge2), so (xB)mid(MQy) is a spanning two-cover. If the mixed component is (QM), then under the standing assumption (|M|ge2), the paths (QM) and (MB=P) splice through the common block (M) to give the Hamilton path (QMB) of (H-{x,y}), contradicting the minimum-counterexample fact that every two-vertex deletion has path-cover number exactly two. Thus this last subcase is impossible as well. Contradiction.

Thus
[
G_x=(P,y)mid Q
]
after the chosen orientation of (y).

Next (x) cannot restore to the pure component (B) of (T_y). If (P=BM), then (xBMy=xPy) is tight because (|B|ge2), and (Q) is the other spanning component. If (P=MB), then (xBy) is tight and the mixed (Mcup Q) component covers the remaining vertices. Both give spanning two-covers.

Hence (x) restores to the mixed (Mcup Q) component.

## A transferred block of order at least two closes the cover

There remain four order possibilities.

### 1. (P=BM) and the mixed component is (MQ)

Then
[
G_x=(B,M,y)mid Q,qquad
G_y=(x,M,Q)mid B.
]
If (|M|ge2), the concatenation
[
B,M,Q
]
is a tight path: the (B)-to-(M) join is inherited from (G_x), the (M)-to-(Q) join from (G_y), and the two joins are separated by at least two vertices of (M). This Hamiltonizes (H-{x,y}), contradicting the minimum-counterexample fact that every two-vertex deletion has path-cover number exactly two.

### 2. (P=BM) and the mixed component is (QM)

Then (xQM) is tight. If (|M|ge2), appending (y) uses the terminal (M,y) join inherited from (G_x), so
[
x,Q,M,y
]
is tight. Together with the pure path (B) this is a spanning two-cover of (H).

### 3. (P=MB) and the mixed component is (MQ)

Then (xMQ) is tight. If (|M|ge2), the initial segment (xM) can be followed by (B,y) using the inherited order (MBy=Py), giving
[
x,M,B,y=x,P,y
]
as a tight path. Together with (Q) this two-covers (H).

### 4. (P=MB) and the mixed component is (QM)

Then (xQM) is tight. If (|M|ge2), append (B,y) using the inherited (MBy) order. The resulting tight path
[
x,Q,M,B,y
]
contains every vertex of (H), contradicting (pc(H)>2).

Thus every no-order-disagreement reciprocal-one-crossing comparison has
[
|M|=1.
]

So the minimal support-disagreement residue is not a multi-vertex block transport: it is a single-vertex transfer between the two common-cover supports.