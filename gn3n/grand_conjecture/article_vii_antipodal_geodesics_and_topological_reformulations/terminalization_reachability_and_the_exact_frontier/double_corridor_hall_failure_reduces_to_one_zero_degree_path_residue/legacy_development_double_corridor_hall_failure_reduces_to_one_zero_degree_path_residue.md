# Double-corridor Hall failure reduces to one zero-degree path residue — preserved pre-item development

## Hall failure for double-corridor attachment has one genuinely new residue

Retain the notation of [[terminal_attachment_matching_gives_an_outward_repair_of_a_double_corridor]]. The terminal attachment graph is bipartite with left side ({P,Q}) and right side ({x,y}), where
[
Tsim eiff h(t_{s-1},t_s,e)=1
]
for the terminal edge of (T).

If this graph has a perfect matching, the double corridor has the outward two-cover repair already recorded there. Suppose it has no perfect matching.

For a (2	imes2) bipartite graph, Hall failure has only two forms.

### 1. Both paths attach only to the same exterior vertex

Suppose, after relabeling, both (P) and (Q) may attach to (x), while neither attaches to (y). Then
[
h(p_{s-1},p_s,y)=0,qquad h(q_{t-1},q_t,y)=0.
]
Boundary antisymmetry gives
[
h(y,p_s,p_{s-1})=1,qquad h(y,q_t,q_{t-1})=1.
]
Exactly one of
[
h(p_s,y,q_t),qquad h(q_t,y,p_s)
]
is tight. In the first case
[
(p_s,y,q_t,q_{t-1})
]
is a Hamiltonian four-path; in the second
[
(q_t,y,p_s,p_{s-1})
]
is a Hamiltonian four-path.

Thus this Hall obstruction automatically exposes a Hamiltonian four-support on the terminal endpoint data. This is the terminal-terminal form of the valid common-reverser argument and uses no minimum-counterexample hypothesis.

The four-support does not by itself complete the outward surgery, because deleting it need not leave a single Hamiltonian path. But it converts this Hall failure into a bounded endpoint-support interface.

### 2. One corridor path has no terminal attachment

The only other Hall obstruction is that one path, say (P), has degree zero:
[
h(p_{s-1},p_s,x)=h(p_{s-1},p_s,y)=0.
]
Hence
[
h(x,p_s,p_{s-1})=h(y,p_s,p_{s-1})=1.
]
In addition the reflected-double corridor classification supplies the initial reversal
[
h(p_2,p_1,x)=1
]
(up to the labeling of the two exterior vertices).

This is genuinely different from the common-reverser configuration: the same vertex (x) occurs with opposite endpoint polarities at the two ends of (P),
[
(p_2,p_1,x),qquad (x,p_s,p_{s-1}),
]
and two distinct exterior vertices reverse the same terminal edge. The valid common-reverser lemma does not identify these patterns, and the old “same-edge twins force bounded support” principle was already known to be false.

Therefore the attachment-matching route has been reduced to one exact local residue:

> **zero-degree corridor residue:** a tight path (P) whose initial edge is reversed by (x), while its terminal edge admits neither (x) nor (y) as an attachment.

Any proof that this residue can be converted either to an outward two-cover order or to a protected bounded carrier closes the local attachment dichotomy. All other terminal-attachment patterns either have a perfect matching or expose a Hamiltonian four-support immediately.

This reduction is independent of the lengths of (P,Q) except for the trivial short-path cases, which are already finite.
