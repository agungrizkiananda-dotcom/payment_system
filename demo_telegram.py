"""Bukti Tugas 2: TelegramNotifier memenuhi Protocol tanpa pewarisan."""
from core.notifiers import TelegramNotifier
from core.processor import PaymentProcessor
from core.protocols import Notifier
from core.registry import buat_metode
from plugins import muat_semua_plugin

muat_semua_plugin()

telegram = TelegramNotifier()
print("Basis kelas TelegramNotifier:", TelegramNotifier.__bases__)
print("isinstance(TelegramNotifier(), Notifier) =", isinstance(telegram, Notifier))

pemroses = PaymentProcessor(telegram)
pemroses.checkout(buat_metode("qris"), 75_000, "@mahasiswa_utr")
