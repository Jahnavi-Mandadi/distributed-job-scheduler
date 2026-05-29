import { useState } from "react";
import axios from "axios";

function TaskForm({ fetchTasks }) {

  const [name, setName] = useState("");
  const [taskType, setTaskType] = useState("");
  const [command, setCommand] = useState("");
  const [dagId, setDagId] = useState("");
  const [dependencyTaskId, setDependencyTaskId] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {

      await axios.post("http://127.0.0.1:5000/tasks", {
        name,
        task_type: taskType,
        command,
        dag_id: parseInt(dagId),
        dependency_task_id: dependencyTaskId
          ? parseInt(dependencyTaskId)
          : null
      });

      fetchTasks();

    } catch (error) {
      console.error(error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Create Task</h2>

      <input
        placeholder="Task Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />

      <br /><br />

      <input
        placeholder="Task Type"
        value={taskType}
        onChange={(e) => setTaskType(e.target.value)}
      />

      <br /><br />

      <input
        placeholder="Command"
        value={command}
        onChange={(e) => setCommand(e.target.value)}
      />

      <br /><br />

      <input
        placeholder="DAG ID"
        value={dagId}
        onChange={(e) => setDagId(e.target.value)}
      />

      <br /><br />

      <input
        placeholder="Dependency Task ID"
        value={dependencyTaskId}
        onChange={(e) => setDependencyTaskId(e.target.value)}
      />

      <br /><br />

      <button type="submit">Create Task</button>
    </form>
  );
}

export default TaskForm;