## 🐾 Taskbar Animation

This is a lightweight Python app that shows an animated pet (like a walking dog, planet, or anything you choose) in the **top-left corner of your Windows taskbar**.
The animation only plays **when you move your mouse** — perfect for adding a bit of life to your desktop!

---

### 🔧 Features

* 🐶 Custom animated GIF support
* 🖱️ Animation plays only when the mouse moves
* 📍Always stays on top (over taskbar)
* 💻 Autostarts with Windows (optional setup)
* 📦 Can be bundled into `.exe` using PyInstaller

---

### 🚀 How to Run

#### 1. Clone this repo or download the source

```bash
git clone https://github.com/yourusername/taskbar-pet-animation.git
cd taskbar-pet-animation
```

#### 2. Install required Python libraries

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, just run:

```bash
pip install pillow pyautogui
```

#### 3. Run the app

```bash
python main.py
```

You should see the animation appear in the top-left corner of your screen!

---

### 🐍 Build `.exe` (Optional)

To generate a standalone `.exe` using PyInstaller:

```bash
pyinstaller --noconsole --onefile main.py --add-data "planet.gif;."
```

* Make sure `planet.gif` is in the same folder.
* The final `.exe` will be inside the `dist` folder.

---

### ⚙️ Autostart with Windows (Optional)

1. Press `Win + R` → type `shell:startup` → hit Enter
2. Place a **shortcut** to your `main.exe` in that folder

Done! Now it will start every time you boot your computer.

---

### 📝 License

This project is free to use and modify under the MIT License.

---
