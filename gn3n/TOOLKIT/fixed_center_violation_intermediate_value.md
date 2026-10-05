# Fixed-center violation intermediate value

**Summary:** In a permutahedron face where the auxiliary vertex is a singleton block, opposite nearest-violation signs at the same protected radius force either a chamber with larger protected radius or a chamber with simultaneous left and right violations at that radius.

## Statement

Let C be a permutahedron face of the auxiliary extension in which r is a singleton block, so its position is fixed across all chambers. Suppose every chamber has no violation at distances <d, and C contains one chamber with a left but no right violation at distance d and another with a right but no left violation at distance d. Then C contains a chamber with either no violation at distance d or both violations at distance d.

## Body

# Fixed-center violation intermediate value

Let `C` be a permutahedron face of the auxiliary extension `H^+`, and suppose the distinguished vertex `r` is a singleton block of the ordered partition defining `C`. Hence `r` occupies the same position `t` in every chamber of `C`.

Fix `d>=1`. Assume every chamber of `C` has no left or right violation at any distance less than `d`. Suppose `C` contains a chamber with violation pair

`(x_d,y_d)=(1,0)`

and another chamber with

`(x_d,y_d)=(0,1)`.

The chamber graph of a permutahedron face is connected: it is the Cartesian product of the adjacent-transposition graphs inside its blocks. Choose a chamber-graph path between the two displayed chambers.

The left and right status coordinates at distance `d` begin at positions

`t-2-d` and `t+d`,

whose difference is `2d+2>=4`. One adjacent transposition changes only status coordinates in four consecutive starting positions `k-2,k-1,k,k+1`, whose span is three. Therefore no chamber-graph edge can change both distance-`d` violation bits simultaneously.

Along the chosen path the pair `(x_d,y_d)` begins at `(1,0)` and ends at `(0,1)`. Since one step cannot change both bits, the path must pass through either

`(0,0)` or `(1,1)`.

In the first case that chamber has no violation at distance `d`; together with the common protection at all smaller distances, its protected radius is strictly larger than `d`. In the second case the chamber has simultaneous left and right violations at distance `d`.

Thus a fixed-center sign change cannot occur directly: it forces radius growth or a symmetric double violation.

## Metadata

- ID: fixed_center_violation_intermediate_value
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: passed
- Refutation: unrefuted
- Toolkit status: Limbo
