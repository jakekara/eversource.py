from .eversource import get_report, REGION_IDS
from .convert import convert
import argparse
import json

def main():
    parser = argparse.ArgumentParser(
        "eversource.py", 
        description="download eversource outage data"
    )

    parser.add_argument(
            "--region-id", 
            choices=REGION_IDS
        )

    parser.add_argument(
        "--format", 
        help="output format", 
        choices=["json", "csv"], 
        default="csv")

    parser.add_argument(
        "--out",
        required=True,
        help="output file name", 
        type=str
    )
    
    args = parser.parse_args()

    data = get_report(args.region_id)

    if args.format == "csv":
        data = convert(data, args.out)
    else:
        open(args.out, "w").write(json.dumps(data, indent=2))

if __name__ == "__main__":

    main()