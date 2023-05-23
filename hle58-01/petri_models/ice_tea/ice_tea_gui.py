def iced_tea_gui(canvas, tk):
    # create GUI places and texts
    place_initial_state_TK = canvas.create_oval(15, 10, 45, 40, outline='black', width=2)#p1
    place_picked_product_TK = canvas.create_oval(95, 75, 125, 105, outline='black', width=2)#p2
    place_10cent_TK = canvas.create_oval(265,25,295,55, outline='black', width=2) #p3
    place_20cent_TK = canvas.create_oval(265,125,295,155, outline='black', width=2) #p4
    place_30cent_TK = canvas.create_oval(425,25,455,55, outline='black', width=2) #p5
    place_40cent_TK = canvas.create_oval(425,125,455,155, outline='black', width=2) #p6
    place_50cent_TK = canvas.create_oval(585, 25, 615, 55, outline='black', width=2) #p7
    place_60cent_TK = canvas.create_oval(585, 125, 615, 155, outline='black', width=2)#p8
    place_final_TK = canvas.create_oval(970,75,1000,105, outline = 'black', width=2)#teliko

    textp1 = canvas.create_text(30, 25, text='P1')
    textp2 = canvas.create_text(110, 90, text='P2')
    textp3 = canvas.create_text(280, 40, text='P3')
    textp4 = canvas.create_text(280, 140, text='P4')
    textp5 = canvas.create_text(440, 40, text='P5')
    textp6 = canvas.create_text(440, 140, text='P6')
    textp7 = canvas.create_text(600, 40, text='P7')
    textp8 = canvas.create_text(600, 140, text='P8')
    textpfinal = canvas.create_text(985, 90, text='P9')

    # create GUI transitions
    T0_TK = canvas.create_rectangle(15, 80, 45, 100, outline='black', width=2)#picked product
    textt0 = canvas.create_text(30, 90, text='T0')
    T1_TK = canvas.create_rectangle(465, 180, 495, 200, outline='black', width=2)#+50
    textt1 = canvas.create_text(480, 190, text='T1')
    T2_TK = canvas.create_rectangle(180, 30, 210, 50, outline='black', width=2)#+10
    textt2 = canvas.create_text(195, 40, text='T2')
    T3_TK = canvas.create_rectangle(180, 130, 210, 150, outline='black', width=2)#+20
    textt3 = canvas.create_text(195, 140, text='T3')
    T4_TK = canvas.create_rectangle(265, 80, 295, 100, outline='black', width=2)#+10+10
    textt4 = canvas.create_text(280, 90, text='T4')
    T5_TK = canvas.create_rectangle(345, 30, 375, 50, outline='black', width=2)#+10+20
    textt5 = canvas.create_text(360, 40, text='T5')
    T6_TK = canvas.create_rectangle(345, 80, 375, 100, outline='black', width=2)#+20+10
    textt6 = canvas.create_text(360, 90, text='T6')
    T7_TK = canvas.create_rectangle(345, 130, 375, 150, outline='black', width=2)#+20+20
    textt7 = canvas.create_text(360, 140, text='T7')
    T8_TK = canvas.create_rectangle(425, 80, 455, 100, outline='black', width=2)#30+10
    textt8 = canvas.create_text(440, 90, text='T8')
    T9_TK = canvas.create_rectangle(505, 30, 535, 50, outline='black', width=2)#30+20
    textt9 = canvas.create_text(520, 40, text='T9')
    T10_TK = canvas.create_rectangle(505, 80, 535, 100, outline='black', width=2)#40+10
    textt10 = canvas.create_text(520, 90, text='T10')
    T11_TK = canvas.create_rectangle(505, 130, 535, 150, outline='black', width=2)
    textt11 = canvas.create_text(520, 140, text='T11')
    T12_TK = canvas.create_rectangle(585, 80, 615, 100, outline='black', width=2)
    textt11 = canvas.create_text(600, 90, text='T12')
    T13_TK = canvas.create_rectangle(665, 30, 695, 50, outline='black', width=2)
    textt11 = canvas.create_text(680, 40, text='T13')
    T14_TK = canvas.create_rectangle(665, 130, 695, 150, outline='black', width=2)
    textt11 = canvas.create_text(680, 140, text='T14')


    # create GUI arrows
    line = canvas.create_line(30, 45, 30, 75, arrow=tk.LAST)#p1 - t0
    line = canvas.create_line(50, 90, 90, 90, arrow=tk.LAST) #t0 - p2
    line = canvas.create_line(130, 80, 170, 50, arrow=tk.LAST)#p2-t2
    line = canvas.create_line(130, 100, 170, 130, arrow=tk.LAST)#p2-t3
    line = canvas.create_line(110, 115, 110, 190, 460, 190, arrow=tk.LAST)#p2-t1 830
    line = canvas.create_line(500, 190, 980, 190, 980, 110, arrow=tk.LAST)#t1-final
    line = canvas.create_line(215, 40, 260, 40, arrow=tk.LAST)#t2-p3
    line = canvas.create_line(215, 140, 260, 140, arrow=tk.LAST)#t3-p4
    line = canvas.create_line(280, 60, 280, 75, arrow=tk.LAST)#p3-t4
    line = canvas.create_line(280, 105, 280, 120, arrow=tk.LAST)#t4-p4
    line = canvas.create_line(300, 40, 340, 40, arrow=tk.LAST)#p3-t5
    line = canvas.create_line(300, 140, 340, 140, arrow=tk.LAST)#p4-t7
    line = canvas.create_line(300, 130, 340, 100, arrow=tk.LAST)#p4-t6
    line = canvas.create_line(380, 80, 420, 50, arrow=tk.LAST)#t6-p5
    line = canvas.create_line(380, 40, 420, 40, arrow=tk.LAST)#t5-p5
    line = canvas.create_line(380, 140, 420, 140, arrow=tk.LAST)#t7-p6
    line = canvas.create_line(440, 60, 440, 75, arrow=tk.LAST)#p5-t8
    line = canvas.create_line(440, 105, 440, 120, arrow=tk.LAST)#t8-p6
    line = canvas.create_line(460, 40, 500, 40, arrow=tk.LAST)#p5-t9
    line = canvas.create_line(540, 40, 580, 40, arrow=tk.LAST)#t9-p7
    line = canvas.create_line(460, 140, 500, 140, arrow=tk.LAST)#p6-t11
    line = canvas.create_line(540, 140, 580, 140, arrow=tk.LAST)#t11-p8
    line = canvas.create_line(620, 40, 660, 40, arrow=tk.LAST)#p7-t13
    line = canvas.create_line(620, 140, 660, 140, arrow=tk.LAST)#p8-t14
    line = canvas.create_line(700, 40, 965, 85, arrow=tk.LAST)#t13-f
    line = canvas.create_line(700, 140, 965, 95, arrow=tk.LAST)#t14-f

    
