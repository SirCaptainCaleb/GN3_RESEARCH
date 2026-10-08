# The symmetric p equals q equals 2 endpoint residue closes explicitly — preserved pre-item development

## Composition

(none yet)

## Development


Assume the minimum-counterexample endpoint normal form in the coboundary-flat ternary sector has p=q=2.

Then the deletion carrier

O=(v_1,v_2,v_3,v_4,v_5,v_6)

has word

0011,

and the omitted vertex x is a perfect insertion blocker with scan

alpha(x,v_i,v_{i+1}) = 11100

for i=1,...,5.

By the perfect-blocker endpoint theorem, the tetrahedron

{x,v_1,v_2,v_3}

is fully curved. In particular, since

alpha(x,v_1,v_2)=1
and
alpha(v_1,v_2,v_3)=0,

full curvature gives

alpha(x,v_1,v_3)=0.

Now consider the full coordinate order

(v_2,v_1,x,v_3,v_4,v_5,v_6).

Its five ternary statuses are:

1. alpha(v_2,v_1,x)=0, because alpha(x,v_1,v_2)=1 and the first triple is its reversal;

2. alpha(v_1,x,v_3)=1, because alpha(x,v_1,v_3)=0 and swapping the first two entries complements the alternating orientation;

3. alpha(x,v_3,v_4)=1, from the third entry of the blocker scan 11100;

4. alpha(v_3,v_4,v_5)=1, from the third status of the deletion word 0011;

5. alpha(v_4,v_5,v_6)=1, from the fourth status of the deletion word.

Thus the full word is

0,1,1,1,1,

which has exactly one change. This contradicts counterexamplehood.

Therefore the exact symmetric residue p=q=2 cannot occur.

Combined with reversal of the deletion order, every minimum flat-sector counterexample may henceforth be oriented so q>=3, and therefore the canonical flat-corner repair always creates the double-full singleton packet of the previous theorem.
