import os
import shutil
import tkinter as tk
import zipfile
from tkinter import filedialog
from tkinter import messagebox


def browse_file():
    jar_file_path.set(filedialog.askopenfilename(filetypes=[("JAR files", "*.jar")]))


def browse_output_dir():
    output_dir.set(filedialog.askdirectory())


def generate_files():
    try:
        jar_file = jar_file_path.get()
        output = output_dir.get()
        new_value_prefix = new_value_prefix_entry.get()
        start_suffix = start_suffix_entry.get()
        end_suffix = end_suffix_entry.get()
        new_file_name = new_file_name_entry.get()

        # 参数检查
        if not jar_file:
            messagebox.showerror("错误", "请选择基础 JAR 文件！")
            return
        if not output:
            messagebox.showerror("错误", "请选择输出目录！")
            return
        if not new_value_prefix:
            messagebox.showerror("错误", "请输入账号前缀！")
            return
        if not start_suffix:
            messagebox.showerror("错误", "请输入账号后缀起始值！")
            return
        if not end_suffix:
            messagebox.showerror("错误", "请输入账号后缀结束值！")
            return
        if not new_file_name:
            messagebox.showerror("错误", "请输入新文件名前缀！")
            return

        try:
            start_suffix = int(start_suffix)
            end_suffix = int(end_suffix)
        except ValueError:
            messagebox.showerror("错误", "账号后缀起始值和结束值必须是整数！")
            return

        if start_suffix > end_suffix:
            messagebox.showerror("错误", "账号后缀起始值不能大于结束值！")
            return

        if not os.path.exists(output):
            os.makedirs(output)

        if not jar_file or not output:
            messagebox.showerror("错误", "请先选择 JAR 文件和输出目录！")
            return

        if not os.path.exists(output):
            os.makedirs(output)

        # 定义需要替换的参数和其前缀
        old_prefix = "username:"

        # 计算后缀的宽度
        suffix_length = max(len(str(start_suffix)), len(str(end_suffix)))

        # 按照指定的后缀范围生成文件
        for suffix in range(start_suffix, end_suffix + 1):
            # 定义每个新 .jar 文件的路径
            new_jar_path = os.path.join(output, f'{new_file_name}{suffix}.jar')
            temp_dir = os.path.join(output, f'temp_{suffix}')

            # 解压原始 .jar 文件到临时目录
            with zipfile.ZipFile(jar_file, 'r') as jar:
                jar.extractall(temp_dir)

            # 修改 MANIFEST.MF 文件中的内容
            manifest_file_path = os.path.join(temp_dir, 'META-INF', 'MANIFEST.MF')
            if os.path.exists(manifest_file_path):
                with open(manifest_file_path, 'r', encoding='utf-8') as file:
                    lines = file.readlines()

                # 替换指定参数的值
                new_value = f"{new_value_prefix}{suffix:0{suffix_length}}"
                new_content = []
                for line in lines:
                    if line.startswith(old_prefix):
                        new_content.append(f"{old_prefix} {new_value}\n")
                    else:
                        new_content.append(line)

                # 将修改后的内容写回 MANIFEST.MF 文件
                with open(manifest_file_path, 'w', encoding='utf-8', newline='') as file:
                    file.writelines(new_content)

            # 重新打包为 .jar 文件
            with zipfile.ZipFile(new_jar_path, 'w', zipfile.ZIP_DEFLATED) as jar:
                for foldername, subfolders, filenames in os.walk(temp_dir):
                    for filename in filenames:
                        file_path = os.path.join(foldername, filename)
                        arcname = os.path.relpath(file_path, temp_dir)
                        jar.write(file_path, arcname)

            # 清理临时目录
            shutil.rmtree(temp_dir)

        messagebox.showinfo("完成", f"{end_suffix - start_suffix + 1}个文件已生成并修改完毕！")
    except Exception as e:
        messagebox.showerror("错误", str(e))


# 创建主窗口
root = tk.Tk()
root.title("专号账号批量生成工具-海贼糕手")

# 定义变量
jar_file_path = tk.StringVar()
output_dir = tk.StringVar()
new_value_prefix_entry = tk.Entry(root)

# 创建并放置控件
tk.Label(root, text="选择基础文件:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
tk.Entry(root, textvariable=jar_file_path, width=40).grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="浏览", command=browse_file).grid(row=0, column=2, padx=10, pady=5)

tk.Label(root, text="选择输出目录:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
tk.Entry(root, textvariable=output_dir, width=40).grid(row=1, column=1, padx=10, pady=5)
tk.Button(root, text="浏览", command=browse_output_dir).grid(row=1, column=2, padx=10, pady=5)

tk.Label(root, text="账号前缀:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
new_value_prefix_entry = tk.Entry(root)
new_value_prefix_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="账号后缀起始值:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
start_suffix_entry = tk.Entry(root)
start_suffix_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="账号后缀结束值:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
end_suffix_entry = tk.Entry(root)
end_suffix_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="新文件名前缀:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
new_file_name_entry = tk.Entry(root)
new_file_name_entry.grid(row=5, column=1, padx=10, pady=5)

tk.Button(root, text="生成文件", command=generate_files).grid(row=6, columnspan=3, pady=20)

# 添加底部标签
bottom_frame = tk.Frame(root)
bottom_frame.grid(row=8, column=0, columnspan=3, sticky="s", pady=5)  # 固定在窗口底部
tk.Label(bottom_frame, text="仅供学习交流，不得用于商业用途，如有侵权请联系删除", anchor="center",
         font=("Helvetica", 12, "bold")).pack()

# 启动主循环
root.mainloop()
