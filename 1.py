import numpy as np
import json

matrix = np.load('./input/matrix_11.npy')

total_sum = int(np.sum(matrix))
total_avg = float(np.mean(matrix))
main_diag_sum = int(np.trace(matrix))
main_diag_avg = float(np.mean(np.diagonal(matrix)))
side_diag_sum = int(np.trace(np.fliplr(matrix)))
side_diag_avg = float(np.mean(np.fliplr(matrix).diagonal()))
max_value = int(np.max(matrix))
min_value = int(np.min(matrix))

normalized_matrix = matrix/total_sum

np.save('./output/1_normal_matrix.npy', normalized_matrix)

result_dict = {
    "sum": total_sum,
    "avr": total_avg,
    "sumMD": main_diag_sum,
    "avrMD": main_diag_avg,
    "sumSD": side_diag_sum,
    "avrSD": side_diag_avg,
    "max": max_value,
    "min": min_value
}

with open('./output/1_result.json', 'w') as json_file:
    json.dump(result_dict, json_file, indent=4)
