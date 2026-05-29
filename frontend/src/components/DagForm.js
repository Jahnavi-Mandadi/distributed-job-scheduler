import { useState } from "react";
import axios from "axios";

function DagForm({ fetchDags }) {
  const [name, setName] = useState("");
  const [schedule, setSchedule] = useState("");
  const [description, setDescription] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await axios.post("http://127.0.0.1:5000/dags", {
        name,
        schedule,
        description,
      });

      setName("");
      setSchedule("");
      setDescription("");

      fetchDags();
    } catch (error) {
      console.error(error);
      alert("Failed to create DAG");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Create Workflow DAG</h2>

      <input
        type="text"
        placeholder="Workflow Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />

      <br /><br />

      <input
        type="text"
        placeholder="Cron Schedule"
        value={schedule}
        onChange={(e) => setSchedule(e.target.value)}
      />

      <br /><br />

      <input
        type="text"
        placeholder="Description"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />

      <br /><br />

      <button type="submit">Create DAG</button>
    </form>
  );
}

export default DagForm;