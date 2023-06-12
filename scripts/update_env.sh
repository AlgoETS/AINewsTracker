#!/bin/bash

new_environment="prod"  # Replace with the desired new environment value

# Update app/config.py
awk -v new_environment="$new_environment" '/^ENVIRONMENT =/ {$NF = new_environment} 1' app/config.py > tmp && mv tmp app/config.py

echo "Environment updated to $new_environment"
