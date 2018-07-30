// Define a variable
var count = 1;
var name = 'Julian';

// Loop
for (var i = 0; i < 10; i++) {
  console.log(i);
}

// Conditionals
if (i == 0) {
  console.log('This is 0!!');
} 

if (i > 0 && i < 10) {
  console.log('Yes, between 0 AND 10');
}

if (i < 0 || i > 10) {
  console.log('Less than 0 OR greater than 10');
}

// Functions

// DEFINE
function add(firstNum, secondNum) {
  return firstNum + secondNum;
}

// CALL
var answer = add(1, 2);
console.log(answer);
