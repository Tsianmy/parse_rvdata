import argparse
import os
import glob
from tqdm import tqdm
from rvdata_parser import RvdataParser

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', '-d', help='path to rvdata files', required=True)
    parser.add_argument('--out_dir', '-o', default=None, help='path to output')
    parser.add_argument('--mode', '-m', default=1, type=int, choices=[1, 2],
        help='parse mode. 1: rvdata2yml | 2: mapdata2txt')
    
    args = parser.parse_args()
    if args.out_dir is None:
        args.out_dir = args.data_dir
    return args

def get_rvdata_flist(path):
    flist = sorted(glob.glob(path))
    return flist

def parse_rvdata(data_dir, out_dir, mode):
    flist = []
    if mode == 1:
        path = os.path.join(data_dir, '*.rvdata*')
    elif mode == 2:
        path = os.path.join(data_dir, 'Map[0-9][0-9][0-9].rvdata*')
    flist = get_rvdata_flist(path)

    rvdata_parser = RvdataParser()
    tqdm_flist = tqdm(flist)
    for rvdata_f in tqdm_flist:
        tqdm_flist.set_description(rvdata_f)
        rvdata_parser.parse_rvdata(rvdata_f)
        basename = os.path.splitext(os.path.basename(rvdata_f))[0]
        if mode == 1:
            save_path = os.path.join(out_dir, basename + '.yml')
            rvdata_parser.to_yaml(save_path)
        elif mode == 2:
            save_path = os.path.join(out_dir, basename + '.txt')
            rvdata_parser.events_to_txt(save_path)

if __name__ == '__main__':
    args = parse_args()
    parse_rvdata(args.data_dir, args.out_dir, args.mode)