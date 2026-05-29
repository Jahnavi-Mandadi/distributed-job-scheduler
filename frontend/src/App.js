import { useEffect, useState } from "react";
import axios from "axios";


import DagForm from "./components/DagForm";
import DagList from "./components/DagList";

import TaskForm from "./components/TaskForm";
import TaskList from "./components/TaskList";
import Monitoring from "./components/Monitoring";

function App() {

  //DAG state
  const [dags, setDags] = useState([]);

  //Task state
  const [tasks, setTasks]= useState([]);

  //Fetch  Dags
  const fetchDags = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:5000/dags");

      setDags(response.data);

    } catch (error) {
      console.error(error);
    }
  };

  //Fetch Tasks
  const fetchTasks=async() => {
    try{
      const response= await axios.get("http://127.0.0.1:5000/tasks");

      setTasks(response.data);

    }catch(error){
      console.error(error);
    }
  };

  //Initial Load
  useEffect(() => {
    fetchDags();
    fetchTasks();
  }, []);
  console.log("DAGS", dags);
  console.log("TASKS", tasks);

  return (
    <div style={{ padding: "40px" }}>

      <h1>Workflow Orchestration Platform</h1>

      {/* DAG Section */}
      <DagForm fetchDags={fetchDags} />

      <br />
      <br />

      <DagList dags={dags} />

      <hr />

      {/* TASK Section */}
      <TaskForm fetchTasks={fetchTasks} />

      <br />
      <br />

      <TaskList tasks={tasks} />

      <hr/>
      <Monitoring/>

    </div>
  );
}

export default App;