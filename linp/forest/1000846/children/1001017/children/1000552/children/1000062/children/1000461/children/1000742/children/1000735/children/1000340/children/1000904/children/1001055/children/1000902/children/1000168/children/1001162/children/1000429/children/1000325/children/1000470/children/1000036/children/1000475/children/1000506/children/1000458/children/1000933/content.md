# A low-defect global-top center has either quadratic omitted-source mass or a linear top-lens packet

## Statement

Let v be an active misaligned global-top center with phi(v)=L, local defect eta_v, and use the switching family/interior-cell notation of 666bd06ca682. Put R_v=L/8-eta_v-O(1), with the same absolute boundary loss as in that theorem. Then at least one of the following holds: (U) there are k>=R_v/2 terminal-retained interior switchers, with distinct omitted entrances x_1,...,x_k satisfying sum_i phi(x_i)>=Lk/2+k(k+1)/8; or (Y) there are Y>=R_v/4 distinct paid/nonflat output cells whose private host vertices are distinct, have potential L, and each supports a clean balanced elementary endpoint lens on the common host maximum path. In particular, if eta_v=o(L), then either k>=(1/16-o(1))L and the omitted entrance-potential mass is at least (65/2048-o(1))L^2, or Y>=(1/32-o(1))L distinct top-potential balanced-lens attachments occur on one host.

## Body

By 666bd06ca682, U+2Y>=R_v, where U is the number of terminal-retained interior switchers and Y is the number of occupied nonflat cells. If U>=R_v/2, apply c48823eea604 to the U terminal-retained switchers on the same maximum L-edge host path. Their omitted entrances are distinct and, writing k=U, satisfy sum_i phi(x_i)>=Lk/2+k(k+1)/8. This is branch (U). Otherwise U<R_v/2, so 2Y>R_v/2 and hence Y>R_v/4. By 91f6c32ab805 those Y cells give Y distinct private host vertices of potential L, each carrying a clean balanced elementary endpoint lens against a maximum path at that private vertex. This is branch (Y). If eta_v=o(L), then R_v=(1/8-o(1))L. In branch (U), k>=(1/16-o(1))L, and substitution into Lk/2+k(k+1)/8 gives [(1/32)+(1/2048)-o(1)]L^2=(65/2048-o(1))L^2. In branch (Y), Y>=(1/32-o(1))L.
