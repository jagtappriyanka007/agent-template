cpdef double score_sum(double[:] values):
    cdef Py_ssize_t i
    cdef double total = 0
    for i in range(values.shape[0]):
        total += values[i]
    return total
