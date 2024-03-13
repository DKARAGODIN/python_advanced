import gen_tex_table as gtt

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
table = gtt.get_tex_table(data)
with open("test1.tex", "w") as f:
    f.write(table)

data = [[1, 2, 3], [4, 5, 6, 7, 8, 9], [], [1]]
table = gtt.get_tex_table(data)
with open("test2.tex", "w") as f:
    f.write(table)


data = [[1, 2, 3], ["a", "bc", "def"], [1.0, 2.0, True, False, None]]
table = gtt.get_tex_table(data)
with open("test3.tex", "w") as f:
    f.write(table)