import sys
import os
import glob
from PIL import Image

def process_image(png_filename):
    base_filename = os.path.splitext(png_filename)[0]
    pna_filename = f"{base_filename}.pna"

    if not os.path.exists(pna_filename):
        print(f"対応するPNAファイルが見つかりません: {pna_filename}")
        return

    try:
        # PNGとPNAファイルを読み込む
        png_image = Image.open(png_filename)
        pna_image = Image.open(pna_filename)
    except IOError as e:
        print(f"ファイルを読み込めませんでした: {e}")
        return

    # PNAをグレースケールに変換
    pna_gray = pna_image.convert("L")

    # PNGを32bit ARGBに変換
    png_argb = png_image.convert("RGBA")

    # PNAの内容をアルファチャンネルとしてPNGに適用
    png_argb.putalpha(pna_gray)

    # PNGファイルを上書き保存
    png_argb.save(png_filename, "PNG")
    print(f"変換完了: {png_filename}")

if __name__ == "__main__":
    #如果有argv
    if len(sys.argv) == 2:
        pattern = sys.argv[1]
        for png_file in glob.glob(pattern):
            process_image(png_file)
    else:
        #遍历当前目录下的所有文件夹中的png文件
        for png_file in glob.glob("**/*.png", recursive=True):
            process_image(png_file)

