# Top-band common-anchor chords are controlled by opposite-end excess plus return cycles

## Statement

Let h be an ascending nonspecial anchor of rank q terminal at v, and let
  Q=(R,h)
be a longest q-edge h-path ending at v, where the precursor R has q-1 edges and avoids v. Let its endpoints be a and y, with y the anchor entrance endpoint, so
  phi(y)=q-1.
Put
  E=phi(a)-(q-1)>=0.

Let F be any family of distinct source-clean whole chords
  e={x,v,u}
on R: each e is ascending nonspecial terminal at v, both x,u lie on R, and a clean maximum source path S_e ending at x is fixed.

For an integer D>=0, let F_D consist of the members with
  phi(e)>=q-D.
Call e unobstructed if S_e does not meet the R-side beyond u toward the endpoint opposite x.

Then
  |{e in F_D : e unobstructed}|
  <= 2E+4D+2.
Consequently
  |{e in F_D : S_e has a second intersection with R beyond u}|
  >= |F_D|-(2E+4D+2).

Thus, in a common-anchor selected family, any top-D rank band larger than the sum of the opposite-end excess E and the band width D necessarily creates proportionally many distinguished source/anchor return cycles.

## Body

Apply the two-endpoint packing theorem df81004a830d to R with threshold
  R0=q-D.
Its endpoint capacities are
  max(0,2(phi(a)-R0)+1)
and
  max(0,2(phi(y)-R0)+1).

Since phi(a)=q-1+E and phi(y)=q-1,
  phi(a)-R0 = E+D-1,
  phi(y)-R0 = D-1.
Hence the total unobstructed capacity is at most
  max(0,2(E+D-1)+1)+max(0,2(D-1)+1).

For all E,D>=0 this is bounded above by
  2E+4D+2,
with harmless slack covering D=0 boundary cases. Therefore at most that many rank-at-least-(q-D) chords are unobstructed. Every remaining member lies in branch (B) of ed412ed8e3b1 and has a clean source rail with a second intersection on the side beyond its opposite terminal.

For such a returned chord, choosing the first return vertex produces the nonspecial cycle budget of ebd43314756d whenever the orientation is toward y; the symmetric endpoint-slack form supplies the analogous ordered return on the a-side.

The only input beyond df81004a830d is the anchor identity phi(y)=q-1.
