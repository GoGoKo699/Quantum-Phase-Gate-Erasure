# Two exact phase gates after one flagged erasure

There are ten probes, one call to $`U_\phi`$ per probe, and no access to the unknown gate afterward. Exactly one probe is erased and the receiver learns its position. Two data qubits arrive after the erasure. The receiver must apply $`U_\phi\otimes U_\phi`$ to both data qubits on every successful run.

## Prepare two blocks

Use two independent five-probe blocks. Within each block prepare the equal superposition of the six strings below. Each occupied probe picks up the same phase $`e^{i\phi}`$ during interrogation, so string $`m`$ carries phase $`e^{im\phi}`$. The program is coherent across all six charges.

| Charge | Probe string |
| ---: | --- |
| 0 | 00000 |
| 1 | 10000 |
| 2 | 11000 |
| 3 | 11100 |
| 4 | 11110 |
| 5 | 11111 |

After loss, discard the entire block containing the erased probe. Since the blocks were prepared independently, the other block still holds its pure, six-charge program. Every possible one-probe erasure leaves one such block. Both blocks count toward the ten-query cost.

## Retrieve the gate

Relabel the six strings by their charge $`m`$ with a fixed, reversible change of basis. The data basis states have weights $`\ell=0,1,1,2`$ in the order $`00,01,10,11`$. The decoder coherently computes $`j=m-\ell`$ and checks whether $`j`$ is one of $`0,1,2,3`$. It reveals the value of $`j`$ on success. Computing the difference coherently keeps the separate values of $`\ell`$ and $`m`$ from being revealed. The program index is uncomputed from $`j`$ and the data weight before the discarded workspace can carry data-charge information.

| Accepted label $`j`$ | Program charge for $`00`$ | Program charge for $`01`$ or $`10`$ | Program charge for $`11`$ |
| ---: | ---: | ---: | ---: |
| 0 | 0 | 1 | 2 |
| 1 | 1 | 2 | 3 |
| 2 | 2 | 3 | 4 |
| 3 | 3 | 4 | 5 |

Each accepted label has one usable program component for every data weight. All six program amplitudes have magnitude $`1/\sqrt{6}`$. For an input

```math
\lvert\Psi\rangle=\sum_{x\in\{00,01,10,11\}}\lvert x\rangle_D\lvert r_x\rangle_R,
```

the vectors $`\lvert r_x\rangle`$ can be arbitrary and can include the amplitudes of the superposition. Conditioned on label $`j`$, the unnormalized joint output is

```math
\frac{e^{ij\phi}}{\sqrt{6}}
\sum_x e^{i|x|\phi}\lvert x\rangle_D\lvert r_x\rangle_R.
```

Only the desired relative factors $`e^{i|x|\phi}`$ remain after normalization. The factor $`e^{ij\phi}`$ is global. Every accepted label has probability $`1/6`$ for a normalized input and the four labels are disjoint, so the total success probability is exactly $`2/3`$. In particular the input superposition of $`00`$ and $`11`$ acquires relative phase $`e^{2i\phi}`$, even though the success flag contains no information about the input's weight.

## Compare product probes

With the same ten queries and one erased probe, a product strategy has nine independent one-qubit charges. The individual occupation probabilities can all differ and the decoder can still act jointly on the nine survivors. For any such distribution $`w`$, the [converse](../science/proof.md) lower bounds failure by the largest mass in two consecutive charges. That maximum is at least the average $`\sum_m w_m(w_m+w_{m+1})`$. In the Fourier representation of this average, the factor contributed by a Bernoulli site of occupation probability $`a`$ is

```math
\lvert 1-a+ae^{i\theta}\rvert^2
=1-4a(1-a)\sin^2(\theta/2)
\geq \cos^2(\theta/2).
```

The weight $`1+\cos\theta`$ in the average is nonnegative. Thus the fair-coin profile gives a lower bound on the average for every choice of the nine occupation probabilities. Expanding that fair-coin integral gives the product-probe success bound

```math
p_{\mathrm{prod}}\leq
1-\frac{\binom{18}{9}+\binom{18}{10}}{4^9}
=\frac{84883}{131072}
\approx 0.64760590.
```

The same bound holds if the strategy randomly chooses its product preparation and tells the decoder which one it chose. The entangled protocol's success is $`2/3`$ on every erasure pattern. These finite numbers give an advantage at fixed query budget for an exact joint task. See the [verification](../verification/README.md) and the [implementation](../science/implementation.md) for the finite checks and full receiver.
