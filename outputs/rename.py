"""
ファイル名の連番を整備する
"""

import os
import glob
import argparse

def make_filelist(folder):
    """
    ファイルリストを取得
    """
    filelist = glob.glob(folder + '**/*.png', recursive=True)
    return filelist

def rename_files(filelist, offset):
    """
    連番を変更
    """
    for i, filename in enumerate(filelist):
        # ファイル名を分割
        dirname, basename = os.path.split(filename)

        # 連番を設定
        renban = f'{i + offset:05d}'

        # ファイル名を変更
        newname = renban + os.path.basename(basename)[5:]
        newname = os.path.join(dirname, newname)
        print(f'{filename} -> {newname}')
        os.rename(filename, newname)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('folder', help='폴더명')
    parser.add_argument('--offset', type=int, default=0, help='시작 번호')
    args = parser.parse_args()

    filelist = make_filelist(args.folder)
    rename_files(filelist, args.offset)