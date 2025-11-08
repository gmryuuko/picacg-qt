import os
import time
import shutil
import sys

download_dir = 'downloads/pack'
nas_dir = '/Volumes/data/manga/HENTAI'
# back_dir = '/Volumes/LUMIX/备份/漫画/HENTAI'

if not os.path.exists(download_dir):
    print('Download directory does not exist.')
    sys.exit()

if not os.path.exists(nas_dir):
    print('NAS directory does not exist.')
    sys.exit()

# if not os.path.exists(back_dir):
#     print('Backup directory does not exist.')
#     sys.exit()


def clean_path(path):
    # 替换路径中的 \xa0 为普通空格
    return path.replace('\xa0', ' ')


def copy_dir(src, dst):
    print(f'Copying {src} to {dst}')
    shutil.copytree(src, dst)
    print('Done')


def copy_file(src, dst):
    print(f'Copying {src} to {dst}')
    shutil.copy(src, dst)
    print('Done')


def get_modification_time(path):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(path)))


# 检查是否有 -y 参数
auto_confirm = '-y' in sys.argv

packs = os.listdir(download_dir)


def confirm(src, dst) -> bool:
    print(f'【{src}】 -> 【{dst}】')
    print('Confirm? (y/n)')
    result = input()
    if result.lower() == 'y':
        return True
    else:
        print('Skip')
        return False


def try_copy_pack(src, dst):
    if not os.path.isdir(src):
        return
    if not os.path.exists(dst):
        if auto_confirm or confirm(src, dst):
            copy_dir(src, dst)
    else:
        zips = [f for f in os.listdir(src) if f.endswith('.zip')]
        for zip in zips:
            src_zip = os.path.join(src, zip)
            dst_zip = os.path.join(dst, zip)
            if not os.path.exists(dst_zip):
                if auto_confirm or confirm(src_zip, dst_zip):
                    copy_file(src_zip, dst_zip)


for pack in packs:
    try_copy_pack(os.path.join(download_dir, pack), os.path.join(nas_dir, pack))
    # try_copy_pack(os.path.join(download_dir, pack), os.path.join(back_dir, pack))

# 询问是否打开目录
open_dirs = input("Do you want to open the directories? (y/n): ")
if open_dirs.lower() == 'y':
    os.system(f'open "{download_dir}"')
    os.system(f'open "{nas_dir}"')
    # os.system(f'open "{back_dir}"')
