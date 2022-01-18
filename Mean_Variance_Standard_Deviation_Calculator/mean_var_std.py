import numpy as np

def calculate(list):
  if len(list) < 9:
    raise ValueError('List must contain nine numbers.')
  else:
    calculations = {}

    # reshape input into 3x3 matrix
    input_matrix = np.array(list)
    input_matrix = input_matrix.reshape((3,3))
    
    #calculate the different values and save them in the dictionary
    calculations['mean'] = compute_measurements(np.mean, input_matrix)
    calculations['variance'] = compute_measurements(np.var, input_matrix)
    calculations['standard deviation'] = compute_measurements(np.std, input_matrix)
    calculations['max'] = compute_measurements(np.max, input_matrix)
    calculations['min'] = compute_measurements(np.min, input_matrix)
    calculations['sum'] = compute_measurements(np.sum, input_matrix)

    return calculations

def compute_measurements(func, matrix):
  result = []

  #calculate measurements with the given function and save them in a list
  result.append(func(matrix, axis=0).tolist())
  result.append(func(matrix, axis=1).tolist())
  result.append(func(matrix.flatten()).tolist())
  
  return result