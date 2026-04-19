import tkinter as tk
from tkinter import messagebox, ttk

#DATA GEJALA
GEJALA = {
    "G1": "Nafas abnormal",
    "G2": "Suara serak",
    "G3": "Perubahan kulit",
    "G4": "Telinga penuh",
    "G5": "Nyeri bicara/menelan",
    "G6": "Nyeri tenggorokan",
    "G7": "Nyeri leher",
    "G8": "Pendarahan hidung",
    "G9": "Telinga berdenging",
    "G10": "Air liur menetes",
    "G11": "Perubahan suara",
    "G12": "Sakit kepala",
    "G13": "Nyeri pinggir hidung",
    "G14": "Serangan vertigo",
    "G15": "Getah bening",
    "G16": "Leher bengkak",
    "G17": "Hidung tersumbat",
    "G18": "Infeksi sinus",
    "G19": "Berat badan turun",
    "G20": "Nyeri telinga",
    "G21": "Selaput lendir merah",
    "G22": "Benjolan leher",
    "G23": "Tubuh tak seimbang",
    "G24": "Bola mata bergerak",
    "G25": "Nyeri wajah",
    "G26": "Dahi sakit",
    "G27": "Batuk",
    "G28": "Tumbuh di mulut",
    "G29": "Benjolan di leher",
    "G30": "Nyeri antara mata",
    "G31": "Radang gendang telinga",
    "G32": "Tenggorokan gatal",
    "G33": "Hidung meler",
    "G34": "Tuli",
    "G35": "Mual muntah",
    "G36": "Letih lesu",
    "G37": "Demam",
}

#DATA PENYAKIT DAN GEJALANYA
PENYAKIT = {
    "Tonsilitis": ["G37", "G12", "G5", "G27", "G6", "G21"],
    "Sinusitis Maksilaris": ["G37", "G12", "G27", "G17", "G33", "G36", "G29"],
    "Sinusitis Frontalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G26"],
    "Sinusitis Edmoidalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G30", "G13", "G26"],
    "Sinusitis Sfenoidalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G29", "G7"],
    "Abses Peritonsiler": ["G37", "G12", "G6", "G15", "G2", "G29", "G10"],
    "Faringitis": ["G37", "G5", "G6", "G7", "G15"],
    "Kanker Laring": ["G5", "G27", "G6", "G15", "G2", "G19", "G1"],
    "Deviasi Septum": ["G37", "G17", "G20", "G8", "G18", "G25"],
    "Laringitis": ["G37", "G5", "G15", "G16", "G32"],
    "Kanker Leher & Kepala": ["G5", "G22", "G8", "G28", "G3", "G11"],
    "Otitis Media Akut": ["G37", "G20", "G35", "G31"],
    "Contact Ulcers": ["G5", "G2"],
    "Abses Parafaringeal": ["G5", "G16"],
    "Barotitis Media": ["G12", "G20"],
    "Kanker Nafasoring": ["G17", "G8"],
    "Kanker Tonsil": ["G6", "G29"],
    "Neuronitis Vestibularis": ["G35", "G24"],
    "Meniere": ["G20", "G35", "G14", "G4"],
    "Tumor Syaraf Pendengaran": ["G12", "G34", "G23"],
    "Kanker Leher Metastatik": ["G29"],
    "Osteosklerosis": ["G34", "G9"],
    "Vertigo Postular": ["G24"],
}


def semua_gejala_unik():
    urut = []
    for daftar in PENYAKIT.values():
        for kode in daftar:
            if kode not in urut:
                urut.append(kode)
    return urut


