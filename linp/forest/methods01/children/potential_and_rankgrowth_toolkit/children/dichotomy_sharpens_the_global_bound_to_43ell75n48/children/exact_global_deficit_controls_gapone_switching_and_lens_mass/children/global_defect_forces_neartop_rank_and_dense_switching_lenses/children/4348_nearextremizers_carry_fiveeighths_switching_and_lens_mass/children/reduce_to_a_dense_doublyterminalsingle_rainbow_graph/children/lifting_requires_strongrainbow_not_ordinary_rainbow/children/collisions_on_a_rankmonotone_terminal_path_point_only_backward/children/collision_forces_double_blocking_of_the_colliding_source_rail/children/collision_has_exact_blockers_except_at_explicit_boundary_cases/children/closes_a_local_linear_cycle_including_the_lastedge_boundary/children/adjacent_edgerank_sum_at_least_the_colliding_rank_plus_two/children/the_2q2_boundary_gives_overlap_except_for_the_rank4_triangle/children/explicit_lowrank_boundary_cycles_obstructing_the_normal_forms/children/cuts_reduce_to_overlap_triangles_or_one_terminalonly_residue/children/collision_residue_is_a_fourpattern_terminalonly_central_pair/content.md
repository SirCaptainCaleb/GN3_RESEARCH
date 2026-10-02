# At a 2q-4 cut the only new collision residue is a four-pattern terminal-only central pair

## Statement

Let
v_0v_1...v_k
be a rainbow terminal-pair path whose parent hyperedges belong to U_11 and have nondecreasing edge ranks.
Fix a cut with
  r_t=q,
  r_{t+1}=2q-4,
and let x_i=v_j be an interior color-terminal collision crossing the cut.

Then at least one of the following holds:

(1) there is an adjacent index s in {j,j+1} such that
    |V(R_i) intersect V(R_s)|>=2;

(2) some edge of R_i together with E_j,E_{j+1} forms a linear 3-cycle;

(3) the ranks are exactly
    r_i=2q-4,
    r_j=r_{j+1}=q,
and both exact contacts of E_j,E_{j+1} with
    R_i=(g_1,...,g_{2q-5})
are opposite terminals, with disjoint contact intervals. Writing c_- for the earlier contact and c_+ for the later one,
    c_- belongs to {
      g_{q-4} intersect g_{q-3},
      private(g_{q-3})
    },
and
    c_+ belongs to {
      private(g_{q-2}),
      g_{q-2} intersect g_{q-1}
    }.

Thus the first genuinely new state one rank below the 2q-3 cut is a four-pattern terminal-only central configuration.

## Body

A collision crossing the cut satisfies
  r_i>=2q-4,
  r_j,r_{j+1}<=q.
The certified bound 867efd696575 gives
  r_i+2<=r_j+r_{j+1}<=2q,
so
  r_i in {2q-4,2q-3,2q-2}.

If r_i=2q-2, both adjacent ranks equal q and the certified even tight form gives (1).

If r_i=2q-3, the two possibilities are the tight odd pattern (q-1,q), which gives (1), and the plus-three pattern (q,q). By c9982d3355c8 and ed2ef3140f4f, that plus-three pattern gives (1) when its contact intervals are disjoint and (2) when they overlap.

Now let r_i=2q-4. The individual lower bounds in 867efd696575 imply
  r_j,r_{j+1}>=q-1.
Hence the only ordered rank pairs are
  (q-1,q-1), (q-1,q), (q,q).
The first is the tight even pattern and gives (1). The mixed pair (q-1,q) gives (1) or (2) by 31582b0327ff.

It remains only
  r_j=r_{j+1}=q.
If the two exact contact intervals overlap, exactness gives (2). Suppose they are disjoint.

If either exact contact is a unique entrance x_s of its parent edge E_s, then x_s belongs to R_i while R_s ends at x_s. Unique-intersection rigidity 5854d853a44b implies that R_i and R_s have at least two common vertices, giving (1).

Therefore failure of (1) and (2) forces both exact contacts to be opposite terminals. Put
  p=2q-5.
The certified terminal-only singleton window 028c2c3f7167 gives, for each rank-q opposite-terminal contact c with first and last occurrence indices a,b,
  b>=p-q+2=q-3,
  a<=q-2,
with b in {a,a+1}.
Thus the possible terminal-only contact vertices are exactly
  g_{q-4} intersect g_{q-3},
  private(g_{q-3}),
  g_{q-3} intersect g_{q-2},
  private(g_{q-2}),
  g_{q-2} intersect g_{q-1}.

Let c_- precede c_+. Because their intervals are disjoint, the earlier interval must end before the later begins. The middle joint
  g_{q-3} intersect g_{q-2}
has interval [q-3,q-2], so if it were c_- there would be no permitted later terminal-only interval beginning after q-2; and if it were c_+ there would be no permitted earlier interval ending before q-3 except the first joint, which is already covered by the stated left set together with the direct interval check below.

More directly, the only terminal-only intervals in increasing order are
  [q-4,q-3],
  [q-3,q-3],
  [q-3,q-2],
  [q-2,q-2],
  [q-2,q-1].
A disjoint ordered pair must therefore choose its earlier interval from the first two and its later interval from the last two. These correspond exactly to the four contact-pair patterns displayed in (3).