# Blocked two-vertex cycle absorption forces uniform cross comparisons — preserved pre-item development

## Development

## Failure of two-vertex cycle absorption forces uniform comparisons

Assume every center tournament of a reversal-antisymmetric ternary coloring h is transitive. Let C be a color-0 tight cyclic order with at least three vertices, and let E be a disjoint set of at least three exterior vertices. Suppose there is no color-0 tight path on C union {x,y} for any two distinct x,y in E.

For c in C write p(c),s(c) for its cyclic predecessor and successor. The center order at c has p(c)<s(c).

### Theorem
Exactly one of the following two necessary configurations holds.

(I) At every cycle center c, every x in E precedes both p(c) and s(c). At every exterior center x in E, every c in C precedes every y in E\setminus{x}.

(II) At every cycle center c, every x in E follows both p(c) and s(c). At every exterior center x in E, every y in E\setminus{x} precedes every c in C.

The word “necessary” matters: neither configuration is asserted to preclude all other monochromatic paths. The theorem says failure of every two-vertex absorption forces one of them.

### Proof: no middle positions
The middle-vertex absorption lemma shows that no x in E lies strictly between p(c) and s(c). Thus each x is either before both (call this position L) or after both (position H) at every c.

Let H_c={x in E:x is in position H at c}.

### Proof: propagation around the cycle
If y is in H_c and x is in position L at s(c), with x!=y, then
(x,s(c),s^2(c),...,p(c),c,y)
is a color-0 tight path on C union {x,y}. Its two new endpoint windows have color 0 by the definitions of L and H, and its other windows come from C. This is excluded.

Hence y in H_c implies E\setminus{y} is contained in H_{s(c)}.

If H_c has at least two members, this implication gives H_{s(c)}=E. If H_c has just one member, then |H_{s(c)}|>=|E|-1>=2, and therefore H_{s^2(c)}=E. Once H is all of E it remains so at every subsequent cycle vertex. Going once around C shows that a nonempty H_c forces H_c=E at every vertex.

Therefore either all H_c are empty, giving the first cycle-center condition, or all H_c=E, giving the second.

### Proof: exterior-center comparisons
In case (I), (x,c,s(c),...) is a color-0 path on C union {x}, for every x,c. If h(y,x,c)=0 for some y in E\setminus{x}, prepending y gives the excluded two-vertex path. Hence h(y,x,c)=1, equivalently h(c,x,y)=0. Thus c precedes y in the center order at x.

In case (II), (...,p(c),c,x) is a color-0 path on C union {x}. Appending y would succeed if h(c,x,y)=0. Therefore h(c,x,y)=1, so y precedes c in the center order at x.

This proves both configurations and their mutual exclusivity.

### Corollary: a monochromatic exterior path completes a one-change order
Under either forced configuration, if E has a monochromatic tight spanning path, then C union E has a spanning one-change order.

Reverse the exterior path if needed to obtain a color-0 order Q. If Q has fewer than three vertices, choose either orientation and regard its tightness as vacuous.

In case (I), use the reversed color-1 cycle cut to end at any c, followed by Q starting (x,y,...). The two crossing windows are
h(s(c),c,x)=1 and h(c,x,y)=0.
Thus the word is a block of 1s followed by a block of 0s.

In case (II), use the forward color-0 cycle cut to end at c, followed by Q reversed, a color-1 path starting (x,y,...). The crossing windows are
h(p(c),c,x)=0 and h(c,x,y)=1.
Thus the word is a block of 0s followed by a block of 1s.

The stated theorem assumes |E|>=3, so both crossing windows exist and Q has a genuine colored window. The short-path observation only explains how the same joining construction extends when a configuration is separately known on a smaller E.

### Closure relevance and limitation
If C union E is the ambient ground set, the corollary is a spanning NOR construction. If it is a proper subset, the remaining ambient vertices are not incorporated.

The theorem is not a reduction of general NOR to NOR on E: a one-change exterior path can have two nonempty color blocks, and the displayed join can then introduce a second change. Monochromatic exterior reachability, or a new splice through the exterior switch, is still required.

For a monochromatic cycle whose one-vertex absorption reaches the maximum possible monochromatic path size, the hypothesis of the theorem holds automatically. Thus a tight maximum in the cycle-to-path absorption process has a rigid cross-comparison structure, not arbitrary insertion failures.
