import fs from 'fs';

const readDatabase = (path) => new Promise((resolve, reject) => {
  fs.readFile(path, 'utf8', (err, data) => {
    if (err) {
      reject(new Error('Cannot load the database'));
      return;
    }
    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const studentsByField = {};

    const rows = lines.slice(1);

    for (const row of rows) {
      const [firstname, , , field] = row.split(',');
      if (!studentsByField[field]) studentsByField[field] = [];
      studentsByField[field].push(firstname);
    }
    resolve(studentsByField);
  });
});

export default readDatabase;
