#!/usr/bin/env bash
set -e

echo "Starting Expense Tracker..."

# Go to project root
ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Create venv if missing
if [ ! -d "$ROOT_DIR/backend/.venv" ]; then
  echo "Creating virtual environment..."
  python3 -m venv "$ROOT_DIR/backend/.venv"
fi

# Activate venv
source "$ROOT_DIR/backend/.venv/bin/activate"

echo "Installing dependencies..."
python3 -m pip install --upgrade pip
python3 -m pip install -r "$ROOT_DIR/requirements.txt"

echo "▶ Starting backend..."
python3 -m uvicorn backend.server:app --reload &

echo "▶ Starting frontend..."
python3 -m streamlit run frontend/app.py
