const express = require('express');
const countStudents = require('./3-read_file_async');

const DATABASE = process.argv[2];
const app = express();

app.get('/', (req, res) => {
  res.status(200).send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  const responseParts = ['This is the list of our students'];
  const originalLog = console.log;

  console.log = (msg) => responseParts.push(msg);

  try {
    await countStudents(DATABASE);
    console.log = originalLog;
    res.status(200).send(responseParts.join('\n'));
  } catch (error) {
    console.log = originalLog;
    res.status(500).send(`${responseParts[0]}\n${error.message}`);
  }
});

app.listen(1245);

module.exports = app;
