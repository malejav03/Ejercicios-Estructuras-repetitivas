numStudents = 10
minusFithy = 0
betweenFithySeventy = 0
betweenSeventyEighty = 0
mostEighty = 0

for i in range(numStudents):
    mark = int(input(f"Digite la nota para el estudiante {(i+1)}: "))
    if (mark < 50):
        minusFithy += 1
        print(f"Hay {minusFithy} estudiante(s) con nota por debajo de 50")
    elif (mark >= 50 and mark < 70):
        betweenFithySeventy += 1
        print(f"Hay {betweenFithySeventy} estudiante(s) con nota entre 50 y 70")
    elif (mark >= 70 and mark < 80):
        betweenSeventyEighty += 1
        print(f"Hay {betweenSeventyEighty} estudiante(s) con nota entre 70 y 80")
    else:
        mostEighty += 1
        print(f"Hay {mostEighty} estudiante(s) con nota mayor o igual a 80")