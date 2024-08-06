import zipfile
import os
import shutil

# 定义路径和参数
jar_file_path = 'xxxxxx/xxxxx/xxx/xx.jar'  # 原始 .jar 文件路径
output_dir = 'xxxxxx/xxxxx/xxx/xx'  # 输出目录路径
username_base = '10086'  # 要修改的账号
new_username_prefix = '10088'  # 修改后的账号前缀
start_suffix = 9  # 后缀的起始值
end_suffix = 18  # 后缀的结束值
new_file_name = '新名称'  # 新文件名的前缀


# 创建输出目录
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 计算生成的份数
copy_count = end_suffix - start_suffix + 1

# 复制文件并修改内容
for i, suffix in enumerate(range(start_suffix, end_suffix + 1), start=1):
    # 定义每个新 .jar 文件的路径
    new_jar_path = os.path.join(output_dir, f'{new_file_name}{i}.jar')
    temp_dir = os.path.join(output_dir, f'temp_{i}')

    # 解压原始 .jar 文件到临时目录
    with zipfile.ZipFile(jar_file_path, 'r') as jar:
        jar.extractall(temp_dir)

    # 修改 MANIFEST.MF 文件中的内容
    manifest_file_path = os.path.join(temp_dir, 'META-INF', 'MANIFEST.MF')
    if os.path.exists(manifest_file_path):
        with open(manifest_file_path, 'r', newline='') as file:
            content = file.read()

        # 生成新的用户名，例如 10088078, 10088079, ..., 10088098
        new_username = f'{new_username_prefix}{suffix:03d}'

        # 修改 username
        modified_content = content.replace(username_base, new_username)

        # 将修改后的内容写回 MANIFEST.MF 文件
        with open(manifest_file_path, 'w', newline='') as file:
            file.write(modified_content)

    # 重新打包为 .jar 文件
    with zipfile.ZipFile(new_jar_path, 'w', zipfile.ZIP_DEFLATED) as jar:
        for foldername, subfolders, filenames in os.walk(temp_dir):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                arcname = os.path.relpath(file_path, temp_dir)
                jar.write(file_path, arcname)

    # 清理临时目录
    shutil.rmtree(temp_dir)

print(f"{copy_count} 个 {new_file_name}.jar 文件已生成并修改完毕！")
