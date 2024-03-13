def get_tex_table(data):
    """
    data - list of lists
    """
    if len(data) == 0:
        return ""

    max_row_len = max(map(len, data))

    table_data = ""
    for row in data:
        table_data +="\\hline \n" + " & ".join(map(str, row)) + " & " * (max_row_len - max(1, len(row))) + " \\\\ \n"
    table_data += "\\hline"

    first_line = "\\begin{tabular}{" + "|c" * max_row_len + "|}\n"
    last_line = "\\end{tabular}\n"
    table = first_line + table_data + last_line
    return table
