# Science of phase-gate storage under erasure

An intact probe program carries the unknown gate in the relative phase between its excitation sectors. A loss flag identifies physical sites; it does not reveal which excitation was lost. The construction avoids this missing information by using only intact blocks. The converse treats the lost bits as a classical record that narrows how widely charge can be distributed in a conditional survivor state.

| Step | Result |
| --- | --- |
| Define the timing, controls and exact output | [Operational model](model.md) |
| Use a pure program as a gate | [Charge-window receiver and optimality](proof.md) |
| Compare a block design with all encodings | [Achievability, sampling converse and finite separation](proof.md) |
| Compile the receiver with known gates | [Circuit and resources](implementation.md) |
| Relate exact storage to estimation, replication and recovery | [Related work](../references/RELATED_WORK.md) |
| Compare exact retrieval with identification after loss | [Flagged marked-address search](flagged-search.md) |

The same analytical bounds cover sparse, extensive and nearly complete loss. Exact success is possible when at least as many probes survive as there are output gates; success can still be small in that regime. The [ten-query example](../learning/WORKED_EXAMPLE.md) shows the receiver label and the cancellation of its global phase. The [verification route](../verification/README.md) checks finite algebra and numerical examples.
