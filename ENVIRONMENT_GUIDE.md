# 🔒 Environment Management Guide

This guide explains how to manage Python environments to avoid conflicts with your global system.

## 🚨 **Why This Matters**

Installing packages globally can cause:
- **Version conflicts** between different projects
- **Dependency conflicts** with system packages
- **Difficult cleanup** when you want to remove packages
- **Security risks** from running packages with system privileges

## 🛡️ **Recommended Approach: Virtual Environment**

### **What is a Virtual Environment?**
A virtual environment is an isolated Python environment that:
- Has its own Python interpreter
- Has its own package directory
- Doesn't interfere with your global Python installation
- Can be easily created, activated, and deleted

### **Benefits:**
✅ **Isolation**: Each project has its own dependencies  
✅ **Clean**: Easy to remove entire environment  
✅ **Safe**: No risk to system Python  
✅ **Reproducible**: Same environment on different machines  

## 🚀 **Quick Setup Options**

### **Option 1: Automated Setup (Recommended)**
```bash
python setup.py
```
This will:
- Ask if you want a virtual environment
- Create one automatically if you choose yes
- Install all dependencies in the isolated environment
- Create activation scripts for easy use

### **Option 2: Manual Virtual Environment**
```bash
# Create virtual environment
python -m venv bank_chatbot_env

# Activate it (Windows)
bank_chatbot_env\Scripts\activate

# Activate it (Mac/Linux)
source bank_chatbot_env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### **Option 3: Using Conda (if you have Anaconda)**
```bash
# Create conda environment
conda create -n bank_chatbot python=3.9

# Activate it
conda activate bank_chatbot

# Install dependencies
pip install -r requirements.txt
```

## 📋 **Environment Management Commands**

### **Virtual Environment Commands**
```bash
# Create virtual environment
python -m venv myenv

# Activate (Windows)
myenv\Scripts\activate

# Activate (Mac/Linux)
source myenv/bin/activate

# Deactivate
deactivate

# Delete environment
rm -rf myenv  # Mac/Linux
rmdir /s myenv  # Windows
```

### **Package Management**
```bash
# Install requirements
pip install -r requirements.txt

# List installed packages
pip list

# Export current environment
pip freeze > requirements_current.txt

# Install specific package
pip install package_name

# Uninstall package
pip uninstall package_name
```

## 🔧 **Project-Specific Setup**

### **For This Banking Chatbot Project:**

1. **Run the setup script:**
   ```bash
   python setup.py
   ```

2. **Choose Option 1** (Virtual Environment) when prompted

3. **Activate the environment:**
   - **Windows**: Double-click `activate_env.bat` or run `bank_chatbot_env\Scripts\activate`
   - **Mac/Linux**: Run `./activate_env.sh` or `source bank_chatbot_env/bin/activate`

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

5. **Deactivate when done:**
   ```bash
   deactivate
   ```

## ⚠️ **What NOT to Do**

### **Avoid These Practices:**
❌ **Don't install globally** without understanding the risks  
❌ **Don't use `sudo pip install`** (can break system Python)  
❌ **Don't mix package managers** (pip + conda in same environment)  
❌ **Don't forget to activate** your virtual environment  

### **Signs You're Using Global Environment:**
- No `(environment_name)` prefix in your terminal
- Packages installed in system directories
- Conflicts with other projects

## 🔍 **Checking Your Environment**

### **Verify Active Environment:**
```bash
# Should show your virtual environment path
which python

# Should show environment name in prompt
# (bank_chatbot_env) C:\project>
```

### **List Installed Packages:**
```bash
pip list
```

### **Check Python Path:**
```bash
python -c "import sys; print(sys.executable)"
```

## 🧹 **Cleanup and Maintenance**

### **Remove Virtual Environment:**
```bash
# Deactivate first
deactivate

# Delete environment folder
rm -rf bank_chatbot_env  # Mac/Linux
rmdir /s bank_chatbot_env  # Windows
```

### **Update Dependencies:**
```bash
# Activate environment
source bank_chatbot_env/bin/activate

# Update packages
pip install --upgrade -r requirements.txt
```

### **Recreate Environment:**
```bash
# Delete old environment
rm -rf bank_chatbot_env

# Run setup again
python setup.py
```

## 🆘 **Troubleshooting**

### **Common Issues:**

**"Command not found: pip"**
- Make sure virtual environment is activated
- Try: `python -m pip install -r requirements.txt`

**"Permission denied"**
- Don't use `sudo` with virtual environments
- Check file permissions on environment folder

**"Package conflicts"**
- Delete and recreate virtual environment
- Use `pip install --force-reinstall package_name`

**"Environment not activating"**
- Check if environment folder exists
- Verify activation script path
- Try manual activation commands

## 📚 **Additional Resources**

- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
- [pip User Guide](https://pip.pypa.io/en/stable/user_guide/)
- [Conda Documentation](https://docs.conda.io/)

---

**💡 Pro Tip**: Always use virtual environments for Python projects. It's a best practice that will save you from many headaches in the future!
