// src/WebApp.jsx
import React, { useState } from "react";
import { uploadAndRank } from "./api";

export default function WebApp() {
  const [file, setFile] = useState(null);
  const [persona, setPersona] = useState("");
  const [job, setJob] = useState("");
  const [result, setResult] = useState(null);

  const handleSubmit = async () => {
    if (!file || !persona || !job) return;
    const res = await uploadAndRank(file, persona, job);
    setResult(res);
  };

  return (
    <div className="p-4 max-w-xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">PDF Ranker</h1>
      <input
        type="text"
        placeholder="Persona (e.g. Product Manager)"
        value={persona}
        onChange={(e) => setPersona(e.target.value)}
        className="mb-2 block w-full px-2 py-1 border rounded"
      />
      <input
        type="text"
        placeholder="Job to be done (e.g. Evaluate PDF)"
        value={job}
        onChange={(e) => setJob(e.target.value)}
        className="mb-2 block w-full px-2 py-1 border rounded"
      />
      <input
        type="file"
        accept=".pdf"
        onChange={(e) => setFile(e.target.files[0])}
        className="mb-4"
      />
      <button
        onClick={handleSubmit}
        className="bg-blue-500 text-white px-4 py-2 rounded"
      >
        Upload & Rank
      </button>
      {result && (
        <pre className="mt-4 bg-gray-100 p-4 rounded text-sm">
          {JSON.stringify(result, null, 2)}
        </pre>
      )}
    </div>
  );
}