#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Factory ERP System - Main Entry Point
نظام إدارة المصنع - نقطة الدخول الرئيسية
"""

import os
import sys
import time
from typing import Optional

class Colors:
    """ANSI Color codes"""
    GREEN = '\033[92m'
    BLACK_BG = '\033[40m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    DIM = '\033[2m'
    CYAN = '\033[96m'


class FactoryERPSystem:
    """Main Factory ERP System"""
    
    def __init__(self):
        self.running = True
        self.authenticated = False
        self.current_user = None
    
    def clear_screen(self):
        """Clear terminal"""
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def print_welcome_banner(self):
        """Print welcome banner"""
        banner = f"""
{Colors.BLACK_BG}{Colors.GREEN}{Colors.BOLD}
╔════════════════════════════════════════════════════════════════════════╗
║                                                                        ║
║           🏭 FACTORY ERP SYSTEM - نظام إدارة المصنع 🏭              ║
║                                                                        ║
║                 Steel Manufacturing Management System                  ║
║                     نظام إدارة تصنيع الحديد                          ║
║                                                                        ║
║                    Version 1.0.0 | September 2026                     ║
║                      Green Screen Terminal UI (TUI)                    ║
║                                                                        ║
╚════════════════════════════════════════════════════════════════════════╝
{Colors.RESET}"""
        print(banner)
    
    def print_main_menu(self):
        """Print main menu"""
        menu = f"""
{Colors.BLACK_BG}{Colors.GREEN}{Colors.BOLD}
╔════════════════════════════════════════════════════════════════════════╗
║                        القائمة الرئيسية (MAIN MENU)                   ║
╠════════════════════════════════════════════════════════════════════════╣
║                                                                        ║
║  [1] 🔐 تسجيل الدخول (Login)                                         ║
║  [2] 📖 اقرأ الوثائق (Read Documentation)                            ║
║  [3] 🚀 تشغيل تطبيق الساعة (Digital Clock)                          ║
║  [4] 😂 تشغيل مولد النكات (Joke Generator)                           ║
║  [5] 📋 تشغيل قائمة المهام (To-Do List)                             ║
║  [6] ℹ️  معلومات عن النظام (About)                                   ║
║  [7] ⚙️  الإعدادات (Settings)                                        ║
║  [Q] 🚪 الخروج (Exit)                                                ║
║                                                                        ║
╚════════════════════════════════════════════════════════════════════════╝
{Colors.RESET}"""
        print(menu)
    
    def show_documentation_menu(self):
        """Show documentation menu"""
        self.clear_screen()
        self.print_welcome_banner()
        
        menu = f"""
{Colors.BLACK_BG}{Colors.GREEN}{Colors.BOLD}
╔════════════════════════════════════════════════════════════════════════╗
║                     📚 الوثائق (DOCUMENTATION)                        ║
╠════════════════════════════════════════════════════════════════════════╣
║                                                                        ║
║  [1] 🚀 البدء السريع (Quick Start Guide)                            ║
║  [2] 🔐 دليل الدخول (How to Login)                                 ║
║  [3] 📂 هيكل المشروع (Project Structure)                            ║
║  [4] 📋 المتطلبات الوظيفية (SRS - Requirements)                    ║
║  [5] 🎯 نظام الصلاحيات (Access Control)                            ║
║  [6] 📊 الميزات الرئيسية (Key Features)                            ║
║  [B] 🔙 رجوع (Back to Main Menu)                                   ║
║                                                                        ║
╚════════════════════════════════════════════════════════════════════════╝
{Colors.RESET}"""
        print(menu)
        
        choice = input(f"{Colors.GREEN}اختر: {Colors.RESET}").strip().upper()
        return choice
    
    def show_quick_start(self):
        """Show quick start guide"""
        self.clear_screen()
        self.print_welcome_banner()
        
        guide = f"""
{Colors.BLACK_BG}{Colors.GREEN}{Colors.BOLD}
╔════════════════════════════════════════════════════════════════════════╗
║                      🚀 البدء السريع (QUICK START)                    ║
╠════════════════════════════════════════════════════════════════════════╣

{Colors.RESET}{Colors.CYAN}الخطوة 1: تسجيل الدخول{Colors.RESET}
{Colors.BLACK_BG}{Colors.GREEN}
  اختر الخيار [1] من القائمة الرئيسية أو اكتب:
  python factory_erp/auth/login.py

{Colors.CYAN}الخطوة 2: بيانات الدخول الافتراضية{Colors.RESET}
  اسم المستخدم (Username): admin
  كلمة المرور (Password): password123

{Colors.CYAN}الخطوة 3: اختر أحد التطبيقات{Colors.RESET}
  • الساعة الرقمية (Digital Clock)
  • مولد النكات (Joke Generator)
  • قائمة المهام (To-Do List)

