from controllers import chapter_controller

def get(event):
    return chapter_controller.get_chapters(event)
