# Thomas McInnes
# CSCI 101 - Section G
# Python Lab 4
# References: None
# Time: 3 hours

all_rows = []

print(f'Enter the number of rows and columns in the subdivision:\nROWS> ', end='')
rows = int(input())
print('COLUMNS> ', end='')
columns = int(input())
print('Enter each row of the subdivision:')

for i in range(0, rows):       # Taking inputs for each row specified. If input errors were checked for with this program, this is where those error checks would go
    print(f'ROW{i}> ', end='')
    indiv_row = input()
    single_row = indiv_row.split(' ')
    all_rows.append(single_row)

# These check for basic ERTs 1 space away
check_up = 'y'
check_down = 'y'
check_left = 'y'
check_right = 'y'
check_upl = 'y'           # The "upl" or "downr" format signifies which corner is looked at. "upl" refers to the top left corner, "downr" refers to the bottom right, etc.
check_upr = 'y'
check_downl = 'y'
check_downr = 'y'

# These check for the super ERTs 2 spaces away (hence the S) (explained more in depth later)
Scheck_up = 'y'
Scheck_down = 'y'
Scheck_left = 'y'
Scheck_right = 'y'
Scheck_upl = 'y'        
Scheck_upr = 'y'
Scheck_downl = 'y'
Scheck_downr = 'y'

# These specify the 8 spaces that are adjacent to the far corners in the super ERT cases (Scheck_upll = up(top),left(left corner),left(left side of corner))
Scheck_upll = 'y'
Scheck_uplr = 'y'
Scheck_uprl = 'y'
Scheck_uprr = 'y'
Scheck_downll = 'y'
Scheck_downlr = 'y'
Scheck_downrl = 'y'
Scheck_downrr = 'y'

current_row = 0
current_col = 0
fail = 0        # My code works by counting up "fail conditions." If those fail conditions reach a certain value, then the building must
coords = []     # not be powered. This fail condition is 24: 8 potential spaces for normal ERTs, and 16 extra spaces for super ERTs.
not_powered = []

