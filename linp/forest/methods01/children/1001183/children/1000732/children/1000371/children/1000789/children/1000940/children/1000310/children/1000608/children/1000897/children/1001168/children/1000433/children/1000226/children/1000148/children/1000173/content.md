# Every interior U_11 collision pays rank-sum surplus, a rotation packet, or a low-rank boundary triangle

## Statement


Let
v_0v_1...v_k
be a rainbow path in the terminal-pair graph whose parent hyperedges
E_s={x_s,v_{s-1},v_s}
belong to U_11 and have nondecreasing edge ranks r_s.

For every interior color-terminal collision x_i=v_j, 1<=j<=i-2, let
R_i=(g_1,...,g_{r_i-1})
be the chosen maximum source path ending at x_i and let h=g_{r_i-1}. At least one of the following holds.

(A) Rank-sum surplus:
  r_j+r_{j+1}>=r_i+3.

(B) Nonboundary exact-half-rank rotation:
  r_j+r_{j+1}=r_i+2,
and either
  (B-even) r_i=2m with m>=3 and r_j=r_{j+1}=m+1,
or
  (B-odd) r_i=2m+1 with m>=2, r_j=m+1, r_{j+1}=m+2, and E_{j+1}!=h.
In either case one adjacent parent edge has its unique entrance at a private vertex of a middle edge of R_i and meets R_i otherwise only at x_i. Rotating through that parent gives an (r_i-1)-edge linear path whose last edge has edge rank at least r_i-1 and which has two distinct possible last vertices of vertex rank at least r_i-1.

(C) Low-rank boundary triangle:
either
  r_i=4 and r_j=r_{j+1}=3,
or
  r_i=5, r_j=3, r_{j+1}=4, and E_{j+1}=h.
In either case the collision closes a local linear 3-cycle.

Thus failure of the plus-three edge-rank-sum inequality is confined to exact half-rank states: all nonboundary states emit the near-owner-rank rotation packet, while the only omitted states are two explicit low-rank triangle boundaries.


## Body


The universal bound 867efd696575 gives
  r_j+r_{j+1}>=r_i+2.
If the sum is at least r_i+3, we are in (A).

Otherwise
  r_j+r_{j+1}=r_i+2.
Apply the boundary-aware tight classification 9b023ed3d700.

If r_i=4, then r_j=r_{j+1}=3 and 9b023ed3d700 gives a local linear 3-cycle. This is the first case of (C).

Suppose next that r_i=2m with m>=3. Then
  r_j=r_{j+1}=m+1,
neither adjacent parent is the host last edge, and f0f28f03b0d9 supplies the full-length even rotation. One adjacent parent enters at the private middle vertex and meets R_i only there and at x_i; the rotated path has length 2m-1=r_i-1, its last edge has edge rank at least r_i-1, and two distinct possible last vertices have vertex rank at least r_i-1. This is (B-even).

Now let r_i=2m+1. The tight classification gives m>=2,
  r_j=m+1,
  r_{j+1}=m+2.
If E_{j+1}=h, 9b023ed3d700 shows that necessarily m=2, hence
  r_i=5, r_j=3, r_{j+1}=4,
and the collision closes the local triangle g_3,E_j,h. This is the second case of (C).

If E_{j+1}!=h, ccb148c02a44 applies. The higher-rank adjacent parent has its exact contact at the private vertex of g_m and meets R_i otherwise only at x_i. The resulting rotation has length 2m=r_i-1; its last edge has edge rank at least r_i-1, and two distinct possible last vertices have vertex rank at least r_i-1. This is (B-odd).

These cases exhaust equality in the universal plus-two bound, proving the trichotomy.
