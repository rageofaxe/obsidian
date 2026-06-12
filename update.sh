#!/bin/bash

# 0. chmod +x update.sh

# 1. Add all changes to the staging area
git add .

# 2. Commit with a fixed message
git commit -m "autoupdate"

# 3. Pull latest changes, then push your updates
git pull --ff -X theirs
git push
