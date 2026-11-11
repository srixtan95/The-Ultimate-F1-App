const yearInput = document.getElementById("year");
const loadButton = document.getElementById("load");
const statusText = document.getElementById("status");
const raceList = document.getElementById("races");

async function loadSchedule() {
  const year = yearInput.value;
  statusText.textContent = "Loading...";
  raceList.innerHTML = "";

  try {
    const response = await fetch(`/api/schedule/${year}`);
    if (!response.ok) {
      throw new Error("Request failed with status " + response.status);
    }

    const races = await response.json();

    for (const race of races) {
      const item = document.createElement("li");
      item.textContent = `Round ${race.round}: ${race.name} (${race.country}), ${race.date}`;
      raceList.appendChild(item);
    }

    statusText.textContent = `${races.length} races in ${year}`;
  } catch (error) {
    statusText.textContent = "Could not load the calendar.";
    console.error(error);
  }
}

loadButton.addEventListener("click", loadSchedule);
loadSchedule();