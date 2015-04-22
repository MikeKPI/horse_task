import openpyxl

FILENAME = 'kv008horse.xlsx'
wb = openpyxl.load_workbook(filename=FILENAME)
sheet_ranges = wb['Лист1']

top_left_corner = None
bottom_right_corner = None
start = None
finish = None


def read():

    for y, row in enumerate(sheet_ranges.rows):
        for x, cell in enumerate(row):
            if cell.border.top.style is not None and \
                            cell.border.left.style is not None:
                top_left_corner = tuple([x, y])
            if cell.border.bottom.style is not None and \
                            cell.border.right.style is not None:
                bottom_right_corner = tuple([x, y])
            if cell.value == 's':
                start = tuple([x, y])
            if cell.value == 'f':
                finish = tuple([x, y])

    input_matrix = [[True for _ in range(top_left_corner[1], bottom_right_corner[1]+1)]
                    for i in range(top_left_corner[0], bottom_right_corner[0]+1)]

    for y in range(top_left_corner[1], bottom_right_corner[1]+1):
        for x in range(top_left_corner[0], bottom_right_corner[0]+1):
            if sheet_ranges.cell(row=y+1, column=x+1).style.fill.fgColor.rgb == 'FFFF0000':
                input_matrix[x-top_left_corner[0]][y-top_left_corner[1]] = False

    return {'board': input_matrix,
            'start': start,
            'finish': finish,
            'tl_corner': top_left_corner}


def draw(iterable):
    wb = openpyxl.load_workbook(filename=FILENAME)
    sr = wb['Лист1']
    for i in iterable:
        sr.cell(row=i.y+1+top_left_corner[0],
                column=i.x+1+top_left_corner[1]).value = '*'
    wb.save()