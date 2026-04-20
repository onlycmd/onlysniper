import asyncio
import random
import json
import os
import sys
import subprocess
import time
from datetime import datetime
from typing import List, Optional, Dict

def check_and_install_dependencies():
    required = ["rich", "curl_cffi", "pyotp"]
    missing = []
    
    for module in required:
        try:
            if module == "curl_cffi":
                import curl_cffi
            elif module == "pyotp":
                import pyotp
            elif module == "rich":
                import rich
        except ImportError:
            missing.append(module)
            
    if missing:
        print(f"Missing modules: {', '.join(missing)}")
        choice = input("Would you like to install them now? (Y/N): ").strip().lower()
        if choice == 'y':
            print("Installing modules... Please wait.")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", *missing])
                print("Modules installed successfully! Restarting software...")
                os.execv(sys.executable, ['python'] + sys.argv)
            except Exception as e:
                print(f"Installation failed: {e}")
                sys.exit(1)
        else:
            print("Cannot continue without missing modules. Exiting.")
            sys.exit(1)

# Check dependencies before anything else
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--no-check":
        pass 
    else:
        check_and_install_dependencies()

# Now it is safe to import rich and others
try:
    import pyotp
    from curl_cffi.requests import AsyncSession
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.live import Live
    from rich.layout import Layout
    from rich import box
except ImportError:
    # This should not happen if the check passed, but for safety:
    print("Dependencies not found. Run the script again.")
    sys.exit(1)

# --- VERSION ---
VERSION = "2.0.0 - ELITE EDITION"

# --- GLOBAL CONSOLE ---
console = Console()

class ProfessionalLogger:
    @staticmethod
    def banner():
        banner_text = f"""
  [bold magenta]██████╗ ███╗   ██╗██╗     ██╗   ██╗███████╗███╗   ██╗██╗██████╗ ███████╗██████╗ [/bold magenta]
  [bold magenta]██╔═══██╗████╗  ██║██║     ╚██╗ ██╔╝██╔════╝████╗  ██║██║██╔══██╗██╔════╝██╔══██╗[/bold magenta]
  [bold magenta]██║   ██║██╔██╗ ██║██║      ╚████╔╝ ███████╗██╔██╗ ██║██║██████╔╝█████╗  ██████╔╝[/bold magenta]
  [bold magenta]██║   ██║██║╚██╗██║██║       ╚██╔╝  ╚════██║██║╚██╗██║██║██╔═══╝ ██╔══╝  ██╔══██╗[/bold magenta]
  [bold cyan]╚██████╔╝██║ ╚████║███████╗   ██║   ███████║██║ ╚████║██║██║     ███████╗██║  ██║[/bold cyan]
  [bold cyan] ╚═════╝ ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═══╝╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝[/bold cyan]
                                [italic white]Professional Discord Vanity Sniper - {VERSION}[/italic white]
        """
        console.print(banner_text)

    @staticmethod
    def info(msg):
        console.print(f"[bold cyan][[info]] [/bold cyan][white]{msg}[/white]")

    @staticmethod
    def success(msg):
        console.print(f"[bold green][[+]] [/bold green][bold white]{msg}[/bold white]")

    @staticmethod
    def warn(msg):
        console.print(f"[bold yellow][[!]] [/bold yellow][yellow]{msg}[/yellow]")

    @staticmethod
    def error(msg):
        console.print(f"[bold red][[error]] [/bold red][white]{msg}[/white]")

    @staticmethod
    def attack(msg):
        console.print(f"[bold magenta][[ATTACK]] [/bold magenta][bold red]{msg}[/bold red]")

