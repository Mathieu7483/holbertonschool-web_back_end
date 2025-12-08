export default function createIteratorObject(report) {
return {
  [Symbol.iterator]() {
    const departments = Object.keys(report.allEmployees);
    let deptIndex = 0;
    let empIndex = 0;

    return {
      next() {
        if (deptIndex >= departments.length) {
          return { done: true };
        }

        const departmentName = departments[deptIndex];
        const employees = report.allEmployees[departmentName];

        if (empIndex >= employees.length) {
          deptIndex++;
          empIndex = 0;
          return this.next();
        }

        const value = {
          department: departmentName,
          employee: employees[empIndex],
        };
        empIndex++;
        return { value, done: false };
      },
    };
  },
};
}