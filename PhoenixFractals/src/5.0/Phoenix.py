def pickColor(comXY):
    julConst = complex(0.5667, 0.0)
    phConst = complex(-0.5, 0.0)
    xyFlipped = complex(comXY.imag, comXY.real)
    xyPrev = 0+0j
    currentXY = xyFlipped
    for i in range(102):
        xySave = currentXY
        currentXY = (currentXY * currentXY) + julConst + (phConst * xyPrev)
        xyPrev = xySave
        if abs(currentXY) > 2:
            return i
    return 101