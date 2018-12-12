from Canvas import Canvas
from entities.Line import Line
from entities.Rectangle import Rectangle
from entities.Block import Block
from InputParameterValidation import parseInputArg, validateInputString, validateInputArgv


def main(argv):
    geometryObj = None
    geoType = argv[0].upper()
    if geoType == 'C':
        Canvas(argv[1], argv[2])
    elif geoType == 'L':
        geometryObj = Line(argv[1], argv[2], argv[3], argv[4])
    elif geoType == 'R':
        geometryObj = Rectangle(argv[1], argv[2], argv[3], argv[4])
    elif geoType == 'B':
        geometryObj = Block(argv[1], argv[2], argv[3])
    elif geoType == 'Q':
        return False
    else:
        print('Geometry type not recognized')
        return True

    canvas = Canvas.getInstance()
    if not canvas:
        print('Canvas needs to be instantiated first')
        return True

    if geometryObj and geometryObj.checkGeometryObjectConstraints():
            canvas.addToCanvas(geometryObj)

    canvas.print()
    return True


if __name__ == '__main__':
    breakCondition = True
    while breakCondition:
        inputStr = input('Enter command: ')

        if not validateInputString(inputStr):
            continue

        argv = parseInputArg(inputStr.split())
        if not argv:
            continue

        if not validateInputArgv(argv):
            continue

        breakCondition = main(argv)
