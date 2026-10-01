# A global size gap forces a non-Hamiltonian complement of order at most twice the minimum side

## Statement

Let H be a minimum counterexample and let P|Q|X be a spanning three-cover minimizing Phi among all spanning three-covers, with p=|P|>=q=|Q|>=c=|X|. Assume the endpoint-square alternative of twosourceblockade_recomp01 does not occur and p>=q+2. Then q=c and p is either c+2 or c+3. Moreover the maximin parameter rho of H equals c, and H contains a tight path A whose complement is non-Hamiltonian of order at most 2c.

## Body

# Proof

Because the endpoint-square alternative of twosourceblockade_recomp01 is excluded, its near-balance conclusion gives

(p-c)+(q-c)<=3.

Write d=p-q>=2 and e=q-c>=0. Then

(p-c)+(q-c)=d+2e<=3.

Hence e=0 and d is either 2 or 3. Therefore q=c and p is c+2 or c+3.

Let rho be the maximum possible minimum component order among spanning three-covers of H. Since the displayed cover has minimum component order c, rho>=c.

If p=c+2, then n=3c+2. A three-cover with minimum component order at least c+1 would have total order at least 3c+3>n, impossible. Hence rho=c.

If p=c+3, then n=3c+3. If rho>=c+1, some spanning three-cover has all three component orders at least c+1. Their sum is exactly 3c+3, so all three orders equal c+1. Its quadratic potential is

3(c+1)^2=3c^2+6c+3,

whereas the displayed profile (c+3,c,c) has potential

(c+3)^2+2c^2=3c^2+6c+9.

This contradicts global Phi-minimality. Thus rho=c also in this case.

Apply the certified sharp maximin theorem in maximin01 with rho=c. If H already has a tight path whose complement is non-Hamiltonian of order at most 2c, we are done. Otherwise the sharp residue supplies a maximin-lex three-cover of orders a,c+1,c with n=a+2c+1.

For n=3c+2 this forces a=c+1, hence profile (c+1,c+1,c), whose potential is

2(c+1)^2+c^2=3c^2+4c+2,

strictly below the displayed (c+2,c,c) potential 3c^2+4c+4.

For n=3c+3 it forces a=c+2, hence profile (c+2,c+1,c), whose potential is

(c+2)^2+(c+1)^2+c^2=3c^2+6c+5,

strictly below the displayed (c+3,c,c) potential 3c^2+6c+9.

Both contradict global Phi-minimality. Therefore the sharp maximin residue is impossible, and H must contain a tight path with non-Hamiltonian complement of order at most 2c. ∎
