const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split("\n");

let [dnaCnt, dnaSize] = input[0].split(" ").map(Number);
let diffCnt = 0;
let ansDna = "";

let dnaList = [];
for (let i = 0; i < dnaCnt; i++) {
  dnaList.push(input[i + 1].trim().split(""));
}

for (let i = 0; i < dnaSize; i++) {
  let alphabetTable = Array(26).fill(0);
  let pivotCnt = 0;
  let selection = "A";

  for (let j = 0; j < dnaCnt; j++) {
    let idx = dnaList[j][i].charCodeAt(0) - 65; // 'A' -> 0
    alphabetTable[idx] += 1;
  }

  for (let j = 0; j < alphabetTable.length; j++) {
    if (alphabetTable[j] > pivotCnt) {
      selection = String.fromCharCode(j + 65);
      pivotCnt = alphabetTable[j];
    }
  }

  ansDna += selection;
  if (pivotCnt < dnaCnt) {
    diffCnt += dnaCnt - pivotCnt;
  }
}

console.log(ansDna);
console.log(diffCnt);
