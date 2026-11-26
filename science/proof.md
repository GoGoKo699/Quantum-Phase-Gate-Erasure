# Proof and construction

## Main result

Use the [storage and retrieval model](model.md) with $`N`$ simultaneous phase queries, $`t`$ flagged probe erasures and $`k`$ delayed output uses. Let $`f^*_{N,t,k}`$ denote the infimum of worst-case failure probabilities, over the phase and erased set, for an exact accepted channel. Define

```math
D_{N,t}=1+\sqrt{\frac{N(N-t)}{t+1}}.
```

Uniformly over integers $`N\ge1`$, $`0\le t\le N`$ and $`k\ge1`$, there are absolute positive constants $`c,C`$ such that

```math
c\min\!\left\{1,\frac{k}{D_{N,t}}\right\}
\le f^*_{N,t,k}
\le C\min\!\left\{1,\frac{k}{D_{N,t}}\right\}.
```

With no erasures the exact optimum is $`f^*_{N,0,k}=\min\{1,k/(N+1)\}`$. With erasures, a strictly positive worst-case success probability is possible exactly when $`k\le N-t`$. In particular, for one output use and $`t\le N/4`$ the failure has order $`\sqrt{t+1}/N`$. The construction below uses one preparation for every erased set and takes the data as input at retrieval.

There is also a matching entanglement-depth tradeoff. Call a probe $`d`$-producible if it is a mixture of pure states, each a product over blocks of at most $`d`$ sites. Allow the receiver to know the mixture component and its partition. For $`1\le d\le N`$ replace $`D_{N,t}`$ in the two-sided bound by

```math
D_{N,t,d}=1+\sqrt{(N-t)\min\!\left\{d,\frac{N}{t+1}\right\}}.
```

Thus depth helps until it reaches order $`N/(t+1)`$. Depth one already attains the optimal order when a constant fraction of sites is lost. This statement concerns failure in the exact-channel task. An order-one failure bound leaves room for different success probabilities at large $`k`$.

## Exact retrieval from a pure program

Let the supplied program have the pure phase orbit

```math
|P_\phi\rangle=\sum_{m=0}^n e^{im\phi}|v_m\rangle,
\qquad
w_m=\langle v_m|v_m\rangle,
```

where the vectors with different indices are orthogonal. They occupy distinct excitation sectors for a probe program. Extend $`w_m`$ by zero. For a batch of $`k`$ output uses the optimal worst-phase success probability is

```math
s_k(w)=\sum_{j\in\mathbb Z}\min_{0\le \ell\le k}w_{j+\ell}.
```

**Converse.** Fix Kraus operators $`K_a`$ for the success map. Feeding the program into $`K_a`$ induces a data operator $`A_a(\phi)`$. The accepted channel has Choi rank at most one, so every $`A_a(\phi)`$ is proportional to $`U_\phi^{\otimes k}`$. Write its scalar coefficient as $`h_a(\phi)`$. For any computational data string $`b`$ of weight $`\ell`$, expanding the diagonal entry gives

```math
e^{i\ell\phi}h_a(\phi)
=\sum_m e^{im\phi}\langle b|K_a\bigl(|v_m\rangle\otimes|b\rangle\bigr).
```

The scalar is a finite Fourier polynomial. Its coefficient at index $`j`$ equals the matrix element for $`m=j+\ell`$ in every one of these equations. Since the success map is trace-nonincreasing, the sum over $`a`$ of the squared modulus of this coefficient is at most $`w_{j+\ell}`$ for every $`\ell`$. Parseval bounds the success averaged over a uniform phase by $`s_k(w)`$, which also bounds worst-phase success.

**Decoder.** Set $`a_j=\min_{0\le\ell\le k}w_{j+\ell}`$. For each $`a_j>0`$ the success Kraus operator with label $`j`$ acts on the data weight-$`\ell`$ sector by taking the program inner product against $`|v_{j+\ell}\rangle/\sqrt{w_{j+\ell}}`$ and multiplying by $`\sqrt{a_j/w_{j+\ell}}`$. It keeps the data in that sector. At fixed $`\ell`$ the program directions for distinct $`j`$ are orthogonal and each squared coefficient is at most one. Across distinct $`\ell`$ the data sectors are orthogonal. The sum of the Kraus squares is therefore bounded by the identity, and the coherent filter can be completed with a failure outcome.

