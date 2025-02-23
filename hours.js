// Sample JSON data (replace this with your actual JSON file)
const schedule = {
  "Tuesday": [9, 16], // 9 AM to 4 PM
  "Wednesday": [10, 18], // 10 AM to 6 PM
  "Saturday": [10, 23], // 10 AM to 6 PM
};

// Function to get the current day and time
function getCurrentDayAndTime() {
  const now = new Date();
  const day = now.toLocaleString('en-US', { weekday: 'long' }); // Get full day name (e.g., "Tuesday")
  const hour = now.getHours(); // Get current hour in 24-hour format
  return { day, hour };
}

// Function to check if the current time is within a range
function isTimeInRange(schedule) {
  const { day, hour } = getCurrentDayAndTime();

  // Check if the day exists in the schedule
  if (schedule[day]) {
    const [start, end] = schedule[day];
    // Check if the current hour is within the range
    return hour >= start && hour < end;
  }

  // If the day is not in the schedule, return false
  return false;
}

// Example usage
const result = isTimeInRange(schedule);
console.log(result); // true if current time is within a range, else false
