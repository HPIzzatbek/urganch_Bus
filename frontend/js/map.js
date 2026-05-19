// 1. Urganch koordinatalari
var map = L.map('map').setView([41.55, 60.63], 13);

// 2. Xarita qatlamini qo'shish
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

// 3. Menyu funksiyasi
function toggleSidebar() {
    var sidebar = document.getElementById("sidebar");
    sidebar.style.width = sidebar.style.width === "250px" ? "0" : "250px";
}

// 4. Jadval panelini ochib-yopish funksiyasi
function toggleSchedule() {
    var panel = document.getElementById("schedule-panel");
    if (panel.style.display === "none" || panel.style.display === "") {
        panel.style.display = "block";
        calculateSchedule(); // Jadvalni hisoblashni chaqirish
    } else {
        panel.style.display = "none";
    }
}

// 5. Jadvalni avtomatik hisoblash
function calculateSchedule() {
    const routes = [
        { name: "1-yo'nalish", buses: 8, km: 10 },
        { name: "2-yo'nalish", buses: 6, km: 10 },
        { name: "3-yo'nalish", buses: 8, km: 12 }
    ];

    var tbody = document.getElementById("schedule-body");
    tbody.innerHTML = ""; // Oldingi ma'lumotlarni tozalash

    routes.forEach(function(r) {
        // Intervalni hisoblash: (Masofa * 2 / Tezlik 60) * 60 daqiqa / Avtobuslar
        var interval = ((r.km * 2 / 60) * 60 / r.buses).toFixed(1);
        tbody.innerHTML += <tr><td>${r.name}</td><td>${r.buses} ta</td><td>${interval} min</td></tr>;
    });
}

// Xaritani yaratayotganda zoomControl-ni o'chirib qo'yamiz
var map = L.map('map', {
    zoomControl: false
}).setView([41.55, 60.63], 13); // Urganch koordinatalari

// Zoom boshqaruvini o'ng pastki burchakka qo'shamiz
L.control.zoom({
    position: 'bottomright'
).addTo(map);
