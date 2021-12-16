let input = [
  "   + -- + - + -   ",
  "   + --- + - +   ",
  "   + -- + - + -   ",
  "   + - + - + - +   ",
];

let result = "";
for (let data of input) {
  console.log(data.replace(/ /g, "").replace(/\+/g, "1").replace(/-/g, "0"));
  console.log(
    parseInt(data.replace(/ /g, "").replace(/\+/g, "1").replace(/-/g, "0"), 2)
  );
  console.log(
    String.fromCharCode(
      parseInt(data.replace(/ /g, "").replace(/\+/g, "1").replace(/-/g, "0"), 2)
    )
  );

  result += String.fromCharCode(
    parseInt(data.replace(/ /g, "").replace(/\+/g, "1").replace(/-/g, "0"), 2)
  );
}

console.log(result);
