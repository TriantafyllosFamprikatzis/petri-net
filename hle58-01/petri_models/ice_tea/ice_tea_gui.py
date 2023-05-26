def ice_tea_gui(canvas, tk):
    # create GUI places and texts
    place_initial_state_TK = canvas.create_oval(15, 10, 45, 40, outline='black', width=2, tags="ice_tea")#p1
    place_picked_product_TK = canvas.create_oval(95, 75, 125, 105, outline='black', width=2, tags="ice_tea")#p2
    place_10cent_TK = canvas.create_oval(265,25,295,55, outline='black', width=2, tags="ice_tea") #p3
    place_20cent_TK = canvas.create_oval(265,125,295,155, outline='black', width=2, tags="ice_tea") #p4
    place_30cent_TK = canvas.create_oval(425,25,455,55, outline='black', width=2, tags="ice_tea") #p5
    place_40cent_TK = canvas.create_oval(425,125,455,155, outline='black', width=2, tags="ice_tea") #p6
    place_50cent_TK = canvas.create_oval(585, 25, 615, 55, outline='black', width=2, tags="ice_tea") #p7
    place_60cent_TK = canvas.create_oval(585, 125, 615, 155, outline='black', width=2, tags="ice_tea")#p8
    place_final_TK = canvas.create_oval(970,75,1000,105, outline = 'black', width=2, tags="ice_tea")#teliko

    textp1 = canvas.create_text(30, 25, text='P1', tags="ice_tea")
    textp2 = canvas.create_text(110, 90, text='P2', tags="ice_tea")
    textp3 = canvas.create_text(280, 40, text='P3', tags="ice_tea")
    textp4 = canvas.create_text(280, 140, text='P4', tags="ice_tea")
    textp5 = canvas.create_text(440, 40, text='P5', tags="ice_tea")
    textp6 = canvas.create_text(440, 140, text='P6', tags="ice_tea")
    textp7 = canvas.create_text(600, 40, text='P7', tags="ice_tea")
    textp8 = canvas.create_text(600, 140, text='P8', tags="ice_tea")
    textpfinal = canvas.create_text(985, 90, text='P9', tags="ice_tea")

    # create GUI transitions
    T0_TK = canvas.create_rectangle(15, 80, 45, 100, outline='black', width=2, tags="ice_tea")#picked product
    textt0 = canvas.create_text(30, 90, text='T0', tags="ice_tea")
    T1_TK = canvas.create_rectangle(465, 180, 495, 200, outline='black', width=2, tags="ice_tea")#+100, +200
    textt1 = canvas.create_text(480, 190, text='T1', tags="ice_tea")
    T2_TK = canvas.create_rectangle(180, 30, 210, 50, outline='black', width=2, tags="ice_tea")#+10
    textt2 = canvas.create_text(195, 40, text='T2', tags="ice_tea")
    T3_TK = canvas.create_rectangle(180, 130, 210, 150, outline='black', width=2, tags="ice_tea")#+20
    textt3 = canvas.create_text(195, 140, text='T3', tags="ice_tea")
    T4_TK = canvas.create_rectangle(265, 80, 295, 100, outline='black', width=2, tags="ice_tea")#+10+10
    textt4 = canvas.create_text(280, 90, text='T4', tags="ice_tea")
    T5_TK = canvas.create_rectangle(345, 30, 375, 50, outline='black', width=2, tags="ice_tea")#+10+20
    textt5 = canvas.create_text(360, 40, text='T5', tags="ice_tea")
    T6_TK = canvas.create_rectangle(345, 80, 375, 100, outline='black', width=2, tags="ice_tea")#+20+10
    textt6 = canvas.create_text(360, 90, text='T6', tags="ice_tea")
    T7_TK = canvas.create_rectangle(345, 130, 375, 150, outline='black', width=2, tags="ice_tea")#+20+20, tags="ice_tea"
    textt7 = canvas.create_text(360, 140, text='T7', tags="ice_tea")
    T8_TK = canvas.create_rectangle(425, 80, 455, 100, outline='black', width=2, tags="ice_tea")#30+10
    textt8 = canvas.create_text(440, 90, text='T8', tags="ice_tea")
    T9_TK = canvas.create_rectangle(505, 30, 535, 50, outline='black', width=2, tags="ice_tea")#30+20
    textt9 = canvas.create_text(520, 40, text='T9', tags="ice_tea")
    T10_TK = canvas.create_rectangle(505, 80, 535, 100, outline='black', width=2, tags="ice_tea")#40+10
    textt10 = canvas.create_text(520, 90, text='T10', tags="ice_tea")
    T11_TK = canvas.create_rectangle(505, 130, 535, 150, outline='black', width=2, tags="ice_tea")
    textt11 = canvas.create_text(520, 140, text='T11', tags="ice_tea")
    T12_TK = canvas.create_rectangle(585, 80, 615, 100, outline='black', width=2, tags="ice_tea")
    textt12 = canvas.create_text(600, 90, text='T12', tags="ice_tea")
    T13_TK = canvas.create_rectangle(665, 30, 695, 50, outline='black', width=2, tags="ice_tea")
    textt13 = canvas.create_text(680, 40, text='T13', tags="ice_tea")
    T14_TK = canvas.create_rectangle(665, 130, 695, 150, outline='black', width=2, tags="ice_tea")
    textt14 = canvas.create_text(680, 140, text='T14', tags="ice_tea")
    T15_TK = canvas.create_rectangle(345, 5, 375, 25, outline='black', width=2, tags="ice_tea")#+50
    textt15 = canvas.create_text(360, 15, text='T15', tags="ice_tea")
    T16_TK = canvas.create_rectangle(665, 5, 695, 25, outline='black', width=2, tags="ice_tea")#50+50
    textt16 = canvas.create_text(680, 15, text='T16', tags="ice_tea")

    # create GUI arrows
    line = canvas.create_line(30, 45, 30, 75, arrow=tk.LAST, tags="ice_tea")#p1 - t0
    line = canvas.create_line(50, 90, 90, 90, arrow=tk.LAST, tags="ice_tea") #t0 - p2
    line = canvas.create_line(130, 80, 170, 50, arrow=tk.LAST, tags="ice_tea")#p2-t2
    line = canvas.create_line(130, 100, 170, 130, arrow=tk.LAST, tags="ice_tea")#p2-t3
    line = canvas.create_line(110, 115, 110, 190, 460, 190, arrow=tk.LAST, tags="ice_tea")#p2-t1 830
    line = canvas.create_line(500, 190, 980, 190, 980, 110, arrow=tk.LAST, tags="ice_tea")#t1-final
    line = canvas.create_line(110, 70, 110, 15, 340, 15, arrow=tk.LAST, tags="ice_tea")#p2-t15
    line = canvas.create_line(215, 40, 260, 40, arrow=tk.LAST, tags="ice_tea")#t2-p3
    line = canvas.create_line(215, 140, 260, 140, arrow=tk.LAST, tags="ice_tea")#t3-p4
    line = canvas.create_line(280, 60, 280, 75, arrow=tk.LAST, tags="ice_tea")#p3-t4
    line = canvas.create_line(280, 105, 280, 120, arrow=tk.LAST, tags="ice_tea")#t4-p4
    line = canvas.create_line(300, 40, 340, 40, arrow=tk.LAST, tags="ice_tea")#p3-t5
    line = canvas.create_line(300, 140, 340, 140, arrow=tk.LAST, tags="ice_tea")#p4-t7
    line = canvas.create_line(300, 130, 340, 100, arrow=tk.LAST, tags="ice_tea")#p4-t6
    line = canvas.create_line(380, 80, 420, 50, arrow=tk.LAST, tags="ice_tea")#t6-p5
    line = canvas.create_line(380, 40, 420, 40, arrow=tk.LAST, tags="ice_tea")#t5-p5
    line = canvas.create_line(380, 140, 420, 140, arrow=tk.LAST, tags="ice_tea")#t7-p6
    line = canvas.create_line(440, 60, 440, 75, arrow=tk.LAST, tags="ice_tea")#p5-t8
    line = canvas.create_line(440, 105, 440, 120, arrow=tk.LAST, tags="ice_tea")#t8-p6
    line = canvas.create_line(460, 40, 500, 40, arrow=tk.LAST, tags="ice_tea")#p5-t9
    line = canvas.create_line(540, 40, 580, 40, arrow=tk.LAST, tags="ice_tea")#t9-p7
    line = canvas.create_line(460, 125, 500, 100, arrow=tk.LAST, tags="ice_tea")#p6-t10
    line = canvas.create_line(460, 140, 500, 140, arrow=tk.LAST, tags="ice_tea")#p6-t11
    line = canvas.create_line(540, 80, 580, 50, arrow=tk.LAST, tags="ice_tea")#t10-p7
    line = canvas.create_line(460, 140, 500, 140, arrow=tk.LAST, tags="ice_tea")#p6-t11
    line = canvas.create_line(600, 60, 600, 75, arrow=tk.LAST, tags="ice_tea")#p7-t12
    line = canvas.create_line(540, 140, 580, 140, arrow=tk.LAST, tags="ice_tea")#t11-p8
    line = canvas.create_line(620, 40, 660, 40, arrow=tk.LAST, tags="ice_tea")#p7-t13
    line = canvas.create_line(620, 140, 660, 140, arrow=tk.LAST, tags="ice_tea")#p8-t14
    line = canvas.create_line(700, 40, 965, 85, arrow=tk.LAST, tags="ice_tea")#t13-f
    line = canvas.create_line(600, 105, 600, 120, arrow=tk.LAST, tags="ice_tea")#t12-p8
    line = canvas.create_line(700, 140, 965, 95, arrow=tk.LAST, tags="ice_tea")#t14-f
    line = canvas.create_line(110, 70, 110, 15, 340, 15, arrow=tk.LAST, tags="ice_tea")#p2-t15
    line = canvas.create_line(380, 15, 520, 15, 580, 25, arrow=tk.LAST, tags="ice_tea")#t15-p7
    line = canvas.create_line(620, 35, 660, 15, arrow=tk.LAST, tags="ice_tea")#p7-t16
    line = canvas.create_line(700, 15, 980, 15, 980, 70, arrow=tk.LAST, tags="ice_tea")#t16-final