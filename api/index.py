import fs from 'fs';
import path from 'path';

// Load student data once when the function is initialized
const filePath = path.join(process.cwd(), 'api', 'q-vercel-json.json');
let studentsData = [];

try {
  const fileData = fs.readFileSync(filePath, 'utf8');
  studentsData = JSON.parse(fileData);
} catch (error) {
  console.error("Failed to read or parse JSON file:", error);
}

export default function handler(req, res) {
  const { name } = req.query;

  if (!name) {
    return res.status(400).json({ error: "Please provide at least one name" });
  }

  // Ensure name is always treated as an array
  const names = Array.isArray(name) ? name : [name];

  const marks = names.map(studentName => {
    const student = studentsData.find(
      s => s.name.toLowerCase() === studentName.toLowerCase()
    );
    return student ? student.marks : null;
  });

  res.status(200).json({ marks });
}
