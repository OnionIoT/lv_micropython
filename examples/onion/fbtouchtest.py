# A simple test for Linux Frame Buffer
# Imports fb (frame buffer) module and uses it as lvgl display driver
# then show a button on screen.

import lvgl as lv
lv.init()
import fb
fb.init()

disp_buf1 = lv.disp_buf_t()
buf1_1 = bytearray(320*10)
lv.disp_buf_init(disp_buf1, buf1_1, None, len(buf1_1)//4)

disp_drv = lv.disp_drv_t()
lv.disp_drv_init(disp_drv)
disp_drv.buffer = disp_buf1
disp_drv.flush_cb = fb.flush
#disp_drv.hor_res = fb.fill
#disp_drv.ver_res = fb.map
lv.disp_drv_register(disp_drv)


import xpt7603
touch = xpt7603.xpt7603()
touch.init()

indev_drv = lv.indev_drv_t()
lv.indev_drv_init(indev_drv) 
indev_drv.type = lv.INDEV_TYPE.POINTER;
indev_drv.read_cb = touch.read;
lv.indev_drv_register(indev_drv);

# Load the screen
scr = lv.obj()
lv.scr_load(scr)

# create objects
def on_button(obj, event):
	print('on_button event')
	if event == lv.EVENT.CLICKED:
		print('button clicked!')


btn = lv.btn(lv.scr_act())
#btn.align(lv.scr_act(), lv.ALIGN.CENTER, 0, 0)
btn.set_pos(50,50)
label = lv.label(btn)
label.set_text("Button")
btn.set_event_cb(on_button)

bar1 = lv.bar(lv.scr_act())
bar1.set_size(200, 30);
bar1.align(None, lv.ALIGN.CENTER, 0, 0);
bar1.set_anim_time(1000);
bar1.set_value(100, lv.ANIM.ON);




print('starting loop')
while True:
	# lv.task_handler()
    pass
    
