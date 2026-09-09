# MongoDB Local Setup Guide
This guide provides instructions on how to download and install MongoDB locally on Windows, macOS, and Linux.
## Windows
1. **Download the Installer:**
   - Go to the [MongoDB Download Center](https://www.mongodb.com/try/download/community).
   - Select "Windows" as the platform and "msi" as the package.
   - Click **Download**.
2. **Run the Installer:**
   - Double-click the downloaded `.msi` file.
   - Follow the installation wizard. Choose the **Complete** setup type.
   - Leave "Install MongoDB as a Service" checked (this runs MongoDB automatically in the background).
   - (Optional) Leave "Install MongoDB Compass" checked if you want a graphical user interface for managing your databases.
3. **Verify Installation:**
   - Open Command Prompt or PowerShell and type:
     ```cmd
     mongod --version
     ```
---
## macOS
The recommended way to install MongoDB on macOS is by using the Homebrew package manager.
1. **Install Homebrew** (skip if you already have it installed):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. **Tap the MongoDB Homebrew Tap:**
   ```bash
   brew tap mongodb/brew
   ```
3. **Install MongoDB Community Edition:**
   ```bash
   brew install mongodb-community@7.0
   ```
4. **Start MongoDB:**
   To run MongoDB as a macOS service (automatically starts on login):
   ```bash
   brew services start mongodb-community@7.0
   ```
   Or, to run it manually in the background just for your current session:
   ```bash
   mongod --config /opt/homebrew/etc/mongod.conf --fork
   ```
5. **Verify Installation:**
   ```bash
   mongod --version
   ```
---
## Linux (Ubuntu/Debian)
These instructions are tailored for Ubuntu (e.g., 22.04 Jammy). For other distributions, you can find the specific package manager instructions on the official MongoDB docs.
1. **Import the MongoDB public GPG Key:**
   ```bash
   curl -fsSL https://pgp.mongodb.com/server-7.0.asc | \
      sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg \
      --dearmor
   ```
2. **Create a list file for MongoDB:**
   ```bash
   echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
   ```
3. **Reload local package database:**
   ```bash
   sudo apt-get update
   ```
4. **Install the MongoDB packages:**
   ```bash
   sudo apt-get install -y mongodb-org
   ```
5. **Start and Enable MongoDB:**
   To start the service and enable it to start on boot:
   ```bash
   sudo systemctl start mongod
   sudo systemctl enable mongod
   ```
6. **Verify Installation:**
   ```bash
   mongod --version
   ```