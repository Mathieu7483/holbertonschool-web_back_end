import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(request, response) {
    const dataPath = process.argv[2];

    readDatabase(dataPath)
      .then((fields) => {
        const responseParts = ['This is the list of our students'];

        const sortedFields = Object.keys(fields)
          .sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));

        for (const field of sortedFields) {
          const students = fields[field];
          responseParts.push(
            `Number of students in ${field}: ${students.length}. List: ${students.join(', ')}`,
          );
        }

        response.status(200).send(responseParts.join('\n'));
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(request, response) {
    const { major } = request.params;
    const dataPath = process.argv[2];

    if (major !== 'CS' && major !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(dataPath)
      .then((fields) => {
        const students = fields[major] || [];
        response.status(200).send(`List: ${students.join(', ')}`);
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }
}

export default StudentsController;
