# Order-preserving intersections with a longest path have bounded positional lag

## Statement

Let A=(a_0,...,a_{lambda-1}) be a globally longest tight path and C a tight path of order s whose common vertices with A occur in the same relative order. If a_i occurs at position p of C, then either a tight triple reverses an ordered A-edge at a_i, or i-(lambda-s) <= p <= i. Hence for a component of order lambda-d in an order-neutral deletion cover, every surviving A-vertex is shifted earlier by at most d; in particular a_0 is initial whenever present and a_{lambda-1} is terminal whenever present.

## Body

# Order-preserving intersections with a longest path have bounded positional lag

Let (H) be a boundary tournament, and let
[
A=(a_0,ldots,a_{lambda-1})
]
be a globally longest tight path. Let
[
C=(c_0,ldots,c_{s-1})
]
be any tight path. Assume that the common vertices of (A) and (C) occur in the same relative order in the two paths.

Suppose (a_i=c_p).

If (p>i), then necessarily (i<lambda-1), and
[
(a_{i+1},a_i,c_{p-1})
]
is tight.

Indeed, the sequence
[
(c_0,ldots,c_{p-1},a_i,a_{i+1},ldots,a_{lambda-1})
]
is vertex-simple: every (A)-vertex preceding (a_i) in (C) has index smaller than (i), by the order-preserving hypothesis. It has
[
(p+1)+(lambda-i-1)=lambda+p-i>lambda
]
vertices. Every consecutive triple is inherited from (C) or (A), except possibly
[
(c_{p-1},a_i,a_{i+1}).
]
That triple cannot be tight, by maximality of (A). Boundary antisymmetry therefore gives
[
(a_{i+1},a_i,c_{p-1})
]
tight.

Now suppose
[
p<i-(lambda-s).
]
Then (i>0), and (p<s-1): if (p=s-1), the displayed strict inequality would imply (i+1>lambda). Hence (c_{p+1}) exists. The sequence
[
(a_0,ldots,a_i,c_{p+1},ldots,c_{s-1})
]
is again vertex-simple, since every (A)-vertex following (a_i) in (C) has index larger than (i). Its order is
[
(i+1)+(s-p-1)=s+i-p>lambda.
]
All consecutive triples are inherited except possibly
[
(a_{i-1},a_i,c_{p+1}).
]
Thus this triple is non-tight, and
[
(c_{p+1},a_i,a_{i-1})
]
is tight.

Consequently, if no tight triple reversing an ordered edge of (A) is produced at (a_i), then
[
i-(lambda-s)le ple i.
]

In particular, if (C) has order (s=lambda-d), then an order-preserving occurrence of (a_i) lies between positions (i-d) and (i). Thus, in the absence of an ordered-disagreement witness, (a_0), whenever it belongs to (C), is the initial vertex of (C), while (a_{lambda-1}), whenever it belongs to (C), is the terminal vertex of (C).