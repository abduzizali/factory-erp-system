## 📖 Digital Clock - Comprehensive Usage Guide

### Quick Start ⚡

```bash
python digital_clock.py
```

---

## Menu Navigation Guide 🗺️

### 1️⃣ Start Clock Display

Launches the live clock showing all configured timezones with auto-refresh.

**Features:**
- Real-time updates (default: every 1 second)
- Current date and time for each timezone
- Automatic DST handling
- Smooth scrolling display

**How to Exit:**
- Press `CTRL+C` (Keyboard Interrupt)
- Or `Q` key followed by Enter

---

### 2️⃣ Add Custom Timezone

Add any timezone from the PyTZ database.

**Steps:**
1. Select option `2` from main menu
2. Enter timezone name (e.g., `Asia/Bangkok`)
3. Enter display name (e.g., `Bangkok (ICT)`)
4. Confirm addition

**Available Timezone Format:**
```
Continent/City
Examples:
  - Asia/Dubai
  - Europe/Paris
  - America/Los_Angeles
  - Africa/Johannesburg
  - Australia/Melbourne
```

**Tip:** Use option `4` to view all available timezones before adding.

---

### 3️⃣ Remove Timezone

Remove a timezone from the display list.

**Steps:**
1. Select option `3` from main menu
2. View current timezone list
3. Enter the number of timezone to remove
4. Confirm removal

**Note:** Changes are temporary until application restarts. To make permanent, edit the Python file.

---

### 4️⃣ Show All Available Timezones

Display complete list of all 400+ available timezones in the PyTZ database.

**Features:**
- Numbered list (1-400+)
- Full timezone path (e.g., `Asia/Shanghai`)
- Scrollable display
- Press ENTER to return to menu

**Common Timezones by Region:**

**🌍 Middle East & North Africa**
- Africa/Cairo (Egypt)
- Africa/Johannesburg (South Africa)
- Asia/Dubai (UAE)
- Asia/Riyadh (Saudi Arabia)
- Asia/Istanbul (Turkey)

**🌏 Asia-Pacific**
- Asia/Bangkok (Thailand)
- Asia/Hong_Kong (Hong Kong)
- Asia/Shanghai (China)
- Asia/Singapore (Singapore)
- Asia/Tokyo (Japan)
- Australia/Sydney (Australia)

**🌎 Americas**
- America/New_York (USA East)
- America/Chicago (USA Central)
- America/Denver (USA Mountain)
- America/Los_Angeles (USA West)
- America/Toronto (Canada)
- America/Mexico_City (Mexico)
- America/Sao_Paulo (Brazil)

**🌍 Europe**
- Europe/London (UK)
- Europe/Paris (France)
- Europe/Berlin (Germany)
- Europe/Moscow (Russia)

---

### 5️⃣ Settings Menu

Configure application preferences.

**Current Settings Options:**
- View timezone count
- Display format (24-hour)
- Auto-refresh status

**Future Settings (v2.0):**
- Refresh rate adjustment
- Color scheme selection
- 12-hour/24-hour format toggle
- Startup timezone preferences

---

## Display Format Examples 📋

### Clock Display Output

```
╔════════════════════════════════════════════════════════════════════════╗
║                    ⏰ DIGITAL CLOCK - WORLD TIMEZONES ⏰             ║
╚════════════════════════════════════════════════════════════════════════╝

╔ CURRENT TIME DISPLAY ╔

║ [1] Mecca (AST)              │ 14:30:45 │ Thursday, 10 September 2026
║ [2] Cairo (EET)              │ 13:30:45 │ Thursday, 10 September 2026
║ [3] London (GMT/BST)         │ 12:30:45 │ Thursday, 10 September 2026
```

**Format Breakdown:**
- `[N]` - Timezone number
- `Name (CODE)` - Timezone display name and abbreviation
- `HH:MM:SS` - Current time in 24-hour format
- `Day, Date Month Year` - Full date

---

## Keyboard Shortcuts Reference ⌨️

### During Clock Display

| Key | Function |
|-----|----------|
| `Q` | Quit clock and return to menu |
| `A` | Add new timezone (quick access) |
| `R` | Remove timezone (quick access) |
| `U` | Change update speed |
| `F2` | Refresh display manually |
| `F5` | Enter full-screen mode |
| `ESC` | Return to main menu |
| `CTRL+C` | Emergency exit |

### In Menu

| Key | Function |
|-----|----------|
| `1-5` | Select menu option |
| `Q` | Quit application |
| `ENTER` | Confirm input |

---

## Common Tasks 🎯

### Task 1: Add Your Local Timezone

```
1. Select "2" (Add Custom Timezone)
2. Enter: Asia/Riyadh (or your timezone)
3. Enter: My Office (KSA)
4. Confirm
```

