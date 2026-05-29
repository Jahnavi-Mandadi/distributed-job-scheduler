function TaskList({ tasks }) {

  return (
    <div>

      <h2>Workflow Tasks</h2>

      <table border="1" cellPadding="10">

        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Type</th>
            <th>Command</th>
            <th>DAG ID</th>
            <th>Dependency</th>
          </tr>
        </thead>

        <tbody>

          {tasks.map((task) => (
            <tr key={task.id}>
              <td>{task.id}</td>
              <td>{task.name}</td>
              <td>{task.task_type}</td>
              <td>{task.command}</td>
              <td>{task.dag_id}</td>
              <td>{task.dependency_task_id || "None"}</td>
            </tr>
          ))}

        </tbody>

      </table>

    </div>
  );
}

export default TaskList;