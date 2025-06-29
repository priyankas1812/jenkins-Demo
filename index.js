let sum = 0;
let evenCount = 0;
let oddCount = 0;

for (let i = 1; i <= 100; i++) {
  sum += i;

  if (i % 2 === 0) {
    evenCount++;
  } else {
    oddCount++;
  }
}

console.log("Sum of first 100 numbers:", sum);
console.log("Count of even numbers:", evenCount);
console.log("Count of odd numbers:", oddCount);
console.log("the demo for jenkins project");