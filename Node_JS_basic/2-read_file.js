const fs = require('fs');

function countStudents(path) {
  let content;

  try {
    content = fs.readFileSync(path, 'utf8');
  } catch (err) {
    throw new Error('Cannot load the database');
  }

  const lines = content.split('\n').filter((line) => line.trim() !== '');

  const header = lines.shift();
  if (!header || lines.length === 0) {
    console.log('Number of students: 0');
    return;
  }

  const studentsByField = {};
  let totalStudents = 0;

  lines.forEach((line) => {
    const data = line.split(',');
    if (data.length === 4 && data[0].trim() !== '') {
      totalStudents += 1;
      const firstName = data[0].trim();
      const field = data[3].trim();

      if (!studentsByField[field]) {
        studentsByField[field] = [];
      }
      studentsByField[field].push(firstName);
    }
  });

  console.log(`Number of students: ${totalStudents}`);

  for (const [field, names] of Object.entries(studentsByField)) {
    console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
  }
}

module.exports = countStudents;
