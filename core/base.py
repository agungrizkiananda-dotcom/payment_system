from abc import ABC, abstractmethod

from core.utils import rupiah


class PembayaranGagal(Exception):
    """Dilempar saat pembayaran ditolak atau tidak valid."""


class PaymentMethod(ABC):
    """Kontrak (abstract base class) untuk semua metode pembayaran."""

    def __init__(self, nama: str):
        self.nama = nama

    @abstractmethod
    def validasi(self, jumlah: float) -> bool:
        """Periksa apakah pembayaran dapat diproses."""

    @abstractmethod
    def bayar(self, jumlah: float) -> str:
        """Proses pembayaran, lalu kembalikan ID transaksi."""

    @abstractmethod
    def biaya_admin(self, jumlah: float) -> float:
        """Hitung biaya admin untuk pembayaran sebesar jumlah."""

    def proses(self, jumlah: float) -> str:
        """Template method: urutan langkah dijaga oleh kelas induk.

        Validasi dan pemotongan saldo memakai total = jumlah + biaya admin.
        """
        if jumlah <= 0:
            raise PembayaranGagal("Jumlah pembayaran harus lebih dari 0")
        biaya = self.biaya_admin(jumlah)
        total = jumlah + biaya
        if not self.validasi(total):
            raise PembayaranGagal(
                f"{self.nama} menolak pembayaran {rupiah(jumlah)} "
                f"(total dengan biaya admin {rupiah(total)})"
            )
        return self.bayar(total)
