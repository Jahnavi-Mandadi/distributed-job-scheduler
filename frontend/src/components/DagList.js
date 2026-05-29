import axios from "axios";

function DagList({ dags }) {

  const runDag = async (dagId) => {

    try {

      await axios.post(
        `http://127.0.0.1:5000/run_dag/${dagId}`
      );

      alert("DAG Run Created");

    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>

      <h2>Workflow DAGs</h2>

      <table border="1" cellPadding="10">

        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Schedule</th>
            <th>Action</th>
          </tr>
        </thead>

        <tbody>

          {dags.map((dag) => (
            <tr key={dag.id}>

              <td>{dag.id}</td>
              <td>{dag.name}</td>
              <td>{dag.schedule}</td>

              <td>
                <button onClick={() => runDag(dag.id)}>
                  Run DAG
                </button>
              </td>

            </tr>
          ))}

        </tbody>

      </table>

    </div>
  );
}

export default DagList;