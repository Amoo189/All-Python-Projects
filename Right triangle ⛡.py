'''⚛⛮⛡POWERED BY || SALEH AMOO || Right triangle ⛡||DELAT||Δ'''
"""┄┄┄┅┅❅✾❅┅┅┄┄┄"""
while True:
    def Right_triangle(Chord, firstlineLeftover, secondlineLeftover):
        if Chord ** 2 == firstlineLeftover** 2 + secondlineLeftover ** 2:
            return '(ツ)⁩⁦⛡it is a Right triangle⛡⁩⁦'
        else:
            return 'ಠ︵ಠ⁩⁦it is not a Right triangle.'
    print("THIS PROGRAM CAN CALCULATE THE RIGHT TRIANGLE")
    Chord = int(input("Enter the Chord of Right triangle:"))
    firstlineLeftover = int(input("Enter the first Left over Line of Right triangle:"))
    secondlineLeftover = int(input("Enter the second Left over Line of Right triangle:"))
    Right_triangle = Right_triangle(Chord, firstlineLeftover, secondlineLeftover)
    print(Right_triangle)
'''┄┄┄┅┅❅✾❅┅┅┄┄┄'''