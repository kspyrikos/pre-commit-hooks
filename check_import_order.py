import os
import sys
import re
import pkgutil

# Get a list of standard libraries
standard_libs = {name for _, name, _ in pkgutil.iter_modules() if name not in sys.builtin_module_names}

def categorize_import(import_line):
    if import_line.startswith('from .') or import_line.startswith('import .'):
        return 'custom'
    module_name = re.split(r'[ .]', import_line)[1]
    if module_name in standard_libs or module_name == 'typing':
        return 'standard'
    if 'import' in import_line and ',' in import_line:
        return 'additional_multiple'
    return 'additional'

def check_import(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    import_lines = [line for line in lines if line.startswith('import') or line.startswith('from')]
    categorized_imports = [categorize_import(line) for line in import_lines]

    expected_order = ['standard', 'additional', 'additional_multiple', 'custom']
    if categorized_imports != sorted(categorized_imports, key=lambda x: expected_order.index(x)):
        print(f"Import order issue in {file_path}")
        return False
    return True

def main():
    files_to_check = [f for f in os.listdir('.') if f.endswith('.py')]
    all_checks_passed = True

    for file_path in files_to_check:
        if not check_import(file_path):
            all_checks_passed = False

    if not all_checks_passed:
        sys.exit(1)

if __name__ == "__main__":
    main()
