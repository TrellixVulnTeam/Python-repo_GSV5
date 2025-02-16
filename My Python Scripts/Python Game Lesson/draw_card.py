import simpleguitk as simplegui

card_back_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")
CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTRE = (CARD_BACK_SIZE[0] / 2, CARD_BACK_SIZE[1] / 2)

def draw(canvas):
	canvas.draw_image(card_back_image, CARD_BACK_CENTRE, CARD_BACK_SIZE, (50, 50), CARD_BACK_SIZE)

frame = simplegui.create_frame('testing', 820, 100)
frame.set_draw_handler(draw)
lable = frame.add_label("Turn = 0")

frame.start()

