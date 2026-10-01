# Singleton cells in the reciprocal rectangle force alternation or two reverse cross-triples

## Statement

Keep the hypotheses of astra004recrect. Suppose one of the four intersection blocks is a singleton. Then the opposite block is also a singleton and the other two blocks have order lambda-1. Let the two large blocks be Y,Z and the singleton blocks be {a},{b}. Since Y and Z are nonsingleton, each is a source or sink in the abstract four-cycle of the four maximum paths. If Y and Z have the same source/sink type, then the whole rectangle alternates: either Ya,Yb,Za,Zb are the four tight maximum paths, or aY,bY,aZ,bZ are. If Y and Z have opposite types, then both singleton corners are through-oriented. At each through singleton, maximality forces the unique central splice triple to be non-tight, hence its reverse is tight. Concretely, after choosing the case Ya and aZ, if y is the last vertex of Y and z the first vertex of Z, then (y,a,z) is non-tight and (z,a,y) is tight; the analogous reverse cross-triple holds through b. Thus the singleton boundary of reciprocal two-crossing equality also reduces to an alternating endpoint rectangle or two explicit reverse cross-triples.

## Body

# Proof

By astra004recrect the four intersection blocks have sizes r,lambda-r,lambda-r,r around the rectangle. If one block is a singleton, then r=1 or lambda-r=1, so its opposite block is also a singleton and the other two have order lambda-1. Rename the large blocks Y,Z and the singleton blocks {a},{b}.

Each large block has order at least two. The through-orientation argument from astra004recrect therefore applies to Y and Z: each is a source or a sink in the directed abstract 4-cycle whose edges are the four maximum paths.

If Y and Z have the same type, the two intervening singleton vertices necessarily have the opposite type, so sources and sinks alternate around the whole rectangle. This gives one of the two displayed alternating forms.

Suppose instead that Y and Z have opposite types. Then both singleton corners are through-oriented. At a, after relabelling the directions if necessary, the two incident maximum paths have forms Y,a and a,Z. Write y for the last vertex of Y and z for the first vertex of Z. If (y,a,z) were tight, the concatenation Y,a,Z would be a tight path: all triples inside Y and Z are inherited, the join into a is inherited from Y,a, the join out of a is inherited from a,Z, and (y,a,z) is the only additional triple spanning the singleton overlap. Its order is (lambda-1)+1+(lambda-1)=2lambda-1>lambda, contradicting maximality of lambda. Hence (y,a,z) is non-tight, so boundary antisymmetry gives (z,a,y) tight. The same argument at b gives the second reverse cross-triple. ∎