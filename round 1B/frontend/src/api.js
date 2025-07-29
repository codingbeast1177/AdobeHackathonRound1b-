// src/api.js
import axios from "axios";

export const uploadAndRank = async (file, persona, job) => {
  const formData = new FormData();
  formData.append("file", file);
  formData.append("persona", persona);
  formData.append("job", job);

  try {
    const response = await axios.post("http://localhost:8000/rank", formData, {
      headers: { "Content-Type": "multipart/form-data" },
    });
    return response.data;
  } catch (error) {
    console.error("Error uploading and ranking:", error);
    throw error;
  }
};