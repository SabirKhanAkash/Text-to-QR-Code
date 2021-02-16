import qrcode
import PySimpleGUI as gui

gui.theme('DarkAmber')
layout = [
	[gui.Text('')],
	[gui.Text('                               WELCOME TO TEXT-TO-QR-CODE CONVERTER     ')],
	[gui.Text('')],
	[gui.Text('')],
	[gui.Text('')],
	[gui.Text('')],
	[gui.Text('')],
	[gui.Text('                                                   ENTER YOUR TEXT: ')],
	[gui.Text('                       '), gui.InputText()],
	[gui.Text('')],
	[gui.Text('                                                   '), gui.Button('Ok'), gui.Button('Cancel')],
	[gui.Text('')],
	[gui.Text(' Note: PNG version of the QR Code will be saved where the TextToQRCode.py file is located.')]
]
window = gui.Window('Text to QR-Code Converter',layout, finalize=True, use_ttk_buttons=True)

while True:
	event, values = window.read()
	if event in (None, 'Cancel'):
		break
	for i in range(25000):
		gui.PopupAnimated(gui.DEFAULT_BASE64_LOADING_GIF, background_color='#2c2825', time_between_frames=100)
	gui.PopupAnimated(None)

	qCode = qrcode.QRCode(
		version=1,
		box_size=15,
		border=10
	)

	data = values[0]

	qCode.add_data(data)
	qCode.make(fit=True)
	img = qCode.make_image(fill="black",back_color="white")
	img.save("My QR-Code.png")
	img.show()

window.close()
