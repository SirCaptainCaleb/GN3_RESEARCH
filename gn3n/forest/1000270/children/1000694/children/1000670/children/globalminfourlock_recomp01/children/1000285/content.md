# Four-side endpoint five-sets force quantitatively more imbalanced complement covers

## Statement

Let H be a minimum counterexample and let X|P|Q be a spanning three-cover minimizing Phi=sum |C_i|^2 among all spanning three-covers of H. Write X=(x_0,x_1,x_2,x_3), |P|=m, |Q|=r, with m,r>=6. Let e be either endpoint of P and f either endpoint of Q. Then each of
F_0={x_0,x_1,x_2,e,f}
and
F_3={x_1,x_2,x_3,e,f}
is Hamiltonian. For i in {0,3}, every two-cover U|V of H-F_i, with u=|U|, v=|V|, satisfies
|u-v|^2 >= |m-r|^2 + 2(m+r)-19.
In particular every such complement two-cover is strictly more imbalanced than the original pair P|Q.

## Body

Global Phi-minimality implies that X union {e} and X union {f} are non-Hamiltonian: if, say, X union {e} were Hamiltonian, replacing X|P by a Hamilton path on X union {e} and the inherited path P-e would change component orders 4,m to 5,m-1 and decrease Phi by 2m-10>0. The same holds for f.

Apply the certified repeated-bad-extension theorem in localextend01 to the displayed Hamilton four-path X and exterior vertices e,f. Since both one-vertex extensions are non-Hamiltonian, the crossed five-sets F_0 and F_3 are Hamiltonian.

Fix i in {0,3} and put K=H-F_i. Because H is a minimum counterexample, K has path-cover number at most two. It cannot be Hamiltonian, since a Hamilton path of K together with a Hamilton path of F_i would give a spanning two-cover of H. Thus K has a two-cover U|V. The argument below applies to every such two-cover.

The three paths F_i|U|V form a spanning three-cover of H, so global Phi-minimality gives
16+m^2+r^2 <= 25+u^2+v^2,
hence
u^2+v^2 >= m^2+r^2-9.
Also
u+v=|K|=m+r-1.
Put d=|m-r| and delta=|u-v|. Using
2(u^2+v^2)=(u+v)^2+delta^2
and
2(m^2+r^2)=(m+r)^2+d^2,
we obtain
(m+r-1)^2+delta^2 >= (m+r)^2+d^2-18,
so
delta^2 >= d^2+2(m+r)-19.

Since m+r>=12, the right side is at least d^2+5, so delta>d. Thus every complement two-cover is strictly more imbalanced than P|Q. ∎
