#!/usr/bin/env python3
"""
Setup script for Smart Bank Assistant
"""

import os
import sys
import subprocess
import shutil
import venv

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        return False
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    return True

def create_virtual_environment():
    """Create a virtual environment for the project"""
    venv_name = "bank_chatbot_env"
    
    if os.path.exists(venv_name):
        print(f"✅ Virtual environment '{venv_name}' already exists")
        return venv_name
    
    print(f"🔧 Creating virtual environment '{venv_name}'...")
    try:
        venv.create(venv_name, with_pip=True)
        print(f"✅ Virtual environment created successfully")
        return venv_name
    except Exception as e:
        print(f"❌ Failed to create virtual environment: {e}")
        return None

def get_pip_command(venv_name=None):
    """Get the appropriate pip command based on environment"""
    if venv_name and os.path.exists(venv_name):
        if sys.platform == "win32":
            return os.path.join(venv_name, "Scripts", "pip.exe")
        else:
            return os.path.join(venv_name, "bin", "pip")
    else:
        return [sys.executable, "-m", "pip"]

def install_dependencies(venv_name=None):
    """Install required dependencies"""
    print("📦 Installing dependencies...")
    
    pip_cmd = get_pip_command(venv_name)
    
    try:
        if isinstance(pip_cmd, str):
            subprocess.check_call([pip_cmd, "install", "-r", "requirements.txt"])
        else:
            subprocess.check_call(pip_cmd + ["install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def create_env_file():
    """Create .env file if it doesn't exist"""
    if os.path.exists(".env"):
        print("✅ .env file already exists")
        return True
    
    print("🔧 Creating .env file...")
    env_content = """# Google API Key for Gemini AI
# Get your API key from: https://makersuite.google.com/app/apikey
GOOGLE_API_KEY=your_google_api_key_here

# Add any other environment variables below
"""
    
    try:
        with open(".env", "w") as f:
            f.write(env_content)
        print("✅ .env file created")
        print("⚠️  Please update the GOOGLE_API_KEY in the .env file")
        return True
    except Exception as e:
        print(f"❌ Failed to create .env file: {e}")
        return False

def check_faq_file():
    """Check if FAQ file exists"""
    if os.path.exists("BankFAQs.csv"):
        print("✅ BankFAQs.csv found")
        return True
    else:
        print("⚠️  BankFAQs.csv not found")
        print("   Please ensure you have a BankFAQs.csv file with 'Question' and 'Answer' columns")
        return False

def run_tests(venv_name=None):
    """Run the test suite"""
    print("🧪 Running tests...")
    try:
        if venv_name and os.path.exists(venv_name):
            if sys.platform == "win32":
                python_cmd = os.path.join(venv_name, "Scripts", "python.exe")
            else:
                python_cmd = os.path.join(venv_name, "bin", "python")
            subprocess.check_call([python_cmd, "test_chatbot.py"])
        else:
            subprocess.check_call([sys.executable, "test_chatbot.py"])
        return True
    except subprocess.CalledProcessError:
        print("❌ Tests failed")
        return False

def create_activation_script(venv_name):
    """Create activation script for easy environment activation"""
    if sys.platform == "win32":
        script_content = f"""@echo off
echo Activating virtual environment...
call {venv_name}\\Scripts\\activate.bat
echo Virtual environment activated!
echo To run the app: streamlit run app.py
echo To deactivate: deactivate
cmd /k
"""
        script_file = "activate_env.bat"
    else:
        script_content = f"""#!/bin/bash
echo "Activating virtual environment..."
source {venv_name}/bin/activate
echo "Virtual environment activated!"
echo "To run the app: streamlit run app.py"
echo "To deactivate: deactivate"
"""
        script_file = "activate_env.sh"
        # Make executable on Unix systems
        os.chmod(script_file, 0o755)
    
    with open(script_file, "w") as f:
        f.write(script_content)
    
    print(f"✅ Created activation script: {script_file}")

def main():
    """Main setup function"""
    print("🏦 Smart Bank Assistant - Setup")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Ask user about virtual environment
    print("\n🔒 Environment Setup Options:")
    print("1. Create virtual environment (Recommended - isolates dependencies)")
    print("2. Install to global environment (Not recommended)")
    
    choice = input("\nChoose option (1 or 2): ").strip()
    
    venv_name = None
    if choice == "1":
        venv_name = create_virtual_environment()
        if not venv_name:
            print("❌ Failed to create virtual environment. Exiting.")
            sys.exit(1)
        create_activation_script(venv_name)
    elif choice == "2":
        print("⚠️  Installing to global environment...")
        confirm = input("Are you sure? This may affect other projects. (y/n): ").lower().strip()
        if confirm not in ['y', 'yes']:
            print("Setup cancelled.")
            sys.exit(0)
    else:
        print("Invalid choice. Exiting.")
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies(venv_name):
        sys.exit(1)
    
    # Create .env file
    if not create_env_file():
        sys.exit(1)
    
    # Check FAQ file
    check_faq_file()
    
    print("\n🎉 Setup completed!")
    print("\nNext steps:")
    print("1. Update the GOOGLE_API_KEY in the .env file")
    print("2. Ensure BankFAQs.csv is in the project directory")
    
    if venv_name:
        print(f"\n🔧 To activate the virtual environment:")
        if sys.platform == "win32":
            print(f"   Run: {venv_name}\\Scripts\\activate")
            print("   Or double-click: activate_env.bat")
        else:
            print(f"   Run: source {venv_name}/bin/activate")
            print("   Or run: ./activate_env.sh")
        print("\n3. Activate the environment, then run: python test_chatbot.py")
        print("4. Activate the environment, then run: streamlit run app.py")
    else:
        print("3. Run: python test_chatbot.py (to test the setup)")
        print("4. Run: streamlit run app.py (to start the application)")
    
    # Ask if user wants to run tests
    response = input("\nWould you like to run tests now? (y/n): ").lower().strip()
    if response in ['y', 'yes']:
        run_tests(venv_name)

if __name__ == "__main__":
    main()
