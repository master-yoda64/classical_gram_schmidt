import time
from typing import List
import numpy as np

def get_orthogonal_vector(v: List[np.ndarray], q: List[np.ndarray], k: int) -> np.ndarray:
    sigma: np.ndarray = np.array([np.dot(q[j], v[k]) * q[j] for j in range(k)])
    w: np.ndarray = v[k] - np.sum(sigma, axis=0)
    return w / np.linalg.norm(w)

def gram_schmidt(vec_list : List[np.ndarray]) -> List[np.ndarray]:
    q: List[np.ndarray] = [np.empty_like(vec_list[0]) for i in range(len(vec_list))]
    for k in range(len(vec_list)):
        q[k]= get_orthogonal_vector(vec_list, q, k)
    return q

def main():
    A = np.array([
        [1, 2, 3], 
        [4, 6, 9], 
        [7, 8, 5]
    ], dtype=np.float32)

    detA = np.linalg.det(A)
    if detA < 1e-10:
        raise ValueError("Matrix is singular")
    cols_vec :List[np.ndarray] = [A[:, i] for i in range(A.shape[1])]

    start = time.time()
    q: List[np.ndarray] = gram_schmidt(cols_vec)
    end = time.time()

    print("--------------------")
    print("Time for calculation: ", end - start)
    matrix = np.column_stack(q)
    print("Matrix Q", matrix)
    print("orthogonality for q0, q1", np.dot(q[0], q[1]) < 1e-10)
    print("--------------------")

    # seed = 4
    # np.random.seed(seed)
    # B = np.random.rand(1000, 1000)
    # start = time.time()
    # q = orthogonalize(B)
    # end = time.time()
    # print("Time for calculation: ", end - start)
    # print("orthogonality for q0, q1", np.dot(q[0], q[1]))
    # print("orthogonality for q0, q2", np.dot(q[0], q[2]))
    # print("orthogonality for q1, q2", np.dot(q[1], q[2]))
    #np.savetxt("regular_1000x1000_matrix.txt", B, delimiter=",")
    

if __name__ == "__main__":
    main()