### Task 2: Set Up for International Team Meeting

```
1. Clear default timezones
2. Add only relevant timezones:
   - Your location
   - Meeting participants' locations
3. Start clock display
4. Pin timezones to reference during call
```

### Task 3: Monitor Multiple Office Locations

```
1. Add New York office (America/New_York)
2. Add London office (Europe/London)
3. Add Dubai office (Asia/Dubai)
4. Add Singapore office (Asia/Singapore)
5. Run live clock to see all office times
```

### Task 4: Display 24-Hour Coverage Timeline

```
Add these timezones to see full day coverage:
- America/Los_Angeles (UTC-8)
- America/New_York (UTC-5)
- Europe/London (UTC+0)
- Asia/Dubai (UTC+4)
- Asia/Singapore (UTC+8)
- Australia/Sydney (UTC+10)
```

---

## Tips & Tricks 💡

### ✅ Performance Optimization

- Display max 10-15 timezones for best performance
- Increase refresh rate to 2-3 seconds for slower systems
- Use Ctrl+C to exit quickly instead of menu navigation

### ✅ Timezone Accuracy

- DST changes are handled automatically
- PyTZ database updates every 3-4 months
- Timezone code (AST, EET, etc.) may change with DST

### ✅ Terminal Configuration

- Use 120+ character width for best display
- Enable 256-color mode in terminal settings
- Maximize terminal window for full-screen mode

### ✅ Using as System Monitor

```bash
# Run in background
nohup python digital_clock.py &

# Add to crontab for startup
@reboot cd /path/to/digital-clock && python digital_clock.py
```

---

## Troubleshooting 🔧

### Issue: Colors Not Displaying Correctly

**Solution:**
```bash
# Set terminal to 256-color mode
export TERM=xterm-256color
python digital_clock.py
```

### Issue: Time Zone Not Found

**Solution:**
1. Check spelling carefully (case-sensitive)
2. Use format: `Continent/City`
3. Run option `4` to view exact timezone name
4. Use `UTC±X` format if needed (e.g., `Etc/GMT-4`)

### Issue: Application Too Slow

**Solution:**
1. Reduce number of timezones
2. Increase refresh rate to 2-3 seconds
3. Close other applications
4. Update PyTZ library: `pip install --upgrade pytz`

### Issue: Terminal Size Warning

**Solution:**
- Resize terminal to at least 80x24 characters
- Use full-screen mode (F5)
- Reduce displayed information

---

## Advanced Configuration 🔬

### Modify Default Timezones (Permanent)

Edit `digital_clock.py` and find this section:

```python
self.timezones = [
    {'name': 'Mecca (AST)', 'tz': 'Asia/Riyadh', 'code': 'AST'},
    {'name': 'Cairo (EET)', 'tz': 'Africa/Cairo', 'code': 'EET'},
    # ... more
]
```

Add or remove as needed.

### Change Refresh Rate Default

Find this line:

```python
self.run_live_clock(refresh_rate=1)
```

Change `1` to desired seconds (e.g., `2` for 2-second refresh).

### Customize Display Colors

Edit the `Colors` class:

```python
class Colors:
    GREEN = '\033[92m'      # Change to '\033[94m' for blue
    BLACK_BG = '\033[40m'   # Change background color
```

ANSI Color Codes:
- 30-37: Foreground colors
- 40-47: Background colors
- 90-97: Bright foreground colors

---

## Integration Examples 🔗

### Use in Shell Scripts

```bash
#!/bin/bash
echo "Checking server times:"
python digital_clock.py << EOF
1
Q
EOF
```

### Cron Job Automation

```bash
# Monitor specific timezones every hour
0 * * * * cd /path/to/digital-clock && python digital_clock.py
```

### Combined with Other Tools

```bash
# Display with system info
python digital_clock.py & 
top &
wait
```

---

## FAQ ❓

**Q: Can I display more than 20 timezones?**
A: Yes, but performance may degrade. Recommended max: 15 timezones.

**Q: How do I save my timezone preferences?**
A: Currently temporary. Edit the Python file for permanent changes (v2.0 will add config file support).

**Q: Does it support 12-hour time format?**
A: Not in current version (v1.0). Edit the time format string for 12-hour display.

**Q: Can I use this in a web application?**
A: Yes, extract the time calculation logic and adapt it for web framework (Flask/Django).

**Q: Is there a mobile version?**
A: Not yet. Consider developing a Python mobile app wrapper (Kivy/PyQt Mobile).

---

## Support & Feedback 📧

- 🐛 Report bugs via GitHub Issues
- 💡 Suggest features
- 🤝 Contribute code improvements
- 📧 Email: abduzizali@example.com

---

**Last Updated:** September 2026 | Version 1.0.0
