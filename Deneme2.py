import turtle
import time
import math

print("İHA kontrol sistemine hoş geldiniz")


class İHA:
    def __init__(self, renk, konum_x, konum_y, rol, takip_mesafe=30):
        self.renk = renk
        self.konum_x = konum_x
        self.konum_y = konum_y
        self.rol = rol
        self.takip_mesafe = takip_mesafe
        self.turtle = turtle.Turtle()
        self.turtle.color(renk)
        self.turtle.shape("triangle")
        self.turtle.penup()
        self.turtle.goto(konum_x, konum_y)
        self.turtle.pendown()

        # Liderin geçmişini tutacak liste
        self.gecmis = [(konum_x, konum_y)] if rol == "Lider" else []

    def git(self, yeni_x, yeni_y):
        self.konum_x = yeni_x
        self.konum_y = yeni_y
        self.turtle.goto(yeni_x, yeni_y)
        if self.rol == "Lider":
            self.gecmis.append((yeni_x, yeni_y))


# Lider ve takipçiler
lider = İHA("white", 0, 0, "Lider")
takipciler = [
    İHA("blue", -40, -40, "Takipçi", takip_mesafe=50),
    İHA("yellow", -60, -60, "Takipçi", takip_mesafe=50),
    İHA("green", -80, -80, "Takipçi", takip_mesafe=50)
]

# Sonsuz işareti parametreleri
a = 300  # ölçek
fps = 10000  # saniye başına kare
adim = 1  # açı adımı (hız kontrolü)

turtle.bgcolor("black")
turtle.title("İHA Sonsuz Döngü Sonsuz İşareti Takip Sistemi")

t_angle = 0  # başlangıç açısı

# Sonsuz döngü
while True:
    # Sonsuz işareti koordinatları (lemniscate of Gerono)
    x = a * math.sin(math.radians(t_angle))
    y = a * math.sin(math.radians(t_angle)) * math.cos(math.radians(t_angle))

    lider.git(x, y)

    # Takipciler lideri ve birbirlerini takip ederek konum güncelleyecek
    for i, takipci in enumerate(takipciler):
        hedef_x, hedef_y = lider.konum_x, lider.konum_y
        if i > 0:
            onceki = takipciler[i - 1]
            hedef_x, hedef_y = onceki.konum_x, onceki.konum_y

        dx = hedef_x - takipci.konum_x
        dy = hedef_y - takipci.konum_y
        mesafe = math.sqrt(dx * dx + dy * dy)

        if mesafe > takipci.takip_mesafe:
            oran = (mesafe - takipci.takip_mesafe) / mesafe
            yeni_x = takipci.konum_x + dx * oran
            yeni_y = takipci.konum_y + dy * oran
            takipci.git(yeni_x, yeni_y)

    t_angle += adim
    if t_angle >= 360:
        t_angle -= 360  # açı sürekli 0-360 arasında kalacak

    time.sleep(1 / fps)
