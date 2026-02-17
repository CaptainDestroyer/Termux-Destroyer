#!/bin/bash

# Navigate to the Termux-Destroyer directory
cd $HOME/Termux-Destroyer || exit

# Pull the latest changes from the remote repository
git pull origin main

# Provide feedback to the user
echo "Repository updated successfully!"
