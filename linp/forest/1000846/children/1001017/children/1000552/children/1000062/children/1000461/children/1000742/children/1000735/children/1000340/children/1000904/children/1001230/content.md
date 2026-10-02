# Near-extremal singleton transfer is periodic away from few defects

## Statement

For the singleton-column transfer automaton used in the 43/48 contact-conflict bound, let an admissible state walk have N transitions, transition weights w_i, and total weight W. If W >= 3N/4-D, then at most 4D+6 transitions fail to lie on the four-cycle 00->01->11->10->00. Hence, after deleting those exceptional transition positions, every remaining interval has the period-four singleton-column weight pattern 2,1,0,0, up to phase.

## Body

Use the transfer automaton and potential function from 1000904:
pi(00)=0, pi(01)=-5/4, pi(10)=-3/4, pi(11)=-3/2.
For an allowed transition sigma->tau of weight w define
  epsilon(sigma,tau)=3/4+pi(sigma)-pi(tau)-w.
The seven transitions listed in 1000904 give epsilon=0 exactly on
  00->01, 01->11, 11->10, 10->00,
while every other allowed transition has epsilon at least 1/4.

For a walk sigma_0,...,sigma_N with transition weights w_1,...,w_N,
  W=sum_i w_i
   =3N/4+pi(sigma_0)-pi(sigma_N)-sum_i epsilon_i.
Since pi takes values in [-3/2,0],
  pi(sigma_0)-pi(sigma_N)<=3/2.
Thus W>=3N/4-D implies
  sum_i epsilon_i<=D+3/2.
Every exceptional transition contributes at least 1/4, so their number is at most 4D+6.

The zero-defect transition graph is the unique directed cycle
  00->01->11->10->00.
Reading the corresponding chosen-column weights from the automaton gives
  2,1,0,0
around this cycle. Therefore every maximal interval containing no exceptional transition follows this period-four pattern, with a phase determined by its initial state.

This is a stability statement for the transfer calculation itself; boundary columns outside the automaton remain separate bookkeeping exactly as in 1000904.