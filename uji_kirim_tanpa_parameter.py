"""Percobaan 2, pertanyaan 3: kirim(self) tanpa parameter."""
from core.protocols import Notifier


class WhatsAppRusak:
    def kirim(self):
        print("tidak punya parameter")


print("isinstance(WhatsAppRusak(), Notifier) =", isinstance(WhatsAppRusak(), Notifier))
try:
    WhatsAppRusak().kirim("a@b.c", "halo")
except TypeError as e:
    print("Saat dipanggil sungguhan ->", type(e).__name__ + ":", e)
