#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
from tkinter import *
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches	
		
def calculate_Pi(*args):
	try:	
		points = int(points_string.get())		
		xy = np.random.uniform(-1, 1, 2 * points).reshape((2, points))
		in_circle = xy[0]**2 + xy[1]**2 <= 1  		
		pi_result = 4* np.sum(in_circle) / points
		pi_string.set(pi_result)		
		inside_xy  = xy [:, in_circle]                       
		outside_xy = xy [:, ~in_circle]	
		
		fig, ax = plt.subplots(1)			
		ax.add_patch(patches.Rectangle((-1, -1),2,2,fill=False))	
		ax.spines['left'].set_position(('data', 0.0))
		ax.spines['bottom'].set_position(('data', 0.0))
		ax.spines['right'].set_color('none')
		ax.spines['top'].set_color('none')	
		blue_circle = plt.Circle((0.0, 0.0), 1 ,  facecolor='none', edgecolor='b')
		ax.scatter(*inside_xy, c='orange',marker='.')
		ax.scatter(*outside_xy, c='grey',marker='.')
		ax.set_aspect('equal')
		ax.add_artist(blue_circle)
		plt.text(-1, -1.2, 'Pi = {}'.format(pi_result))
		plt.title('Wybrano {} punktow'.format(points))
		fig.savefig('scatter_plot.pdf')
		fig.show()
		print ('Otrzymane przyblizenie liczby Pi dla', points , 'punktow to:', pi_result)
	
	except ValueError:
		pass				
		
    
root = Tk()
root.title("Obliczanie Pi metodą Monte Carlo")
root.geometry("470x180")
root.resizable(0, 0)

mainframe = ttk.Frame(root, padding="35 25 35 25")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

points_string = StringVar()
pi_string = StringVar()

ttk.Label(mainframe, text="Podaj liczbę punktów:").grid(column=0, row=0, sticky=W)
points_entry = ttk.Entry(mainframe, width=20, textvariable=points_string)
points_entry.grid(column=1, row=0, sticky=(W))
ttk.Button(mainframe, text="Oblicz", command=calculate_Pi).grid(column=2, row=0, sticky=E)

ttk.Label(mainframe, textvariable="").grid(column=0, row=1)

ttk.Label(mainframe, text="Otrzymana wartość Pi wynosi").grid(column=0, row=2, sticky=(W))
ttk.Label(mainframe, textvariable=pi_string).grid(column=1, row=2, sticky=(W))

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

points_entry.focus()
root.bind('<Return>', calculate_Pi)

root.mainloop()