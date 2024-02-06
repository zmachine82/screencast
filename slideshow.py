


class SlideshowApp:
    def __init__(self, image_loader, display):
        self.current_image_time = 0
        self.current_time = 1
        self.image_loader = image_loader
        self.display = display

    def start(self):
        # The main application loop goes here
        while self.image_loader.has_images():
            self.display.handle_events()
            if self.current_time > self.current_image_time:
                image = self.image_loader.load_image()
                self.current_image_time = self.display.display_image(image) + 5000
            self.current_time = self.display.get_time()

        pass


