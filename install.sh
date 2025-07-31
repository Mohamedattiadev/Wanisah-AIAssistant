#!/bin/bash

# ---------------------------
# Wanisah Installer Script
# Requires Python 3.11.9 via pyenv
# ---------------------------

echo "📦 Starting Wanisah installation..."
echo "-----------------------------------"

# STEP 1: Install Arch system dependencies
if [[ ! -f arch_req.txt ]]; then
	echo "❌ Missing 'arch_req.txt'. Please make sure it exists."
	exit 1
fi

echo "🔧 Installing required system packages with pacman..."
sudo pacman -Syu --needed --noconfirm $(<arch_req.txt)

# STEP 2: Ensure python3.11 is available (via pyenv or system)
if ! command -v python3.11 &>/dev/null; then
	echo "❌ python3.11 not found. Please install it with pyenv:"
	echo ""
	echo "   pyenv install 3.11.9"
	echo "   pyenv local 3.11.9"
	echo ""
	exit 1
fi

# STEP 3: Create virtual environment with python3.11 if it doesn't exist
if [[ ! -d "venv" ]]; then
	echo "🐍 Creating Python 3.11 virtual environment..."
	python3.11 -m venv venv
else
	echo "🔄 Virtual environment already exists. Activating it..."
fi

# STEP 4: Activate virtual environment (based on user's shell)
SHELL_NAME=$(basename "$SHELL")
if [[ "$SHELL_NAME" == "fish" ]]; then
	source venv/bin/activate.fish
elif [[ "$SHELL_NAME" == "zsh" || "$SHELL_NAME" == "bash" ]]; then
	source venv/bin/activate
else
	echo "⚠️ Unknown shell: $SHELL_NAME. Attempting default activation..."
	source venv/bin/activate 2>/dev/null || {
		echo "❌ Could not activate virtual environment. Please do so manually."
		exit 1
	}
fi

# STEP 5: Install Python dependencies
if [[ ! -f requirements.txt ]]; then
	echo "❌ Missing 'requirements.txt'. Please make sure it exists."
	exit 1
fi

echo "📦 Installing Python packages from requirements.txt..."
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "✅ Wanisah was installed successfully!"
echo "🚀 You can now start it by running: python main.py"
