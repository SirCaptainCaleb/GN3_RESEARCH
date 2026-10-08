# Protected-carrier separator and the acyclic-carrier reduction

## Composition

(none yet)

## Development

## Protected-carrier filtration and the exact separator obligation

The existential face-poset filtration in the current composition is not, by itself, sufficient for iteration. If
[
mathcal P_r={F:F	ext{ contains at least one chamber of witness depth }ge r},
]
then a face (Finmathcal P_r) may also contain chambers with witness depth (<r). The mixed-cell classification from the finite terminal theorem was proved in a protected face, where **every** chamber avoids witness edges closer to (e_r). Thus the implication
[
F	ext{ contains both }+e_r,-e_rLongrightarrow F	ext{ contains a deeper chamber}
]
cannot simply be iterated on arbitrary vertices of (Delta(mathcal P_r)) without a stronger mixed-face theorem.

A protected filtration removes this issue.

For (rge1), let (X_r) be the invariant subcomplex of the permutahedron boundary consisting of all faces (F) such that every chamber of (F) has nearest selected witness depth at least (r). Thus
[
X_1=partial P,
qquad
X_{r+1}subseteq X_r.
]
A face (Fsubset X_r) is therefore genuinely protected from all witness edges closer to (e_r), so the finite mixed-cell analysis applies on every face of (X_r).

On the face poset of (X_r), define
[
s_r(F)=
egin{cases}
+1,&F	ext{ contains a }+e_r	ext{ chamber and no }-e_r	ext{ chamber},\
-1,&F	ext{ contains a }-e_r	ext{ chamber and no }+e_r	ext{ chamber},\
0,&	ext{otherwise}.
end{cases}
]
Along a chain there is no direct (+)/(-) conflict, so after barycentric subdivision the zero set
[
S_r=Delta{Fsubset X_r:s_r(F)=0}
]
is an invariant separator and
[
gamma(S_r)ge gamma(X_r)-1.
]

The missing point is now exactly the passage from this separator to (X_{r+1}).

For a zero face (Fin S_r), define its **outward locus**
[
D_r(F)=X_{r+1}cap F,
]
viewed as the subcomplex of (F) consisting of subfaces all of whose chambers avoid (e_r) as well as every closer witness. If (F) contains no depth-(r) chamber, then (D_r(F)=F). If (F) is mixed, the existing mixed-cell escape/terminal analysis gives at least one outward chamber unless the finite terminal branch already yields a spanning two-cover; hence (D_r(F)
eqarnothing).

A sufficient local strengthening is:

**Protected mixed-cell acyclicity lemma.** In a counterexample, for every protected zero face (Fsubset X_r), the outward locus (D_r(F)) is nonempty and contractible (acyclic would already suffice for the cohomological-index version).

Because (Gsubseteq F) implies (D_r(G)subseteq D_r(F)), the family (Fmapsto D_r(F)) is an equivariant carrier on the separator poset. The equivariant acyclic-carrier theorem then gives an equivariant map
[
S_rlongrightarrow X_{r+1}.
]
Consequently
[
gamma(X_{r+1})gegamma(S_r)gegamma(X_r)-1.
]
Starting from (gamma(X_1)=m+1) and using (d=m-2), iteration forces (X_{d+1}
eqarnothing), hence a witness-free chamber and therefore a spanning two-cover.

So the global terminalization theorem is reduced to a genuinely local statement on protected mixed cells: prove contractibility (or sufficient equivariant acyclicity) of the (e_r)-free outward locus. This is stronger than merely producing one outward chamber, but it is exactly the amount of local topology needed to make the relative-index recursion rigorous.

The finite classification suggests the proof. In nonterminal mixed cells, the determining windows decouple across face blocks; the outward locus should be a face-product separator and hence contractible. The only failures of such product separation are precisely the centered/overlapping terminal configurations already bounded by ten vertices. The next step is therefore to prove the face-product contractibility directly and then check that the bounded terminal cases either close by the finite theorem or have contractible outward locus after terminal-support surgery.