With the supplied phase program, the induced data operator on outcome $`j`$ is $`\sqrt{a_j}e^{ij\phi}U_\phi^{\otimes k}`$. The sector-dependent phase thus acts on the data while the remaining phase is global. Accepting every such $`j`$ attains $`s_k(w)`$ independently of phase, and the channel identity also holds on reference-entangled data.

**No erasures.** For $`u>0`$ the set $`A_u=\{m:w_m\ge u\}`$ lies in $`\{0,\ldots,N\}`$. It contains at most $`(|A_u|-k)_+`$ complete windows of $`k+1`$ consecutive indices. To see this, count the windows within each consecutive run of $`A_u`$. For $`k\le N+1`$ this number is at most $`(1-k/(N+1))|A_u|`$. Integrating over $`u`$ bounds $`s_k(w)`$ by $`1-k/(N+1)`$. The uniform distribution over all $`N+1`$ charges attains this bound. For $`k>N`$ no full window exists. Mixed probes obey the same converse by the rank-one argument for mixtures below.

## Converse with erased probes

### Failure and charge concentration

Write $`T_kw`$ for the same charge distribution shifted up by $`k`$. The pure program formula implies

```math
1-s_k(w)\ge \mathrm{TV}(w,T_kw)
\ge \max_{j\in\mathbb Z}\sum_{r=j}^{j+k-1} w_r .
```

The first inequality uses the minimum of the endpoint weights in place of the minimum over a full window, together with $`\mathrm{TV}(p,q)=1-\sum_j\min\{p_j,q_j\}`$. The second compares the two distributions on a half-line. The difference of their masses on a half-line is exactly the mass of one $`k`$-site window. For a symmetric unimodal profile both inequalities are equalities. Every window has its smallest weight at an endpoint. The difference of the shifted profiles changes sign at most once, because the larger weight is the one closer to the common profile's original center. A half-line then realizes the total-variation distance.

If the charge distribution has standard deviation $`\sigma`$, Chebyshev's inequality puts at least $`3/4`$ of its mass in an interval of radius $`2\sigma`$ around the mean. The same statement holds for $`\sigma=0`$ because the distribution is then a point mass. This interval contains at most $`4\sigma+1`$ integers, which can be covered by at most $`1+(4\sigma+1)/k`$ windows of length $`k`$. Therefore

```math
1-s_k(w)\ge \frac{3k}{4(k+4\sigma+1)}.
```

### What the erasures reveal

It suffices to decompose the probe preparation into pure states with phase-independent probabilities. For a pure pre-query probe and a size-$`t`$ erasure set $`S`$, expand the erased subsystem in the computational basis before tracing it out. Conditional on the erased bit string $`x_S`$, the surviving program is a pure phase orbit. The phase on the erased sites contributes only a conditional global factor, and the mixture weights are phase independent. The receiver cannot assume access to this expansion label. It can be used for a converse because a positive mixture of accepted Choi matrices supported on a fixed rank-one ray has every positively weighted component supported on that ray. Each hidden component therefore separately satisfies the exact-success promise, with possibly different success probabilities. This observation also justifies conditioning on a pure preparation component.

Let $`X`$ have the computational-basis probability law of the pure probe, and let $`M`$ be its total weight. Sample $`S`$ uniformly from size-$`t`$ subsets, independently of $`X`$. The conditional survivor charge variance is

```math
\sigma(S,X_S)^2=\mathrm{Var}(M\mid S,X_S).
```

For $`1\le t\le N`$ and $`N\ge2`$, estimate $`M`$ by multiplying the weight of $`X_S`$ by $`N/t`$. At fixed full string of weight $`M`$, the count in the sample is hypergeometric. The estimate is unbiased on this sampling and has mean squared error $`M(N-M)(N-t)/(t(N-1))`$. Conditional expectation minimizes mean squared error, yielding

```math
\mathbb E_{S,X_S}\sigma^2
\le \frac{N^2(N-t)}{4t(N-1)}
\le \frac{N(N-t)}{t+1}.
```