class SistemPakarTHT:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Sistem Pakar Diagnosa Penyakit THT")
        self.root.geometry("760x520")
        self.root.minsize(760, 520)

        self.urutan_gejala = semua_gejala_unik()
        self.index = 0
        self.gejala_positif = set()

        self._buat_widget()
        self._reset_tampilan_awal()

    def _buat_widget(self):
        container = ttk.Frame(self.root, padding=16)
        container.pack(fill="both", expand=True)

        ttk.Label(
            container,
            text="Aplikasi Sistem Pakar Diagnosa Penyakit THT",
            font=("Arial", 16, "bold"),
        ).pack(anchor="center", pady=(0, 12))

        self.status_var = tk.StringVar()
        ttk.Label(container, textvariable=self.status_var, font=("Arial", 10, "italic")).pack(anchor="w")

        self.pertanyaan_var = tk.StringVar()
        self.kotak_pertanyaan = ttk.Label(
            container,
            textvariable=self.pertanyaan_var,
            relief="solid",
            padding=16,
            anchor="center",
            justify="center",
            font=("Arial", 12),
            wraplength=680,
        )
        self.kotak_pertanyaan.pack(fill="x", pady=12)

        tombol_frame = ttk.Frame(container)
        tombol_frame.pack(pady=8)

        self.btn_ya = ttk.Button(tombol_frame, text="Ya", command=lambda: self.jawab(True))
        self.btn_ya.grid(row=0, column=0, padx=8)

        self.btn_tidak = ttk.Button(tombol_frame, text="Tidak", command=lambda: self.jawab(False))
        self.btn_tidak.grid(row=0, column=1, padx=8)

        self.btn_mulai = ttk.Button(container, text="Mulai Diagnosa", command=self.mulai_diagnosa)
        self.btn_mulai.pack(pady=(8, 14))

        ttk.Label(container, text="Riwayat gejala positif:").pack(anchor="w")
        self.listbox = tk.Listbox(container, height=10)
        self.listbox.pack(fill="both", expand=True, pady=(6, 0))

    def _reset_tampilan_awal(self):
        self.status_var.set("Klik tombol mulai untuk memulai diagnosa.")
        self.pertanyaan_var.set("Sistem akan menanyakan gejala satu per satu.")
        self.btn_ya.state(["disabled"])
        self.btn_tidak.state(["disabled"])
        self.btn_mulai.state(["!disabled"])
        self.listbox.delete(0, tk.END)

    def mulai_diagnosa(self):
        self.index = 0
        self.gejala_positif = set()
        self.listbox.delete(0, tk.END)
        self.btn_ya.state(["!disabled"])
        self.btn_tidak.state(["!disabled"])
        self.btn_mulai.state(["disabled"])
        self._tampilkan_pertanyaan()

    def _tampilkan_pertanyaan(self):
        if self.index >= len(self.urutan_gejala):
            self.proses_hasil()
            return

        kode = self.urutan_gejala[self.index]
        self.status_var.set(f"Pertanyaan {self.index + 1} dari {len(self.urutan_gejala)}")
        self.pertanyaan_var.set(f"Apakah Anda mengalami {GEJALA[kode].lower()}?")

    def jawab(self, ya: bool):
        if self.index >= len(self.urutan_gejala):
            return

        kode = self.urutan_gejala[self.index]
        if ya:
            self.gejala_positif.add(kode)
            self.listbox.insert(tk.END, f"{kode} - {GEJALA[kode]}")

        self.index += 1
        self._tampilkan_pertanyaan()

    def proses_hasil(self):
        exact = []
        ranking = []
        for nama, daftar_gejala in PENYAKIT.items():
            syarat = set(daftar_gejala)
            cocok = self.gejala_positif & syarat
            skor = len(cocok)
            total = len(syarat)
            persentase = (skor / total) * 100 if total else 0
            ranking.append((nama, skor, total, persentase))
            if syarat.issubset(self.gejala_positif):
                exact.append((nama, skor, total, persentase))

        ranking.sort(key=lambda x: (-x[3], -x[1], x[2], x[0]))

        if exact:
            isi = ["Penyakit yang cocok 100%:"]
            for nama, skor, total, persentase in exact:
                isi.append(f"- {nama} ({skor}/{total} gejala, {persentase:.0f}%)")
        else:
            isi = ["Tidak ada penyakit yang cocok 100%.", "Kemungkinan terdekat:"]
            kandidat = [item for item in ranking[:5] if item[1] > 0]
            if kandidat:
                for nama, skor, total, persentase in kandidat:
                    isi.append(f"- {nama} ({skor}/{total} gejala, {persentase:.0f}%)")
            else:
                isi.append("- Belum ada gejala yang cukup untuk menentukan penyakit.")

        isi.append("\nCatatan: hasil ini hanya simulasi pembelajaran, bukan pengganti diagnosis dokter.")
        messagebox.showinfo("Hasil Diagnosa", "\n".join(isi))

        self._reset_tampilan_awal()
        self.status_var.set("Diagnosa selesai. Klik mulai untuk mengulang.")
        self.pertanyaan_var.set("Proses diagnosa selesai.")


if __name__ == "__main__":
    root = tk.Tk()
    app = SistemPakarTHT(root)
    root.mainloop()
