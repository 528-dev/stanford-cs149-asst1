1.  Build and run `sqrt`. Report the ISPC implementation speedup for 
  single CPU core (no tasks) and when using all cores (with tasks). What 
  is the speedup due to SIMD parallelization? What is the speedup due to 
  multi-core parallelization?

- 4.85x speedup from ISPC, because of SIMD in single core
- 59.32x speedup from task ISPC, because of 64 tasks(but 32 hardware threads on my computer) and SIMD.

2.  Modify the contents of the array values to improve the relative speedup 
  of the ISPC implementations. Construct a specifc input that __maximizes speedup over the sequential version of the code__ and report the resulting speedup achieved (for both the with- and without-tasks ISPC implementations). Does your modification improve SIMD speedup?
  Does it improve multi-core speedup (i.e., the benefit of moving from ISPC without-tasks to ISPC with tasks)? Please explain why.

- `values[i] = 2.999f;`
- 6.93x speedup from ISPC and 100.93x speedup from task ISPC for two reasons below:
    - The computation time longer and relatively the scheduling overhead become shorter.
    - I set the same value to inputs array, so there is balanced workload

3.  Construct a specific input for `sqrt` that __minimizes speedup for ISPC (without-tasks) over the sequential version of the code__. Describe this input, describe why you chose it, and report the resulting relative performance of the ISPC implementations. What is the reason for the loss in efficiency? 
    __(keep in mind we are using the `--target=avx2` option for ISPC, which generates 8-wide SIMD instructions)__. 

- `values[i] = 1;` 
- 1.36x speedup from ISPC and 1.24x speedup from task ISPC because:
    - Computation time is extremely short, so schedule overhead occupy the whole execution

- `if (i % 8 == 0) values[i] = 2.999;`
  `else values[i] = 1; `
- 0.92x speedup from ISPC and 14.20 speedup from task ISPC because:
    - Without-task ISPC is almost like sequential for imbalanced workload with additional cost for vectorization.
    - With-task ISPC could preform better with a great scheduling policy.

4. **RESERVE**

