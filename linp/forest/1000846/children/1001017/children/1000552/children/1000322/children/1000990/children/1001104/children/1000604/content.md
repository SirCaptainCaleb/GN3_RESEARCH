# Equality obstructions force a leave-degree spike in residues zero and two

## Statement

Let d=floor(2ell/3), n=6d+1+s, and U be the leave graph of an exact-density P_ell-free linear triple system. Then Delta(U)>=6d+s-4ell+4. Hence Delta(U)>=s+4 when ell=0 mod3, Delta(U)>=s when ell=1 mod3, and Delta(U)>=s+2 when ell=2 mod3. Thus residues 0 and 2 force the leave to be genuinely more irregular than its average degree s.

## Body

Let ell>=4, d=floor(2ell/3), and let H be an exact-density linear triple system with
  |E(H)|=d|V(H)|.
Write
  n=6d+1+s
and let U be its uncovered-pair leave graph. Then
  d_H(v)=(n-1-d_U(v))/2=(6d+s-d_U(v))/2.

If
  delta(H)>=2ell-1,
then by 6a4d9b21f0c3 every vertex has endpoint potential at least
  ceil((delta(H)+1)/2)>=ell,
so H contains P_ell. Therefore every P_ell-free exact-density system must have
  delta(H)<=2ell-2.

Equivalently, for some vertex v,
  (6d+s-d_U(v))/2 <= 2ell-2,
so
  d_U(v) >= 6d+s-4ell+4.
Hence
  Delta(U) >= 6d+s-4ell+4.                         (1)

Evaluate (1) by residues.

If ell=3r, d=2r:
  Delta(U)>=s+4.

If ell=3r+1, d=2r:
  Delta(U)>=s.

If ell=3r+2, d=2r+1:
  Delta(U)>=s+2.

Thus a P_ell-free equality layer forces a genuine upward spike in the leave degree in residues 0 and 2:
- ell≡0 mod3: some leave vertex has degree at least average+4;
- ell≡2 mod3: some leave vertex has degree at least average+2.

In the critical residue ell≡1 mod3, (1) only says Delta(U)>=s, which is automatic from the average and so gives no irregularity.

Combining with parity d_U(v)≡n-1 mod2 can sharpen the first impossible small-s cases. For example:
- residue 0, s=2: leave degrees are even with average 2, but P_ell-freeness requires Delta(U)>=6;
- residue 2, s=2: leave degrees are even with average 2 and require Delta(U)>=4.
These force concentrated leave defects and correspondingly low-degree vertices in H.
