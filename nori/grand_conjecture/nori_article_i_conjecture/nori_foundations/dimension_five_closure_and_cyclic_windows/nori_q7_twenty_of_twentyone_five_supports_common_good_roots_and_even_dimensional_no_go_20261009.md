# At least 32 Q7 roots have 20/21 good five-supports; exact even-dimensional no-go

# Twenty of the twenty-one physical five-supports are simultaneously good at many roots of every legal \(Q_7\) coloring

Let \(c\) be a reversal-odd coloring of actual ordered three-faces of \(Q_7\). For each five-coordinate set \(B\subset[7]\), write \(E_B\) for the set of initial roots at which **all** 120 five-orders on \(B\) have alternating three-window color words. Define
\[
 b(x)=|\{B\in\binom{[7]}5:x\in E_B\}|.
\]

**Theorem (quantitative nearly-total common-root synchronization).** At least **32 of the 128 physical roots** \(x\) satisfy \(b(x)\le1\). Thus at each of these roots genuine at-most-one-switch five-geodesics exist on at least **20 of all 21** distinct five-coordinate supports, simultaneously. If there are exactly \(h\le3\) heavy supports (defined below), the explicit lower bound on the number of these roots improves to \(44-4h\).

*Proof.* The established root-density classification for Q7 gives \(|E_B|\in\{0,2,4,6,8,10,12,16\}\). Call \(B\) heavy when \(|E_B|\ge10\). The previously proved four-heavy physical-face obstruction says there are at most three heavy supports in any one legal coloring. Every light support contributes at most eight bad roots, and every heavy support contributes at most sixteen. Hence
\[
 \sum_{x\in Q_7}b(x)=\sum_{B\in\binom{[7]}5}|E_B|
 \le 16h+8(21-h)=168+8h\le192.
\]
If \(T\) is the set of roots with \(b(x)\ge2\), then \(2|T|\le\sum_x b(x)\). Therefore
\[
 |\{x:b(x)\le1\}|
 \ge128-\left\lfloor(168+8h)/2\right\rfloor
 =44-4h\ge32.
\]
Every root with \(b(x)\le1\) supports genuine one-change five-paths on all the remaining at least twenty five-supports, by the definition of \(E_B\). \(\square\)

**Important scope:** The supports on which each chosen root succeeds depend on the coloring and may vary from root to root. This is stronger in *number of simultaneous supports at some root* than the fourteen-*arbitrarily prescribed*-supports theorem, but it does not imply good paths on any prescribed twenty-support family. More importantly, the repository's explicit legal Q7 coloring with *every proper support good at one root* and *all full paths at that root bad* shows that even \(b(x)=0\) does not supply the missing full-path terminal-memory and seam compatibility. Accordingly the grand closure obligation is a same-root two-tail extraction or a root-changing full-path exchange, not a larger support-coverage estimate.

**Even-dimensional obstruction to transferring the matching method.** For any even \(n\ge8\) and any fixed seven-coordinate set \(U\subset[n]\), consider
\[
 c(F,\pi)=\sum_{j\notin \operatorname{free}(F)}b_j(F)\pmod2.
\]
Because \(n-3\) is odd, complementing the physical face reverses this color, so it is a globally valid NORI coloring (independent of \(\pi\)). At any root \(x\) whose bits in \(U\) are all zero, let \(B\subset U\) have size five. Every five-step \(B\)-path from \(x\) has three window colors
\[
  (\epsilon,\;1+\epsilon,\;\epsilon),
 \qquad \epsilon=\sum_{j\notin U}x_j\pmod2,
\]
since each successive window replaces one as-yet-zero free coordinate with a previously traversed coordinate fixed to one. Consequently **all 21 five-supports inside \(U\) are bad at that single root**, unlike the matching-two theorem special to full \(Q_7\). This is a genuine dimensional-lifting obstruction arising from the additional exterior bits. The same coloring still has globally good full paths: for any fixed full direction order \(p\), choose the starting bits with \(x_{p_{i+3}}=1-x_{p_i}\) for each \(i=1,\dots,n-3\); the exterior Hamming weight is then constant from window to window, so the full word is monochromatic.
