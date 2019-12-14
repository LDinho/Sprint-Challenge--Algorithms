#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  `O(n)` The operation depends on a single loop, and when input size increases, the runtime (number of operations) will grow at the same rate as the input.


b) `O(n^2)` In this code block, the first loop runs `O(n)` and the second loop would also run `n` times `O(n)`.


c) `O(n)`  This order of operation is `O(n)` because the runtime is affected by the size of input due to the recursive nature of the code.

## Exercise II

For a building with `n` number of floors, first possible solution would be to investigate each floor starting at the very first floor (floor 1). In other words, consider the building as a sorted array, and each index has a floor number. Test the breakage of an egg at each index, starting at 1 and moving up 1 index up/forward, keeping track of your position and whether the egg broke at each index. Compare at which position where the egg broke from the previous floor index will give you the safest floor number for the eggs. This describes a linear search type of algorithm where the runtime complexity would likely be `O(n)`.
