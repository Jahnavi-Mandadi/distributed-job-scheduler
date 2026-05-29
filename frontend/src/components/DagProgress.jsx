function DagProgress({ taskRuns }) {

  const total = taskRuns.length;

  const success = taskRuns.filter(
    t => t.state === "success"
  ).length;

  const percentage =
    total === 0
      ? 0
      : Math.round((success / total) * 100);

  return (
    <div>

      <h3>DAG Progress</h3>

      <div
        style={{
        width: "700px",
        height: "35px",
        border: "1px solid black",
        borderRadius: "8px",
        overflow: "hidden"
        }}
      >
        <div
            style={{
            width: `${percentage}%`,
            height: "100%",
            backgroundColor: "green",
            transition: "width 0.5s ease"
        }}
    />
      </div>

      <p>{percentage}% Complete</p>

    </div>
  );
}

export default DagProgress;