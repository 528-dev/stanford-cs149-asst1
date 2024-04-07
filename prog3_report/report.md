# assignment 1
## program 3
### Part 1
1.  Compile and run the program mandelbrot ispc. __The ISPC compiler is currently configured to emit 8-wide AVX2 vector instructions.__  What is the maximum
  speedup you expect given what you know about these CPUs?
  Why might the number you observe be less than this ideal? (Hint:
  Consider the characteristics of the computation you are performing?
  Describe the parts of the image that present challenges for SIMD
  execution? Comparing the performance of rendering the different views
  of the Mandelbrot set may help confirm your hypothesis.).  

- run the excutable file `mandelbrot_ispc`:
> ljh@ljh-virtual-machine:~/asst1/prog3_mandelbrot_ispc$ ./mandelbrot_ispc   
[mandelbrot serial]:            [123.848] ms  
Wrote image file mandelbrot-serial.ppm  
[mandelbrot ispc]:              [21.362] ms  
Wrote image file mandelbrot-ispc.ppm  
                                (5.80x speedup from ISPC)  
- There is only 5.80x speedup from ISPC, but the ideal speedup should be 8.00x. Maybe the reason is the function call `mandel(x, y, maxIterations)` which leads to unbalanced workload among 8 vector lanes.

### Part 2
1.  Run `mandelbrot_ispc` with the parameter `--tasks`. What speedup do you
  observe on view 1? What is the speedup over the version of `mandelbrot_ispc` that
  does not partition that computation into tasks?

- ljh@ljh-virtual-machine:~/asst1/prog3_mandelbrot_ispc$ ./mandelbrot_ispc --tasks  
[mandelbrot serial]:            [124.594] ms  
Wrote image file mandelbrot-serial.ppm  
[mandelbrot ispc]:              [21.151] ms  
Wrote image file mandelbrot-ispc.ppm  
[mandelbrot multicore ispc]:    [10.185] ms  
Wrote image file mandelbrot-task-ispc.ppm  
                                (5.89x speedup from ISPC)  
                                (12.23x speedup from task ISPC)  
- observation: about 2x speedup 

2.  There is a simple way to improve the performance of
  `mandelbrot_ispc --tasks` by changing the number of tasks the code
  creates. By only changing code in the function
  `mandelbrot_ispc_withtasks()`, you should be able to achieve
  performance that exceeds the sequential version of the code by over 32 times!
  How did you determine how many tasks to create? Why does the
  number you chose work best?

- The number of super-threads is the best number of tasks. 


3.  _Extra Credit: (2 points)_ What are differences between the thread
  abstraction (used in Program 1) and the ISPC task abstraction? There
  are some obvious differences in semantics between the (create/join
  and (launch/sync) mechanisms, but the implications of these differences
  are more subtle. Here's a thought experiment to guide your answer: what
  happens when you launch 10,000 ISPC tasks? What happens when you launch
  10,000 threads? (For this thought experiment, please discuss in the general case
  - i.e. don't tie your discussion to this given mandelbrot program.)

  The smart-thinking student's question: Hey wait! Why are there two different mechanisms (foreach and launch) for expressing independent, parallelizable work to the ISPC system? Couldn't the system just partition the many iterations of foreach across all cores and also emit the appropriate SIMD code for the cores?

Answer: Great question! And there are a lot of possible answers. Come to office hours.
 > Q3 RESERVE