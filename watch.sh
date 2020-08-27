# Check CT outages every 5 minutes
while [ 1 -eq 1 ]; do
    TIMESTAMP=$(date +%y-%m-%d.%H-%M.%Z)
    FNAME=$TIMESTAMP.csv
    python -m eversource \
        --region-id=conn \
        --format=csv \
        --out="$FNAME"
    sleep 300
done
