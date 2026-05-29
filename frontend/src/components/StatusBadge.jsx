function StatusBadge({ status }) {

  const colors = {
    pending: "orange",
    running: "blue",
    success: "green",
    failed: "red"
  };

  return (
    <span
      style={{
        color: "white",
        backgroundColor: colors[status] || "gray",
        padding: "5px 10px",
        borderRadius: "5px"
      }}
    >
      {status}
    </span>
  );
}

export default StatusBadge;