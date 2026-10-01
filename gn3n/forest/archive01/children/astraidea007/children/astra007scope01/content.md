# Astra-007 needs an independent route to the fractional threshold two

## Statement

Let H be a minimum counterexample. The certified fractional bounds give tau*(H)<3. If Astra-007 is assumed true for H, then any surviving counterexample must also satisfy tau*(H)>2, because tau*(H)<=2 would imply pc(H)<=ceil(tau*(H))<=2. Hence the only surviving range under Astra-007 is 2<tau*(H)<3, where the rounding inequality yields only pc(H)<=3, already known. In the sharp half-order shell tau*(H)=2+1/lambda exactly, so Astra-007 alone is inert there. Thus a proof of the grand theorem through Astra-007 still needs an independent mechanism forcing tau*(H)<=2 or other integral structure that bypasses this ceiling.

## Body

# Proof

Let H be a minimum counterexample. By minimum-counterexample calculus,

pc(H)=3.

The certified concentrated deletion-averaging bound gives

tau*(H) <= 2+1/lambda < 3,

where lambda is the maximum tight-path order and lambda>=2.

Now assume Astra-007 holds for H. If tau*(H)<=2, then

pc(H) <= ceil(tau*(H)) <= 2,

contradicting that H is a counterexample. Therefore any minimum counterexample surviving under the additional assumption of Astra-007 must satisfy

2 < tau*(H) < 3.

Throughout this interval,

ceil(tau*(H))=3,

so Astra-007 says only

pc(H)<=3,

which is already known with equality.

The sharp half-order shell makes this limitation exact. By fractionalsharpshell01, if n=2lambda+1 then

tau*(H)=2+1/lambda>2.

Hence Astra-007 gives pc(H)<=3 and no more.

Consequently Astra-007 is an auxiliary rounding bridge, not an independent closure route from the currently certified fractional bounds. To prove the grand theorem through it one first needs a separate theorem forcing tau*(H)<=2, such as a weighted-half statement equivalent by LP duality to the absence of a dual fractional obstruction, or some additional integral structure that closes the sharp shell by another mechanism.