{Colors.CYAN}الخطوة 4: استكشف الميزات{Colors.RESET}
  • جرب كل تطبيق
  • اقرأ الوثائق
  • تعرف على الأدوار المختلفة

{Colors.CYAN}المستخدمون المتاحون:{Colors.RESET}
  1. admin (مدير النظام)
  2. manager (المدير العام)
  3. finance (مدير المالية)
  4. purchase (مدير المشتريات)
  5. warehouse (أمين المستودع)
  6. production (مدير الإنتاج)
  7. hr (مدير الموارد البشرية)
  8. accountant (المحاسب)

  جميعهم بنفس كلمة المرور: password123

{Colors.BLACK_BG}{Colors.GREEN}╚════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
"""
        print(guide)
        input(f"\n{Colors.GREEN}اضغط ENTER للمتابعة...{Colors.RESET}")
    
    def show_about(self):
        """Show about information"""
        self.clear_screen()
        self.print_welcome_banner()
        
        about = f"""
{Colors.BLACK_BG}{Colors.GREEN}{Colors.BOLD}
╔════════════════════════════════════════════════════════════════════════╗
║                     ℹ️  حول النظام (ABOUT)                           ║
╠════════════════════════════════════════════════════════════════════════╣

{Colors.RESET}{Colors.CYAN}نظام إدارة المصنع المتكامل{Colors.RESET}
Integrated Factory Management System

{Colors.CYAN}الإصدار:{Colors.RESET} 1.0.0-alpha
{Colors.CYAN}تاريخ الإصدار:{Colors.RESET} سبتمبر 2026
{Colors.CYAN}الحالة:{Colors.RESET} 🟢 قيد التطوير النشط

{Colors.CYAN}الميزات الرئيسية:{Colors.RESET}
{Colors.BLACK_BG}{Colors.GREEN}
  ✅ نظام مصادقة آمن (Secure Authentication)
  ✅ واجهة Green Screen Terminal UI (Classic TUI Interface)
  ✅ دعم اللغة العربية والإنجليزية (Bilingual Support)
  ✅ نظام صلاحيات متقدم (Advanced RBAC)
  ✅ سجل تدقيق شامل (Comprehensive Audit Trail)
  ✅ تطبيقات مساعدة (Utility Applications)
  ✅ تخزين محلي آمن (Secure Local Storage)

{Colors.CYAN}المكونات المتاحة:{Colors.RESET}
  • 🔐 نظام المصادقة والدخول
  • 🕐 الساعة الرقمية بمناطق زمنية متعددة
  • 😂 مولد النكات العشوائية
  • 📋 قائمة المهام مع التخزين المحلي

{Colors.CYAN}المكونات قيد الإنشاء:{Colors.RESET}
  • 📊 نظام المحاسبة العامة
  • 🛒 نظام المشتريات والموردين
  • 📦 نظام المخزون والمستودعات
  • 🏭 نظام الإنتاج
  • 💼 نظام المبيعات
  • 👥 نظام الموارد البشرية والرواتب
  • 🔧 نظام الصيانة والأصول
  • 📈 التقارير والإحصائيات

{Colors.CYAN}الفريق:{Colors.RESET}
  تم التطوير بواسطة: Factory ERP Development Team
  البريد الإلكتروني: support@factory-erp.local
  الموقع: github.com/abduzizali/factory-erp-system

{Colors.CYAN}الترخيص:{Colors.RESET}
  MIT License - للاستخدام الحر والتعديل

