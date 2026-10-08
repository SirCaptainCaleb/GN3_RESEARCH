# Identical codimension-two blocker scans collapse to one explicit omission

## Composition

(none yet)

## Development

Let alpha be alternating with zero tetrahedral coboundary. Let
O=(v_1,...,v_m)
have one-change word
0^p1^q,
with p,q>=3. Let x,y be two exterior coordinates with IDENTICAL insertion scans
s_i=alpha(x,v_i,v_{i+1})=alpha(y,v_i,v_{i+1}).

Flatness on {x,y,v_i,v_{i+1}} gives
alpha(x,y,v_i) xor alpha(x,y,v_{i+1})
=
s_i xor s_i
=
0.
Hence
c=alpha(x,y,v_i)
is independent of i. Exchanging the order of x,y complements c, so consecutive pair insertion may choose the common pair bit to be either 0 or 1.

Use the blocking-core inequality from the arbitrary-scan insertion theorem:
s_{p-1} >= s_p >= s_{p+1}.

First suppose
s_{p-1} <= s_{p+1}.
Then the two inequalities force equality
s_{p-1}=s_p=s_{p+1}.
Insert x,y consecutively at the switch gap and choose their order so that the two pair-middle bits equal this common value. The new four-window packet is constant and connects the untouched zero prefix to the untouched one suffix without a return change. Thus the enlarged full order is one-change. In a counterexample this case is impossible.

Consequently any surviving identical-scan pair has
s_{p-1}=1,
s_{p+1}=0.
In particular the right branch of the arbitrary-scan replacement theorem applies. Its local core forces
s_{p+2}=s_{p+3}=0.
Replace
z=v_{p+3}
by x. The resulting order
O_x'
on
(O union {x}) minus {z}
is one-change. Its replacement packet is
(0,0,s_{p+4})
with the obvious endpoint truncation.

Now insert y immediately adjacent to x at the replacement position.

Let
A=v_{p+2},
C=v_{p+4}.
Because the x-replacement packet has its first central status zero, the window immediately before the pair is already target-zero. Because x and y have identical scans and the sector is flat, replacing x by y at this position gives the same outer reconnection statuses.

More explicitly, order the local coordinates as
...,A,x,y,C,...
or
...,A,y,x,C,...
The two new middle windows have the common value
alpha(A,x,y)=alpha(x,y,C)=c
in the first order, and 1-c in the reversed pair order.
Choose the pair order making these two values zero.

The left outer window is the same zero appearing in the x-replacement packet. The right outer window equals the corresponding y-scan value and therefore equals the right outer status of the x-replacement packet, namely s_{p+4}. Hence the local packet becomes
0,0,0,s_{p+4},
which is monotone and splices into the same untouched suffix as O_x'.

Therefore the enlarged order on
(O union {x,y}) minus {z}
is again one-change.

### Codimension-two identical-scan exchange theorem

For p,q>=3 in the coboundary-flat alternating ternary sector, two exterior vertices with identical scans relative to a one-change carrier have only two outcomes:

1. consecutive pair insertion at the switch gives a spanning one-change order; or
2. there is an explicit original carrier coordinate z (in the right branch z=v_{p+3}, with the symmetric left version after reversal) such that replacing z by BOTH exterior vertices gives a one-change order omitting z.

Thus identical blocking behavior does not create a codimension-two obstruction. It either closes the instance or collapses the two omitted coordinates to one explicit new omission.

This supplies an augmenting exchange move for synchronization arguments on common (n-2)-coordinate carriers. It is conditional on p,q>=3; short phases require the existing separate endpoint analysis.
