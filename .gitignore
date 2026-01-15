import turtle
import math
import random

# ================== GAZ PARÇACIK SİSTEMİ ==================
class GazSistemi:
    def __init__(self):
        self.parcaciklar = []
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.penup()
        self.t.color("white")  # <<< GAZ RENGİ

    def ekle(self, x, y, life=20):
        self.parcaciklar.append({
            "x": x + random.uniform(-2, 2),
            "y": y + random.uniform(-2, 2),
            "life": life
        })

    def guncelle(self):
        self.t.clear()
        yeni = []

        for p in self.parcaciklar:
            p["life"] -= 1
            if p["life"] > 0:
                self.t.goto(p["x"], p["y"])
                self.t.dot(4)
                yeni.append(p)

        self.parcaciklar = yeni


gaz_sistemi = GazSistemi()

# ================== İHA SINIFI ==================
class IHA:
    def __init__(self, renk, x, y, rol, takip_mesafe=20, hiz=3):
        self.x = x
        self.y = y
        self.rol = rol
        self.takip_mesafe = takip_mesafe
        self.hiz = hiz

        self.t = turtle.Turtle()
        self.t.color(renk)
        self.t.shape("triangle")
        self.t.penup()
        self.t.goto(x, y)
        self.t.setheading(90)

        self.gecmis = [(x, y)] if rol == "Lider" else None

    def gaz_birak(self):
        aci = math.radians(self.t.heading())
        gx = self.x - math.cos(aci) * 10
        gy = self.y - math.sin(aci) * 10
        gaz_sistemi.ekle(gx, gy)

    def git(self, dx, dy):
        self.x += dx
        self.y += dy
        self.t.goto(self.x, self.y)
        self.gaz_birak()

        if self.rol == "Lider":
            self.gecmis.append((self.x, self.y))

    def hedefe_git(self, hx, hy):
        dx = hx - self.x
        dy = hy - self.y
        mesafe = math.hypot(dx, dy)

        if mesafe < self.takip_mesafe:
            return

        dx /= mesafe
        dy /= mesafe

        aci = math.degrees(math.atan2(dy, dx))
        self.t.setheading(aci)
        self.git(dx * self.hiz, dy * self.hiz)


# ================== EKRAN ==================
ekran = turtle.Screen()
ekran.bgcolor("black")
ekran.title("Geçmişe Dayalı İHA Takip Sistemi")
ekran.tracer(0)

# ================== KOORDİNAT YAZICI ==================
yazici = turtle.Turtle()
yazici.hideturtle()
yazici.color("white")
yazici.penup()
yazici.goto(-380, 260)

def koordinat_yaz(lider):
    yazici.clear()
    yazici.write(
        f"Lider Koordinatları\nX: {lider.x:.1f}\nY: {lider.y:.1f}",
        font=("Arial", 12, "bold")
    )

# ================== LİDER ==================
lider = IHA("white", 0, 0, "Lider", hiz=6)

# ================== TAKİPÇİLER ==================
takipciler = [
    IHA("blue", -40, -40, "Takipçi"),
    IHA("yellow", -60, -60, "Takipçi"),
    IHA("green", -80, -80, "Takipçi")
]

# ================== WASD KONTROL ==================
def w(): lider.git(0, 15)
def s(): lider.git(0, -15)
def a(): lider.git(-15, 0)
def d(): lider.git(15, 0)

ekran.listen()
ekran.onkeypress(w, "w")
ekran.onkeypress(s, "s")
ekran.onkeypress(a, "a")
ekran.onkeypress(d, "d")

# ================== ANA GÜNCELLEME ==================
def guncelle():
    gecmis = lider.gecmis

    hedef_indeksleri = [-5, -10, -15]

    for takipci, idx in zip(takipciler, hedef_indeksleri):
        if len(gecmis) >= abs(idx):
            hx, hy = gecmis[idx]
            takipci.hedefe_git(hx, hy)

    gaz_sistemi.guncelle()
    koordinat_yaz(lider)

    ekran.update()
    ekran.ontimer(guncelle, 30)

guncelle()
turtle.mainloop()