For a $`d`$-producible preparation, condition also on the pure product-of-blocks component. The conditional surviving program is still a product over the surviving parts of the blocks. If these have lengths $`\ell_b`$, their independent charges lie in intervals of widths $`\ell_b`$. Thus every such conditional variance is at most $`\sum_b\ell_b^2/4\le d(N-t)/4`$. This also gives a bound with $`t=0`$, when the sampling estimate is unnecessary.

Average the pure-program failure bound over the erased basis expansion, the phase and the uniformly sampled erased set. Convexity of $`1/(k+4\sigma+1)`$ and $`\mathbb E\sigma\le\sqrt{\mathbb E\sigma^2}`$ show that this average failure is at least

```math
\frac{3k}{4(k+4\sqrt{V}+1)},
```

where $`V`$ is either variance upper bound, or their minimum if both apply. The worst-case failure is at least this average. This proves the stated lower orders. The single-site case $`N=1`$ with no losses is covered by the exact formula. With no surviving site all conditional programs have one charge and the failure is one.

Every conditional orbit has spectrum in $`\{0,\ldots,N-t\}`$. Consequently the pure-program formula rules out positive success for $`k>N-t`$, including isolated phases by positivity and continuity of the success functions.

## Construction that attains the order

### Store phase across a block

For a block of $`L`$ probe sites, initialize

```math
\frac{1}{\sqrt{L+1}}\sum_{m=0}^L|1^m0^{L-m}\rangle.
```

The $`L`$ simultaneous queries put phase $`e^{im\phi}`$ on its weight-$`m`$ term. Prepare $`B=\lfloor N/L\rfloor`$ identical independent blocks and put any remaining query inputs in $`|0\rangle`$. After loss, discard every block touched by an erasure. At least $`B-t`$ blocks remain intact. Conditioned on the flagged set these intact blocks still carry their original pure phase programs. Knowing the flag, apply the exact pure-program decoder jointly to their total charge.

When $`R`$ blocks survive, the weights are the law of a sum of $`R`$ independent discrete uniforms on $`\{0,\ldots,L\}`$. This law is symmetric and unimodal. A symmetric unimodal sequence can be decomposed as a mixture of uniform distributions on consecutive intervals with the same center by subtracting layers from its outermost weights. The convolution of two interval uniforms has a symmetric trapezoidal mass profile, with a triangular profile when their lengths agree. Applying that convolution to the mixture proves preservation of symmetry and unimodality. Hence the decoder fails with probability exactly the maximum mass of a window of $`k`$ consecutive charges.

### Bound that window mass

Set $`q=L+1`$. For $`R\ge1`$ the peak charge mass is at most $`C_0/(q\sqrt R)`$ for an absolute constant $`C_0`$. For $`R=1`$ this is immediate. In general the characteristic function of one block has modulus

```math
|\Phi(u)|=\left|\frac{\sin(qu/2)}{q\sin(u/2)}\right|.
```

Fourier inversion bounds each charge mass by the integral of $`|\Phi(u)|^R`$ on $`[-\pi,\pi]`$ divided by $`2\pi`$. For $`0\le u\le\pi/q`$, apply $`1-\cos x\ge2x^2/\pi^2`$ to $`u(Y-Y')`$ for independent uniform variables $`Y,Y'`$. Their difference has mean square $`(q^2-1)/6`$, giving $`1-|\Phi(u)|^2\ge(q^2-1)u^2/(3\pi^2)`$. The integral on this region is bounded by a Gaussian integral of order $`1/(q\sqrt R)`$. For $`\pi/q\le u\le\pi`$ use $`|\Phi(u)|\le \pi/(qu)`$. For $`R\ge2`$ the tail integral is at most $`\pi/[q(R-1)]`$. It follows that failure is at most $`\min\{1,C_0 k/(q\sqrt R)\}`$.

For $`t<N/4`$ and $`N\ge2`$ choose

```math
L=\min\!\left\{d,\left\lfloor\frac{N}{2(t+1)}\right\rfloor\right\},
\qquad B=\lfloor N/L\rfloor .
```

