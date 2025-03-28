import numpy as np
import time

def create_and_transpose_matrices(num_matrices=1000, size=100):
    """
    Create random matrices and calculate their transposes.
    
    Args:
        num_matrices (int): Number of matrices to create
        size (int): Size of each matrix (size x size)
        
    Returns:
        float: Time taken to complete the operation
    """
    start_time = time.time()
    
    # Create and transpose matrices
    for i in range(num_matrices):
        # Create a random matrix with values between 0 and 1
        matrix = np.random.rand(size, size)
        
        # Calculate the transpose
        transposed = matrix.T
        
        # Optional: Uncomment to print information about each matrix
        # if i % 100 == 0:
        #     print(f"Matrix {i}: Original shape {matrix.shape}, Transposed shape {transposed.shape}")
    
    elapsed_time = time.time() - start_time
    return elapsed_time

if __name__ == "__main__":
    # Parameters
    NUM_MATRICES = 500000
    MATRIX_SIZE = 100
    
    print(f"Creating and transposing {NUM_MATRICES} matrices of size {MATRIX_SIZE}x{MATRIX_SIZE}...")
    
    # Run the function
    elapsed_time = create_and_transpose_matrices(NUM_MATRICES, MATRIX_SIZE)
    
    print(f"Operation completed in {elapsed_time:.2f} seconds")
    
    # Optional: Calculate some statistics
    approx_memory = (NUM_MATRICES * 2 * MATRIX_SIZE * MATRIX_SIZE * 8) / (1024 ** 3)  # in GB (8 bytes per float64)
    print(f"Approximate peak memory usage: {approx_memory:.2f} GB")
    
    ops_per_matrix = 2 * MATRIX_SIZE * MATRIX_SIZE  # Creating + transposing
    total_ops = NUM_MATRICES * ops_per_matrix
    print(f"Operations per second: {total_ops / elapsed_time:.2e}")

