# Circuit for exact phase-gate retrieval

The storage circuit prepares a product of equal-size blocks, then applies one unknown phase gate to each probe qubit in parallel. After the erasure flags arrive, the retrieval circuit selects intact blocks and applies the requested phase to data that may be entangled with a reference. The known gate set consists of $`X`$, CNOT, Toffoli and single-qubit rotations with specified real angles. This gate set gives an exact circuit model.

## Prepare and select the blocks

For a block of $`L`$ probes, prepare the uniform superposition of strings $`1^j0^{L-j}`$ for $`0\leq j\leq L`$. Start with all qubits in $`0`$. Rotate qubit $`i`$ conditioned on qubit $`i-1`$ being $`1`$, with no control for $`i=1`$. The rotation sends $`0`$ to $`0`$ with probability $`1/(L-i+2)`$ and to $`1`$ with the complementary probability. Once a branch has a zero, the later qubits in that branch stay zero. Each possible stopping position has probability $`1/(L+1)`$, including the branch with all ones. The block uses one unconditional rotation and $`L-1`$ controlled rotations. Querying the phase gate writes $`e^{ij\phi}`$ into the amplitude of the string of weight $`j`$.

Use the flags to select $`R`$ intact blocks. Because the initial state is a product across blocks, erasure of another block leaves the selected blocks in a pure product state. There are $`T=RL`$ phase-exposed qubits in the selected blocks.

## Compress the block charges

Convert each unary string to a label $`j`$ using reversible gates. In order $`i=1,\ldots,L-1`$, apply CNOT with qubit $`i+1`$ as control and qubit $`i`$ as target. At step $`i`$ both original bits in that step are available. The resulting bits encode $`x_i\oplus x_{i+1}`$, with $`x_{L+1}=0`$. They contain a single $`1`$ at position $`j`$ for a nonzero label and all zeros for label $`0`$. XOR the binary index into a fresh register and clear the original bits with equality controls on that register. This costs $`O(L\log(L+1))`$ gates per block.

Compute the total charge $`M=\sum_i j_i`$ into a fresh register. Let $`C_r(s)`$ count ordered tuples of $`r`$ labels in $`0,\ldots,L`$ with total $`s`$, with $`C_0(0)=1`$ and $`C_0(s)=0`$ otherwise.

```math
C_r(s)=\sum_{j=0}^{L}C_{r-1}(s-j).
```

For each total $`M`$, a controlled unitary prepares the uniform superposition of its label tuples. Start a work register with remainder $`s=M`$. With $`r`$ labels left and $`C_r(s)>0`$, prepare the next label $`j`$ with real nonnegative amplitude $`\sqrt{C_{r-1}(s-j)/C_r(s)}`$, then subtract $`j`$ from the remainder. The amplitudes telescope and the remainder returns to zero. The inverse of this circuit, controlled by $`M`$, erases the individual labels coherently and leaves the charge state

```math
\sum_{M=0}^{T}\sqrt{\frac{C_R(M)}{(L+1)^R}} e^{iM\phi}|M\rangle.
```

The table can be computed in $`O(R^2L)`$ classical integer additions and subtractions using a sliding sum. Each entry has at most $`1+R\log_2(L+1)`$ bits. A binary tree uses at most $`L`$ rotations for each controlled label preparation. There are at most $`rL+1`$ possible remainders at step $`r`$, giving $`O(T^2)`$ rotations. The equality and prefix controls contribute $`O(\log(T+1))`$ gates per rotation using reusable work qubits.

## Apply and herald the gate

For a requested batch of $`k\geq1`$ phase gates, reversibly compute the data Hamming weight $`s`$ and replace program charge $`M`$ with $`m=M-s`$. A modular register of width sufficient to represent $`T+k+1`$ distinct values separates negative differences from the accepted range. If $`0\leq m\leq T-k`$, rotate a flag from $`0`$ with amplitude on $`1`$ given by

```math
\sqrt{\frac{\min\{C_R(m),C_R(m+k)\}}{C_R(m+s)}}.
```

Otherwise leave the flag at $`0`$. If $`k>T`$, this decoder always rejects. The count profile is symmetric and unimodal since discrete uniform sequences are symmetric and unimodal and convolution preserves that property. Therefore the numerator is the smallest count in the window $`m,\ldots,m+k`$ and the rotation is well defined. Uncompute the weight and measure the flag and $`m`$. On success the amplitude for data weight $`s`$ includes $`e^{i(m+s)\phi}`$, multiplied by a factor independent of $`s`$. For a given $`m`$, the factor $`e^{im\phi}`$ is global. The data channel is $`U_\phi^{\otimes k}`$, including when the data are entangled with a reference. The success probability is

```math
p=\frac{1}{(L+1)^R}\sum_{m=0}^{T-k}\min\{C_R(m),C_R(m+k)\}.
```

The same steps apply to a target with a known integer charge spectrum in $`0,\ldots,k`$ containing both endpoints, if its charge can be computed and uncomputed coherently. For that target, count the cost of its charge computation in place of the Hamming-weight computation.

The flag stage uses $`O(Tk)`$ parameter rotations for $`1\leq k\leq T`$. Using classical flag-dependent parameters, the full preparation and retrieval cost for a $`k`$-qubit batch is $`O(N^2\log(N+1))`$ known elementary gates and $`O(N+k)`$ live qubits, with one parallel layer of $`N`$ unknown-gate calls. A finite discrete gate set generally requires angle approximation, which can change the accepted channel.

## Success when the batch grows with the number of probes

For identical intact blocks, the failure probability equals the mass of the $`k`$ most central total-charge levels, or one if $`k>T`$. This follows by comparing the symmetric unimodal count profile with its shift by $`k`$. Let $`\sigma_R^2=RL(L+2)/12`$ be the total-charge variance and let $`\Phi`$ be the standard normal distribution function. The standardized third absolute moment of a discrete uniform variable on $`0,\ldots,L`$ is bounded independently of $`L\geq1`$. Berry–Esseen and the integer endpoints of the central interval give

```math
p=2\Phi\left(-\frac{k}{2\sigma_R}\right)+O(R^{-1/2}).
```

The error bound is uniform in $`L\geq1`$ and $`k`$. In particular, when $`t\to\infty`$ and $`t/N\to0`$, use $`2t`$ blocks of size $`L=\lfloor N/(2t)\rfloor`$ and keep exactly $`R=t`$ intact blocks. If $`k\sqrt{t}/N\to a`$, this circuit’s worst-pattern success probability converges to $`2\Phi(-2\sqrt{3}\,a)`$.
