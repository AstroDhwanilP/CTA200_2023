import numpy as np

def do_iteration(c, max_iterations = 100):
    # Initialize the arrays for the iteration count and the absolute value of z
    iterations = np.zeros_like(c, dtype=np.int32)
    abs_z = np.zeros_like(c, dtype=np.float32)

    # Iterate the equation z_{i + 1} = z_i^2 + c
    z = np.zeros_like(c)
    for i in range(max_iterations):
        z = z**2 + c

        #finding the diverged points
        diverged_points = abs(z) > 2  #(for Mandelbrot set) 

        #appending the values to the arrays for iteration count and abs(z) array
        iterations[diverged_points & (iterations == 0)] = i + 1
        
    return iterations
