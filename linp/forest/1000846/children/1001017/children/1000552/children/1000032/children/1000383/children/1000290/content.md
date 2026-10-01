# Recovered Astra 11/12 architecture: charged three-quarters bound via consecutive rank pairs

## Statement

The interrupted Astra route is best reconstructed as follows.

For v put p=phi(v), and let c_+(v) count ascending nonspecial edges e={x,v,u} for which v is terminal and phi(u)>=p.

TARGET LOCAL BOUND:
  c_+(v) <= floor(3p/4).

Every ascending edge can be assigned to a terminal of minimum endpoint potential, so it is counted by c_+ at its assigned terminal. Hence
  A <= sum_v c_+(v) <= (3/4) sum_v phi(v).

Combining with certified ascending accounting
  3m-A <= 2 sum_v phi(v)-n
gives
  m <= (11/12) sum_v phi(v)-n/3.
For a P_ell-free system:
  m <= ((11ell-15)/12)n.

A sufficient local lemma is the consecutive-rank block:
  for every v and q, at most three charged ascending terminal edges at v have ranks in {q,q+1}.
The charged rank floor and rank-pair arithmetic then give the exact floor(3p/4) bound, with odd-central-window capacities supplying the residue corrections.

The screenshots' clean-nearby-contact mechanism is rigorously represented by 990186a1aaa6, 08f894b8cb5e, and eac2e3da3eea: appropriate clean contacts in nearby rail/path positions splice to a path too long for an ascending entrance. This mechanism crucially uses clean/entrance structure and does not invoke the false arbitrary consecutive-single-blocker claim.

The remaining gap is to prove the consecutive-rank block or an equivalent global charge. A four-edge counterexample is already confined to q+1<=p<=2q-2. At p=2q-2 in the mixed q,(q+1)^3 pattern, the rank-q entrance is universally the central joint on every maximum p-path. Relative to its canonical entrance rail, every high competitor is either a strict-interior clean singleton chord or a two-contact chord; singleton contacts two positions apart are forbidden. Relative to a chosen high-edge witness, every other high competitor is additionally tail-terminal or cross-splice-blocked.

## Body

This object records the reconstructed proof architecture, not a completed proof of the local three-quarters bound. It corrects the earlier factor-two guess in 0904073d4cbf: Astra's target is most naturally the charged terminal count floor(3phi(v)/4), not an unrestricted 3phi(v)/2 terminal-incidence bound.
