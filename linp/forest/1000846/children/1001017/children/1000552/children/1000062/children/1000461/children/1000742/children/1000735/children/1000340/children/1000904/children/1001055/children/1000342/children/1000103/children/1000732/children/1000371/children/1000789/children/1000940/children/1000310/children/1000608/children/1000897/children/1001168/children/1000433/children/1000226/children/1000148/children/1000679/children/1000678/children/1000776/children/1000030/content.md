# In the odd tight reciprocal-exchange residue the two cross-terminal contacts lie on the same side of the aligned joint

## Statement

Retain alternative (3) of ac73dd583c10. Let
  A=R_j
be the m-edge chosen maximum source path ending at x_j, and let
  B=R_{j+1}
be the (m+1)-edge chosen maximum source path ending at x_{j+1}.

The paths A and B have exactly one common vertex z, which is an internal joint at the same path-edge index k on both paths. Thus write
  A=A^- union A^+,
  B=B^- union B^+,
where A^-,B^- are the k-edge prefixes ending at z and A^+,B^+ are the complementary suffixes from z to x_j,x_{j+1}.

The exact cross-contacts are
  E_{j+1} intersect V(A)={v_{j+1}},
  E_j intersect V(B)={v_{j-1}}.

Then v_{j+1} and v_{j-1} lie on the same side of z:
either
  v_{j+1} in V(A^- ) minus {z}
and
  v_{j-1} in V(B^- ) minus {z},
or
  v_{j+1} in V(A^+ ) minus {z}
and
  v_{j-1} in V(B^+ ) minus {z}.

The two mixed orders are impossible.

## Body

The concatenations
  H_j:=B^- followed by A^+
and
  H_{j+1}:=A^- followed by B^+
are linear paths because A and B have exactly one common vertex z. Their lengths are
  |H_j|=k+(m-k)=m,
  |H_{j+1}|=k+(m+1-k)=m+1.
They end at x_j and x_{j+1}, respectively.

Suppose first that
  v_{j-1} lies before z on B
while
  v_{j+1} lies after z on A.
Then H_{j+1}=A^- followed by B^+ is disjoint from E_j: the vertex x_j lies on the omitted suffix A^+, the vertex v_{j-1} lies on the omitted prefix B^-, and the common terminal x_i is absent from both source paths. Also H_{j+1} meets E_{j+1} only at its last vertex x_{j+1}: its other terminal v_{j+1} lies on the omitted suffix A^+, and x_i is absent.

Therefore
  H_{j+1},E_{j+1},E_j
is a linear path of length
  (m+1)+2=m+3
ending in E_j. But phi(E_j)=m+1, contradiction.

Now suppose
  v_{j-1} lies after z on B
while
  v_{j+1} lies before z on A.
Then H_j=B^- followed by A^+ meets E_j only at its last vertex x_j: v_{j-1} lies on the omitted suffix B^+ and x_i is absent. It is disjoint from E_{j+1}: x_{j+1} lies on the omitted suffix B^+, v_{j+1} lies on the omitted prefix A^-, and x_i is absent.

Hence
  H_j,E_j,E_{j+1}
is a linear path of length
  m+2=phi(E_{j+1})
ending in E_{j+1} through the common terminal x_i. Since E_{j+1} is nonspecial and its unique entrance is x_{j+1}, this is a longest E_{j+1}-ending path with the wrong entrance, contradiction.

Thus neither mixed order can occur, proving the same-side assertion.
