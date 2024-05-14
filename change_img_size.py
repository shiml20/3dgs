from PIL import Image
import os

# 输入文件夹路径和输出文件夹路径
input_folder = "/home/sml/3dgs/splat/tsinghua/the_old_gate"
output_folder = "/home/sml/3dgs/splat/tsinghua/the_old_gate_small_size"

# 如果输出文件夹不存在，则创建
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历输入文件夹中的每张图片
for filename in os.listdir(input_folder):
    # 检查文件是否为图片
    if filename.endswith(".JPG") or filename.endswith(".png"):
        # 打开图片
        with Image.open(os.path.join(input_folder, filename)) as img:
            # 获取图片原始尺寸
            width, height = img.size
            # 缩小图片尺寸
            new_width = width // 8
            new_height = height // 8
            # 调整图片尺寸
            resized_img = img.resize((new_width, new_height), Image.LANCZOS)
            # 保存调整后的图片到输出文件夹中
            resized_img.save(os.path.join(output_folder, filename))
            print(f"{filename} 已缩小并保存到 {output_folder}")