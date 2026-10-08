# Audit correction: tournament representation survives but source-sink induction fails — preserved pre-item development

## Audit correction: the tournament representation is valid, but the source/sink induction is not

Section 328 contains a genuine structural representation and an invalid induction step.

### What is valid

For a coboundary-flat alternating ternary orientation alpha, the construction in §328 correctly gives a tournament switching class t with
alpha(a,b,c)=t(a,b) xor t(b,c) xor t(c,a).
Tournament switching preserves alpha.

Also, for a directed Hamiltonian path in a representative t, the alpha-status at rank i is exactly the backward distance-two chord bit t(v_{i+2},v_i).

### The induction error

The proof then makes x a sink and applies induction to the subtournament W=V\{x}. The induction hypothesis may require switching a subset T of W to obtain its directed Hamiltonian path.

Extending that switch to the full vertex set flips the x-v edge precisely for v in T. Therefore x is generally no longer a sink. Including x in the switch merely flips the complementary set of x-edges. Unless T is empty or all of W, neither extension keeps x uniformly a sink/source.

Thus the claimed simultaneous realization
- prescribed switching representative on W, and
- x uniform to all of W
is not automatic.

### Exact compatibility condition

Let P=(v_1,...,v_m) be a fixed order of W. Ask whether some switching representative makes P directed and x a sink.

Writing the switching bits as s_v, the sink conditions determine s_v relative to s_x. The directed-path condition on v_i,v_{i+1} then reduces exactly to
alpha(x,v_i,v_{i+1})=0
for every i.

Hence a simultaneous sink extension exists iff the insertion scan of x along P is the constant zero word. The source version has the same condition.

So the failed induction silently assumes precisely the monochromatic-scan condition whose absence drives the deletion/blocker theory.

### Correct reformulation retained

The tournament representation remains valuable:

The coboundary-flat ternary NOR problem is equivalent to finding, in a tournament switching class, a representative and a Hamiltonian directed path whose backward distance-two chord word has at most one change.

But switching cannot independently normalize the new vertex after choosing the smaller path. Any successful induction must control the scan of the inserted vertex, for example through the audited insertion/replacement dynamics or a reversible connector argument.

Accordingly §328 must not be cited as closure.
