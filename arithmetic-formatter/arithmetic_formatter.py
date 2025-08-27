def arithmetic_arranger(problems, show_answers=False):
    """
    Arrange arithmetic problems vertically and neatly.

    Parameters:
        problems (list of str): Arithmetic problems as strings (e.g. "32 + 8").
        show_answers (bool): If True, also display the results.

    Returns:
        str: The formatted arithmetic problems or an error message.
    """

    # 1) Check maximum number of problems
    if len(problems) > 5:
        return "Error: Too many problems."

    line1, line2, line3, line4 = [], [], [], []

    # 2) Parse each problem
    for prob in problems:
        left, op, right = prob.split()

        # 3) Validate operator
        if op not in ("+", "-"):
            return "Error: Operator must be '+' or '-'."

        # 4) Validate operands (digits only)
        if not left.isdigit() or not right.isdigit():
            return "Error: Numbers must only contain digits."

        # 5) Validate length (max 4 digits each)
        if len(left) > 4 or len(right) > 4:
            return "Error: Numbers cannot be more than four digits."

        # 6) Format each row with proper spacing
        width = max(len(left), len(right)) + 2
        line1.append(left.rjust(width))
        line2.append(op + right.rjust(width - 1))
        line3.append("-" * width)

        if show_answers:
            result = str(int(left) + int(right) if op == "+" else int(left) - int(right))
            line4.append(result.rjust(width))

    # 7) Join rows with four spaces between problems
    arranged = "    ".join(line1) + "\n" + \
               "    ".join(line2) + "\n" + \
               "    ".join(line3)

    if show_answers:
        arranged += "\n" + "    ".join(line4)

    return arranged
