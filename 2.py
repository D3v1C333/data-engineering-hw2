import numpy as np
import os

matrix = np.load('./input/matrix_11.npy')
condition = matrix > 511 # 500 + 11 вариант

x, y = np.where(condition)
z = matrix[condition]

np.savez('./output/2_result.npz', x=x, y=y, z=z)

np.savez_compressed('./output/2_result_compressed.npz', x=x, y=y, z=z)


print(f"Размер оригинального файла: {os.path.getsize('./output/2_result.npz')}")
print(f"Размер сжатого файла: {os.path.getsize('./output/2_result_compressed.npz')}")

