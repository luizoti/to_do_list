"""Module with a task enum type."""

TASK_STATES: dict[int, str] = {
    0: "Pending",
    1: "Completed",
    2: "In Progress",
}

TASK_PRIORITYS: dict[int, str] = {
    0: "Low",
    1: "Normal",
    2: "High",
}
