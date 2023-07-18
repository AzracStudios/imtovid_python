import cv2 

def resize_clip_and_overlay_on_blurred_image(path, file_name, width, height):
    print(f"Processing {path}...")
    img_overlay = cv2.imread(path)
    img_bg = cv2.imread(path)

    img_width = img_overlay.shape[1]
    img_height = img_overlay.shape[0]

    width_factor = width / img_width
    height_factor = height / img_height

    width_factor = min(width_factor, height_factor)
    
    img_bg = cv2.resize(src=img_bg, dsize=(width, height))
    img_bg = cv2.GaussianBlur(img_bg, (551, 551), 0)

    img_overlay = cv2.resize(
        src=img_overlay,
        dsize=(int(img_width * width_factor),
                int(img_height * width_factor)),
    )


    img_final = img_bg.copy()

    x_start = int((width - img_overlay.shape[1]) / 2)
    x_end = img_overlay.shape[1] + x_start

    y_start = int((height - img_overlay.shape[0]) / 2)
    y_end = img_overlay.shape[0] + y_start

    img_final[y_start:y_end,x_start:x_end] = img_overlay

    cv2.imwrite(f"./temp/image/{file_name}", img_final)

    print("Done!\n")
    return f"./temp/image/{file_name}"
