/*
Write a Go function, find_square() that accepts an integer number, n and returns the square of n.
Invoke the function and display the square of the number.

Test your code by using the given sample inputs.
Verify your code by using the 2nd sample input(highlighted) given below:

+--------------+-----------------+
| Sample Input | Expected Output |
+--------------+-----------------+
|       5      |        25       |
+--------------+-----------------+
|       3      |  	             |
+--------------+-----------------+
*/


package main

import ("fmt")

func find_square(n int) {
    var square int =0
    square=n*n
    fmt.Println(square)
}

func main() {
    //Write your program logic here
    var n int=3
    find_square(n)
}
