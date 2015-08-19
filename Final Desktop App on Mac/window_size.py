__author__ = 'Panagiotis Filiotis'

class Window():

    # function that gets initially the dimensions of the window(height and width) and calculates which is the position
    # on the center of the screen to place the new window

    def center_window(self,root , width=300, height=200):
        # get screen's width and height
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        # calculates the new positions x, y
        x = (ws / 2) - (width / 2)
        y = (hs / 2) - (height / 2)
        root.geometry('%dx%d+%d+%d' % (width, height, x, y-75))
