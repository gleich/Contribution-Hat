#!/bin/bash

rm -rf ~/sense_hat_containerized

mkdir ~/sense_hat_containerized

touch ~/sense_hat_containerized/data.json

touch ~/sense_hat_containerized/leds.json

rm -rf ~/contribution-hat-config

mkdir ~/contribution-hat-config

cp ./contribution-hat/config_template.yaml ~/contribution-hat-config/config.yaml