Take $`d=N`$ when depth is unrestricted. This gives $`B\ge2(t+1)`$ and $`R\ge B-t\ge B/2`$ for every loss pattern. Using $`B\ge N/(2L)`$ and $`L\ge\tfrac14\min\{d,N/(t+1)\}`$ yields $`q\sqrt R\ge\tfrac14\sqrt{N\min\{d,N/(t+1)\}}`$. The failure bound has the claimed order. In the unrestricted lossless case choose a single block of length $`N`$ to obtain the exact optimum.

For $`t\ge N/4`$ use fair one-site probes $`|+\rangle`$, each an intact block if it survives. The charge distribution is binomial on the $`N-t`$ surviving sites. Its peak has order at most $`1/\sqrt{N-t+1}`$, by the uniform convolution bound for $`q=2`$, including a single point mass when no site survives. Here $`D_{N,t,d}\le1+2\sqrt{N-t}`$, so this achieves the required order. Fair one-site probes give positive weight to all charges in $`\{0,\ldots,N-t\}`$. Used at any loss budget they prove positive success when $`k\le N-t`$.

## A finite advantage over all product probes

Take $`N=10`$, $`t=1`$ and $`k=2`$. Use two uniform five-site blocks. Whatever the flag, one block is intact. Its six charge weights are all $`1/6`$, so there are four full windows of three weights. The proven decoder succeeds with probability $`2/3`$.

In a pure product program the nine survivor charges are independent Bernoulli variables, with arbitrary, possibly different probabilities. For their sum law $`w`$ and characteristic function $`\Psi`$,

```math
\begin{aligned}
1-s_2(w)&\ge\max_m(w_m+w_{m+1})\\
&\ge\sum_m w_m(w_m+w_{m+1})\\
&=\frac{1}{2\pi}\int_{-\pi}^{\pi}|\Psi(u)|^2(1+\cos u)\,du.
\end{aligned}
```

For a Bernoulli variable with parameter $`p`$ the squared modulus of its characteristic function is $`1-4p(1-p)\sin^2(u/2)\ge\cos^2(u/2)`$. Since the integrand multiplier is nonnegative, the displayed integral is bounded below by the integral for nine fair coins. Its value is

```math
\frac{\binom{18}{9}+\binom{18}{10}}{4^9}
=\frac{46189}{131072}.
```

The best product-probe success probability is therefore at most $`84883/131072\approx0.647606`$. The mixture argument extends the bound to shared-randomness product probes and the converse already allows arbitrary collective decoding.

## Bounds on success at large batch sizes

The failure order alone leaves open the rate at which success vanishes for large batches. The [explicit block circuit](implementation.md#success-when-the-batch-grows-with-the-number-of-probes) has a Gaussian limit in a specified sparse-loss scaling. A uniform upper bound on the best success probability complements that construction.

For any real charge center $`a`$, split the sum of $`\min(w_m,w_{m+k})`$ at $`m=a-k/2`$. In the lower half bound the minimum by $`w_m`$, and in the upper half use $`w_{m+k}`$. This upper bounds $`s_k(w)`$ by the probability of lying at distance at least $`k/2`$ from $`a`$.

For each erased set and lost-bit component, center the survivor charge at $`NZ/t-Z`$, where $`Z`$ is the lost charge. Averaging the resulting tail bound is equivalent to bounding the probability of $`|M-NZ/t|\ge k/2`$ for a uniformly sampled erased subset. At fixed full string, apply Hoeffding's inequality for sampling without replacement to the erased count and separately to its complement. With $`K=N-t`$, the exponents are $`tk^2/(2N^2)`$ and $`t^2k^2/(2N^2K)`$. The larger is at least $`tk^2/(4NK)`$. The phase average and then the loss-set average upper bound the worst-case success guarantee:

```math
1-f^*_{N,t,k}\le \min\!\left\{1,\;2e^{-tk^2/(4N(N-t))}\right\}
\qquad (1\le t<N).
```

For depth $`d`$, choose the conditional mean as the center. The conditional block charges are independent and the sum of their squared interval widths is at most $`d(N-t)`$. The independent-variable version yields the additional upper bound $`2e^{-k^2/[2d(N-t)]}`$ for $`t<N`$. For $`k>N-t`$ the exact success guarantee is zero. These bounds need not give the optimal exponent or limiting success profile. [Hoeffding, Theorems 2 and 4](https://doi.org/10.1080/01621459.1963.10500830)
