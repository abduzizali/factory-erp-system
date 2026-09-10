#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Random Joke Generator using External APIs
مولد النكات العشوائية باستخدام APIs خارجية
Green Screen Terminal UI (TUI) Style
"""

import requests
import json
import os
import sys
from typing import Optional, Dict, Tuple
import time

class Colors:
    """ANSI Color codes - الألوان"""
    GREEN = '\033[92m'
    BLACK_BG = '\033[40m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    DIM = '\033[2m'
    CYAN = '\033[96m'


class JokeGenerator:
    """Random Joke Generator - مولد النكات"""
    
    def __init__(self):
        self.api_providers = {
            '1': {
                'name': 'JokeAPI',
                'url': 'https://v2.jokeapi.dev/joke/Any',
                'type': 'json'
            },
            '2': {
                'name': 'Official Joke API',
                'url': 'https://official-joke-api.appspot.com/random_joke',
                'type': 'json'
            },
            '3': {
                'name': 'QuotesGarden',
                'url': 'https://quotes-api.techwithaniruddh.repl.co/api/quotes',
                'type': 'json'
            },
            '4': {
                'name': 'Random Advice Slip',
                'url': 'https://api.adviceslip.com/advice',
                'type': 'json'
            }
        }
        
        self.joke_history = []
        self.current_provider = '1'
    
    def clear_screen(self):
        """Clear terminal screen"""
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def print_header(self):
        """Print green screen TUI header"""
        header = f"""
{Colors.BLACK_BG}{Colors.GREEN}{Colors.BOLD}
╔════════════════════════════════════════════════════════════════════════╗
║                                                                        ║
║              😂 RANDOM JOKE GENERATOR - مولد النكات 😂                ║
║                                                                        ║
║              Green Screen Terminal UI (TUI) Display System             ║
║                         Using External APIs                            ║
║                                                                        ║
╚════════════════════════════════════════════════════════════════════════╝
{Colors.RESET}"""
        print(header)
    
    def print_separator(self, char='═', length=70):
        """Print horizontal separator"""
        sep = f"{Colors.BLACK_BG}{Colors.GREEN}╠{char * length}╣{Colors.RESET}"
        print(sep)
    
    def get_joke_from_api(self, provider_id: str = '1') -> Tuple[bool, Dict]:
        """
        Fetch joke from external API
        جلب النكتة من API خارجي
        
        Returns: (success, joke_data)
        """
        try:
            if provider_id not in self.api_providers:
                return False, {'error': 'Invalid provider'}
            
            provider = self.api_providers[provider_id]
            
            # Set timeout and headers
            headers = {
                'User-Agent': 'Factory-ERP-JokeGenerator/1.0'
            }
            
            print(f"\n{Colors.CYAN}{Colors.DIM}جاري الاتصال بـ {provider['name']}...{Colors.RESET}")
            
            response = requests.get(
                provider['url'],
                headers=headers,
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                return True, data
            else:
                return False, {'error': f'API returned {response.status_code}'}
        
        except requests.exceptions.Timeout:
            return False, {'error': 'Connection timeout - المهلة الزمنية انتهت'}
        except requests.exceptions.ConnectionError:
            return False, {'error': 'No internet connection - لا توجد اتصالية'}
        except requests.exceptions.RequestException as e:
            return False, {'error': str(e)}
        except json.JSONDecodeError:
            return False, {'error': 'Invalid JSON response'}
        except Exception as e:
            return False, {'error': f'Unknown error: {str(e)}'}
    
    def parse_joke_from_jokeapi(self, data: Dict) -> Dict:
        """Parse joke from JokeAPI format"""
        if data.get('type') == 'single':
            return {
                'joke': data.get('joke', ''),
                'source': 'JokeAPI',
                'category': data.get('category', 'General'),
                'safe': data.get('safe', True)
            }
        elif data.get('type') == 'twopart':
            return {
                'setup': data.get('setup', ''),
                'delivery': data.get('delivery', ''),
                'source': 'JokeAPI',
                'category': data.get('category', 'General'),
                'safe': data.get('safe', True)
            }
        else:
            return {'error': 'Unknown joke format'}
    
    def parse_joke_from_official_api(self, data: Dict) -> Dict:
        """Parse joke from Official Joke API format"""
        return {
            'setup': data.get('setup', ''),
            'delivery': data.get('punchline', ''),
            'source': 'Official Joke API',
            'joke_type': data.get('type', ''),
            'id': data.get('id', '')
        }
    
    def parse_joke_from_quote_api(self, data: Dict) -> Dict:
        """Parse joke/quote from Quotes API format"""
        if isinstance(data, list) and len(data) > 0:
            quote = data[0]
        else:
            quote = data
        
        return {
            'quote': quote.get('text', quote.get('quote', '')),
            'author': quote.get('author', 'Unknown'),
            'source': 'QuotesGarden',
            'category': quote.get('category', 'General')
        }
    
    def parse_joke_from_advice_api(self, data: Dict) -> Dict:
        """Parse advice from Advice Slip API format"""
        return {
            'advice': data.get('slip', {}).get('advice', ''),
            'slip_id': data.get('slip', {}).get('slip_id', ''),
            'source': 'Advice Slip API'
        }
    
    def format_joke_display(self, joke_data: Dict) -> str:
        """Format joke for display"""
        display = f"\n{Colors.BLACK_BG}{Colors.GREEN}{Colors.BOLD}╔ النكتة (JOKE) ╔{Colors.RESET}\n"
        
        if 'error' in joke_data:
            display += f"{Colors.RED}❌ خطأ: {joke_data['error']}{Colors.RESET}\n"
        
        elif 'joke' in joke_data:
            display += f"{Colors.YELLOW}{joke_data['joke']}{Colors.RESET}\n"
        
        elif 'setup' in joke_data and 'delivery' in joke_data:
            display += f"{Colors.YELLOW}السؤال: {joke_data['setup']}{Colors.RESET}\n"
            display += f"{Colors.GREEN}{Colors.BOLD}الجواب: {joke_data['delivery']}{Colors.RESET}\n"
        
        elif 'quote' in joke_data:
            display += f"{Colors.YELLOW}\"{joke_data['quote']}\"{Colors.RESET}\n"
            if 'author' in joke_data:
                display += f"{Colors.DIM}- {joke_data['author']}{Colors.RESET}\n"
        
        elif 'advice' in joke_data:
            display += f"{Colors.YELLOW}💡 {joke_data['advice']}{Colors.RESET}\n"
        
        # Add metadata
        if 'source' in joke_data:
            display += f"{Colors.DIM}\n📌 المصدر (Source): {joke_data['source']}{Colors.RESET}"
        
        if 'category' in joke_data:
            display += f"{Colors.DIM}\n📂 الفئة (Category): {joke_data['category']}{Colors.RESET}"
        
        display += f"\n{Colors.BLACK_BG}{Colors.GREEN}╚{'═' * 70}╝{Colors.RESET}\n"
        
        return display
    
    def display_providers_menu(self):
        """Display available providers"""
        self.clear_screen()
        self.print_header()
        
        menu = f"\n{Colors.BLACK_BG}{Colors.GREEN}{Colors.BOLD}╔ اختر مصدر النكات (Select Joke Provider) ╔\n{Colors.RESET}\n"
        
        for key, provider in self.api_providers.items():
            menu += f"{Colors.GREEN}  [{key}] {provider['name']:30}{Colors.RESET}\n"
        
        menu += f"\n{Colors.GREEN}  [R] جرب جميع المصادر (Try All Providers){Colors.RESET}\n"
        menu += f"{Colors.GREEN}  [H] السجل (History){Colors.RESET}\n"
        menu += f"{Colors.GREEN}  [Q] الخروج (Quit){Colors.RESET}\n"
        
        print(menu)
    
    def display_main_menu(self):
        """Display main menu"""
        self.clear_screen()
        self.print_header()
        
        menu = f"""
{Colors.BLACK_BG}{Colors.GREEN}{Colors.BOLD}
╔ القائمة الرئيسية (MAIN MENU) ╔
║
║  [1] الحصول على نكتة عشوائية (Get Random Joke)
║  [2] اختر مصدر النكات (Select Provider)
║  [3] اعرض السجل (Show History)
║  [4] الإعدادات (Settings)
║  [Q] الخروج (Quit)
║
╚════════════════════════════════════════════════════════════════════════╝
{Colors.RESET}"""
        print(menu)
    
    def get_random_joke(self):
        """Get and display random joke"""
        success, data = self.get_joke_from_api(self.current_provider)
        
        if not success:
            print(f"{Colors.RED}❌ خطأ في الاتصال: {data.get('error')}{Colors.RESET}")
            return
        
        # Parse based on provider
        provider_name = self.api_providers[self.current_provider]['name']
        
        if provider_name == 'JokeAPI':
            parsed_joke = self.parse_joke_from_jokeapi(data)
        elif provider_name == 'Official Joke API':
            parsed_joke = self.parse_joke_from_official_api(data)
        elif provider_name == 'QuotesGarden':
            parsed_joke = self.parse_joke_from_quote_api(data)
        elif provider_name == 'Random Advice Slip':
            parsed_joke = self.parse_joke_from_advice_api(data)
        else:
            parsed_joke = data
        
        # Add to history
        self.joke_history.append({
            'joke': parsed_joke,
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'provider': provider_name
        })
        
        # Display
        self.clear_screen()
        self.print_header()
        print(self.format_joke_display(parsed_joke))
        
        input(f"{Colors.GREEN}اضغط ENTER للمتابعة (Press ENTER to continue)...{Colors.RESET}")
    
    def show_history(self):
        """Display joke history"""
        self.clear_screen()
        self.print_header()
        
        if not self.joke_history:
            print(f"\n{Colors.YELLOW}لا توجد نكات في السجل (No jokes in history){Colors.RESET}\n")
            input(f"{Colors.GREEN}اضغط ENTER للمتابعة...{Colors.RESET}")
            return
        
        print(f"\n{Colors.BLACK_BG}{Colors.GREEN}{Colors.BOLD}╔ السجل ({len(self.joke_history)} نكات) ╔\n{Colors.RESET}")
        
        for i, entry in enumerate(self.joke_history[-10:], 1):  # Show last 10
            print(f"{Colors.CYAN}[{i}] {entry['timestamp']} - {entry['provider']}{Colors.RESET}")
            if 'joke' in entry['joke']:
                print(f"    {entry['joke']['joke'][:60]}...")
            elif 'setup' in entry['joke']:
                print(f"    {entry['joke']['setup'][:60]}...")
            print()
        
        input(f"{Colors.GREEN}اضغط ENTER للرجوع...{Colors.RESET}")
    
    def try_all_providers(self):
        """Try to get joke from all providers"""
        self.clear_screen()
        self.print_header()
        
        print(f"\n{Colors.CYAN}جاري محاولة جميع المصادر...{Colors.RESET}\n")
        
        for key, provider in self.api_providers.items():
            print(f"{Colors.GREEN}جاري محاولة {provider['name']}...{Colors.RESET}")
            
            success, data = self.get_joke_from_api(key)
            
            if success:
                print(f"{Colors.GREEN}✓ نجح!{Colors.RESET}\n")
                
                # Parse and display
                if provider['name'] == 'JokeAPI':
                    parsed = self.parse_joke_from_jokeapi(data)
                elif provider['name'] == 'Official Joke API':
                    parsed = self.parse_joke_from_official_api(data)
                elif provider['name'] == 'QuotesGarden':
                    parsed = self.parse_joke_from_quote_api(data)
                elif provider['name'] == 'Random Advice Slip':
                    parsed = self.parse_joke_from_advice_api(data)
                
                print(self.format_joke_display(parsed))
                print()
            else:
                print(f"{Colors.RED}✗ فشل: {data.get('error')}{Colors.RESET}\n")
        
        input(f"{Colors.GREEN}اضغط ENTER للرجوع...{Colors.RESET}")
    
    def select_provider(self):
        """Select joke provider"""
        self.display_providers_menu()
        
        choice = input(f"{Colors.GREEN}اختر: {Colors.RESET}").strip()
        
        if choice in self.api_providers:
            self.current_provider = choice
            provider_name = self.api_providers[choice]['name']
            print(f"{Colors.GREEN}✓ تم اختيار {provider_name}{Colors.RESET}")
            time.sleep(1)
        elif choice.upper() == 'R':
            self.try_all_providers()
        elif choice.upper() == 'H':
            self.show_history()
        elif choice.upper() == 'Q':
            return 'quit'
    
    def show_settings(self):
        """Display settings menu"""
        self.clear_screen()
        self.print_header()
        
        settings = f"""
{Colors.BLACK_BG}{Colors.GREEN}{Colors.BOLD}
╔ الإعدادات (SETTINGS) ╔
║
║  المصدر الحالي: {self.api_providers[self.current_provider]['name']}
║  عدد النكات المحفوظة: {len(self.joke_history)}
║  اللغة: العربية والإنجليزية
║  الوضع: Green Screen Terminal UI
║
║  [1] تغيير المصدر (Change Provider)
║  [2] حذف السجل (Clear History)
║  [3] حول البرنامج (About)
║  [B] رجوع (Back)
║
╚════════════════════════════════════════════════════════════════════════╝
{Colors.RESET}"""
        print(settings)
        
        choice = input(f"{Colors.GREEN}اختر: {Colors.RESET}").strip().upper()
        
        if choice == '1':
            self.select_provider()
        elif choice == '2':
            self.joke_history = []
            print(f"{Colors.GREEN}✓ تم حذف السجل{Colors.RESET}")
            time.sleep(1)
        elif choice == '3':
            self.show_about()
        elif choice == 'B':
            pass
    
    def show_about(self):
        """Show about dialog"""
        self.clear_screen()
        self.print_header()
        
        about = f"""
{Colors.BLACK_BG}{Colors.GREEN}{Colors.BOLD}
╔ حول البرنامج (ABOUT) ╔
║
║  Random Joke Generator v1.0
║  مولد النكات العشوائية
║
║  تم التطوير بواسطة:
║  Factory ERP System Team
║
║  المميزات:
║  ✓ اتصال بـ APIs خارجية متعددة
║  ✓ واجهة Terminal UI خضراء كلاسيكية
║  ✓ سجل النكات
║  ✓ دعم اللغة العربية والإنجليزية
║
║  لا توجد تبعيات خارجية معقدة
║  Simple, Reliable, Fast
║
╚════════════════════════════════════════════════════════════════════════╝
{Colors.RESET}"""
        print(about)
        
        input(f"{Colors.GREEN}اضغط ENTER للرجوع...{Colors.RESET}")
    
    def run(self):
        """Main application loop"""
        while True:
            self.display_main_menu()
            
            choice = input(f"{Colors.GREEN}اختر الخيار (Select option): {Colors.RESET}").strip().upper()
            
            if choice == '1':
                self.get_random_joke()
            elif choice == '2':
                result = self.select_provider()
                if result == 'quit':
                    break
            elif choice == '3':
                self.show_history()
            elif choice == '4':
                self.show_settings()
            elif choice == 'Q':
                print(f"\n{Colors.GREEN}وداعاً! (Goodbye!)...")
                print(f"شكراً لاستخدامك مولد النكات! 😂{Colors.RESET}\n")
                break
            else:
                print(f"{Colors.RED}❌ خيار غير صحيح (Invalid option){Colors.RESET}")
                time.sleep(1)


def main():
    """Main entry point"""
    print(f"{Colors.BLACK_BG}{Colors.GREEN}")
    print("جاري تحميل البرنامج... (Initializing...)")
    print(f"{Colors.RESET}")
    time.sleep(1)
    
    generator = JokeGenerator()
    generator.run()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.GREEN}تم إيقاف البرنامج (Program terminated){Colors.RESET}\n")
        sys.exit(0)
    except Exception as e:
        print(f"{Colors.RED}خطأ: {str(e)}{Colors.RESET}\n")
        sys.exit(1)
