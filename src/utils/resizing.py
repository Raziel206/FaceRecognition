from src import cv

def resize(frame, window_name='frame'):
    h, w = frame.shape[:2]
    win_w, win_h = cv.getWindowImageRect(window_name)[2:]

    scale = min(win_w / w, win_h / h)
    new_w, new_h = int(w * scale), int(h * scale)
    resized = cv.resize(frame, (new_w, new_h))

    canvas = cv.copyMakeBorder(
        resized,
        top=(win_h - new_h)//2,
        bottom=(win_h - new_h + 1)//2,
        left=(win_w - new_w)//2,
        right=(win_w - new_w + 1)//2,
        borderType=cv.BORDER_CONSTANT,
        value=(0, 0, 0)
    )
    return canvas
