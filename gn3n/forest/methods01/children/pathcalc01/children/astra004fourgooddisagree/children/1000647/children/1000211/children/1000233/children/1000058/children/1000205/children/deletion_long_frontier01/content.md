# Every long deletion component enters reversal, a Hamiltonian four-support, or strict quadratic descent

## Statement

Let H be a minimum counterexample and let H-x=P|Q be a deletion two-cover with P of order at least six. Then at least one of the following occurs: (1) H contains a genuine reversing tight triple; (2) H contains a proper Hamiltonian four-vertex set W such that H-W is non-Hamiltonian with path-cover number two; (3) H has a spanning three-cover admitting an explicit strict decrease of the quadratic component-size potential Phi. Thus every such deletion cover yields a reversing triple, such a Hamiltonian four-set, or strict quadratic-potential descent.

## Body

Apply deletion_long_threeway01. Its reversal alternative is outcome (1), and its strict quadratic-descent alternative is outcome (3). It remains to treat the one-label internal omission replacement. In that outcome, for some internal vertex p_{j+1} of P, the deletion H-p_{j+1} has a two-cover P'|Q in which P' is obtained from P by replacing p_{j+1} with x in the inherited order. Because p_{j+1} is internal and P' is a tight path, the consecutive triple (p_j,x,p_{j+2}) is tight. Apply ba4e4fe7757b to this span-two cross. It says W={p_j,p_{j+1},x,p_{j+2}} is Hamiltonian. W is proper because Q is nonempty and disjoint from W. If H-W were Hamiltonian, Hamilton paths on W and H-W would form a spanning two-cover of H, impossible. By minimum-counterexample calculus H-W therefore has path-cover number exactly two. Hence outcome (2) holds. These alternatives exhaust deletion_long_threeway01.
