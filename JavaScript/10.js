const n = prompt('입력');

for (let i = 1; i <= n; i++) {
  let blank = '';
  for (let k = 1; k <= n - i; k++) {
    blank = blank + ' ';
  }

  for (let j = 1; j <= i * 2 - 1; j++) {
    blank = blank + '*';
  }
  console.log(blank);
}
