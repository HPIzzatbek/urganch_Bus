# 🚌 Urganch Bus — Jamoat Transporti Boshqaruv Tizimi

Urganch shahri uchun zamonaviy veb-boshqaruv tizimi. **Glassmorphism dizayn**, interaktiv **Leaflet.js xarita**, **real-vaqt avtobus simulyatsiya** va **Flask backend**.

---

## 📁 Loyiha Tuzilmasi

```
urganch-bus/
├── backend/
│   ├── app.py              ← Flask API serveri (asosiy fayl)
│   ├── models.py           ← SQLite jadvallar (routes, stops, buses, schedules)
│   ├── seed_data.py        ← Boshlang'ich 3 yo'nalish ma'lumotlari
│   ├── requirements.txt    ← Python kutubxonalari
│   └── urganch_bus.db      ← SQLite bazasi (serverdan keyin yaratiladi)
├── frontend/
│   ├── index.html          ← Asosiy sahifa (semantic HTML5)
│   ├── css/
│   │   └── style.css       ← Glassmorphism + Dark mode + Responsive
│   └── js/
│       ├── app.js          ← Asosiy logika, API, sidebar, simulyatsiya
│       ├── map.js          ← Leaflet.js xarita moduli
│       └── timer.js        ← Countdown timer moduli
└── run-server.bat          ← Bir marta bosish bilan ishga tushirish
```

---

## 🚀 Ishga Tushirish

### 1. Python kutubxonalarini o'rnatish (birinchi marta)
```bash
cd backend
pip install flask flask-cors
```

### 2. Serverni ishga tushirish
**Windows:** `run-server.bat` faylini ikki marta bosing

**Yoki terminal orqali:**
```bash
cd backend
python app.py
```

### 3. Brauzerda ochish
```
http://127.0.0.1:5000
```

---

## 🌐 API Endpointlar

| Endpoint | Metod | Tavsif |
|----------|-------|--------|
| `/api/routes` | GET | Barcha faol yo'nalishlar (bekatlar bilan) |
| `/api/schedule?route_id=1` | GET | Yo'nalish jadvali |
| `/api/buses` | GET | Barcha avtobuslar ro'yxati |
| `/api/stops?route_id=1` | GET | Bekatlar ro'yxati |
| `/api/realtime` | GET | Avtobus simulyatsiya ma'lumotlari |

---

## 🗺 3 ta Yo'nalish

| # | Yo'nalish | Bekatlar | Rang |
|---|-----------|----------|------|
| 1 | Vokzal → Aeroport | 6 bekat | 🔵 Ko'k |
| 2 | Yangi Urgench → Xorazm Universiteti | 6 bekat | 🟢 Yashil |
| 3 | Do'stlik → Karvon Bozor | 7 bekat | 🟡 Sariq |

---

## ✨ Xususiyatlar

- **Glassmorphism dizayn** — zamonaviy shisha effekti
- **Dark/Light mode** — tungi va kunduzgi rejim
- **Interaktiv xarita** — Leaflet.js + OpenStreetMap
- **Yo'nalish animatsiyasi** — polyline va glow effekti
- **Avtobus harakati** — smooth interpolyatsiya animatsiya
- **Countdown timer** — rang o'zgaruvchi (yashil → sariq → qizil)
- **Real-vaqt simulyatsiya** — 15 soniyada yangilanadi
- **Responsive** — mobil qurilmalarga moslashgan
- **Offline rejim** — backend ishlamasa demo rejimida ishlaydi

---

## 🔧 Texnologiyalar

| Frontend | Backend | Baza |
|----------|---------|------|
| HTML5, CSS3 | Python 3.x | SQLite |
| JavaScript ES6+ | Flask 3.0 | — |
| Leaflet.js 1.9 | Flask-CORS | — |
| Google Fonts (Inter) | — | — |

---

## 📜 Litsenziya

MIT — Urganch shahri jamoat loyihasi
