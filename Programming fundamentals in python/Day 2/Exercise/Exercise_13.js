/*
Write a JavaScript program to display the sum of two given numbers if the numbers are same. If not, display double the sum.

Test your code by using the given sample input.
+--------------+-----------------+
| Sample Input | Expected Output |
+--------------+-----------------+
|      5,5     |       10        |
+--------------+-----------------+

*/

//PF-Exer-13
num1 = 5
num2 = 5
sum = num1 + num2
//Write your code here
if(num1==num2){
    console.log(sum)
}
else{
    console.log(2*sum)
}
