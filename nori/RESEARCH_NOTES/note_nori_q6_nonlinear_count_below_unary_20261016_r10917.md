# Q6 nonlinear geodesic-count construction defeats all unary minimizers

- Stable ID: note_nori_q6_nonlinear_count_below_unary_20261016_r10917
- Author: unspecified; session provenance retained
- Primary home: subsection:complementary_rank_geodesic_counting_and_parity_blindness
- Labels: NORI1, geodesic-count, global-compression-obstruction, computational-enumeration, unary
- Lifecycle: active
- Epistemic status: computational
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r10917_3
- Updated session: session_nori_r10917_3
- Disposition: none
- Successor: none

## Related references

- note:note_nori_q4_red_geodesic_count_extremizers_20261016_r10917

## Research note

Let N_0(c) be the number of rooted ordered red full antipodal geodesics of a legal antipodally odd binary edge coloring of Q_n.

**Theorem (nonlinear Q6 beats every unary Q6 in red-geodesic count).** Define M(a,b,c)=ab+ac+bc over F_2 (Boolean majority). On Q_6 take
c_0=x_5, c_5=x_0,
c_1=1+M(x_0,x_4,x_5), c_2=c_1+x_0+x_5,
c_4=1+M(x_0,x_1,x_5), c_3=c_4+x_0+x_5.
Then c is legal, and N_0(c)=80. A complete finite enumeration of all 10^6 unary legal Q6 colorings c_i=x_{r(i)}+epsilon_i, r(i)!=i, gives minimum N_0=128, with 3240 attaining unary colorings. Consequently
min_{legal Q6 c} N_0(c) <= 80 < 128 = min_{unary Q6 c} N_0(c).
This refutes the conjecture that a global minimizer of red full-geodesic count can always be chosen unary.

**Human proof of the count 80.** Each rule ignores its own bit; global bit complementation flips M and all linear terms as required. In a red full geodesic, directions 0 and 5 both occur. If initially x_0=x_5=1 then neither of these moves is red; if initially x_0=x_5=0, using either one blocks the other. Thus x_0 != x_5. The first of these two moves changes the one-valued bit to zero, producing x_0=x_5=0; at this intermediate state every rule in directions 1,2,3,4 has color one. Hence 0 and 5 must be consecutive, occurring as 0,5 if x_0=1, or 5,0 if x_5=1. Before and after this two-step block, x_0 != x_5, so M(x_0,z,x_5)=z, and the other colors reduce to
c_1=1+x_4, c_2=x_4, c_3=x_1, c_4=1+x_1.
These rules admit a red full four-direction geodesic precisely when x_1 != x_4. Its direction order is then forced: 2,4,1,3 if (x_1,x_4)=(1,0), and 3,1,4,2 if (x_1,x_4)=(0,1). The values of x_2 and x_3 are unrestricted. There are 2*2*2*2=16 admissible starting states, and the consecutive pair 0,5 can be inserted at any of five gaps within the forced four-direction order. Thus N_0=16*5=80.

**General unary counting formula (proved).** For c_i=x_{r(i)}+epsilon_i on Q_n and each direction permutation pi, define
theta_i(pi)=epsilon_i + 1_{pi^{-1}(r(i))<pi^{-1}(i)} (mod 2).
The red full-geodesic constraints at initial root x are x_{r(i)}=theta_i(pi). For each reader j all values theta_i(pi) with r(i)=j must agree. If they do, there are 2^{n-|im r|} admissible roots; otherwise none. Therefore
N_0(c)=2^{n-|im r|} * sum_{pi in S_n} product_{j in im r} 1_{theta_i(pi) is constant over r^{-1}(j)}.
Proof: the Boolean rule at its occurrence reads the initial bit of its reader plus one if that reader has already moved. Each used reader bit is fixed by its children; unread bits remain free.

**Reproducible finite certificate.** The independent C++ program nori_q6_unary_counterexample.cpp enumerates every r(i) in [6] without i and every sign epsilon_i, totaling (2*5)^6=1,000,000 unary rules, with the dynamic program D_x(empty)=1 and
D_x(S)=sum_{i in S}[c_i(x xor 1_S)=0] D_x(S without i),
then N_0(c)=sum_x D_x([6]). It reports "nonlinear count=80" and "unary minimum=128, attaining unary colorings=3240". It independently checks edge consistency and antipodal oddness for the nonlinear example. The finite unary minimum is computer-assisted; the nonlinear count and the general unary formula have complete combinatorial proofs.

**Scope.** The inequality separates a nonlinear coloring from all unary colorings in one dimension. It does not determine the minimum N_0 over every legal Q6 coloring and does not refute NORI1. This closes the proposed global unary-extremizer proof strategy without requiring any conjecture about minima in higher dimensions.
