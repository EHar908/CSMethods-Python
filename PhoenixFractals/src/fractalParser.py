from fractalFactory import makeFractal

def parseFile(file):
    fractalInfo = {}
    if file != "":
        f = open(file)
        for line in f:
            line = line.lower().strip()
            line = line.replace(" ", "")
            d = line.split(":")
            if d[0] == "type":
                if isinstance(d[1], str):
                    fractalInfo[d[0]] = d[1]
                else:
                    raise RuntimeError("In your file, the 'type' key should be paired with a valid string value.")
            elif d[0] == "centerx":
                convertX = safe_convert(d[1], float)
                if isinstance(convertX, float):
                    fractalInfo[d[0]] = convertX
                else:
                    raise RuntimeError("In your file, the 'centerX' key should be paired with a valid float value.")
            elif d[0] == "centery":
                convertY = safe_convert(d[1], float)
                if isinstance(convertY, float):
                    fractalInfo[d[0]] = convertY
                else:
                    raise RuntimeError("In your file, the 'centerY' key should be paired with a valid float value.")
            elif d[0] == "axislength":
                convertAxis = safe_convert(d[1], float)
                if isinstance(convertAxis, float):
                    fractalInfo[d[0]] = convertAxis
                else:
                    raise RuntimeError("In your file, the 'axisLength' key should be paired with a valid float value.")
            elif d[0] == "pixels":
                convertPix = safe_convert(d[1], int)
                if isinstance(convertPix, int):
                    fractalInfo[d[0]] = convertPix
                else:
                    raise RuntimeError("In your file, the 'pixels' key should be paired with a valid integer value.")
            elif d[0] == "iterations":
                convertIterations = safe_convert(d[1], int)
                if isinstance(convertIterations, int):
                    fractalInfo[d[0]] = convertIterations
                else:
                    raise RuntimeError("In your file, the 'iterations' key should be paired with a valid integer value.")
            elif d[0] == "preal":
                convertPreal = safe_convert(d[1], float)
                if isinstance(convertPreal, float):
                    fractalInfo[d[0]] = convertPreal
                else:
                    raise RuntimeError("In your file, the 'pReal' key should be paired with a valid float value.")
            elif d[0] == "pimag":
                convertPimag = safe_convert(d[1], float)
                if isinstance(convertPimag, float):
                    fractalInfo[d[0]] = convertPimag
                else:
                    raise RuntimeError("In your file, the 'pImag' key should be paired with a valid float value.")
            elif d[0] == "creal":
                convertCreal = safe_convert(d[1], float)
                if isinstance(convertCreal, float):
                    fractalInfo[d[0]] = convertCreal
                else:
                    raise RuntimeError("In your file, the 'cReal' key should be paired with a valid float value.")
            elif d[0] == "cimag":
                convertCimag = safe_convert(d[1], float)
                if isinstance(convertCimag, float):
                    fractalInfo[d[0]] = convertCimag
                else:
                    raise RuntimeError("In your file, the 'cImag' key should be paired with a valid float value.")
        f.close()
    else:
        fractalInfo["type"] = "mandelbrot" #The following info is for the "leaf" mandelbrot image
        fractalInfo["centerx"] = -1.643577002 #changed 1.5.. to 1.6..
        fractalInfo["centery"] = -0.000058690069
        fractalInfo["axislength"] = 0.000851248888 #added one 8 in front of the 5
        fractalInfo["pixels"] = 512
        fractalInfo["iterations"] = 111
    newFractal = makeFractal(fractalInfo)
    return newFractal

def safe_convert(obj, new_type):
    """
    Convert 'obj' to 'new_type' without crashing.

    :param obj: An object to convert into a new type
    :param new_type: Type constructor function

    :return: A new object of type 'new_type', or None if the conversion is not possible
    """
    if not type(new_type) == type:
        raise ValueError(f"Second argument must be a valid Python type")
    try:
        return new_type(obj)
    except ValueError:
        return None


