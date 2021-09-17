from tkinter import *
from tkinter.ttk import *
import qrcode
from PIL import Image, ImageTk

root = Tk()
root.geometry("450x500")
root.title("QR Generator")

link_var = StringVar()
output_result = ""
link = ""


def submit():
    link = link_var.get()
    qr = qrcode.QRCode(version=3, error_correction=qrcode.
                       constants.ERROR_CORRECT_L, box_size=25, border=2,)
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    for c in ['\"', '/', ':', '.']:
        if c in link:
            link = link.replace(c, '')
    link = "qrcodes\\" + link + '.png'
    img.save(link)
    gen_result['text'] = "Files Saved as: " + link

    img_size = (275, 275)
    img_display = ImageTk.PhotoImage(Image.open(link).resize(img_size))
    img_label = Label(frame, image=img_display)
    img_label.image = img_display
    img_label.grid(row=10, column=0, columnspan=2)
    link_var.set("")

frame = Frame(root).grid()

entry_label = Label(frame, width=15, text="Enter Link:")
entry_label.grid(row=0, column=0, padx=10, pady=10)

link_entry = Entry(frame, width=50, textvariable=link_var)
link_entry.grid(row=0, column=1, padx=10, pady=10)

# btn = Button(frame, text="Get QR", command=submit)
# btn.grid(row=1, column=1, padx=10, pady=10, sticky=E)

gen_result = Label(frame, text=link, width=50)
gen_result.grid(row=1, column=0, padx=10, pady=10)

root.mainloop()
