import { useEffect, useState } from "react";
import axios from "axios";

import StatusBadge from "./StatusBadge";
import DagProgress from "./DagProgress";

function Monitoring() {

  const [dagRuns,setDagRuns]=useState([]);
  const [taskRuns,setTaskRuns]=useState([]);

  useEffect(() => {

  fetchDagRuns();
  fetchTaskRuns();

  const interval = setInterval(() => {

    fetchDagRuns();
    fetchTaskRuns();

    }, 3000);

  return () => clearInterval(interval);

}, []);

  const fetchDagRuns=async()=>{

    const response=
      await axios.get(
        "http://127.0.0.1:5000/dag_runs"
      );

    setDagRuns(response.data);
  };

  const fetchTaskRuns=async()=>{

    const response=
      await axios.get(
        "http://127.0.0.1:5000/task_runs"
      );

    setTaskRuns(response.data);
  };

  return(

    <div>

      <h2>DAG Runs</h2>

      <table
        border="1"
        cellPadding="10"
        style={{
        width: "80%",
        marginBottom: "20px"
         }}
>

        <thead>
          <tr>
            <th>ID</th>
            <th>DAG ID</th>
            <th>Status</th>
          </tr>
        </thead>

        <tbody>

          {dagRuns.map(run=>(
            <tr key={run.id}>
              <td>{run.id}</td>
              <td>{run.dag_id}</td>
              <td style={{ textAlign: "center" }}>
                <StatusBadge status={run.state} />
              </td>
            </tr>
          ))}

        </tbody>

      </table>
      
      <br/>

      <DagProgress taskRuns={taskRuns} />


      <h2>Task Runs</h2>

      <table
        border="1"
        cellPadding="10"
        style={{
        width: "80%",
        marginBottom: "20px"
        }}
>

        <thead>
          <tr>
            <th>ID</th>
            <th>Task ID</th>
            <th>Status</th>
          </tr>
        </thead>

        <tbody>

          {taskRuns.map(run=>(
            <tr key={run.id}>
              <td>{run.id}</td>
              <td>{run.task_id}</td>
              <td style={{ textAlign: "center" }}>
                <StatusBadge status={run.state} />
              </td>
            </tr>
          ))}

        </tbody>

      </table>

    </div>
  );
}

export default Monitoring;