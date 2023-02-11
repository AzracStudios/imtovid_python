import cv2 

def resize_clip_and_overlay_on_blurred_image(path, file_name):
    print(f"Processing {path}...")
    img_overlay = cv2.imread(path)
    img_bg = cv2.imread(path)

    img_width = img_overlay.shape[1]
    img_height = img_overlay.shape[0]

    if img_width < 2000:
        width_factor = 2000 / img_width
        height_factor = 2000 / img_height

        width_factor = width_factor if width_factor < height_factor else height_factor

        img_bg = cv2.resize(src=img_bg, dsize=(2000, 2000))
        img_bg = cv2.blur(src=img_bg, ksize=(350, 350))

        img_overlay = cv2.resize(
            src=img_overlay,
            dsize=(int(img_width * width_factor),
                   int(img_height * width_factor)),
        )

    img_final = img_bg.copy()

    x_start = int((2000 - img_overlay.shape[0]) / 2)

    x_end = img_overlay.shape[0] + x_start

    y_start = int((2000 - img_overlay.shape[1]) / 2)
    y_end = img_overlay.shape[1] + y_start

    img_final[x_start:x_end, y_start:y_end] = img_overlay

    cv2.imwrite(f"./temp/image/{file_name}", img_final)

    print("Done!\n")
    return f"./temp/image/{file_name}"
