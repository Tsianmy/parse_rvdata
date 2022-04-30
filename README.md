Based on https://github.com/ChronoMonochrome/rvdata2json

### Extra dependencies

`pip install pyyaml rubymarshal`

### Usage

```shell
python main.py [-h]  --data_dir DATA_DIR [--out_dir OUT_DIR] [--mode {1,2}]
optional arguments:
  -h, --help
  --data_dir DATA_DIR, -d DATA_DIR
                        path to rvdata files
  --out_dir OUT_DIR, -o OUT_DIR
                        path to output
  --mode {1,2}, -m {1,2}
                        parse mode. 1: rvdata2yml | 2: mapdata2txt
```

#### Parse rvdata to yml

`python main.py -d </path/to/Data/> [-m 1]`

#### Parse Mapxxx.rvdata to txt

`python main.py -d </path/to/Data> [-m 2]`