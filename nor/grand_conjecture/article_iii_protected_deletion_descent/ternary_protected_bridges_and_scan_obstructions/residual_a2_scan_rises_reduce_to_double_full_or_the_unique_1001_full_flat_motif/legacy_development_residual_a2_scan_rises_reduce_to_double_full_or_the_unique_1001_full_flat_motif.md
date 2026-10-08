# Residual A2 scan rises reduce to double-full or the unique 1001 full-flat motif — preserved pre-item development

## Any later rise in a residual A2 suffix scan creates a canonical singleton barrier

Work in the recurrent flat A2 replacement cycle. For one residual coordinate (u), use its companion protected deletion order obtained by deleting the final (u) from the seven-coordinate weave. Its protected front has word
[
0,1,1,1
]
and then continues through the untouched common suffix
[
T=(t_1,t_2,ldots)
]
whose consecutive ternary windows all have color (1).

Write
[
s(j)=alpha(u,t_j,t_{j+1})
]
for the residual suffix scan. The proved A2 scan theorem shows that (s) is (101)-free.

Suppose nevertheless that (s) has a later rise (0	o1). Choose an index (j) with
[
s(j)=0,qquad s(j+1)=1.
]
Since (101) is forbidden, whenever (jge2) one necessarily has
[
s(j-1)=0.
]

Put
[
e=t_{j-2},qquad a=t_{j-1},qquad b=t_j,qquad c=t_{j+1},qquad d=t_{j+2}
]
when the indicated coordinates exist. Insert (u) between (b) and (c) in the companion deletion order.

Because the old suffix is monochromatic (1),
[
alpha(e,a,b)=alpha(a,b,c)=alpha(b,c,d)=1.
]
The four consecutive statuses around the insertion are
[
alpha(e,a,b)=1,
]
[
alpha(a,b,u)=alpha(u,a,b)=s(j-1)=0,
]
[
alpha(b,u,c)=1-alpha(u,b,c)=1-s(j)=1,
]
[
alpha(u,c,d)=s(j+1)=1.
]
Hence every later scan rise creates an isolated singleton packet
[
1,0,1
]
on the five coordinates
[
(e,a,b,u,c),
]
followed immediately by the surrounding target color (1).

### The right transition is always fully curved

The right transition is the ordered tetrahedron
[
(a,b,u,c)
]
with consecutive statuses (0,1).

One off-face is the untouched suffix face
[
alpha(a,b,c)=1.
]
The tetrahedral parity identity on ({u,a,b,c}), using
[
alpha(u,a,b)=0,qquad alpha(u,b,c)=0,qquad alpha(a,b,c)=1,
]
forces
[
alpha(u,a,c)=1,
]
hence by alternation
[
alpha(a,u,c)=0.
]
Thus the two off-faces are (1,0), exactly the fully-curved pattern for a (0	o1) transition.

### The left transition is full except for the shortest possible valley

The left transition is
[
(e,a,b,u)
]
with consecutive statuses (1,0). Its first off-face is
[
alpha(e,a,u)=alpha(u,e,a)=s(j-2).
]
The tetrahedral parity identity then forces the other off-face to be its complement. Therefore:

- if (s(j-2)=0), the off-faces are (0,1), so the left transition is fully curved;
- if (s(j-2)=1), the off-faces are (1,0), so the left transition is flat.

Consequently every return of a residual scan from (0) to (1) has one of only two local forms.

1. **Long zero valley.** If the rise is preceded by at least three consecutive zeros, then insertion produces an exact double-full singleton (101). It therefore enters the established double-full one-sided resolution machinery.
2. **Shortest valley.** The only rise not already double-full is
   [
   1,0,0,1.
   ]
   It produces a mixed flat/full singleton: the left (1	o0) transition is flat and the right (0	o1) transition is fully curved.

Thus the audited global fact “residual scans are (101)-free” can be strengthened structurally without assuming the invalid single-step propagation claim:

> every later (0	o1) return is either a double-full singleton barrier or the unique mixed (1001) full/flat motif.

This is a boundary-safe reduction because the companion deletion order keeps the protected front and every suffix coordinate outside the insertion packet in its original relative order. The remaining propagation problem is no longer arbitrary: it is enough to eliminate the (1001) mixed full/flat motif and to control the exported side of the double-full resolution.
