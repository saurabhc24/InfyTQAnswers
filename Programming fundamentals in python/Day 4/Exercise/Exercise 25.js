/*
Write a Java Script function, find_sum() that accepts an integer, n and returns the sum of first, n numbers.
Invoke the function and display the sum of first n numbers.

Test your code by using the given sample input.
+--------------+-----------------+
| Sample Input | Expected Output |
+--------------+-----------------+
|       6      |      21         |
+--------------+-----------------+
*/

//JS-Exer-25

//Start writing your code here
function find_sum(n){
    var sum=0;
    for(i=1;i<=n;i++){
        sum=sum+i;
    }
    console.log(sum);
}
