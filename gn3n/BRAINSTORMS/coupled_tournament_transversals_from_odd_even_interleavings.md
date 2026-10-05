# Coupled tournament transversals from odd-even interleavings

Reformulate an arbitrary boundary 3-tournament H using its local tournaments T_b on V-{b}, where a->c in T_b iff (a,b,c) is tight. Split a spanning order into odd-position and even-position subsequences. The status word is then exactly two interleaved transversal-path conditions in these local tournaments. Pursue Hamilton-transversal, temporal-tournament, and global exchange arguments directly on this coupled system, with no minimum-counterexample hypothesis.

CORRECTIONS AND VARIABLE-PAIRING FRONTIER.

The fixed-balanced-partition pair-state targets are too strong. Computational stress tests at r=5 produced self-indexed tournament systems for which every perfect matching M in a prescribed A x B has alpha(D[M])>=3; even the weaker demand that some fixed-partition M have directed path-cover number at most two can fail. Thus the bipartition must remain variable.

VARIABLE ORDERED-PAIRING MODEL. On an even vertex set, choose an ordered perfect pairing into states (u,v). For two states (u,v),(x,y), put an arc
  (u,v)->(x,y)
iff (u,v,x) and (v,x,y) are tight. A directed path of states is exactly the concatenated tight path u,v,x,y,... . Hence an ordered perfect pairing whose state digraph has path-cover number at most two yields a spanning two-cover. The matching/pairing is part of the variable state and may be changed by local four-vertex exchanges.

PARITY ISSUE. An existing two-cover whose two path orders are both even is represented directly by consecutive ordered pairs. If both path orders are odd, pair each internally leaves one unpaired endpoint from each component. Simple endpoint transfer resolves the parity unless the two junction statuses in the concatenation P,Q^rev are exactly 01. Thus 01 is the unique elementary parity residue.

FOUR-VERTEX NON-HAMILTONIAN EXTENSION LEMMA. Let a,b,c be three vertices. Once the three independent boundary-tournament choices on {a,b,c} are fixed, there is at most one extension to a fourth vertex x for which {a,b,c,x} is non-Hamiltonian. In sign-cochain notation let
  A=tau_a(b,c), B=tau_b(a,c), C=tau_c(a,b).
For a non-Hamiltonian extension x the nine new signs are forced:
  tau_a(b,x)=B, tau_a(c,x)=C,
  tau_b(a,x)=A, tau_b(c,x)=-C,
  tau_c(a,x)=-A, tau_c(b,x)=-B,
  tau_x(a,b)=-C, tau_x(a,c)=-B, tau_x(b,c)=-A.
There are eight possible base signatures (A,B,C), and these formulas give the eight non-Hamiltonian boundary tournaments on four labeled vertices. This is a short complete K4 classification; six of the eight are edge-orderable matching-block K4s and two form a complementary non-edge-orderable pair.

3+3 PARITY NORMALIZATION. Let P=(a,b,c) and Q=(x,y,z) be disjoint tight 3-paths. Then some four-subset of their six vertices is Hamiltonian, hence P union Q has a two-cover of size profile 4+2.

Proof: suppose for contradiction that every four-subset is non-Hamiltonian. In particular {a,b,c,x} and {a,b,c,y} are non-Hamiltonian extensions of the same triple, so by the extension lemma x and y have identical forced interaction with a,b,c.

Because (a,b,c) is tight, B=+1. If A=-1, the path
  x,b,a,y
is tight: both triples x,b,a and b,a,y are forced tight by the table. If A=+1 and C=-1, then both x,b? More directly, both (a,x,b) and (a,y,b) are tight, and exactly one of (x,b,y),(y,b,x) is tight by boundary reversal, so one of
  a,x,b,y
  a,y,b,x
is a tight Hamilton path on {a,b,x,y}. If A=+1 and C=+1, both (b,x,a) and (b,y,a) are tight, and exactly one of (x,a,y),(y,a,x) is tight, so one of
  b,x,a,y
  b,y,a,x
is tight. In every case a Hamiltonian four-subset exists, contradiction.

Thus the first nontrivial odd/odd parity case always normalizes globally, even though all simple endpoint transfers may fail.

This suggests but does not yet prove a general parity-normalization theorem: every two-cover on an even vertex set may admit another two-cover with both path orders even. The K4 extension lemma gives a new structural tool for attacking the 01 residue without minimum-counterexample analysis.

AUXILIARY PAIR STATE. In H+ with auxiliary rho, if rho is placed as the second coordinate of state (a,rho), that state is an absolute sink in the pair-state digraph. Any old state (x,b) points to (a,rho) iff (x,b,a) is tight; the second transition is automatic. This may normalize the variable-pairing problem even if full parity normalization is unnecessary.
