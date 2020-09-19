from tkinter import *
from tkinter import ttk

points = []

def add_point ( event ) :
	print ( str ( event.x ) + "\t" + str ( event.y ) )
	cv.create_rectangle (
			event.x - 1, event.y - 1,
			event.x + 1, event.y + 1
		)

	points.append ( [ event.x, event. y ] )

	if len ( points ) > 1 :
		## get the width of the canvas
		width = int ( cv.cget ( 'width' ) )

		## count the sum
		x_avg = 0
		y_avg = 0
		for p in points :
			x_avg += p [ 0 ]
			y_avg += p [ 1 ]

		## get the averages
		x_avg /= len ( points )
		y_avg /= len ( points )

		## calc the slope
		slope = 0
		slope_div = 0

		for p in points :
			slope += ( p [ 0 ] - x_avg ) * ( p [ 1 ] - y_avg )
			slope_div += ( p [ 0 ] - x_avg ) ** 2

		slope /= slope_div

		## show the regression line
		cv.delete ( 'regression' )
		cv.create_line (
			0, y_avg + slope * ( - x_avg ),
			width, y_avg + slope * ( width - x_avg ),
			tags = 'regression'
			)

root = Tk ()
cv = Canvas ( root, width = 500, height = 500 )
cv.pack ( expand = 1, fill = 'both', side = 'top' )
cv.bind ( '<1>', add_point )

root.mainloop ( )
