# eversource.py

Get eversource outage data.


## Overview

The eversource outage page here takes a while to load, which sucks during a power outage when you have limited cellular data.

This script just downloads the data files without anything necessary to render the web page.

## Usage

```bash 
$ python3 -m eversource.__main__ --help
usage: eversource.py [-h] [--region-id {east,west,hampshire,conn}]
                     [--format {json,csv}] --out OUT

download eversource outage data

optional arguments:
  -h, --help            show this help message and exit
  --region-id {east,west,hampshire,conn}
  --format {json,csv}   output format
  --out OUT             output file name
```

## Example usage

Downloading Connecticut data to CSV 

```bash
(venv) $ python -m eversource.__main__ --region-id conn --out "example-output/conn.csv"
```

Downloading Connecticut data to JSON

```bash
(venv) $ python -m eversource.__main__ --region-id conn --out "example-output/conn.json" --format=json
```

## Watch and record outages continuously

The script `watch.sh` shows how you might want to set up a simple script to record outages every five minutes. This demo uses `conn` (Connecticut) as the region.
