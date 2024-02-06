from implementations.FileSystemImageLoader import FileSystemImageLoader
from implementations.PyGameImageDisplay import PyGameImageDisplay
from slideshow import SlideshowApp

loader = FileSystemImageLoader("./test")
display = PyGameImageDisplay()

app = SlideshowApp(loader, display)

app.start()
