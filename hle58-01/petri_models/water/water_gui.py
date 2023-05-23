"""
def water_gui(canvas, tk):
    # create GUI places and texts
    place_initial_state_TK = canvas.create_oval(30, 75, 60, 105, outline='black', width=2)#p1
    place_picked_product_TK = canvas.create_oval(210, 75, 240, 105, outline='black', width=2)#p2
    place_10cent_TK = canvas.create_oval(390,25,420,55, outline='black', width=2) #p3
    place_20cent_TK = canvas.create_oval(390,125,420,155, outline='black', width=2) #p4 
    place_30cent_TK = canvas.create_oval(570,25,600,55, outline='black', width=2) #p5
    place_40cent_TK = canvas.create_oval(570,125,600,155, outline='black', width=2) #p6
    place_50cent_TK = canvas.create_oval(750, 75, 780, 105, outline='black', width=2) #p7
    # place_complete_TK = canvas.create_oval(930, 75, 960, 105, outline='black', width=2)#p8
    # place_cancel_TK = canvas.create_oval(840, 160, 870, 190, outline='black', width=2)#p9
    
    textp1 = canvas.create_text(45, 90, text='P1')
    textp2 = canvas.create_text(225, 90, text='P2')
    textp3 = canvas.create_text(405, 40, text='P3')
    textp4 = canvas.create_text(405, 140, text='P4')
    textp5 = canvas.create_text(585, 40, text='P5')
    textp6 = canvas.create_text(585, 140, text='P6')
    textp7 = canvas.create_text(765, 90, text='P7')
    # textp8 = canvas.create_text(945, 90, text='P8')
    # textp9 = canvas.create_text(855, 175, text='P9')

    # create GUI transitions
    T0_TK = canvas.create_rectangle(120, 80, 150, 100, outline='black', width=2)#picked product
    textt0 = canvas.create_text(135, 90, text='T0')
    T1_TK = canvas.create_rectangle(480, 165, 510, 185, outline='black', width=2)#+50
    textt1 = canvas.create_text(495, 175, text='T1')
    T2_TK = canvas.create_rectangle(300, 30, 330, 50, outline='black', width=2)#+10
    textt2 = canvas.create_text(315, 40, text='T2')
    T3_TK = canvas.create_rectangle(300, 130, 330, 150, outline='black', width=2)#+20
    textt3 = canvas.create_text(315, 140, text='T3')
    T4_TK = canvas.create_rectangle(390, 80, 420, 100, outline='black', width=2)#+10+10
    textt4 = canvas.create_text(405, 90, text='T4')
    T5_TK = canvas.create_rectangle(480, 30, 510, 50, outline='black', width=2)#+10+20
    textt5 = canvas.create_text(495, 40, text='T5')
    T6_TK = canvas.create_rectangle(480, 80, 510, 100, outline='black', width=2)#+20+10
    textt6 = canvas.create_text(495, 90, text='T6')
    T7_TK = canvas.create_rectangle(480, 130, 510, 150, outline='black', width=2)#+20+20
    textt7 = canvas.create_text(495, 140, text='T7')
    T8_TK = canvas.create_rectangle(570, 80, 600, 100, outline='black', width=2)#30+10
    textt8 = canvas.create_text(585, 90, text='T8')
    T9_TK = canvas.create_rectangle(660, 30, 690, 50, outline='black', width=2)#30+20
    textt9 = canvas.create_text(675, 40, text='T9')
    T10_TK = canvas.create_rectangle(660, 130, 690, 150, outline='black', width=2)#40+10
    textt10 = canvas.create_text(675, 140, text='T10')
    # T11_TK = canvas.create_rectangle(840, 80, 870, 100, outline='black', width=2)
    # textt11 = canvas.create_text(855, 90, text='T11')

    # create GUI arrows
    line = canvas.create_line(70, 90, 110, 90, arrow=tk.LAST)#p1 - t0
    line = canvas.create_line(160, 90, 200, 90, arrow=tk.LAST) #t0 - p3
    line = canvas.create_line(225, 115, 225, 175, 470, 175, arrow=tk.LAST)#p3-t1 830
    line = canvas.create_line(520, 175, 760, 175, 760, 110, arrow=tk.LAST)#t1-p8 
    line = canvas.create_line(250, 80, 290, 50, arrow=tk.LAST)#p3-t2
    line = canvas.create_line(250, 100, 290, 130, arrow=tk.LAST)#p3-t3
    line = canvas.create_line(340, 40, 380, 40, arrow=tk.LAST)#t2-p4
    line = canvas.create_line(430, 40, 470, 40, arrow=tk.LAST)#p4-t5
    line = canvas.create_line(340, 140, 380, 140, arrow=tk.LAST)#t3-p5
    line = canvas.create_line(405, 60, 405, 75, arrow=tk.LAST)#p4-t4
    line = canvas.create_line(405, 105, 405, 120, arrow=tk.LAST)#t4-p5
    line = canvas.create_line(520, 40, 560, 40, arrow=tk.LAST)#t5-p6
    line = canvas.create_line(430, 140, 470, 140, arrow=tk.LAST)#p5-t7
    line = canvas.create_line(520, 140, 560, 140, arrow=tk.LAST)#t7-p7
    line = canvas.create_line(585, 60, 585, 75, arrow=tk.LAST)#p6-t8
    line = canvas.create_line(585, 105, 585, 120, arrow=tk.LAST)#t8-p7
    line = canvas.create_line(430, 130, 470, 100, arrow=tk.LAST)#p5-t6
    line = canvas.create_line(515, 90, 555, 60, arrow=tk.LAST)#t6-p6
    line = canvas.create_line(610, 40, 650, 40, arrow=tk.LAST)#p6-t9 
    line = canvas.create_line(610, 140, 650, 140, arrow=tk.LAST)#p7-t10
    line = canvas.create_line(700, 40, 740, 70, arrow=tk.LAST)#t9-p8
    line = canvas.create_line(700, 140, 740, 110, arrow=tk.LAST)#t10-p8
    # line = canvas.create_line(790, 90, 830, 90, arrow=tk.LAST)#p8-t11
    # line = canvas.create_line(880, 90, 920, 90, arrow=tk.LAST)#t11-p9
    # line = canvas.create_line(855, 110, 855, 150, arrow=tk.LAST)#t11-p10"""