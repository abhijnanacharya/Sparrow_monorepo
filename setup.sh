#!/bin/bash


set -e  # Exit on any error

echo "🚀 Setting up Word Cloud Visualizer..."
echo ""


GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' 

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check for Python
echo -e "${BLUE}Checking Python installation...${NC}"
if ! command_exists python3; then
    echo -e "${YELLOW}Python 3 is not installed. Please install Python 3.8 or higher.${NC}"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo -e "${GREEN}Found Python ${PYTHON_VERSION}${NC}"

# Check for Node.js
echo -e "${BLUE}Checking Node.js installation...${NC}"
if ! command_exists node; then
    echo -e "${YELLOW}Node.js is not installed. Please install Node.js 16 or higher.${NC}"
    exit 1
fi

NODE_VERSION=$(node --version)
echo -e "${GREEN}Found Node.js ${NODE_VERSION}${NC}"

echo ""
echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Setting up Backend (FastAPI)${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Navigate to backend directory
cd backend || exit 1

# Check if virtual environment exists
if [ -d ".venv" ] || [ -d "venv" ]; then
    echo -e "${YELLOW}Virtual environment already exists. Skipping creation.${NC}"
    echo -e "${YELLOW}If you want to recreate it, delete .venv or venv folder and run again.${NC}"
else
    echo "Creating Python virtual environment..."
    python3 -m venv .venv
    echo -e "${GREEN}Virtual environment created${NC}"
fi

# Activate virtual environment
echo "Activating virtual environment..."
if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
elif [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
else
    echo -e "${YELLOW}Could not find virtual environment activation script${NC}"
    exit 1
fi

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip --quiet

# Install backend dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt --quiet

echo -e "${GREEN}Backend dependencies installed successfully${NC}"
echo ""

# Return to root directory
cd ..

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Setting up Frontend (React)${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Navigate to frontend directory
cd frontend || exit 1

# Check if node_modules exists
if [ -d "node_modules" ]; then
    echo -e "${YELLOW}node_modules already exists. Skipping install.${NC}"
    echo -e "${YELLOW}If you want to reinstall, delete node_modules folder and run again.${NC}"
else
    echo "Installing Node.js dependencies..."
    npm install --silent
    
    echo -e "${GREEN}Frontend dependencies installed successfully${NC}"
fi

# Return to root directory
cd ..

echo ""
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}✅ Setup completed successfully!${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo -e "${BLUE}To start the application:${NC}"
echo ""
echo -e "${YELLOW}Backend:${NC}"
echo "  cd backend"
echo "  source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate"
echo "  uvicorn main:app --reload"
echo ""
echo -e "${YELLOW}Frontend:${NC}"
echo "  cd frontend"
echo "  npm run dev"
echo ""
echo -e "${BLUE}Backend will run on: http://localhost:8000${NC}"
echo -e "${BLUE}Frontend will run on: http://localhost:5173${NC}"
echo -e "${BLUE}API docs available at: http://localhost:8000/docs${NC}"
echo ""