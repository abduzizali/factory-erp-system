#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
To-Do List Application with Local Storage
تطبيق قائمة المهام مع التخزين المحلي
Green Screen Terminal UI (TUI) Style
"""

import json
import os
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Tuple
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
    BLUE = '\033[94m'


class Task:
    """Task model - نموذج المهمة"""
    
    def __init__(self, task_id: int, title: str, description: str = "",
                 priority: str = "Medium", due_date: str = "", status: str = "Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.priority = priority  # High, Medium, Low
        self.due_date = due_date
        self.status = status  # Pending, In Progress, Completed, Cancelled
        self.created_at = datetime.now().isoformat()
        self.completed_at = None
    
    def to_dict(self) -> Dict:
        """Convert task to dictionary"""
        return {
            'task_id': self.task_id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'due_date': self.due_date,
            'status': self.status,
            'created_at': self.created_at,
            'completed_at': self.completed_at
        }
    
    @staticmethod
    def from_dict(data: Dict) -> 'Task':
        """Create task from dictionary"""
        task = Task(
            data['task_id'],
            data['title'],
            data.get('description', ''),
            data.get('priority', 'Medium'),
            data.get('due_date', ''),
            data.get('status', 'Pending')
        )
        task.created_at = data.get('created_at', datetime.now().isoformat())
        task.completed_at = data.get('completed_at')
        return task


class TodoListManager:
    """Todo List Manager with Local Storage - مدير قائمة المهام"""
    
    def __init__(self, storage_file: str = 'todo_tasks.json'):
        self.storage_file = storage_file
        self.tasks: List[Task] = []
        self.next_task_id = 1
        self.load_tasks()
    
    def save_tasks(self) -> bool:
        """Save tasks to local storage"""
        try:
            data = {
                'tasks': [task.to_dict() for task in self.tasks],
                'next_task_id': self.next_task_id,
                'last_saved': datetime.now().isoformat()
            }
            with open(self.storage_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"Error saving tasks: {str(e)}")
            return False
    
    def load_tasks(self) -> bool:
        """Load tasks from local storage"""
        try:
            if os.path.exists(self.storage_file):
                with open(self.storage_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.tasks = [Task.from_dict(t) for t in data.get('tasks', [])]
                    self.next_task_id = data.get('next_task_id', len(self.tasks) + 1)
            return True
        except Exception as e:
            print(f"Error loading tasks: {str(e)}")
            return False
    
    def add_task(self, title: str, description: str = "", priority: str = "Medium",
                due_date: str = "") -> Tuple[bool, str]:
        """Add new task"""
        if not title.strip():
            return False, "❌ عنوان المهمة مطلوب (Task title required)"
        
        task = Task(self.next_task_id, title, description, priority, due_date)
        self.tasks.append(task)
        self.next_task_id += 1
        
        if self.save_tasks():
            return True, f"✅ تم إضافة المهمة #{task.task_id}"
        else:
            return False, "❌ فشل في حفظ المهمة"
    
    def get_task(self, task_id: int) -> Optional[Task]:
        """Get task by ID"""
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None
    
    def update_task(self, task_id: int, title: str = None, description: str = None,
                   priority: str = None, due_date: str = None, status: str = None) -> Tuple[bool, str]:
        """Update existing task"""
        task = self.get_task(task_id)
        if not task:
            return False, f"❌ المهمة #{task_id} غير موجودة"
        
        if title:
            task.title = title
        if description is not None:
            task.description = description
        if priority:
            task.priority = priority
        if due_date is not None:
            task.due_date = due_date
        if status:
            task.status = status
            if status == "Completed":
                task.completed_at = datetime.now().isoformat()
        
        if self.save_tasks():
            return True, f"✅ تم تحديث المهمة #{task_id}"
        else:
            return False, "❌ فشل في تحديث المهمة"
    
    def delete_task(self, task_id: int) -> Tuple[bool, str]:
        """Delete task"""
        task = self.get_task(task_id)
        if not task:
            return False, f"❌ المهمة #{task_id} غير موجودة"
        
        self.tasks.remove(task)
        if self.save_tasks():
            return True, f"✅ تم حذف المهمة #{task_id}"
        else:
            return False, "❌ فشل في حذف المهمة"
    
    def get_tasks_by_status(self, status: str) -> List[Task]:
        """Get tasks filtered by status"""
        return [task for task in self.tasks if task.status == status]
    
    def get_tasks_by_priority(self, priority: str) -> List[Task]:
        """Get tasks filtered by priority"""
        return [task for task in self.tasks if task.priority == priority]
    
    def get_overdue_tasks(self) -> List[Task]:
        """Get overdue tasks"""
        today = datetime.now().date()
        overdue = []
        for task in self.tasks:
            if task.due_date and task.status != "Completed":
                try:
                    due = datetime.fromisoformat(task.due_date).date()
                    if due < today:
                        overdue.append(task)
                except:
                    pass
        return overdue
    
    def get_task_statistics(self) -> Dict:
        """Get statistics about tasks"""
        return {
            'total': len(self.tasks),
            'pending': len(self.get_tasks_by_status("Pending")),
            'in_progress': len(self.get_tasks_by_status("In Progress")),
            'completed': len(self.get_tasks_by_status("Completed")),
            'cancelled': len(self.get_tasks_by_status("Cancelled")),
            'overdue': len(self.get_overdue_tasks()),
            'high_priority': len(self.get_tasks_by_priority("High")),
            'completion_rate': round(
                len(self.get_tasks_by_status("Completed")) / len(self.tasks) * 100
                if self.tasks else 0, 1
            )
        }


class TodoListUI:
    """Terminal UI for Todo List - واجهة قائمة المهام"""
    
    def __init__(self):
        self.todo_manager = TodoListManager()
    
    def clear_screen(self):
        """Clear terminal"""
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def print_header(self):
        """Print header"""
        header = f"""
{Colors.BLACK_BG}{Colors.GREEN}{Colors.BOLD}
╔════════════════════════════════════════════════════════════════════════╗
║                                                                        ║
║              📋 TO-DO LIST APPLICATION - قائمة المهام 📋             ║
║                                                                        ║
║              Green Screen Terminal UI (TUI) with Local Storage         ║
║                                                                        ║
╚════════════════════════════════════════════════════════════════════════╝
{Colors.RESET}"""
        print(header)
    
    def print_separator(self, char='═', length=70):
        """Print separator"""
        print(f"{Colors.BLACK_BG}{Colors.GREEN}╠{char * length}╣{Colors.RESET}")
    
    def display_main_menu(self):
        """Display main menu"""
        self.clear_screen()
        self.print_header()
        
        stats = self.todo_manager.get_task_statistics()
        
        menu = f"""
{Colors.BLACK_BG}{Colors.GREEN}{Colors.BOLD}
╔ القائمة الرئيسية (MAIN MENU) ╔
║
║  📊 الإحصائيات (Statistics):
║     📌 الإجمالي: {stats['total']:3} | ⏳ قيد الانتظار: {stats['pending']:3} | 🔄 قيد التنفيذ: {stats['in_progress']:3}
║     ✅ مكتمل: {stats['completed']:3} | ⛔ ملغي: {stats['cancelled']:3} | ⚠️  متأخر: {stats['overdue']:3}
║     📈 نسبة الإنجاز: {stats['completion_rate']}%
║
║  الخيارات:
║  [1] عرض جميع المهام (Show All Tasks)
║  [2] إضافة مهمة جديدة (Add New Task)
║  [3] البحث عن مهمة (Search Task)
║  [4] تحديث مهمة (Update Task)
║  [5] حذف مهمة (Delete Task)
║  [6] عرض المهام المتأخرة (Show Overdue Tasks)
║  [7] الإحصائيات التفصيلية (Detailed Statistics)
║  [8] الإعدادات (Settings)
║  [Q] الخروج (Quit)
║
╚════════════════════════════════════════════════════════════════════════╝
{Colors.RESET}"""
        print(menu)
    
    def format_task_display(self, task: Task, show_details: bool = False) -> str:
        """Format task for display"""
        # Priority color
        priority_color = {
            'High': Colors.RED,
            'Medium': Colors.YELLOW,
            'Low': Colors.GREEN
        }.get(task.priority, Colors.DIM)
        
        # Status color
        status_emoji = {
            'Pending': '⏳',
            'In Progress': '🔄',
            'Completed': '✅',
            'Cancelled': '⛔'
        }.get(task.status, '•')
        
        # Check if overdue
        is_overdue = False
        if task.due_date and task.status != "Completed":
            try:
                due = datetime.fromisoformat(task.due_date).date()
                is_overdue = due < datetime.now().date()
            except:
                pass
        
        overdue_mark = "⚠️ " if is_overdue else ""
        
        display = f"{Colors.BLACK_BG}{Colors.GREEN}║ "
        display += f"{status_emoji} #{task.task_id:3} {Colors.RESET}"
        display += f"{Colors.BOLD}{task.title[:40]:40}{Colors.RESET} "
        display += f"{Colors.DIM}[{priority_color}{task.priority:6}{Colors.RESET}{Colors.DIM}]{Colors.RESET} "
        
        if task.due_date:
            display += f"{overdue_mark}{Colors.DIM}{task.due_date[:10]}{Colors.RESET}"
        
        if show_details:
            display += f"\n{Colors.DIM}    {task.description[:60]}{Colors.RESET}"
        
        return display
    
    def display_all_tasks(self):
        """Display all tasks"""
        self.clear_screen()
        self.print_header()
        
        if not self.todo_manager.tasks:
            print(f"\n{Colors.YELLOW}لا توجد مهام (No tasks){Colors.RESET}\n")
            input(f"{Colors.GREEN}اضغط ENTER للرجوع...{Colors.RESET}")
            return
        
        print(f"\n{Colors.BLACK_BG}{Colors.GREEN}{Colors.BOLD}╔ جميع المهام ╔\n{Colors.RESET}")
        
        # Group by status
        statuses = ["Pending", "In Progress", "Completed", "Cancelled"]
        for status in statuses:
            tasks = self.todo_manager.get_tasks_by_status(status)
            if tasks:
                print(f"{Colors.CYAN}{Colors.BOLD}📌 {status}{Colors.RESET}\n")
                for task in tasks:
                    print(self.format_task_display(task))
                print()
        
        input(f"{Colors.GREEN}اضغط ENTER للرجوع...{Colors.RESET}")
    
    def add_new_task(self):
        """Add new task"""
        self.clear_screen()
        self.print_header()
        
        print(f"\n{Colors.BLACK_BG}{Colors.GREEN}{Colors.BOLD}╔ إضافة مهمة جديدة ╔\n{Colors.RESET}")
        
        title = input(f"{Colors.GREEN}العنوان (Title): {Colors.RESET}").strip()
        if not title:
            print(f"{Colors.RED}❌ العنوان مطلوب{Colors.RESET}")
            time.sleep(1)
            return
        
        description = input(f"{Colors.GREEN}الوصف (Description) [اختياري]: {Colors.RESET}").strip()
        
        print(f"\n{Colors.GREEN}الأولوية (Priority):{Colors.RESET}")
        print(f"  [1] عالي (High)")
        print(f"  [2] متوسط (Medium) [افتراضي]")
        print(f"  [3] منخفض (Low)")
        priority_choice = input(f"{Colors.GREEN}اختر: {Colors.RESET}").strip()
        priority = {'1': 'High', '2': 'Medium', '3': 'Low'}.get(priority_choice, 'Medium')
        
        due_date = input(f"{Colors.GREEN}تاريخ الاستحقاق (Due Date) [YYYY-MM-DD] [اختياري]: {Colors.RESET}").strip()
        
        success, message = self.todo_manager.add_task(title, description, priority, due_date)
        print(f"\n{message}")
        time.sleep(1)
    
    def search_task(self):
        """Search for task"""
        self.clear_screen()
        self.print_header()
        
        print(f"\n{Colors.BLACK_BG}{Colors.GREEN}{Colors.BOLD}╔ البحث عن مهمة ╔\n{Colors.RESET}")
        
        search_input = input(f"{Colors.GREEN}أدخل رقم المهمة أو الكلمة: {Colors.RESET}").strip()
        
        if not search_input:
            return
        
        # Try to parse as ID
        try:
            task_id = int(search_input)
            task = self.todo_manager.get_task(task_id)
            if task:
                print(f"\n{Colors.GREEN}تم العثور على المهمة:{Colors.RESET}\n")
                print(self.format_task_display(task, show_details=True))
            else:
                print(f"\n{Colors.RED}❌ لم يتم العثور على المهمة{Colors.RESET}")
        except ValueError:
            # Search by keyword
            print(f"\n{Colors.GREEN}نتائج البحث:{Colors.RESET}\n")
            found = False
            for task in self.todo_manager.tasks:
                if search_input.lower() in task.title.lower() or search_input.lower() in task.description.lower():
                    print(self.format_task_display(task))
                    found = True
            
            if not found:
                print(f"{Colors.RED}❌ لم يتم العثور على نتائج{Colors.RESET}")
        
        input(f"\n{Colors.GREEN}اضغط ENTER للرجوع...{Colors.RESET}")
    
    def update_task_ui(self):
        """Update task"""
        self.clear_screen()
        self.print_header()
        
        print(f"\n{Colors.BLACK_BG}{Colors.GREEN}{Colors.BOLD}╔ تحديث مهمة ╔\n{Colors.RESET}")
        
        try:
            task_id = int(input(f"{Colors.GREEN}رقم المهمة: {Colors.RESET}"))
            task = self.todo_manager.get_task(task_id)
            
            if not task:
                print(f"{Colors.RED}❌ المهمة غير موجودة{Colors.RESET}")
                time.sleep(1)
                return
            
            print(f"\n{Colors.CYAN}المهمة الحالية:{Colors.RESET}")
            print(self.format_task_display(task, show_details=True))
            
            print(f"\n{Colors.GREEN}اختر ما تريد تحديثه:{Colors.RESET}")
            print(f"  [1] العنوان")
            print(f"  [2] الوصف")
            print(f"  [3] الأولوية")
            print(f"  [4] تاريخ الاستحقاق")
            print(f"  [5] الحالة")
            
            choice = input(f"{Colors.GREEN}اختر: {Colors.RESET}").strip()
            
            if choice == '1':
                new_title = input(f"{Colors.GREEN}العنوان الجديد: {Colors.RESET}")
                success, msg = self.todo_manager.update_task(task_id, title=new_title)
            elif choice == '2':
                new_desc = input(f"{Colors.GREEN}الوصف الجديد: {Colors.RESET}")
                success, msg = self.todo_manager.update_task(task_id, description=new_desc)
            elif choice == '3':
                print(f"[1] عالي | [2] متوسط | [3] منخفض")
                p_choice = input(f"{Colors.GREEN}اختر: {Colors.RESET}")
                priority = {'1': 'High', '2': 'Medium', '3': 'Low'}.get(p_choice, 'Medium')
                success, msg = self.todo_manager.update_task(task_id, priority=priority)
            elif choice == '4':
                new_date = input(f"{Colors.GREEN}التاريخ الجديد [YYYY-MM-DD]: {Colors.RESET}")
                success, msg = self.todo_manager.update_task(task_id, due_date=new_date)
            elif choice == '5':
                print(f"[1] Pending | [2] In Progress | [3] Completed | [4] Cancelled")
                s_choice = input(f"{Colors.GREEN}اختر: {Colors.RESET}")
                status = {'1': 'Pending', '2': 'In Progress', '3': 'Completed', '4': 'Cancelled'}.get(s_choice)
                if status:
                    success, msg = self.todo_manager.update_task(task_id, status=status)
                else:
                    print(f"{Colors.RED}❌ اختيار غير صحيح{Colors.RESET}")
                    return
            
            print(f"\n{msg}")
            time.sleep(1)
        
        except ValueError:
            print(f"{Colors.RED}❌ أدخل رقماً صحيحاً{Colors.RESET}")
            time.sleep(1)
    
    def delete_task_ui(self):
        """Delete task"""
        self.clear_screen()
        self.print_header()
        
        print(f"\n{Colors.BLACK_BG}{Colors.GREEN}{Colors.BOLD}╔ حذف مهمة ╔\n{Colors.RESET}")
        
        try:
            task_id = int(input(f"{Colors.GREEN}رقم المهمة: {Colors.RESET}"))
            
            task = self.todo_manager.get_task(task_id)
            if not task:
                print(f"{Colors.RED}❌ المهمة غير موجودة{Colors.RESET}")
                time.sleep(1)
                return
            
            print(f"\n{Colors.YELLOW}المهمة المراد حذفها:{Colors.RESET}")
            print(self.format_task_display(task, show_details=True))
            
            confirm = input(f"\n{Colors.RED}هل أنت متأكد؟ (Yes/No): {Colors.RESET}").strip().upper()
            
            if confirm in ['YES', 'Y', 'نعم']:
                success, msg = self.todo_manager.delete_task(task_id)
                print(f"\n{msg}")
                time.sleep(1)
        
        except ValueError:
            print(f"{Colors.RED}❌ أدخل رقماً صحيحاً{Colors.RESET}")
            time.sleep(1)
    
    def show_overdue_tasks(self):
        """Show overdue tasks"""
        self.clear_screen()
        self.print_header()
        
        overdue = self.todo_manager.get_overdue_tasks()
        
        print(f"\n{Colors.BLACK_BG}{Colors.GREEN}{Colors.BOLD}╔ المهام المتأخرة ╔\n{Colors.RESET}")
        
        if not overdue:
            print(f"{Colors.GREEN}✅ لا توجد مهام متأخرة!{Colors.RESET}\n")
        else:
            print(f"{Colors.RED}⚠️  عدد المهام المتأخرة: {len(overdue)}\n{Colors.RESET}")
            for task in overdue:
                print(self.format_task_display(task))
                print()
        
        input(f"{Colors.GREEN}اضغط ENTER للرجوع...{Colors.RESET}")
    
    def show_statistics(self):
        """Show detailed statistics"""
        self.clear_screen()
        self.print_header()
        
        stats = self.todo_manager.get_task_statistics()
        
        print(f"\n{Colors.BLACK_BG}{Colors.GREEN}{Colors.BOLD}╔ الإحصائيات التفصيلية ╔\n{Colors.RESET}")
        
        stats_display = f"""
{Colors.CYAN}المجاميع:{Colors.RESET}
  {Colors.BOLD}الإجمالي:{Colors.RESET} {stats['total']} مهمة
  
