// Params


const GEOJSON_URL = "data/russia_subjects_89_copy.geojson";
const DATA_URL = "data/salaries.json";

let DATA = {};
let currentLevel = new URLSearchParams(location.search).get("level") || "middle";
if (!["applicant", "intern", "junior", "middle", "senior"].includes(currentLevel)) currentLevel = "middle";
document.querySelectorAll(".buttons button").forEach((b) => b.classList.toggle("active", b.dataset.level === currentLevel));


const LEVEL_FIELD = {
  applicant: "applicant",
  intern: "intern",
  junior: "junior",
  middle: "middle",
  senior: "senior"
};

const NO_DATA_COLOR = "#ccc";

// D3 lib init


const width = document.getElementById("map-container").clientWidth;
const height = document.getElementById("map-container").clientHeight;

const svg = d3.select("#map")
  .attr("viewBox", `0 0 ${width} ${height}`)
  .attr("preserveAspectRatio", "xMidYMid meet");

const mapGroup = svg.append("g");

const projection = d3.geoMercator().rotate([-105, 0]);
const path = d3.geoPath().projection(projection);

// Zoom 


const zoom = d3.zoom()
  .scaleExtent([1, 4])
  .extent([[0, 0], [width, height]])
  .translateExtent([[0, 0], [width, height]])
  .on("zoom", (event) => mapGroup.attr("transform", event.transform));

svg.call(zoom);

// HTML elements


const infoBox    = document.getElementById("info-box");
const infoName   = document.getElementById("info-name");
const infoRating = document.getElementById("info-rating");
const tooltip    = document.getElementById("tooltip");

// Data and color


function getEntry(name, level = currentLevel) {
  const field = LEVEL_FIELD[level];
  return field ? (DATA[name]?.[field] ?? null) : null;
}

// Score 1–100 (null = "Нет данных")
function getValue(name, level = currentLevel) {
  return getEntry(name, level)?.score ?? null;
}

function getSalary(name, level = currentLevel) {
  return getEntry(name, level)?.salary ?? null;
}

function formatScore(v) {
  return v === null ? "Нет данных" : String(v);
}

function formatSalary(v) {
  return v === null ? "—" : v.toLocaleString("ru-RU") + " ₽";
}

// Gradient 1–100 (красный → зелёный)
const colorScale = d3.scaleLinear()
  .domain([1, 50, 100])
  .range(["#e74c3c", "#f1c40f", "#2ecc71"])
  .clamp(true);

function buildColorScale() {}  

function getColor(name) {
  const v = getValue(name);
  return v === null ? NO_DATA_COLOR : colorScale(v);
}

// Load data


Promise.all([
  d3.json(GEOJSON_URL),
  d3.json(DATA_URL)
]).then(([geoData, data]) => {
  DATA = data;
  window.geoData = geoData;

  projection.fitSize([width, height], geoData);

  // Movement borders
  const [[x0, y0], [x1, y1]] = path.bounds(geoData);
  const pad = 20;
  zoom.translateExtent([[x0 - pad, y0 - pad], [x1 + pad, y1 + pad]]);

  buildColorScale();

  mapGroup.selectAll("path")
    .data(geoData.features)
    .enter()
    .append("path")
    .attr("class", "region")
    .attr("d", path)
    .attr("fill", (d) => getColor(d.properties?.name))
    .on("click", (event, d) => showInfoBox(event, d.properties?.name || "Неизвестный"))
    .on("mouseover", (event, d) => showTooltip(event, d.properties?.name || "Неизвестный"))
    .on("mousemove", moveTooltip)
    .on("mouseout", hideTooltip);

  updateTopList();
  setupDistrictFilter();
}).catch((err) => {
  console.error("❌ Ошибка загрузки:", err);
});

// Infobox


