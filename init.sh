#!/bin/bash

cwd=pwd

cd ~

rm -rf sense_hat_containerized

mkdir sense_hat_containerized

cd sense_hat_containerized

touch data.json

touch leds.json

cd ~

mkdir contribution-hat-config

cd $cwd

cp ./contribution-hat/config_template.yaml ~/contribution-hat-config/config.yaml