{Colors.CYAN}حسب الحالة:{Colors.RESET}
  {Colors.YELLOW}⏳ قيد الانتظار:{Colors.RESET} {stats['pending']}
  {Colors.BLUE}🔄 قيد التنفيذ:{Colors.RESET} {stats['in_progress']}
  {Colors.GREEN}✅ مكتمل:{Colors.RESET} {stats['completed']}
  {Colors.RED}⛔ ملغي:{Colors.RESET} {stats['cancelled']}

{Colors.CYAN}حسب الأولوية:{Colors.RESET}
  {Colors.RED}عالي (High):{Colors.RESET} {stats['high_priority']}

{Colors.CYAN}معدلات:{Colors.RESET}
  {Colors.GREEN}نسبة الإنجاز:{Colors.RESET} {stats['completion_rate']}%
  {Colors.RED}المهام المتأخرة:{Colors.RESET} {stats['overdue']}
"""
        print(stats_display)
        
        input(f"{Colors.GREEN}اضغط ENTER للرجوع...{Colors.RESET}")
    
    def run(self):
        """Main application loop"""
        while True:
            self.display_main_menu()
            
            choice = input(f"{Colors.GREEN}اختر الخيار: {Colors.RESET}").strip().upper()
            
            if choice == '1':
                self.display_all_tasks()
            elif choice == '2':
                self.add_new_task()
            elif choice == '3':
                self.search_task()
            elif choice == '4':
                self.update_task_ui()
            elif choice == '5':
                self.delete_task_ui()
            elif choice == '6':
                self.show_overdue_tasks()
            elif choice == '7':
                self.show_statistics()
            elif choice == '8':
                self.show_settings()
            elif choice == 'Q':
                print(f"\n{Colors.GREEN}شكراً لاستخدام تطبيق المهام! (Thank you!)...")
                print(f"وداعاً! (Goodbye!){Colors.RESET}\n")
                break
            else:
                print(f"{Colors.RED}❌ خيار غير صحيح{Colors.RESET}")
                time.sleep(1)
    
    def show_settings(self):
        """Show settings menu"""
        self.clear_screen()
        self.print_header()
        
        settings = f"""
{Colors.BLACK_BG}{Colors.GREEN}{Colors.BOLD}
╔ الإعدادات (SETTINGS) ╔
║
║  ملف التخزين: {self.todo_manager.storage_file}
║  عدد المهام: {len(self.todo_manager.tasks)}
║  اللغة: العربية والإنجليزية
║  الوضع: Green Screen Terminal UI
║
║  [1] حول البرنامج (About)
║  [2] مساعدة (Help)
║  [B] رجوع (Back)
║
╚════════════════════════════════════════════════════════════════════════╝
{Colors.RESET}"""
        print(settings)
        
        choice = input(f"{Colors.GREEN}اختر: {Colors.RESET}").strip().upper()
        
        if choice == '1':
            self.show_about()
        elif choice == '2':
            self.show_help()


def main():
    """Main entry point"""
    print(f"{Colors.BLACK_BG}{Colors.GREEN}")
    print("جاري تحميل البرنامج... (Initializing...)")
    print(f"{Colors.RESET}")
    time.sleep(1)
    
    app = TodoListUI()
    app.run()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.GREEN}تم إيقاف البرنامج (Program terminated){Colors.RESET}\n")
    except Exception as e:
        print(f"\n{Colors.RED}خطأ: {str(e)}{Colors.RESET}\n")
