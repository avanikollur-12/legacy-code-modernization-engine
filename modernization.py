import re

def detect_language(code):
    if "#include" in code:
        return "C"
    elif "System.out.println" in code or "public static void main" in code:
        return "Java"
    elif "print " in code or "def " in code:
        return "Python"
    else:
        return "Unknown"


def modernize_code(code):
    original_code = code

    # -------- Python Modernization --------
    # Convert print "text" → print("text")
    code = re.sub(r'print\s+"([^"]*)"', r'print("\1")', code)

    # -------- Java Modernization --------
    # Convert String args[] → String[] args
    code = code.replace("String args[]", "String[] args")

    # -------- C Modernization --------
    # Convert main() → int main()
    if "main()" in code and "int main()" not in code:
        code = code.replace("main()", "int main()")

    # -------- Formatting Improvements --------
    code = code.replace("{", "{\n")
    code = code.replace(";", ";\n")

    return original_code, code