function showInfoBox(event, name) {
  if (!infoBox) return;
  infoName.textContent = name;
  const v = getValue(name);
  const ranked = Object.keys(DATA).filter((n) => getValue(n) !== null).sort((a, b) => getValue(b) - getValue(a));
  const place = ranked.indexOf(name) + 1;

  document.getElementById("info-body").innerHTML = `
    <div class="score ${v === null ? "none" : ""}">
      <strong>${v === null ? "Нет данных" : v}</strong>
      ${v === null ? "" : `<span>Рейтинг ${levelLabel()}</span>`}
    </div>
    <div class="rows">
      <div>Зарплата IT <b>${formatSalary(getSalary(name))}</b></div>
      <div>Федеральный округ <b>${DATA[name]?.district ?? "—"}</b></div>
      ${place ? `<div>Место в рейтинге <b>${place} из ${ranked.length}</b></div>` : ""}
    </div>`;

  const box = document.getElementById("map-container").getBoundingClientRect();
  infoBox.style.left = Math.min(event.clientX - box.left + 14, box.width - 280) + "px";
  infoBox.style.top  = Math.min(Math.max(event.clientY - box.top - 60, 8), box.height - 250) + "px";
  infoBox.classList.remove("hidden");
}

function levelLabel() {
  const btn = document.querySelector(`.buttons button[data-level="${currentLevel}"]`);
  return btn ? btn.textContent : currentLevel;
}

document.addEventListener("click", (e) => {
  if (!e.target.closest(".region") && !e.target.closest(".info-box")) {
    infoBox?.classList.add("hidden");
  }
});

// Tooltip

function showTooltip(event, name) {
  if (!tooltip) return;
  tooltip.textContent = `${name} — ${formatScore(getValue(name))}`;
  tooltip.classList.remove("hidden");
  moveTooltip(event);
}

function moveTooltip(event) {
  if (!tooltip) return;
  const rect = document.getElementById("map-container").getBoundingClientRect();
  tooltip.style.left = (event.clientX - rect.left + 15) + "px";
  tooltip.style.top  = (event.clientY - rect.top - 30) + "px";
}

function hideTooltip() {
  tooltip?.classList.add("hidden");
}

// Switch career levels


document.querySelectorAll(".buttons button").forEach((btn) => {
  btn.addEventListener("click", () => {
    document.querySelectorAll(".buttons button").forEach((b) => b.classList.remove("active"));
    btn.classList.add("active");
    currentLevel = btn.dataset.level;
    infoBox?.classList.add("hidden");
    buildColorScale();
    updateMapColors();
    updateTopList();
  });
});

function updateMapColors() {
  mapGroup.selectAll(".region")
    .transition()
    .duration(500)
    .attr("fill", (d) => getColor(d.properties?.name));
}

// Top 10 list

function updateTopList() {
  const list = document.getElementById("top-list");
  if (!list) return;

  const sorted = Object.keys(DATA)
    .map((name) => ({ name, value: getValue(name) }))
    .filter((item) => item.value !== null)
    .sort((a, b) => b.value - a.value)
    .slice(0, 10);

  if (!sorted.length) {
    list.innerHTML = "<li>Нет данных для этого профиля</li>";
    return;
  }

  list.innerHTML = sorted.map((item, i) => `
    <li>
      <span>${item.name}</span>
      <strong>${item.value}</strong>
    </li>
  `).join("");
}

// District filter + zoom buttons


function setupDistrictFilter() {
  const select = document.getElementById("district-select");
  const districts = [...new Set(Object.values(DATA).map((d) => d.district))].filter(Boolean).sort();
  districts.forEach((d) => select.insertAdjacentHTML("beforeend", `<option>${d}</option>`));

  select.addEventListener("change", () => {
    const chosen = select.value;
    mapGroup.selectAll(".region")
      .transition().duration(300)
      .style("opacity", (d) => (!chosen || DATA[d.properties?.name]?.district === chosen) ? 1 : 0.2);
  });
}

document.getElementById("zoom-in")?.addEventListener("click", () => svg.transition().call(zoom.scaleBy, 1.5));
document.getElementById("zoom-out")?.addEventListener("click", () => svg.transition().call(zoom.scaleBy, 1 / 1.5));
document.getElementById("zoom-reset")?.addEventListener("click", () => svg.transition().call(zoom.transform, d3.zoomIdentity));