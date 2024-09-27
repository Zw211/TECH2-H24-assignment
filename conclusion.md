# Conclusion

After timing all three functions on three different datasets, It is visible that the
**builtin python functions** are most efficient for 100,000 and 10,000 loops. 
**NumPy method** is the fastest for 1,000 loops. The for loop performed the worst at 1,000 loops at 1.14ms

> #### Times:
>
> ##### Builtin method
>
> - 5.68 μs ± 3.53 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)
> - 50.3 μs ± 56.1 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
> - 502 μs ± 496 ns per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
>
> ##### *For loop* method
>
> - 10.5 μs ± 16.6 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)
> - 111 μs ± 150 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
> - 1.14 ms ± 6.18 μs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
>
> ##### NumPy method
>
> - 15.8 μs ± 27.6 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)
> - 51.9 μs ± 73.6 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
> - 400 μs ± 436 ns per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
