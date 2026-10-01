# Central-window ordering boosts switching source mass to 185/512

## Statement

Let v be an active misaligned vertex with p=phi(v)>=8, and let F_v be a switching family from b032348c1a8a relative to the chosen maximum p-edge path P_v. Put s=|F_v|, and order the switcher edge ranks
  r_1<=...<=r_s.
Then for every i=1,...,s,
  r_i >= ceil((2p+i+3)/4).
Hence, writing x_i for the unique entrance of the i-th switcher,
  sum_{i=1}^s phi(x_i)
  >= sum_{i=1}^s (ceil((2p+i+3)/4)-1)
  >= (p/2)s + s^2/8 - s/8.

Since b032348c1a8a gives
  s>=beta(p)-eta_v-ceil((3q(v)-4)/4),
a low-defect center eta_v=o(p) satisfies
  sum_{f in F_v}phi(x_f) >= (185/512-o(1))p^2.

For simultaneous switching families at several centers,
  sum_v [ (p_v/2)s_v+s_v^2/8-s_v/8 ]
  <= sum_y (phi(y)-1)max(0,2phi(y)-3),
where s_v=|F_v|.

## Body

Every switcher f in F_v is an ascending nonspecial edge terminal at v, has rank strictly below p because v is misaligned, and is single on the chosen maximum p-edge path P_v.

For an integer R<p let
  N_R=|{f in F_v: phi(f)<=R}|.
The central-window theorem 49080cbf1371 applies to the entire family of ascending terminal edges of rank at most R that are single on P_v, so
  N_R<=max(0,4R-2p-3).                                (1)

Now order the switcher ranks r_1<=...<=r_s. Taking R=r_i in (1) gives
  i<=4r_i-2p-3,
hence
  r_i>=ceil((2p+i+3)/4).                              (2)

Ascendingness gives phi(x_i)=r_i-1. Therefore
  sum_i phi(x_i)
   >=sum_{i=1}^s(ceil((2p+i+3)/4)-1)
   >=sum_{i=1}^s(2p+i-1)/4
   =(p/2)s+s^2/8-s/8.                                (3)

By b032348c1a8a,
  s>=beta(p)-eta_v-ceil((3q(v)-4)/4).
Since q(v)<=p-1,
  s>=(5/8)p-eta_v-O(1).
If eta_v=o(p), substitute s=(5/8-o(1))p into the increasing quadratic on the right of (3):
  (p/2)(5p/8)+(1/8)(25p^2/64)-o(p^2)
  =(5/16+25/512-o(1))p^2
  =(185/512-o(1))p^2.

Finally choose switching families simultaneously. By 2f54b541202a,
  sum_v sum_{f in F_v}phi(x_f)
  <=sum_y(phi(y)-1)max(0,2phi(y)-3).
Combining with (3) center by center yields the global displayed inequality.
