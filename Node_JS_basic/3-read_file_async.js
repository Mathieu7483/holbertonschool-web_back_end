const fs = require('fs').promises;

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, { encoding: 'utf8' });
    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const header = lines.shift();
    if (!header) return;
    const studentsByField = {};
    let totalStudents = 0;

    lines.forEach((line) => {
      const student = line.split(',');
      if (student.length === 4 && student[0].trim() !== '') {
        totalStudents += 1;
        const firstName = student[0].trim();
        const field = student[3].trim();

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
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