for i in all_rows:      # Grabs a WHOLE row from all_rows

    for j in i:     # Grabs item j in the row that just got grabbed

        if current_row == 0:          # This checks if the spaces in the normal ERT range are "out of bounds" to avoid index errors later
            check_up = 'n'
            fail += 1                 # If a direction is out of bounds, there's no possible way for a power source to be there, so the fail condition increases
        if (current_col == 0) or (columns == 1):
            check_left = 'n'
            fail += 1
        if (current_row == (rows - 1)) or (rows == 1):
            check_down = 'n'
            fail += 1
        if (current_col == columns - 1) or (columns == 1):
            check_right = 'n'
            fail += 1
        if (check_up == 'n') or (current_col == 0) or (columns == 1):
            check_upl = 'n'
            fail += 1
        if (check_up == 'n') or (current_col == columns - 1) or (columns == 1):
            check_upr = 'n'
            fail += 1
        if (check_down == 'n') or (current_col == 0) or (columns == 1):
            check_downl = 'n'
            fail += 1
        if (check_down == 'n') or (current_col == columns - 1) or (columns == 1):
            check_downr = 'n'
            fail += 1

        if current_row <= 1:        # This checks if the spaces in the super ERT range are "out of bounds"
            Scheck_up = 'n'              
            fail += 1               
        if (current_col <= 1) or (columns <= 2):
            Scheck_left = 'n'
            fail += 1
        if (current_row >= (rows - 2)) or (rows <= 2):
            Scheck_down = 'n'
            fail += 1
        if (current_col >= columns - 2) or (columns <= 2):
            Scheck_right = 'n'
            fail += 1

        if (Scheck_up == 'n') or (current_col <= 1) or (columns <= 2):      # Checks the far corners of the super ERTs
            Scheck_upl = 'n'
            fail += 1                                                                           
        if (Scheck_up == 'n') or (current_col >= columns - 2) or (columns <= 2):   
            Scheck_upr = 'n'                                                        
            fail += 1
        if (Scheck_down == 'n') or (current_col <= 1) or (columns <= 2):
            Scheck_downl = 'n'
            fail += 1
        if (Scheck_down == 'n') or (current_col >= columns - 2) or (columns <= 2):
            Scheck_downr = 'n'
            fail += 1

        if (Scheck_down == 'n') or (check_right == 'n'):        # Checks the sides next to the corners
            Scheck_downrl = 'n'                                 # Determined based on what corner sides are possible to be in bounds when other values are out of bounds
            fail += 1
        if (Scheck_down == 'n') or (check_left == 'n'):
            Scheck_downlr = 'n'            
            fail += 1
        if (Scheck_left == 'n') or (check_down == 'n'):
            Scheck_downll = 'n'            
            fail += 1
        if (Scheck_left == 'n') or (check_up == 'n'):
            Scheck_upll = 'n'            
            fail += 1
        if (Scheck_up == 'n') or (check_right == 'n'):
            Scheck_uprl = 'n'            
            fail += 1
        if (Scheck_up == 'n') or (check_left == 'n'):
            Scheck_uplr = 'n'            
            fail += 1
        if (Scheck_right == 'n') or (check_up == 'n'):
            Scheck_uprr = 'n'            
            fail += 1
        if (Scheck_right == 'n') or (check_down == 'n'):
            Scheck_downrr = 'n'            
            fail += 1

        if j == 'b':
                                                                        # If there's a building at the position being checked, the code checks the area around for
            if check_up != 'n':                                         # ERTs. For every space that could have an ERT but doesn't, a fail point is added.
                if (not all_rows[current_row - 1][current_col] == 'S') and (not all_rows[current_row - 1][current_col] == 'T'):  # If the out of bounds check earlier found that the building
                    fail += 1                                                                                                    # is OOB, the step is skipped (the fail point was already added, avoids index errors)
            if check_down != 'n':                                                                                                # Also, in the nearest 8 spaces, it doesn't matter if the ERT is normal or super
                if (not all_rows[current_row + 1][current_col] == 'S') and (not all_rows[current_row + 1][current_col] == 'T'):  # so both T and S are tested for
                    fail += 1
            if check_left != 'n':
                if (not all_rows[current_row][current_col - 1] == 'S') and (not all_rows[current_row][current_col - 1] == 'T'):
                    fail += 1
            if check_right != 'n':
                if (not all_rows[current_row][current_col + 1] == 'S') and (not all_rows[current_row][current_col + 1] == 'T'):
                    fail += 1

            if check_upl != 'n':
                if (not all_rows[current_row - 1][current_col - 1] == 'S') and (not all_rows[current_row - 1][current_col - 1] == 'T'):
                    fail += 1
            if check_upr != 'n':
                if (not all_rows[current_row - 1][current_col + 1] == 'S') and (not all_rows[current_row - 1][current_col + 1] == 'T'):
                    fail += 1
            if check_downl != 'n':
                if (not all_rows[current_row + 1][current_col - 1] == 'S') and (not all_rows[current_row + 1][current_col - 1] == 'T'):
                    fail += 1
            if check_downr != 'n':
                if (not all_rows[current_row + 1][current_col + 1] == 'S') and (not all_rows[current_row + 1][current_col + 1] == 'T'):
                    fail += 1
            
            if Scheck_up != 'n':                                            # This checks for ERTs in the 16 spaces further away from the point
                if not all_rows[current_row - 2][current_col] == 'S':       # This particular section just checks the top, left, bottom and right positions
                    fail += 1
            if Scheck_down != 'n':
                if not all_rows[current_row + 2][current_col] == 'S':
                    fail += 1
            if Scheck_left != 'n':
                if not all_rows[current_row][current_col - 2] == 'S':
                    fail += 1
            if Scheck_right != 'n':
                if not all_rows[current_row][current_col + 2] == 'S':
                    fail += 1

            if Scheck_upl != 'n':
                if not all_rows[current_row - 2][current_col - 2] == 'S':   # This checks the far corners for super ERTs
                    fail += 1                                                   
            if Scheck_upr != 'n':
                if not all_rows[current_row - 2][current_col + 2] == 'S':
                    fail += 1
            if Scheck_downl != 'n':
                if not all_rows[current_row + 2][current_col - 2] == 'S':
                    fail += 1
            if Scheck_downr != 'n':
                if not all_rows[current_row + 2][current_col + 2] == 'S':
                    fail += 1

            if Scheck_upll != 'n':
                if not all_rows[current_row - 1][current_col - 2] == 'S':   # These last two sections check the spots next to the corners for super ERTs
                    fail += 1                                                   
            if Scheck_uprr != 'n':
                if not all_rows[current_row - 1][current_col + 2] == 'S':
                    fail += 1
            if Scheck_downll != 'n':
                if not all_rows[current_row + 1][current_col - 2] == 'S':
                    fail += 1
            if Scheck_downrr != 'n':
                if not all_rows[current_row + 1][current_col + 2] == 'S':
                    fail += 1

            if Scheck_uplr != 'n':
                if not all_rows[current_row - 2][current_col - 1] == 'S':
                    fail += 1                                                   
            if Scheck_uprl != 'n':
                if not all_rows[current_row - 2][current_col + 1] == 'S':
                    fail += 1
            if Scheck_downlr != 'n':
                if not all_rows[current_row + 2][current_col - 1] == 'S':
                    fail += 1
            if Scheck_downrl != 'n':
                if not all_rows[current_row + 2][current_col + 1] == 'S':
                    fail += 1

        if fail == 24:         # If the fail condition gets all the way to 24, there's nothing powering that specific building. 
            coords.append(current_row)      # The building's coordinates are put into a list temporarily, then that list is added to a
            coords.append(current_col)      # master list. The former list is then cleared for later inputs.
            not_powered.append(coords)
            coords = []

        check_up = 'y'      # This resets variables to their default values.
        check_down = 'y'
        check_left = 'y'
        check_right = 'y'
        check_upr = 'y'
        check_upl = 'y'
        check_downl = 'y'
        check_downr = 'y'  

        Scheck_up = 'y'
        Scheck_down = 'y'
        Scheck_left = 'y'
        Scheck_right = 'y'
        Scheck_upl = 'y'
        Scheck_upr = 'y'
        Scheck_downl = 'y'
        Scheck_downr = 'y'

        Scheck_upll = 'y'
        Scheck_uplr = 'y'
        Scheck_uprl = 'y'
        Scheck_uprr = 'y'
        Scheck_downll = 'y'
        Scheck_downlr = 'y'
        Scheck_downrl = 'y'
        Scheck_downrr = 'y'     # I'm sure there's some way to consolidate these variables into a list of some sort, however the sunk cost fallacy hit me hard here

        fail = 0                    
        current_col += 1     # Increases the column number being checked

    current_row += 1    # Increases the row number being checked, sets the column being checked back to 0 to loop over again
    current_col = 0

if not_powered == []:   # If the master list is empty, then none of the buildings are not powered, so True is output. Otherwise, false is output and the list is given.
    print(f'All buildings are powered! :)\nOUTPUT True')
else:
    print(f'Not all buildings are powered... :(\nOUTPUT False\nThe following buildings located at (row, column) are not powered:')
    print(f'OUTPUT {not_powered}')