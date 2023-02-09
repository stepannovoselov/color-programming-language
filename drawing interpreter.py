from PIL import Image
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror

print(r"""
 ________  ___  _______  _________        ___  ________   _________  _______   ________  ________  ________  _______  _________  _______   ________     
|\   __  \|\  \|\  ___ \|\___   ___\     |\  \|\   ___  \|\___   ___\\  ___ \ |\   __  \|\   __  \|\   __  \|\  ___ \|\___   ___\\  ___ \ |\   __  \    
\ \  \|\  \ \  \ \   __/\|___ \  \_|     \ \  \ \  \\ \  \|___ \  \_\ \   __/|\ \  \|\  \ \  \|\  \ \  \|\  \ \   __/\|___ \  \_\ \   __/|\ \  \|\  \   
 \ \   ____\ \  \ \  \_|/__  \ \  \       \ \  \ \  \\ \  \   \ \  \ \ \  \_|/_\ \   _  _\ \   ____\ \   _  _\ \  \_|/__  \ \  \ \ \  \_|/_\ \   _  _\  
  \ \  \___|\ \  \ \  \_|\ \  \ \  \       \ \  \ \  \\ \  \   \ \  \ \ \  \_|\ \ \  \\  \\ \  \___|\ \  \\  \\ \  \_|\ \  \ \  \ \ \  \_|\ \ \  \\  \| 
   \ \__\    \ \__\ \_______\  \ \__\       \ \__\ \__\\ \__\   \ \__\ \ \_______\ \__\\ _\\ \__\    \ \__\\ _\\ \_______\  \ \__\ \ \_______\ \__\\ _\ 
    \|__|     \|__|\|_______|   \|__|        \|__|\|__| \|__|    \|__|  \|_______|\|__|\|__|\|__|     \|__|\|__|\|_______|   \|__|  \|_______|\|__|\|__|      (fake)                                                                                                       
""")


def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb


img_path = askopenfilename(title="Выберите картинку", filetypes=(("png files", "*.png"),))

if img_path == "":
    exit()

img = Image.open(img_path)
if (img.height, img.width) != (46, 60):
    showerror("Ошибка", "Файл должен быть размером 60x46")
    exit()

python_code = "stack = []\ndef get_input():\n    a = input('>> ')\n    if a.isnumeric():\n        return [int(a)]\n    else:\n        return [ord(i) for i in a]\n\n\n"

black_count = 0
red_count = 0
tabulation = False
functions_count = 0
not_use = []

for h in range(img.height):
    for w in range(img.width):
        r, g, b = img.getpixel((w, h))
        hex = rgb_to_hex((r, g, b))

        if hex == "000000":
            black_count += 1
            if black_count % 2 == 0:
                tabulation = False
                python_code += "\n"

            else:
                functions_count += 1
                python_code += "def " + "_" * functions_count + "():\n    global stack\n"


        elif hex == "ffffff":
            if tabulation:
                python_code += "        if len(stack) >= 1:\n            print(stack[-1])\n"
            else:
                python_code += "    if len(stack) >= 1:\n        print(stack[-1])\n"

        elif hex == "808080":
            if tabulation:
                python_code += "        if len(stack) >= 1:\n            print(chr(stack[-1]))\n"
            else:
                python_code += "    if len(stack) >= 1:\n        print(chr(stack[-1]))\n"

        elif hex == "ff0000":
            red_count += 1

        elif hex == "ffff00":
            if tabulation:
                python_code += "        if len(stack) >= 2:\n            a, b = stack[-1], stack[-2]\n            stack = stack[:len(stack)-2]\n            stack.append(a+b)\n"
            else:
                python_code += "    if len(stack) >= 2:\n        a, b = stack[-1], stack[-2]\n        stack = stack[:len(stack)-2]\n        stack.append(a+b)\n"

        elif hex == "00ff00":
            if tabulation:
                python_code += f"        stack.append({red_count})\n"
            else:
                python_code += f"    stack.append({red_count})\n"
            red_count = 0

        elif hex == "008cf0":
            if tabulation:
                python_code += "        stack += get_input()\n"
            else:
                python_code += "    stack += get_input()\n"

        elif hex == "ff00ff":
            if tabulation:
                python_code += "        if len(stack) >= 2:\n            a, b = stack[-1], stack[-2]\n            stack = stack[:len(stack)-2]\n            if a != 0:\n                stack.append(int(b/a))\n"
            else:
                python_code += "    if len(stack) >= 2:\n        a, b = stack[-1], stack[-2]\n        stack = stack[:len(stack)-2]\n        if a != 0:\n            stack.append(int(b/a))\n"

        elif hex == "b57900":
            if tabulation:
                python_code += "        if len(stack) >= 2:\n            a, b = stack[-1], stack[-2]\n            stack = stack[:len(stack)-2]\n            stack.append(a*b)\n"
            else:
                python_code += "    if len(stack) >= 2:\n        a, b = stack[-1], stack[-2]\n        stack = stack[:len(stack)-2]\n        stack.append(a*b)\n"

        elif hex == "013220":
            if tabulation:
                tabulation = False
            else:
                tabulation = True
                python_code += f"    if stack[-1] == {red_count}:\n"
                red_count = 0

        elif hex == "00508a":
            if tabulation:
                python_code += "        if len(stack) >= 1:\n            stack = stack[:len(stack)-1]\n"
            else:
                python_code += "    if len(stack) >= 1:\n        stack = stack[:len(stack)-1]\n"

        elif hex == "8b0000":
            if tabulation:
                python_code += "        if len(stack) >= 1:\n            stack[-1] = stack[-1] * -1\n"
            else:
                python_code += "    if len(stack) >= 1:\n        stack[-1] = stack[-1] * -1\n"

        elif hex == "9400d3":
            if tabulation:
                python_code += "        if len(stack) >= 2:\n            stack = stack[1:] + stack[:1]\n"
            else:
                python_code += "    if len(stack) >= 2:\n        stack = stack[1:] + stack[:1]\n"

        elif hex == "ff8c00":
            if tabulation:
                python_code += "        " + "_" * red_count + "()\n"
            else:
                python_code += "    " + "_" * red_count + "()\n"
            red_count = 0

        elif hex == "008b8b":
            if tabulation:
                tabulation = False
            else:
                if red_count != 0:
                    python_code += f"    for i_t_e_r in range({red_count}):\n"
                    tabulation = True
                    red_count = 0

        elif hex == "7fffd4":
            if tabulation:
                python_code += "        if len(stack) >= 1:\n            stack.append(stack[-1])\n"
            else:
                python_code += "    if len(stack) >= 1:\n        stack.append(stack[-1])\n"

        elif hex == "f0e68c":
            not_use.append(functions_count)

for i in range(1, functions_count + 1):
    if i not in not_use:
        python_code += "_" * i + "()\n"

print("\n\nУспешный запуск")

try:
    exec(python_code)
except Exception as error:
    print("Произошла ошибка!")
    print(error)
