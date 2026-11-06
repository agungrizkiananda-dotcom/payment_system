"""Percobaan 4, pertanyaan 2: buat_metode() sebelum muat_semua_plugin()."""
from core.registry import buat_metode, daftar_plugin

print("Plugin terdaftar sebelum muat_semua_plugin():", daftar_plugin())
try:
    buat_metode("transfer")
except KeyError as e:
    print("KeyError:", e)
