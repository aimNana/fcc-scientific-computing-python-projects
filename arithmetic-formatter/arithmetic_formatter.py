def arithmetic_arranger(problems, show_answers=False):
    # 1) Troppi problemi?
    if len(problems) > 5:
        return "Error: Too many problems."

    line1, line2, line3, line4 = [], [], [], []

    # 2) Scorro tutti i problemi
    for prob in problems:
        left, op, right = prob.split()

        # 3) Operatore valido?
        if op not in ("+", "-"):
            return "Error: Operator must be '+' or '-'."

        # 4) Solo cifre?
        if not left.isdigit() or not right.isdigit():
            return "Error: Numbers must only contain digits."

        # 5) Massimo quattro cifre?
        if len(left) > 4 or len(right) > 4:
            return "Error: Numbers cannot be more than four digits."

        # 6) Costruisco le righe
        width = max(len(left), len(right)) + 2
        line1.append(left.rjust(width))
        line2.append(op + right.rjust(width - 1))
        line3.append("-" * width)

        if show_answers:
            result = str(int(left) + int(right) if op == "+" else int(left) - int(right))
            line4.append(result.rjust(width))

    # 7) Unisco con quattro spazi tra le colonne
    arranged = "    ".join(line1) + "\n" + \
               "    ".join(line2) + "\n" + \
               "    ".join(line3)

    if show_answers:
        arranged += "\n" + "    ".join(line4)

    return arranged

