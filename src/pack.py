import os
import re
import shutil

commies_root = 'downloads/commies'
meta_root = 'downloads/meta'
output_root = 'downloads/pack'

no_meta = []

def to_zip(eps_d, res_d, meta_d):
    eps_d = os.path.join(eps_d, 'original')
    episodes = os.listdir(eps_d)
    for episode in episodes:
        print(f'Compressing... {episode}')
        meta_src = os.path.join(meta_d, episode, "ComicInfo.xml")
        meta_dst = os.path.join(eps_d, episode, "ComicInfo.xml")
        if os.path.exists(meta_src):
            shutil.copyfile(meta_src, meta_dst)
        else:
            no_meta.append(meta_src)
        shutil.make_archive(
            os.path.join(res_d, episode),
            'zip',
            os.path.join(eps_d, episode)
        )


if __name__ == '__main__':
    commies = os.listdir(commies_root)
    old = os.listdir(output_root)

    for commic in commies:
        if commic not in old:
            eps_d = os.path.join(commies_root, commic)
            res_d = os.path.join(output_root, commic)
            meta_d = os.path.join(meta_root, commic)
            print(f'Processing: {commic}')
            os.mkdir(res_d)
            to_zip(eps_d, res_d, meta_d)

    if len(no_meta) > 0:
        print("Cannot find metadata:")
        for s in no_meta:
            print(s)
