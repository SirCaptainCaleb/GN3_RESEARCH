# Nonascending top-rank rotation outputs are all-top edges

## Statement

In the setup of 09e3d5b2bd6b, suppose the output edge g_j is nonspecial and nonascending. Then all three vertices of g_j have endpoint potential L.

More explicitly, writing
  g_j={z_{j-1}, b_j, z_j},
where z_{j-1}=g_{j-1}∩g_j, b_j is private on the host path, and z_j=g_j∩g_{j+1}, one has
  phi(z_{j-1})=phi(b_j)=phi(z_j)=L.

Hence the nonascending branch of the top-rank rotation-output packet consists entirely of rank-L edges induced on the top-potential vertex set V_L={w:phi(w)=L}.

## Body

The output edge g_j comes from an occupied blocker cell C_{j-2}. By 465568d6d8dc, the associated L-edge rotation can end with either
  b_j
or
  z_{j-1}
as a last vertex.
Since L is the global maximum path length,
  phi(b_j)=phi(z_{j-1})=L.                             (1)

By 09e3d5b2bd6b, if g_j is nonspecial nonascending then its unique entrance is the forward joint z_j and
  phi(z_j)=L.                                         (2)

The three vertices z_{j-1},b_j,z_j are exactly the three vertices of the linear-path edge g_j. Combining (1) and (2) proves the claim.
