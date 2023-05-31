def water_gui(canvas, tk):
    # create GUI places and texts
    place_initial_state_TK = canvas.create_oval(15, 10, 45, 40, outline='black', width=2, tags="water")#p1
    place_picked_product_TK = canvas.create_oval(95, 75, 125, 105, outline='black', width=2, tags="water")#p2
    place_10cent_TK = canvas.create_oval(265,25,295,55, outline='black', width=2, tags="water") #p3
    place_20cent_TK = canvas.create_oval(265,125,295,155, outline='black', width=2, tags="water") #p4
    place_30cent_TK = canvas.create_oval(425,25,455,55, outline='black', width=2, tags="water") #p5
    place_40cent_TK = canvas.create_oval(425,125,455,155, outline='black', width=2, tags="water") #p6
    place_final_TK = canvas.create_oval(970,75,1000,105, outline = 'black', width=2, tags="water")#teliko

    textp1 = canvas.create_text(30, 25, text='P1', tags="water")
    textp2 = canvas.create_text(110, 90, text='P2', tags="water")
    textp3 = canvas.create_text(280, 40, text='P3', tags="water")
    textp4 = canvas.create_text(280, 140, text='P4', tags="water")
    textp5 = canvas.create_text(440, 40, text='P5', tags="water")
    textp6 = canvas.create_text(440, 140, text='P6', tags="water")
    textpfinal = canvas.create_text(985, 90, text='P7', tags="water")

    # create GUI transitions
    T0_TK = canvas.create_rectangle(15, 80, 45, 100, outline='black', width=2, tags="water")#picked product
    textt0 = canvas.create_text(30, 90, text='T0')
    T1_TK = canvas.create_rectangle(465, 180, 495, 200, outline='black', width=2, tags="water")#+50
    textt1 = canvas.create_text(480, 190, text='T1')
    T2_TK = canvas.create_rectangle(180, 30, 210, 50, outline='black', width=2, tags="water")#+10
    textt2 = canvas.create_text(195, 40, text='T2')
    T3_TK = canvas.create_rectangle(180, 130, 210, 150, outline='black', width=2, tags="water")#+20
    textt3 = canvas.create_text(195, 140, text='T3')
    T4_TK = canvas.create_rectangle(265, 80, 295, 100, outline='black', width=2, tags="water")#+10+10
    textt4 = canvas.create_text(280, 90, text='T4')
    T5_TK = canvas.create_rectangle(345, 30, 375, 50, outline='black', width=2, tags="water")#+10+20
    textt5 = canvas.create_text(360, 40, text='T5')
    T6_TK = canvas.create_rectangle(345, 80, 375, 100, outline='black', width=2, tags="water")#+20+10
    textt6 = canvas.create_text(360, 90, text='T6')
    T7_TK = canvas.create_rectangle(345, 130, 375, 150, outline='black', width=2, tags="water")#+20+20
    textt7 = canvas.create_text(360, 140, text='T7')
    T8_TK = canvas.create_rectangle(425, 80, 455, 100, outline='black', width=2, tags="water")#30+10
    textt8 = canvas.create_text(440, 90, text='T8')
    T9_TK = canvas.create_rectangle(505, 30, 535, 50, outline='black', width=2, tags="water")#30+20
    textt9 = canvas.create_text(520, 40, text='T9')
    T10_TK = canvas.create_rectangle(505, 130, 535, 150, outline='black', width=2, tags="water")
    textt10 = canvas.create_text(520, 140, text='T10')


    # create GUI arrows
    line = canvas.create_line(30, 45, 30, 75, arrow=tk.LAST, tags="water")#p1 - t0
    line = canvas.create_line(50, 90, 90, 90, arrow=tk.LAST, tags="water") #t0 - p2
    line = canvas.create_line(130, 80, 170, 50, arrow=tk.LAST, tags="water")#p2-t2
    line = canvas.create_line(130, 100, 170, 130, arrow=tk.LAST, tags="water")#p2-t3
    line = canvas.create_line(110, 115, 110, 190, 460, 190, arrow=tk.LAST, tags="water")#p2-t1 830
    line = canvas.create_line(500, 190, 980, 190, 980, 110, arrow=tk.LAST, tags="water")#t1-final
    line = canvas.create_line(215, 40, 260, 40, arrow=tk.LAST, tags="water")#t2-p3
    line = canvas.create_line(215, 140, 260, 140, arrow=tk.LAST, tags="water")#t3-p4
    line = canvas.create_line(280, 60, 280, 75, arrow=tk.LAST, tags="water")#p3-t4
    line = canvas.create_line(280, 105, 280, 120, arrow=tk.LAST, tags="water")#t4-p4
    line = canvas.create_line(300, 40, 340, 40, arrow=tk.LAST, tags="water")#p3-t5
    line = canvas.create_line(300, 140, 340, 140, arrow=tk.LAST, tags="water")#p4-t7
    line = canvas.create_line(300, 130, 340, 100, arrow=tk.LAST, tags="water")#p4-t6
    line = canvas.create_line(380, 80, 420, 50, arrow=tk.LAST, tags="water")#t6-p5
    line = canvas.create_line(380, 40, 420, 40, arrow=tk.LAST, tags="water")#t5-p5
    line = canvas.create_line(380, 140, 420, 140, arrow=tk.LAST, tags="water")#t7-p6
    line = canvas.create_line(440, 60, 440, 75, arrow=tk.LAST, tags="water")#p5-t8
    line = canvas.create_line(440, 105, 440, 120, arrow=tk.LAST, tags="water")#t8-p6
    line = canvas.create_line(460, 40, 500, 40, arrow=tk.LAST, tags="water")#p5-t9
    line = canvas.create_line(540, 40, 965, 85, arrow=tk.LAST, tags="water")#t9-f
    line = canvas.create_line(460, 140, 500, 140, arrow=tk.LAST, tags="water")#p6-t11
    line = canvas.create_line(540, 140, 965, 95, arrow=tk.LAST, tags="water")#t11-f