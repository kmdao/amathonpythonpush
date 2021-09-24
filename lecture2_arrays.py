import numpy as np

x = np.array([1, 2, 3, 4])
print(x)

hw = np.array([170, 163, 188, 150])
quiz = np.array([45, 40, 50, 36])
test = np.array([160, 195, 138, 172])

print("The homework grades are")
print(hw)
print("The quiz grades are")
print(quiz)
print("The test grades are")
print(test)

print(type(hw))  # type is 'ndarray' which is n dimensional
# check the number of dimensions variable has
print("Hw has this many dimensions")
print(hw.ndim)

# shape gives dimensions/rows/length and elements/columns so this has length of 4 and gives (4,)
print("Hw has the shape")
print(hw.shape)

# All operations are element-wise ß
