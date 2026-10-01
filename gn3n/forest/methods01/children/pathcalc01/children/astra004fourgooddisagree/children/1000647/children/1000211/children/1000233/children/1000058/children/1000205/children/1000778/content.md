# A short omitted-label cross is a displayed-edge reversal or an exact omission replacement

## Statement

Let H be a minimum counterexample and H-x=P|Q an exact deletion two-cover, with P=(p_0,...,p_{m-1}). Suppose 1<=j<k<=m-2, 1<=k-j<=3, and (p_j,x,p_k) is tight. Then at least one of the following holds:

(1) a tight triple reverses one of the displayed neighboring edges (p_{j-1},p_j) or (p_k,p_{k+1}) of P;

(2) k=j+2 and H-p_{j+1} has the exact deletion two-cover P'|Q, where
P'=(p_0,...,p_j,x,p_{j+2},...,p_{m-1});
equivalently the omitted label x makes a neutral one-for-one internal replacement of p_{j+1};

(3) k=j+3 and H-{p_{j+1},p_{j+2}} has the exact two-cover P'|Q, where
P'=(p_0,...,p_j,x,p_{j+3},...,p_{m-1}).
Consequently H has the legal spanning three-cover
P' | Q | (p_{j+1},p_{j+2})
with component orders |P|-1, |Q|, 2.

For k=j+1 only outcome (1) is possible.

## Body

Set
L=(p_{j-1},p_j,x),  R=(x,p_k,p_{k+1}).
The middle triple (p_j,x,p_k) is tight by hypothesis.

If L is non-tight, boundary reversal antisymmetry gives
(x,p_j,p_{j-1})
tight, reversing the displayed edge (p_{j-1},p_j). If R is non-tight, antisymmetry gives
(p_{k+1},p_k,x)
tight, reversing (p_k,p_{k+1}). Thus outcome (1) holds unless both L and R are tight. Assume henceforth both are tight.

If k=j+1, the three triples L, (p_j,x,p_{j+1}), R are exactly the new triples required to insert x between p_j and p_{j+1} in the full displayed order P. This would make P+x Hamiltonian, and together with Q would give a spanning two-cover of H, impossible. Hence this case cannot have both boundary triples tight, proving the final assertion.

If k=j+2, replace the local segment
p_j,p_{j+1},p_{j+2}
of P by
p_j,x,p_{j+2}.
The only new triples are precisely L, (p_j,x,p_{j+2}), and R, all tight. Hence
P'=(p_0,...,p_j,x,p_{j+2},...,p_{m-1})
is a Hamilton tight path on (V(P)-{p_{j+1}}) union {x}. Together with Q it covers H-p_{j+1}. This deletion subtournament cannot be Hamiltonian, or a Hamilton path on H-p_{j+1} together with singleton p_{j+1} would two-cover H. Therefore P'|Q is an exact deletion two-cover, giving (2).

If k=j+3, the identical splice replaces
p_j,p_{j+1},p_{j+2},p_{j+3}
by
p_j,x,p_{j+3},
so P' is tight on (V(P)-{p_{j+1},p_{j+2}}) union {x}. Thus P'|Q is a two-cover of H-{p_{j+1},p_{j+2}}. The two-vertex deletion cannot be Hamiltonian, since a Hamilton path on its complement together with the tight two-vertex path (p_{j+1},p_{j+2}) would two-cover H. Hence the displayed two-cover is exact. Restoring the deleted consecutive pair as its own tight path gives the stated spanning three-cover. This is (3).