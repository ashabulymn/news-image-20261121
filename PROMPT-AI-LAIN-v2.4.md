# Prompt untuk AI lain — audit editorial independen v2.4 (adaptasi dari prompt v2.3, 21 Nov 2026)

Prompt ini adalah adaptasi dari PROMPT-AI-LAIN-v2.3.md (yang disusun ChatGPT). Dipakai untuk memeriksa kandidat v2.4 sebelum submit — submit ini kemungkinan yang terakhir, jadi audit harus setajam mungkin. Jawab dalam Bahasa Indonesia.

---

INDEPENDENT EDITORIAL AUDIT — KITA v2.4
Target: Top 1 — World News in One Image, 21 November 2026

Bertindak sebagai:
- International newspaper picture editor.
- Senior infographic designer.
- Fact-checking editor.
- Visual communication auditor.
- Competitive AI-image evaluator.

Tujuan: menghasilkan satu keputusan objektif tentang apakah gambar layak disubmit dan perubahan apa yang paling meningkatkan peluang menang.

## A. WAJIB MEMERIKSA SUMBER

Buka dan periksa:
1. Gambar final 1024×1024.
2. Gambar 300×300.
3. Gambar perbandingan rank 1, rank 10, v2.3, dan kandidat terbaru (v2.4).
4. Halaman asli rank 1 dan rank 10.
5. Halaman bounty dan leaderboard.
6. Seluruh berita yang tercantum dalam gambar.
7. Repository dan prompt produksi.

Jangan mengklaim telah membuka sumber yang gagal diakses.

## B. AUDIT FAKTA

Buat tabel untuk setiap berita: Nomor berita. Headline. Tanggal kejadian. Tanggal publikasi. Zona waktu. Angka dan klaim utama. Sumber primer atau sumber berita tepercaya. Status: verified, questionable, incorrect, atau unverified. Tindakan: keep, rewrite, replace, atau remove.

Aturan:
- Prioritaskan kejadian pada Sabtu 21 November 2026 UTC.
- Bedakan kejadian pada 20 November lokal dengan laporan 21 November UTC.
- Jangan menyamakan tanggal publikasi dengan tanggal kejadian.
- Jangan membuat angka atau konteks tambahan.
- Klaim yang belum terverifikasi harus ditandai atau dihilangkan.
- Jangan mengisi kekosongan berita dengan informasi rekaan.

## C. AUDIT VISUAL

Nilai gambar dalam dua kondisi: 1. 1024×1024. 2. 300×300.

Periksa: Hierarki judul dan headline. KPI. Hero illustrations. Kartu berita. Wire. Peta dan legenda. DATE CHECK. Footer dan sumber. Periksa kontras, ukuran font, keterbacaan, pemotongan, overlap, dan konsistensi ilustrasi. Jangan menganggap teks terbaca hanya karena dapat dibaca ketika diperbesar.

## D. PERBANDINGAN KOMPETITIF

Bandingkan secara spesifik: Rank 1. Rank 10. KITA v2.3 (kandidat sebelumnya). KITA v2.4 (kandidat terbaru). Jelaskan keunggulan dan kekurangan setiap gambar berdasarkan elemen visual yang benar-benar terlihat. Jangan menganggap jumlah cerita yang lebih banyak otomatis lebih baik.

## E. PENILAIAN RESMI

Berikan skor 1–5:
1. One-day news.
2. Selection and breadth.
3. Readability.
4. Faithfulness.
5. Craft.

Berikan alasan konkret untuk setiap skor. Pisahkan skor editorial dari prediksi hasil kompetisi.

## F. OPTIMASI

Buat tiga daftar:
- WAJIB: Perubahan yang dapat mencegah kehilangan skor besar.
- OPSIONAL: Perubahan yang berpotensi memperkuat desain.
- JANGAN DIUBAH: Elemen yang sudah bekerja dengan baik.

Optimalkan untuk pembacaan pada ukuran 300×300. Pertahankan kualitas berita lebih tinggi daripada jumlah berita.

## G. KEPUTUSAN AKHIR

Pilih satu: SUBMIT AS IS. / REVISE BEFORE SUBMIT. / KEEP CURRENT LIVE ENTRY.

Kemudian berikan: Prediksi skor dengan rentang, bukan angka palsu yang presisi. Risiko terbesar. Peluang masuk 50 besar. Peluang 10 besar. Peluang juara pertama. Daftar perubahan final berdasarkan dampak. Jangan menjanjikan kemenangan.

## H. PRINSIP UTAMA

Factual accuracy > jumlah berita. Readability > kepadatan. Editorial hierarchy > dekorasi. Specific events > generic headlines. Clear attribution > unsupported claims.

Jangan mengarang fakta untuk membuat desain terlihat lebih lengkap. Berikan hasil dalam Bahasa Indonesia, langsung, kritis, dan spesifik.

---

## Konteks v2.3 → v2.4 (yang berubah)

Dua review v2.3: ChatGPT 16,5/25 (vonis revisi; standar UTC ketat) dan nanoMuse 18/25 (vonis revisi; tabelnya mencampur v2.3 dengan entri live). Satu kesalahan nyata yang ditemukan dan sudah diperbaiki di v2.4: wire 28 Ahmedabad (final Jumat 20 Nov di semua zona waktu) diganti ROME — protes Gen Z biaya hidup berlanjut Sabtu di Eropa, mogok transport Italia (CNN). Satu butir lemah yang diganti: wire 29 Nusseibeh "believed to have blocked" diganti WASHINGTON — FBI menyelidiki dugaan peretasan database kejahatan nasional NCIC (Reuters, artikel 21 Nov). Tambahan kecil: jam Davao di kartu 11 kini "~00:08 PHT". Selebihnya v2.4 identik dengan v2.3 (diff terverifikasi: hanya 8 baris berubah).

## Link yang dipakai

- v2.4 ukuran penuh: https://raw.githubusercontent.com/ashabulymn/news-image-20261121/main/preview-v2.4.png
- v2.4 versi 300px: https://raw.githubusercontent.com/ashabulymn/news-image-20261121/main/preview-300px-v2.4.png
- Gambar perbandingan terbaru (rank 1, rank 10, v2.3, v2.4): https://raw.githubusercontent.com/ashabulymn/news-image-20261121/main/perbandingan-v2.4-rank1-rank10.png
- v2.3 ukuran penuh (kandidat sebelumnya): https://raw.githubusercontent.com/ashabulymn/news-image-20261121/main/preview-v2.3.png
- Rank 1 — @samatch-we, 99,1923% (12-0-0), 35 cerita, $20: https://make.fun/s/01a1fc1b-a9c9-7076-88f4-3f07ba3a5936
- Rank 10 saat ini (19:29 WIB) — @guy-sensei, 99,0173% (11-1-0), 36 cerita, $2: https://make.fun/s/01a1fbfa-733d-755e-9393-dacfdbcaf5c4
- Catatan: panel rank 10 di gambar perbandingan adalah @sunny-panda-23 (98,9984%, 35 cerita, $2) dari snapshot 18:12 WIB — ia sudah keluar dari 10 besar per 19:29 WIB: https://make.fun/s/01a1fbec-e9b9-76c0-8a7c-0d8f5710a164
- Entri live kami (v2) — @ashabul-yamin, 97,0079% (11-1-0), #2209 per 19:29 WIB: https://make.fun/s/01a1fd11-c6df-70b2-a2b6-e7e4eab22d25
- Halaman bounty (S&K + feed live): https://make.fun/bounty/news-image-20261121
- Leaderboard live: https://make.fun/bounty/news-image-20261121/leaderboard
