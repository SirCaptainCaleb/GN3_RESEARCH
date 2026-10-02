# Quadratic-minimal trapped covers have no 1- or 2-side and a 3-side only through order thirteen

## Statement

Let H be a minimum counterexample and let A|B|C be a Phi-minimal spanning three-cover in a connected Astra-003 component containing no two-cover, with a=|A|>=b=|B|>=c=|C|. Then c>=3. Moreover, if c=3 then a<=5, and hence |V(H)|<=13. Thus for |V(H)|>=14 every Phi-minimal trapped three-cover has all three component orders at least four.

## Body

# Small sides at a quadratic minimum

Let H be a minimum counterexample, and let A|B|C minimize Phi in a trapped Astra-003 connected component. Write a>=b>=c for the component orders. The minimum-counterexample calculus gives |V(H)|>10.

## Sides of order one or two

If c=1, then a+b=n-1>=10, so a>=5. The set consisting of C and either endpoint of A has order two and is Hamiltonian. Since a>=c+2, the endpoint-transfer lemma gives a strict Phi-decrease, contradiction.

If c=2, then a+b=n-2>=9, so a>=5. The set consisting of C and either endpoint of A has order three and is Hamiltonian. Again the endpoint-transfer lemma gives a strict Phi-decrease. Hence c>=3.

## A side of order three

Assume c=3. Suppose for contradiction that a>=6, and write

A=(a_0,...,a_{a-1}).

Because a>=c+2, Phi-minimality and the endpoint-transfer lemma imply that both four-sets

V(C) union {a_0},   V(C) union {a_{a-1}}

are non-Hamiltonian.

Consider the five-set

S=V(C) union {a_0,a_{a-1}}.

If H[S] were non-Hamiltonian, the certified five-set structure theorem would allow at most one non-Hamiltonian four-vertex subset of S. But the two displayed four-sets are distinct and both non-Hamiltonian. Therefore H[S] is Hamiltonian.

Let L be a Hamilton path on S. Removing the two endpoints of A leaves the tight path

A^circ=(a_1,...,a_{a-2})

of order a-2. Hence L|A^circ is an exact two-path cover of V(A) union V(C), so replacing A|C by L|A^circ is one legal Astra-003 move. The old squared-size contribution is

a^2+3^2,

while the new contribution is

5^2+(a-2)^2.

The decrease is

a^2+9-[25+(a-2)^2]=4a-20>0

for a>=6, contradicting Phi-minimality.

Thus a<=5 whenever c=3. Since b<=a,

n=a+b+3<=5+5+3=13.

Consequently, if n>=14, every Phi-minimal trapped three-cover has minimum component order at least four.