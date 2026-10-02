# Low defect forces thick potential superlevels

## Statement

Let H be a finite linear 3-graph, let v be an active misaligned vertex with p=phi(v)>=8 and q=q(v)<p, and let eta_v be the local defect from b032348c1a8a. Put
  V_{\ge p}={w:phi(w)>=p}.
Then
  |V_{\ge p}| >= (1/2)[beta(p)-eta_v-ceil((3q-4)/4)]-O(1)
and therefore, since q<=p-1,
  |V_{\ge p}| >= (5/16)p-(1/2)eta_v-O(1).

Equivalently,
  eta_v >= (5/8)p-2|V_{\ge p}|-O(1).

Consequently, for any sequence satisfying the 43/48 near-extremal hypotheses of d287da5967d5, for every fixed epsilon>0 all but o(S) endpoint-potential mass lies on vertices v with
  |V_{\ge phi(v)}| >= (5/16-epsilon)phi(v).
Thus asymptotic 43/48 sharpness cannot be supported by sparse high-potential spikes; almost all potential mass must lie in quantitatively thick superlevel sets.

## Body

Fix v. By b032348c1a8a, after choosing a maximum-rank ascending terminal anchor and the designated maximum p-edge path P_v, there is a switching family F_v with
  |F_v| >= beta(p)-eta_v-ceil((3q-4)/4).                (1)
Every member of F_v is a single blocker on P_v.

Apply the single-blocker rotation packet theorem 5f8d96bf566a to P_v and F_v. There is an absolute constant C such that one obtains a set R(v) of distinct rotation endpoints with
  |R(v)| >= |F_v|/2-C,                                 (2)
and every w in R(v) satisfies
  phi(w)>=p.
Hence R(v) is a subset of V_{\ge p}. Combining (1) and (2),
  |V_{\ge p}|
  >=(1/2)[beta(p)-eta_v-ceil((3q-4)/4)]-C.             (3)

Because q<=p-1 and the ceiling term is increasing in q,
  ceil((3q-4)/4)<=ceil((3p-7)/4).
Using beta(p)=floor((11p-16)/8), the difference
  (1/2)[beta(p)-ceil((3p-7)/4)]
is
  (5/16)p-O(1).
Thus
  |V_{\ge p}| >= (5/16)p-(1/2)eta_v-O(1),              (4)
which is equivalent to the displayed defect lower bound.

Now take a 43/48 near-extremal sequence as in d287da5967d5. That corollary gives
  sum_v eta_v=o(S)
and says that inactive/aligned/bounded-potential vertices carry only o(S) potential mass.

Fix epsilon>0. Among the remaining active misaligned vertices, call v defect-bad when eta_v>epsilon phi(v). Then
  epsilon sum_{v defect-bad}phi(v)
  < sum_v eta_v=o(S),
so defect-bad vertices carry o(S) potential mass. For every other active misaligned vertex with sufficiently large p, (4) gives
  |V_{\ge p}| >= (5/16-epsilon/2)p-O(1)
              >= (5/16-epsilon)p.
The finitely bounded p-range contributes O(n_+)=o(S). Therefore all but o(S) potential mass lies on vertices satisfying the claimed thick-superlevel inequality.