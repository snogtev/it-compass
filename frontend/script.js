// ============================================================
// 1. НАСТРОЙКИ
// ============================================================

const GEOJSON_URL = "data/russia.geojson";
const MOCK_URL = "data/mock-ratings.json";

let MOCK_DATA = {};      // ← сюда загрузим JSON
let currentLevel = "abiturient";

// Уровни (пока просто коэффициенты для вида, реальные веса — с бэка)
const LEVEL_WEIGHTS = {
  abiturient: { edu: 0.40, intern: 0.20, job: 0.20, digital: 0.10, weather: 0.10 },
  junior:     { job: 0.35, company: 0.15, edu: 0.20, k_life: 0.15, digital: 0.10, logistics: 0.05 },
  middle:     { k_life: 0.30, k_mortgage: 0.15, digital: 0.20, job: 0.15, weather: 0.10, logistics: 0.10 },
  senior:     { k_life: 0.25, tax: 0.15, weather: 0.25, logistics: 0.20, digital: 0.15 }
};

// ============================================================
// 2. ИНИЦИАЛИЗАЦИЯ D3
// ============================================================

const width = document.getElementById("map-container").clientWidth;
const height = document.getElementById("map-container").clientHeight;

const svg = d3.select("#map")
  .attr("viewBox", `0 0 ${width} ${height}`)
  .attr("preserveAspectRatio", "xMidYMid meet");

const mapGroup = svg.append("g");

const projection = d3.geoMercator()
  .center([100, 60])
  .scale(300)
  .translate([width / 2, height / 2]);

const path = d3.geoPath().projection(projection);

// ============================================================
// 3. ЗУМ
// ============================================================

const zoom = d3.zoom()
  .scaleExtent([0.5, 8])
  .on("zoom", (event) => mapGroup.attr("transform", event.transform));

svg.call(zoom);

// ============================================================
// 4. ЭЛЕМЕНТЫ HTML
// ============================================================

const infoBox    = document.getElementById("info-box");
const infoName   = document.getElementById("info-name");
const infoRating = document.getElementById("info-rating");
const tooltip    = document.getElementById("tooltip");

// ============================================================
// 5. ЦВЕТ
// ============================================================

function getColor(rating) {
  if (rating === undefined || rating === null) return "#ccc";
  return d3.scaleLinear()
    .domain([0, 50, 100])
    .range(["#e74c3c", "#f1c40f", "#2ecc71"])(rating);
}

// ============================================================
// 6. ЗАГРУЗКА ДАННЫХ
// ============================================================

Promise.all([
  d3.json(GEOJSON_URL),
  d3.json(MOCK_URL)
]).then(([geoData, mockData]) => {
  MOCK_DATA = mockData;
  window.geoData = geoData;

  console.log("✅ GeoJSON загружен:", geoData.features.length, "регионов");
  console.log("✅ Мок-данные загружены:", Object.keys(mockData).length, "регионов");

  // Рисуем карту
  mapGroup.selectAll("path")
    .data(geoData.features)
    .enter()
    .append("path")
    .attr("class", "region")
    .attr("d", path)
    .attr("fill", (d) => {
      const name = d.properties?.NL_NAME_1 || d.properties?.NAME_1 || "";
      const rating = MOCK_DATA[name];
      return getColor(rating);
    })
    .on("click", (event, d) => {
      const name = d.properties?.NL_NAME_1 || d.properties?.NAME_1 || "Неизвестный";
      showInfoBox(event, name, MOCK_DATA[name]);
    })
    .on("mouseover", (event, d) => {
      const name = d.properties?.NL_NAME_1 || d.properties?.NAME_1 || "Неизвестный";
      showTooltip(event, name);
    })
    .on("mousemove", moveTooltip)
    .on("mouseout", hideTooltip);

  console.log("🗺️ Карта отрисована");
  updateTopList();
}).catch((err) => {
  console.error("❌ Ошибка загрузки:", err);
});

// ============================================================
// 7. ИНФОБОКС
// ============================================================

function showInfoBox(event, name, rating) {
  if (!infoBox) return;
  infoName.textContent = name;
  infoRating.textContent = rating !== undefined
    ? `Балл (${currentLevel}): ${rating}`
    : "Нет данных";

  const rect = event.target.getBoundingClientRect();
  infoBox.style.left = rect.left + "px";
  infoBox.style.top  = (rect.top - 80) + "px";
  infoBox.classList.remove("hidden");
}

document.addEventListener("click", (e) => {
  if (!e.target.closest(".region") && !e.target.closest(".info-box")) {
    infoBox?.classList.add("hidden");
  }
});

// ============================================================
// 8. ТУЛТИП
// ============================================================

function showTooltip(event, name) {
  if (!tooltip) return;
  tooltip.textContent = name;
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

// ============================================================
// 9. ПЕРЕКЛЮЧЕНИЕ УРОВНЕЙ
// ============================================================

document.querySelectorAll(".buttons button").forEach((btn) => {
  btn.addEventListener("click", () => {
    document.querySelectorAll(".buttons button").forEach((b) => b.classList.remove("active"));
    btn.classList.add("active");
    currentLevel = btn.dataset.level;
    console.log("Уровень изменён на:", currentLevel);
    updateMapColors();
    updateTopList();
  });
});

function updateMapColors() {
  mapGroup.selectAll(".region")
    .transition()
    .duration(500)
    .attr("fill", (d) => {
      const name = d.properties?.NL_NAME_1 || d.properties?.NAME_1 || "";
      return getColor(MOCK_DATA[name]);
    });
}

// ============================================================
// 10. ТОП-10
// ============================================================

function updateTopList() {
  const list = document.getElementById("top-list");
  if (!list) return;

  const sorted = Object.entries(MOCK_DATA)
    .map(([name, rating]) => ({ name, rating }))
    .sort((a, b) => b.rating - a.rating)
    .slice(0, 10);

  list.innerHTML = sorted.map((item, i) => `
    <li>
      <span><span class="rank">${i + 1}.</span>${item.name}</span>
      <strong>${item.rating}</strong>
    </li>
  `).join("");
}