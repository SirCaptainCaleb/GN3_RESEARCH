# Lens-free exact D+Y cell payment theorem

## Statement

Let P=(g_1,...,g_p) be a maximum p-edge path ending at v, and let F be a family of distinct edges through v such that each has exactly one off-v contact with P. Restrict to the interior two-slot cells
  C_i={b_i,z_i}, 1<=i<=p-3,
and let s_int be the number of members of F whose unique contact lies in these cells.

Let D be the number of doubly occupied interior cells. For each occupied C_i let h_i=g_{i+2} be its standard rotation output, and call C_i unpaid when h_i is the flat ascending branch (3) of 6205fe95ecf8; call it paid otherwise. Let Y be the number of paid occupied cells.

Then
  D+Y >= s_int-ceil((p-3)/2).

Every paid cell has at least one of:
(a) phi(h_i)>p;
(b) phi(h_i)=p and h_i is special;
(c) phi(h_i)=p, h_i is nonspecial nonascending, with its forward joint of vertex rank at least p.
Every doubly occupied cell supports a linear 3-cycle formed by its host edge and its two blocker edges.

Thus this exact D+Y payment inequality is independent of any endpoint-lens assertion and of any dense-switching theorem.

## Body

Let C be the number of occupied interior cells. Each cell has exactly two possible contact vertices, and distinct edges through v have distinct non-v contact vertices by linearity. Hence every occupied cell contains one or two F-contacts and
  s_int=C+D.                                           (1)

By the certified flat-output independence theorem 3c0ac5d646f1, the unpaid occupied cells form an independent set in the path of p-3 interior cell positions. If A denotes their number, then
  A<=ceil((p-3)/2).                                    (2)

By definition Y=C-A. Combining (1) and (2),
  D+Y=D+C-A=s_int-A
      >=s_int-ceil((p-3)/2).

The classification of a paid cell is exactly the complement of branch (3) in the exhaustive output theorem 6205fe95ecf8, giving alternatives (a)-(c).

Finally, suppose C_i is doubly occupied. Its two contact vertices are b_i and z_i, used by distinct blocker edges f_b,f_z through v. The two blockers meet exactly at v. The host edge g_i meets f_b at b_i and f_z at z_i, and linearity forbids any additional pairwise intersections. Since v is not on g_i, the three edges
  g_i,f_b,f_z
form a linear 3-cycle.

No use is made of b032348c1a8a, 465568d6d8dc, b35b0fd4e4cd, or any endpoint-lens statement.
