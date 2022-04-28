#!/bin/bash

if [[ -f "log.csv" ]]; then
  rm log.csv
fi

touch log.csv

# while true; do
for i in {1..500}; do
    adc_raw=`cat /sys/bus/iio/devices/iio:device0/in_voltage0_raw`
    adc_scale=`cat /sys/bus/iio/devices/iio:device0/in_voltage0_scale`
    # echo $adc_scale
    result=`echo $adc_raw*$adc_scale | bc`
    echo $i, $result >> log.csv
    echo $result
    sleep 0.01
done
