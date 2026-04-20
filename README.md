# 🚀 OnlySniper - Elite Edition (v2.0.0)

![License](https://img.shields.io/github/license/onlycmd/onlysniper?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-2.0.0--Elite-magenta?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge)

**OnlySniper Elite** is a high-performance, professional Discord Vanity URL sniper designed for speed, stealth, and ease of use. It mimics official Discord clients to minimize detection and maximizes claim success with optimized asynchronous requests.

---

## ✨ Features / Özellikler

### 🌍 English
- **🚀 Ultra-Fast Claims:** Optimized asynchronous logic for millisecond-level reaction times.
- **🎨 Rich Terminal UI:** Professional dashboard with live statistics (CPS, Errors, Checks).
- **🛡️ Stealth Mode:** Advanced TLS fingerprinting that mimics the **Discord Desktop (Electron)** client.
- **🔑 Auto 2FA Automation:** Automatically generates and submits 2FA codes using `pyotp`.
- **📦 Smart Dependencies:** Automatically detects and installs missing modules on startup.
- **📑 Detailed Diagnostics:** Real-time token health checks (MFA status, Validity).

### 🇹🇷 Türkçe
- **🚀 Ultra Hızlı:** Milisaniye düzeyinde tepki süresi için optimize edilmiş asenkron mantık.
- **🎨 Zengin Arayüz:** Canlı istatistikler (CPS, Hata, Sorgu) içeren profesyonel panel.
- **🛡️ Gizlilik Modu:** **Discord Masaüstü (Electron)** uygulamasını taklit eden gelişmiş TLS parmak izi.
- **🔑 Otomatik 2FA:** `pyotp` kullanarak 2FA kodlarını otomatik üretir ve gönderir.
- **📦 Akıllı Bağımlılıklar:** Eksik modülleri açılışta otomatik algılar ve kurar.
- **📑 Detaylı Analiz:** Token sağlığını (MFA durumu, Geçerlilik) anlık doğrular.

---

## 🛠️ Configuration / Kurulum (config.json)

```json
{
    "guild_id": "YOUR_SERVER_ID",
    "target_url": "target-vanity",
    "webhook_url": "YOUR_DISCORD_WEBHOOK",
    "threads": 10,
    "check_interval": 0.05,
    "use_proxies": false,
    "two_factor_secret": "YOUR_2FA_SECRET_KEY"
}
```

---

## 🚀 Getting Started / Başlangıç

### Prerequisites
- Python 3.8 or higher.
- A valid Discord Token with Manage Server permissions on the target guild.

### Direct Run (Auto-Install)
Simply run the script. It will automatically ask to install missing dependencies:
```bash
python onlysniper.py
```

### Manual Installation
```bash
pip install -r requirements.txt
```

---

## 📸 Screenshots / Görseller

*(New V2.0 Dashboard Interface)*
> [!NOTE]
> The software features a dynamic LIVE panel showing your real-time performance.

---

## ⚠️ Disclaimer / Uyarı
This tool is for educational purposes only. Self-botting is against Discord's Terms of Service. Use at your own risk.

Bu araç sadece eğitim amaçlıdır. Self-bot kullanımı Discord Hizmet Şartları'na aykırıdır. Tüm sorumluluk kullanıcıya aittir.

---

## 🤝 Contributing
Feel free to open issues or submit pull requests to improve the speed and stealth of OnlySniper!

---
**Developed with ❤️ by [onlycmd](https://github.com/onlycmd)**
