#!/bin/bash

echo $@

python3 -c "import numpy as np;x=2048;a=np.random.rand(x,x,x);print(a.shape)"

# ^^^ allocate 8bytes per float64, 8 * ( 2048 ^ 3) = 68.7 GB