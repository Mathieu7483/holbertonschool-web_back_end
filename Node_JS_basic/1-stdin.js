process.stdout.write('Welcome to Holberton School, what is your name?\n');
process.stdin.on('data', (Input) => {
  process.stdout.write(`Your name is: ${Input}`);
});
process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
