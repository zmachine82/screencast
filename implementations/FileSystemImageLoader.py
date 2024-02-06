from ports.image_loader_port import ImageLoaderPort
import os
from PIL import Image


class FileSystemImageLoader(ImageLoaderPort):
    def __init__(self, image_folder):
        self.current_image = 0
        self.total_images = 0
        self.image_files = []
        self.image_folder = image_folder
        self.lookup_images()

    def load_image(self):
        if self.has_images():
            image_path = self.image_files[self.current_image]
            self.current_image += 1
            if self.current_image == self.total_images:
                self.lookup_images()
                print("resetting")
            return Image.open(image_path)

        print("resetting end")

    def has_images(self):
        return self.current_image < self.total_images

    def lookup_images(self):
        self.image_files = [os.path.join(self.image_folder, file) for file in os.listdir(self.image_folder) if
                            file.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]

        self.total_images = len(self.image_files)
        self.current_image = 0
