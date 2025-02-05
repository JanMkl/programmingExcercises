'''
                  +-------------------------+
                  ¦ 34 ¦ 21 ¦ 32 ¦ 41 ¦ 25  ¦
                  +----+----+----+----+-----¦
                  ¦ 14 ¦ 42 ¦ 43 ¦ 14 ¦ 31  ¦
                  +----+----+----+----+-----¦
                  ¦ 54 ¦ 45 ¦ 52 ¦ 42 ¦ 23  ¦
                  +----+----+----+----+-----¦
                  ¦ 33 ¦ 15 ¦ 51 ¦ 31 ¦ 35  ¦
                  +----+----+----+----+-----¦
                  ¦ 21 ¦ 52 ¦ 33 ¦ 13 ¦ 23  ¦
                  +---------------------------+

In this problem you are to write a program to explore the above array for a treasure. The values
in the array are clues. Each cell contains an integer between 11 and 55; for each value the
ten's digit represents the row number and the unit's digit represents the column number of the
cell containing the next clue. Starting in the upper left corner (at 1,1), use the clues to guide
your search of the array. (The first two clues are 11, 34). The treasure is a cell whose value is
the same as its coordinates.

Your program must first either use the given example or  read in the treasure map data into a 5 by 5
array. Your program should output the cells it visits during its search, and a message indicating
where you found the treasure.
'''

# ADD IMPORT IF NEEDED

def treasureHunt(tmap):
    '''
    Find the treasure in the array. Treasure is defined as a cell that points to itself.
    :param tmap: Array containing the values from which to search for the treasure
    :return: Either string containing the position of the treasure and path to it or string not
    found if there was no path leading to the treasure.
    '''
    # YOUR CODE GOES HERE
    return f"found at XXX and path was XXX, steps XXX"
    #return f"not found! :-("

def main():
    treasureMap = [
        [ 34, 21, 32, 41, 25 ],
        [ 14, 42, 43, 14, 31 ],
        [ 54, 45, 52, 42, 23 ],
        [ 33, 15, 51, 31, 35 ],
        [ 21, 52, 33, 13, 23 ]]
    print(f"Starting at 11. Treasure", treasureHunt(treasureMap))

if __name__ == "__main__":
    main()