class OnlySniperElite:
    def __init__(self):
        self.config = self._load_config()
        self.tokens = self._load_list("tokens.txt")
        self.proxies = self._load_list("proxies.txt")
        
        self.guild_id = self.config.get("guild_id")
        self.target_url = self.config.get("target_url")
        self.webhook_url = self.config.get("webhook_url")
        self.threads = self.config.get("threads", 10)
        self.interval = self.config.get("check_interval", 0.05)
        self.mfa_secret = self.config.get("two_factor_secret")
        
        self.found = False
        self.headers_list = []
        self.stats = {"checks": 0, "errors": 0, "start_time": time.time()}

    def _load_config(self) -> dict:
        try:
            with open("config.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            ProfessionalLogger.error(f"Config could not be loaded: {e}")
            sys.exit(1)

    def _load_list(self, path) -> List[str]:
        if not os.path.exists(path):
            return []
        with open(path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip() and not line.startswith("#")]

    def _get_discord_headers(self, token: str) -> dict:
        """Mimics official Discord Desktop Client headers for higher trust."""
        return {
            "Authorization": token,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9015 Chrome/108.0.5359.215 Electron/22.3.26 Safari/537.36",
            "X-Discord-Locale": "tr-TR",
            "X-Debug-Options": "bugReporterEnabled",
            "Accept": "*/*",
        }

    async def validate_all_tokens(self):
        """Advanced token diagnostics with a UI table."""
        table = Table(title="Token Health Report", box=box.ROUNDED)
        table.add_column("Username", style="cyan")
        table.add_column("2FA", justify="center")
        table.add_column("Status", justify="center")
        
        ProfessionalLogger.info("Diagnosing tokens...")
        
        async with AsyncSession(impersonate="chrome110") as session:
            for token in self.tokens:
                try:
                    headers = self._get_discord_headers(token)
                    resp = await session.get("https://discord.com/api/v10/users/@me", headers=headers)
                    
                    if resp.status_code == 200:
                        data = resp.json()
                        mfa = "[bold green]ON[/bold green]" if data.get("mfa_enabled") else "[bold red]OFF[/bold red]"
                        table.add_row(f"{data['username']}", mfa, "[green]VALID[/green]")
                        self.headers_list.append(headers)
                    else:
                        table.add_row(f"Unknown ({token[:10]}...)", "N/A", "[red]INVALID[/red]")
                except Exception:
                    table.add_row(f"Error ({token[:10]}...)", "N/A", "[red]ERROR[/red]")

        console.print(table)
        if not self.headers_list:
            ProfessionalLogger.error("No valid tokens! Exiting.")
            sys.exit(1)

    async def send_webhook(self, content: str):
        if not self.webhook_url: return
        async with AsyncSession() as session:
            try: await session.post(self.webhook_url, json={"content": content})
            except: pass

    async def claim(self, session: AsyncSession, base_header: dict):
        """Ultra-fast claim logic."""
        url = f"https://discord.com/api/v10/guilds/{self.guild_id}/vanity-url"
        payload = {"code": self.target_url}
        header = base_header.copy()
        
        if self.mfa_secret:
            totp = pyotp.TOTP(self.mfa_secret.replace(" ", ""))
            header["X-Discord-MFA"] = totp.now()

        try:
            resp = await session.patch(url, headers=header, json=payload)
            if resp.status_code in [200, 204]:
                self.found = True
                ProfessionalLogger.attack(f"URL SECURED: discord.gg/{self.target_url}")
                await self.send_webhook(f"🚀 **BOOM! URL ALINDI!**\nURL: discord.gg/{self.target_url}\nZaman: {datetime.now()}")
                return True
            else:
                ProfessionalLogger.error(f"Claim failed | Status: {resp.status_code} | Reason: {resp.text}")
        except Exception as e:
            ProfessionalLogger.error(f"Critical Claim Exception: {e}")
        return False

    async def worker(self, worker_id: int):
        """High-performance worker loop."""
        proxy = random.choice(self.proxies) if self.proxies and self.config.get("use_proxies") else None
        
        async with AsyncSession(
            proxies={"http": proxy, "https": proxy} if proxy else None,
            impersonate="chrome110",
            timeout=1.5
        ) as session:
            
            check_url = f"https://discord.com/api/v10/invites/{self.target_url}"
            
            while not self.found:
                try:
                    header = random.choice(self.headers_list)
                    resp = await session.get(check_url, headers=header)
                    self.stats["checks"] += 1

                    if resp.status_code == 404:
                        ProfessionalLogger.attack(f"Worker-{worker_id}: DETECTED FREE URL! EXECUTING...")
                        await self.claim(session, header)
                        break
                    
                    elif resp.status_code == 429:
                        self.stats["errors"] += 1
                        retry = resp.json().get('retry_after', 1)
                        await asyncio.sleep(retry)
                        continue
                    
                    await asyncio.sleep(self.interval)
                    
                except Exception:
                    self.stats["errors"] += 1
                    await asyncio.sleep(0.1)

    def get_status_panel(self) -> Panel:
        elapsed = time.time() - self.stats["start_time"]
        cps = self.stats["checks"] / elapsed if elapsed > 0 else 0
        
        status_text = (
            f"[bold white]Target:[/bold white] [cyan]discord.gg/{self.target_url}[/cyan]\n"
            f"[bold white]Checks:[/bold white] [green]{self.stats['checks']}[/green]\n"
            f"[bold white]Errors:[/bold white] [red]{self.stats['errors']}[/red]\n"
            f"[bold white]Speed:[/bold white] [yellow]{cps:.2f} check/sec[/yellow]\n"
            f"[bold white]Threads:[/bold white] [magenta]{self.threads}[/magenta]"
        )
        return Panel(status_text, title="[bold green]Live Stats[/bold green]", border_style="bright_blue", box=box.DOUBLE)

    async def run(self):
        ProfessionalLogger.banner()
        await self.validate_all_tokens()
        
        ProfessionalLogger.info(f"Initiating attack on: [bold yellow]{self.target_url}[/bold yellow]")
        
        tasks = [self.worker(i) for i in range(self.threads)]
        
        with Live(self.get_status_panel(), refresh_per_second=4) as live:
            while not self.found:
                live.update(self.get_status_panel())
                await asyncio.sleep(0.2)
        
        ProfessionalLogger.success("Operation complete. Sniper shutting down.")

async def main():
    sniper = OnlySniperElite()
    await sniper.run()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        ProfessionalLogger.warn("User aborted. Goodbye.")
    except Exception as e:
        ProfessionalLogger.error(f"Fatal System Failure: {e}")