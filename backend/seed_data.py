"""
seed_data.py — Urganch Bus uchun boshlang'ich ma'lumotlar
3 ta haqiqiy Urganch yo'nalish, bekatlar, avtobuslar va jadvallar
"""

from models import get_db_connection, init_db


# ─────────────────────────────────────────────
#  Haqiqiy Urganch koordinatalari (taxminiy)
#  Markaz: 41.5480° N, 60.6330° E
# ─────────────────────────────────────────────

ROUTES = [
    {
        "number": "1",
        "name": "Vokzal — Aeroport",
        "color": "#3B82F6",  # moviy
        "description": "Temir yo'l vokzalidan Aeroportgacha asosiy yo'nalish",
    },
    {
        "number": "2",
        "name": "Urganch dehqon bozori — Urganch Davlat Universiteti",
        "color": "#10B981",  # yashil
        "description": "Urganch dehqon bozoridan Urganch Davlat niversitetigacha",
    },
    {
        "number": "3",
        "name": "Urganch Amir Temur Parkidan — Eski TATU Urganch Filiali",
        "color": "#F59E0B",  # sariq
        "description": "Urganch Amir Temur Parkidan Eski TATU Urganch Filialigacha",
    },
]

# Har yo'nalish uchun bekatlar [nomi, kenglik, uzunlik]
STOPS = {
    "1": [
        ("Temir yo'l Vokzali bekati",         41.554, 60.60631),
        ("Oybek ko'chasi bekati",             41.548, 60.625),
        ("Al-Xorazmiy ko'chasi bekatlari",    41.5449, 60.6306),
        ("Markaziy dehqon bozori atrofi",     41.5542, 60.6251),
        ("Urganch shahar markazi bekatlari",  41.5518, 60.6314),
        ("Aeroport bekati",                   39.69033, 66.98879),
    ],
    "2": [
        ("Dehqon bozori bekati",   41.5526, 60.6318),
        ("Hamkorbank",             41.5506, 60.6310),
        ("SUM",                    41.55, 60.63),
        ("Markaziy pochta",        41.5500, 60.6333),
        ("Yoshlar Markazi",        41.557291, 60.616027),
        ("Urganch Davlat Universiteti bekati",   41.5573, 60.6056),
    ],
    "3": [
        ("Amir Temur parki",     41.5505, 60.6315),
        ("Amir Temur ko'chasi",  41.5573, 60.6160),
        ("Memorial shifoxona",   41.5456, 60.6312),
        ("Urganch Davlat Universitetiga yaqin atroflar", 41.55725, 60.60564),
        ("Shahar markazi",       41.5518, 60.6333),
        ("Urganch shahar avtovokzal", 41.5386, 60.6326),
        ("Eski TATU Urganch filiali", 41.5500, 60.6333),
    ],
}

# Avtobus/karta
BUSES = {
    "1": [("90 A 123 BC", 45), ("90 A 456 BC", 45)],
    "2": [("90 B 789 BC", 35), ("90 B 321 BC", 35)],
    "3": [("90 C 654 BC", 30), ("90 C 987 BC", 30)],
}

# Jadval: (avtobus indeksi, bekat indeksi, vaqt)
SCHEDULES = {
    "1": [
        # Bus 0
        (0, 0, "07:00"), (0, 1, "07:10"), (0, 2, "07:18"),
        (0, 3, "07:25"), (0, 4, "07:33"), (0, 5, "07:45"),
        (0, 0, "09:00"), (0, 1, "09:10"), (0, 2, "09:18"),
        (0, 3, "09:25"), (0, 4, "09:33"), (0, 5, "09:45"),
        # Bus 1
        (1, 0, "08:00"), (1, 1, "08:10"), (1, 2, "08:18"),
        (1, 3, "08:25"), (1, 4, "08:33"), (1, 5, "08:45"),
        (1, 0, "10:00"), (1, 1, "10:10"), (1, 2, "10:18"),
        (1, 3, "10:25"), (1, 4, "10:33"), (1, 5, "10:45"),
    ],
    "2": [
        (0, 0, "07:15"), (0, 1, "07:22"), (0, 2, "07:30"),
        (0, 3, "07:38"), (0, 4, "07:46"), (0, 5, "07:55"),
        (1, 0, "08:15"), (1, 1, "08:22"), (1, 2, "08:30"),
        (1, 3, "08:38"), (1, 4, "08:46"), (1, 5, "08:55"),
    ],
    "3": [
        (0, 0, "07:30"), (0, 1, "07:37"), (0, 2, "07:44"),
        (0, 3, "07:50"), (0, 4, "07:57"), (0, 5, "08:05"),
        (0, 6, "08:12"),
        (0, 0, "09:30"), (0, 1, "09:37"), (0, 2, "09:44"),
        (0, 3, "09:50"), (0, 4, "09:57"), (0, 5, "10:05"),
        (0, 6, "10:12"),
    ],
}


def seed():
    """Bazani boshlang'ich ma'lumotlar bilan to'ldurish"""
    conn = get_db_connection()
    cursor = conn.cursor()

    # Agar ma'lumotlar allaqachon mavjud bo'lsa — o'tkazib yuborish
    existing = cursor.execute("SELECT COUNT(*) FROM routes").fetchone()[0]
    if existing > 0:
        print("[Seed] Ma'lumotlar allaqachon mavjud. O'tkazildi.")
        conn.close()
        return

    route_id_map = {}   # number -> db id
    bus_id_map = {}     # (number, bus_idx) -> db id
    stop_id_map = {}    # (number, stop_idx) -> db id

    # ─── Yo'nalishlarni kiritish ───────────────────────────────────────────
    for route in ROUTES:
        cursor.execute(
            "INSERT INTO routes (number, name, color, description) VALUES (?, ?, ?, ?)",
            (route["number"], route["name"], route["color"], route["description"]),
        )
        route_id_map[route["number"]] = cursor.lastrowid

    # ─── Bekatlarni kiritish ───────────────────────────────────────────────
    for route_num, stops in STOPS.items():
        rid = route_id_map[route_num]
        for i, (name, lat, lng) in enumerate(stops):
            cursor.execute(
                "INSERT INTO stops (route_id, name, lat, lng, order_num) VALUES (?, ?, ?, ?, ?)",
                (rid, name, lat, lng, i),
            )
            stop_id_map[(route_num, i)] = cursor.lastrowid

    # ─── Avtobuslarni kiritish ─────────────────────────────────────────────
    for route_num, buses in BUSES.items():
        rid = route_id_map[route_num]
        for i, (plate, capacity) in enumerate(buses):
            cursor.execute(
                "INSERT INTO buses (route_id, plate_number, capacity) VALUES (?, ?, ?)",
                (rid, plate, capacity),
            )
            bus_id_map[(route_num, i)] = cursor.lastrowid

    # ─── Jadvallarni kiritish ──────────────────────────────────────────────
    for route_num, entries in SCHEDULES.items():
        rid = route_id_map[route_num]
        for bus_idx, stop_idx, depart_time in entries:
            bid = bus_id_map[(route_num, bus_idx)]
            sid = stop_id_map[(route_num, stop_idx)]
            cursor.execute(
                "INSERT INTO schedules (route_id, bus_id, stop_id, depart_time) VALUES (?, ?, ?, ?)",
                (rid, bid, sid, depart_time),
            )

    conn.commit()
    conn.close()
    print("[Seed] Barcha ma'lumotlar muvaffaqiyatli kiritildi!")


if __name__ == "__main__":
    init_db()
    seed()
