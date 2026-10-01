# A one-blue mixed triangle is a paired transfer to the opposite support

## Statement

Assume the one-blue-edge mixed-triangle normal form compatmixedtri37(B), in its common-core paired-switch subbranch: F_a,F_b are support-compatible but order-incompatible, F_c is support-incompatible with each, all three induce one common core partition R|S, and a,b each switch class when F_c is compared with the blue pair. Then a and b restore into the same support class across F_a,F_b. After naming that class R, exactly one of two support patterns occurs depending on the class of c in the blue pair: either F_a=(R+{b,c})|S, F_b=(R+{a,c})|S, F_c=R|(S+{a,b}); or F_a=(R+{b})|(S+{c}), F_b=(R+{a})|(S+{c}), F_c=R|(S+{a,b}). No insertion-slot relation between a and b is implied by support compatibility alone.

## Body

# Proof

Support compatibility of F_a and F_b means that on H-{a,b} the two covers have the same two support classes.

Suppose the omitted labels a and b restored into different common support classes. Then the component of F_a containing b and the component of F_b containing a are disjoint Hamiltonian supports whose union is V(H), giving a spanning two-cover of H. Hence a and b restore into the same common support class.

Anchor the common core partition as R|S and name the restoration class R. Thus b lies with R in F_a and a lies with R in F_b.

The surviving label c has the same support class in F_a and F_b because that pair is support-compatible. There are two cases.

## Case 1: c lies with R in F_a,F_b

Then the support partitions are

F_a=(R+{b,c}) | S,
F_b=(R+{a,c}) | S.

By compatmixedtri37(B), b switches class from F_a to F_c and a switches class from F_b to F_c. Therefore in F_c both a and b lie with S. Since c is omitted there,

F_c=R | (S+{a,b}).

## Case 2: c lies with S in F_a,F_b

Then

F_a=(R+{b}) | (S+{c}),
F_b=(R+{a}) | (S+{c}).

Again both a and b switch class in F_c, so

F_c=R | (S+{a,b}).

These are the two support-level paired-transfer patterns.

The blue pair F_a,F_b is support-compatible but order-incompatible, not fully compatible. Thus the common-support insertion-slot conclusion from d43a7c9e2f61 does not apply, and no equal-or-adjacent slot claim is made.