
import numpy as np

# Stack
# Take a list of array and create a new one with all of them stack together. The new 
# array will have one more dimension then the individual ones
arrays = [np.random.randn(3, 4) for _ in range(10)]
print(f"stack function: {np.stack(arrays, axis=0).shape}")


