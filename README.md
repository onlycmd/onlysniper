# 🎯 OnlySniper - Professional Discord Vanity Sniper

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/Maintained%3F-yes-brightgreen?style=for-the-badge" alt="Maintained">
</p>

---

## 🇹🇷 Türkçe Açıklama

**OnlySniper**, Discord sunucuları için özel URL'leri (vanity URL) milisaniyeler içinde yakalamak üzere tasarlanmış, yüksek performanslı ve profesyonel bir araçtır.

### ✨ Özellikler
- **TLS Fingerprinting:** `curl_cffi` kullanarak gerçek bir Chrome 110 tarayıcısı gibi davranır. Cloudflare ve Discord bot korumalarını bypass eder.
- **Otomatik Token Doğrulama:** Başlangıçta tüm tokenları kontrol eder, geçersiz olanları ayıklar.
- **Çoklu Token Desteği:** Birden fazla hesap kullanarak rate limit riskini minimize eder.
- **Asenkron Mimari:** `asyncio` ile en yüksek hızda çalışma.
- **Webhook Entegrasyonu:** URL alındığında Discord üzerinden anlık bildirim gönderir.
- **Proxy Desteği:** IP ban riskine karşı proxy rotasyonu.

### 🚀 Kurulum ve Kullanım
1. Bağımlılıkları kurun: `pip install -r requirements.txt`
2. `config.json` dosyasını düzenleyin (Hedef URL ve Sunucu ID).
3. `tokens.txt` dosyasına Discord tokenlarınızı ekleyin.
4. `start.bat` dosyasına çift tıklayarak başlatın.

---

## 🇺🇸 English Description

**OnlySniper** is a high-performance, professional-grade tool designed to claim Discord vanity URLs within milliseconds.

### ✨ Features
- **TLS Fingerprinting:** Uses `curl_cffi` to impersonate a real Chrome 110 browser. Bypasses Cloudflare and Discord bot protections.
- **Automatic Token Validation:** Checks all tokens at startup and filters out invalid ones.
- **Multi-Token Support:** Use multiple accounts to minimize rate limit risks.
- **Asynchronous Architecture:** Powered by `asyncio` for maximum speed.
- **Webhook Integration:** Sends instant Discord notifications when a URL is claimed.
- **Proxy Support:** Proxy rotation to prevent IP bans.

### 🚀 Installation & Usage
1. Install dependencies: `pip install -r requirements.txt`
2. Edit `config.json` (Target URL and Guild ID).
3. Add your Discord tokens to `tokens.txt`.
4. Double-click `start.bat` to launch.

---

## ⚠ Important Tips / Önemli İpuçları

> [!WARNING]
> **Thread Management / Thread Yönetimi:**
> - **EN:** Keep the `threads` count in `config.json` balanced with your token count. For 1 token, 5-10 threads are ideal. Too many threads may cause your tokens to get rate-limited or flagged quickly.
> - **TR:** `config.json` içindeki `threads` sayısını token sayınıza göre dengeli tutun. 1 token için 5-10 thread idealdir. Çok fazla thread kullanmak, tokenlarınızın hızlıca rate limit yemesine veya işaretlenmesine (flag) neden olabilir.

---

## �📂 Project Structure / Proje Yapısı
- `onlysniper.py`: Main engine / Ana motor.
- `config.json`: Settings / Ayarlar.
- `tokens.txt`: Discord tokens / Token listesi.
- `proxies.txt`: Proxy list / Proxy listesi.
- `start.bat`: Easy launcher / Kolay başlatıcı.

---

## ⭐ Support / Destek
If you like this project, please consider giving it a **Star** and **Forking** it! Your support helps me improve the tool further.

Eğer bu projeyi beğendiyseniz, lütfen bir **Yıldız (Star)** vermeyi ve **Forklamayı** unutmayın! Desteğiniz projeyi geliştirmem için bana motivasyon sağlıyor.

---

## ⚠️ Disclaimer / Uyarı
This tool is for educational purposes only. Using automated tools on Discord may violate their Terms of Service. Use at your own risk.

Bu araç sadece eğitim amaçlıdır. Discord üzerinde otomatize araçlar kullanmak hizmet şartlarını ihlal edebilir. Tüm sorumluluk kullanıcıya aittir.
