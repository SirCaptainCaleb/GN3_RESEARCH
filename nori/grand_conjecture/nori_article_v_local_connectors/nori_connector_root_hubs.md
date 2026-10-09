# Root hubs, midpoint witnesses and terminal caps

# Bichromatic root diamonds and certified seam repairs

Let c color actual ordered three-faces of Q_n. A monochromatic four-edge geodesic is witnessed by its two overlapping ordered three-face windows. A bichromatic hub is a cube vertex supporting such genuine connectors in both colors. Two questions then arise: which endpoint caps does a hub force, and when can two paths through the same hub be spliced without introducing additional changes?

## Same-root opposite-color diamonds

Suppose x and y are cube vertices at distance four and there are monochromatic geodesics P_0 and P_1 from x to y with direction orders (c,a,b,d) and (a,c,d,b), of colors 0 and 1 respectively. Let e be an unused coordinate. Appending e to either path produces a genuine five-edge geodesic, with two original windows of constant color and one new terminal window. Both new windows lie in the same actual three-face through y, with free set {b,d,e} but with distinct orders (b,d,e) and (d,b,e). Their colors are independent unless a physical reversal relation actually identifies their orbits. The diamond therefore provides two candidate continuations with explicit terminal-color tests, not an automatic common monochromatic extension.

Under additional global maximality assumptions, failures of both continuations force the corresponding ordered-cap colors to be opposite to their original path colors. Such identities can feed a root exchange, provided the newly exposed starting and terminal windows are checked in the same manner.

## Four-way splicing at a common physical midpoint

Let P and Q be full antipodal geodesics from the same root x, whose first ell used-coordinate sets agree, where 3<=ell<=n−3. Both paths reach the identical midpoint y after ell steps, and both suffixes traverse the complementary coordinate support. Hence any of the four choices of prefix from P or Q and suffix from P or Q yields a genuine full antipodal geodesic: no direction is repeated.

Write a chosen prefix A with last two directions (u,v) and a chosen suffix B with first two directions (w,t). The actual window-color word of AB consists, in order, of the interior three-windows of A, followed by

c(F_y({u,v,w});(u,v,w)),  c(F_y({v,w,t});(v,w,t)),

and then the interior windows of B. This follows by listing consecutive triples of the concatenated direction word; exactly two triples straddle the seam. The two displayed windows are physical faces at the common midpoint, so root identification is exact.

Thus selecting a prefix and suffix whose interior words each have the desired constant phase leaves exactly two independently checkable seam colors. A monochromatic hub through y may repair both when its certified edge geometry matches the ordered pairs. Merely knowing that P and Q cross at y, or have balancing topological labels, does not settle those seam colors.

## Closure obligation

The four-way splice lemma converts a topological or counting coincidence into a finite set of physical seam checks. The opposite-color diamond supplies locally rich candidates but can be blocked by ordered-cap colors on shared physical faces. A global connector theorem must force one successful choice across a compatible family of roots or cut positions. This is the precise interface between local bichromatic hub abundance and full one-switch antipodal extraction.