{Colors.BLACK_BG}{Colors.GREEN}╚════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
"""
        print(about)
        input(f"\n{Colors.GREEN}اضغط ENTER للرجوع...{Colors.RESET}")
    
    def login_to_system(self):
        """Login to system"""
        try:
            from factory_erp.auth.login import LoginUI
            login_ui = LoginUI()
            login_ui.run()
        except Exception as e:
            print(f"{Colors.RED}❌ خطأ في تحميل نظام الدخول: {str(e)}{Colors.RESET}")
            input(f"{Colors.GREEN}اضغط ENTER للمتابعة...{Colors.RESET}")
    
    def run_digital_clock(self):
        """Run digital clock application"""
        try:
            from utilities.digital_clock.digital_clock import JokeGenerator
            # Since we're running from main, we need to adjust the import
            # This is a placeholder - actual implementation would import correctly
            print(f"\n{Colors.GREEN}جاري تشغيل الساعة الرقمية...{Colors.RESET}")
            print(f"{Colors.YELLOW}الرجاء تشغيل: python utilities/digital-clock/digital_clock.py{Colors.RESET}\n")
            time.sleep(2)
        except Exception as e:
            print(f"{Colors.RED}❌ خطأ: {str(e)}{Colors.RESET}")
            input(f"{Colors.GREEN}اضغط ENTER للرجوع...{Colors.RESET}")
    
    def run_joke_generator(self):
        """Run joke generator application"""
        try:
            print(f"\n{Colors.GREEN}جاري تشغيل مولد النكات...{Colors.RESET}")
            print(f"{Colors.YELLOW}الرجاء تشغيل: python utilities/joke-generator/joke_generator.py{Colors.RESET}\n")
            time.sleep(2)
        except Exception as e:
            print(f"{Colors.RED}❌ خطأ: {str(e)}{Colors.RESET}")
            input(f"{Colors.GREEN}اضغط ENTER للرجوع...{Colors.RESET}")
    
    def run_todo_list(self):
        """Run to-do list application"""
        try:
            print(f"\n{Colors.GREEN}جاري تشغيل قائمة المهام...{Colors.RESET}")
            print(f"{Colors.YELLOW}الرجاء تشغيل: python utilities/todo-list/todo_app.py{Colors.RESET}\n")
            time.sleep(2)
        except Exception as e:
            print(f"{Colors.RED}❌ خطأ: {str(e)}{Colors.RESET}")
            input(f"{Colors.GREEN}اضغط ENTER للرجوع...{Colors.RESET}")
    
    def show_settings(self):
        """Show settings menu"""
        self.clear_screen()
        self.print_welcome_banner()
        
        settings = f"""
{Colors.BLACK_BG}{Colors.GREEN}{Colors.BOLD}
╔════════════════════════════════════════════════════════════════════════╗
║                     ⚙️  الإعدادات (SETTINGS)                         ║
╠════════════════════════════════════════════════════════════════════════╣
║                                                                        ║
║  [1] 🎨 تغيير نمط الواجهة (Change Theme) - قيد التطوير              ║
║  [2] 🌍 تغيير اللغة (Change Language)                               ║
║  [3] 🔐 إعدادات الأمان (Security Settings)                          ║
║  [4] 📱 إعدادات العرض (Display Settings)                            ║
║  [5] 🔔 الإشعارات (Notifications) - قيد التطوير                    ║
║  [B] 🔙 رجوع (Back)                                                 ║
║                                                                        ║
╚════════════════════════════════════════════════════════════════════════╝
{Colors.RESET}"""
        print(settings)
        
        choice = input(f"{Colors.GREEN}اختر: {Colors.RESET}").strip().upper()
        
        if choice == '1':
            print(f"{Colors.YELLOW}هذه الميزة قيد التطوير...{Colors.RESET}")
            time.sleep(1)
        elif choice == '2':
            print(f"{Colors.YELLOW}النظام يدعم العربية والإنجليزية بالفعل{Colors.RESET}")
            time.sleep(1)
        elif choice == 'B':
            return
        else:
            print(f"{Colors.RED}❌ خيار غير صحيح{Colors.RESET}")
            time.sleep(1)
    
    def run(self):
        """Main application loop"""
        while self.running:
            self.clear_screen()
            self.print_welcome_banner()
            self.print_main_menu()
            
            choice = input(f"{Colors.GREEN}اختر الخيار: {Colors.RESET}").strip().upper()
            
            if choice == '1':
                self.login_to_system()
            elif choice == '2':
                while True:
                    doc_choice = self.show_documentation_menu()
                    if doc_choice == '1':
                        self.show_quick_start()
                    elif doc_choice == '2':
                        print(f"{Colors.YELLOW}انظر HOW_TO_LOGIN.md{Colors.RESET}")
                        time.sleep(2)
                    elif doc_choice == '3':
                        print(f"{Colors.YELLOW}انظر PROJECT_STRUCTURE.md{Colors.RESET}")
                        time.sleep(2)
                    elif doc_choice == '4':
                        print(f"{Colors.YELLOW}انظر SRS.md (الوثيقة الأصلية){Colors.RESET}")
                        time.sleep(2)
                    elif doc_choice == 'B':
                        break
                    else:
                        print(f"{Colors.RED}❌ خيار غير صحيح{Colors.RESET}")
                        time.sleep(1)
            elif choice == '3':
                self.run_digital_clock()
            elif choice == '4':
                self.run_joke_generator()
            elif choice == '5':
                self.run_todo_list()
            elif choice == '6':
                self.show_about()
            elif choice == '7':
                self.show_settings()
            elif choice == 'Q':
                print(f"\n{Colors.GREEN}شكراً لاستخدام نظام إدارة المصنع!{Colors.RESET}")
                print(f"{Colors.GREEN}Thank you for using Factory ERP System!{Colors.RESET}\n")
                self.running = False
            else:
                print(f"{Colors.RED}❌ خيار غير صحيح{Colors.RESET}")
                time.sleep(1)


def main():
    """Main entry point"""
    system = FactoryERPSystem()
    system.run()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.GREEN}تم إيقاف البرنامج (Program terminated){Colors.RESET}\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.RED}خطأ: {str(e)}{Colors.RESET}\n")
        sys.exit(1)
