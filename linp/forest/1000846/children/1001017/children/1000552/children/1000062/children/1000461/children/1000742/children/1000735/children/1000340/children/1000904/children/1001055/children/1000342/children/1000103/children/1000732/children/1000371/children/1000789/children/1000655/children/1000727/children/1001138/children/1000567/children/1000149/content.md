# Near equality in clean-retained packing has a unique period-five normal form

## Statement

Use the clean-retained central-window setup of 7e047fd40dd7 at a rank cutoff R<p, with N=2R-p-1 eligible joint cells, and let m=|X_{\le R}|. Put
  Delta = 4N/5 + 7/5 - m >= 0.

Then all but at most 5Delta of the eligible cell transitions are on the unique critical five-cycle of the cell automaton. Consequently the eligible window can be partitioned into at most 5Delta+1 consecutive intervals such that, on each interval away from its boundary, the clean-retained occupancy pattern is periodic of period five:
  (private+joint), private, empty, joint, empty,
up to cyclic phase.

In particular, if m=4N/5-o(N), then after deleting o(N) cells the clean-retained contact pattern is a union of period-five intervals of the displayed form.

## Body

Recall the five reachable automaton states from 7e047fd40dd7:
  A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,1), E=(1,1,1),
with potentials
  psi(A)=0,
  psi(B)=-4/5,
  psi(C)=-3/5,
  psi(D)=-6/5,
  psi(E)=-7/5.

For every allowed transition tau:s->t carrying cell weight w(tau), the proof of 7e047fd40dd7 established
  w(tau) <= 4/5 + psi(s)-psi(t).
Define its slack
  sigma(tau)=4/5+psi(s)-psi(t)-w(tau)>=0.

Inspecting the allowed transition list shows that sigma(tau)=0 exactly for the five transitions
  A --(private+joint;2)--> D,
  D --(private;1)--> E,
  E --(empty;0)--> C,
  C --(joint;1)--> B,
  B --(empty;0)--> A.
They form one directed five-cycle. Every other allowed transition has slack at least 1/5.

Let the N eligible cells induce transitions tau_1,...,tau_N between successive automaton states. Summing the exact slack identity gives
  m = 4N/5 + psi(start)-psi(end) - sum_j sigma(tau_j).
Since the potential range has width 7/5,
  psi(start)-psi(end) <= 7/5.
Therefore
  sum_j sigma(tau_j)
  <= 4N/5+7/5-m
  = Delta.
As every noncritical transition contributes at least 1/5,
  #{j:sigma(tau_j)>0} <= 5Delta.                       (1)

Delete those exceptional transition positions. On every remaining consecutive run, every transition is critical. But the critical transition graph is the single directed cycle
  A->D->E->C->B->A.
Hence the cell weights/types along each run repeat
  (private+joint), private, empty, joint, empty
up to cyclic phase.

There are at most one more critical run than exceptional transitions, so at most 5Delta+1 runs. Equation (1) also gives the asymptotic conclusion immediately when m=4N/5-o(N).