# :notebook: algorithms
some algorithms implemented in python, cpp and javascript <br /> <br />

## :rocket: Searching algorithms: <br />
In computer science, a search algorithm is any algorithm which solves the search problem, namely, to retrieve information stored within some data structure,
 or calculated in the search space of a problem domain, either with discrete or continuous values. <br /> 

* :bookmark: **Binary Search:** <br />
In computer science, binary search, also known as half-interval search, logarithmic search, or binary chop, is a search algorithm that finds the position of a target value within a sorted array. Binary search compares the target value to the middle element of the array.
The main idea of the algorithms is to divide the given sorted array A into two subarrays at each step and look for the key element K in one of two subarrays. <br />
(You can read the code "BinarySearch.ipynb" // Everything documented, commented. <br />

* :bookmark: **Linear Search:** <br />
In this searching technique, we compare each array element with the key element (k), that we are looking for.
It's a very simple algorithm, but you may need to check every element of the array. If the key element is presented in the array, then the search is successful, otherwise is not. <br />
(You can read the code "LinearSearch.ipynb" // Everything documented, commented) <br />

* :bookmark: **Jump Search:** <br />
Jump search is a searching algorithms for sorted arrays. The basic idea is to check fewer elements(than linear algebra) by jumping ahead. <br />
(You can read the code "JumpSearch.ipynb" // Everything documented, commented) <br /> 

## :rocket: Recursive algorithms: <br />
A recursive algorithm is an algorithm which calls itself with "smaller (or simpler)" input values, and which obtains the result for the current input by 
applying simple operations to the returned value for the smaller (or simpler) input. <br />


* :bookmark: **Fibonacci Sequence**: <br />
Recursion means "defining a problem in terms of itself". This can be a very powerful tool in writing algorithms. 
Recursion comes directly from Mathematics, where there are many examples of expressions written in terms of themselves. 
For example, the Fibonacci sequence is defined as: F(i) = F(i-1) + F(i-2) 
(You can read the cide "Fibonacci_Sequence.ipynb" // Everything documented, commented) <br /> 

## :rocket: Backtracking algorithms: <br /> 
Backtracking is a general algorithm for finding all solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate as soon as it determines that the candidate cannot possibly be completed to a valid solution. <br /> 



## :rocket: Sorting Algorithms: <br />
Sorting algorithms were Basically made to sort a specific data structure such as an array, vector, list..etc 
You can optimize your searching via using multiple methods to do the work. A Sorting Algorithm is used to rearrange a given array or list elements according to a comparison operator on the elements. The comparison operator is used to decide the new order of element in the respective data structure. 
* :bookmark: **Bubblle Sort**: <br />
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.
<br />
* :bookmar: **Recursive Sorting**: <br />
Its the same as the bubble sort but we'll implement it recursively.Recursive Bubble Sort has no performance/implementation advantages, but can be a good question to check one’s understanding of Bubble Sort and recursion.
If we take a closer look at Bubble Sort algorithm, we can notice that in first pass, we move largest element to end (Assuming sorting in increasing order). In second pass, we move second largest element to second last position and so on.<br />

