#!/usr/bin/bash

SECRET="bigtent"

try_decrypt() {
    echo $1 | gpg --batch --yes --passphrase-fd 0 firefox.log.gz.gpg > /dev/null 2>&1
    if [ "$?" -eq 0 ]; then
        echo $1 | gpg --batch --yes --passphrase-fd 0 signal.log.gpg > /dev/null 2>&1
        echo "SUCCESS (PASSPHRASE: $1)"
        exit 0
    fi
}


YEARS=(2021 2020)
MONTHS=("01" "02" "03" "04" "05" "06" "07" "08" "09" "10" "11" "12")
DAYS=("01" "02" "03" "04" "05" "06" "07" "08" "09" 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31)

for year in ${YEARS[*]}; do
    for month in ${MONTHS[*]}; do
          for day in ${DAYS[*]}; do
            str="$year-$month-$day $SECRET" 
            key="$(echo -n $str | sha256sum | cut -d ' ' -f 1)"
            try_decrypt "$key"
          done
       done
done
