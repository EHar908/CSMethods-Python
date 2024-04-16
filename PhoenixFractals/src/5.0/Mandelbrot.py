def pickColor(comXY):
    complexNum = complex(0, 0)
    for i in range(111):
        complexNum = complexNum * complexNum + comXY
        if abs(complexNum) > 2:
            return i
    return 110