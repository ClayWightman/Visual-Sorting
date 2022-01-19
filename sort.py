from PIL import Image, ImageDraw
import random

def makeInsertionSortGif(height, width, pixels):
    print("Starting Insertion Sort")
    images = [makeImage(height, width, pixels)]
    for i in range(1, len(pixels)):
        key = pixels[i][0]
        valueHolder = pixels[i]
        j = i-1
        while j >= 0 and key < pixels[j][0]:
            pixels[j+1] = pixels[j]
            j -= 1
        pixels[j+1] = valueHolder
        images.append(makeImage(height, width, pixels))
    images.append(makeImage(height,width,pixels))
    print("Insertion sort finished with " + str(len(images)) + " images")
    images[0].save('sort_images/insertion_sort.gif', save_all = True, append_images = images[1:], optimized = False, duration = 1)
    


def makeBubbleSortGif(height, width, pixels):
    print("Starting bubble sort")
    images = [makeImage(height, width, pixels)]
    count = 0
    for i in range(len(pixels)-1):
        for j in range(0, len(pixels) -i -1):
            if pixels[j][0] > pixels[j+1][0]:
                if count%100 == 0:
                    images.append(makeImage(height, width, pixels))
                pixels[j], pixels[j+1] = pixels[j+1], pixels[j]
                count += 1
    print("Bubble sort finished with " + str(len(images)) + " images")
    images[0].save('sort_images/bubble_sort.gif', save_all = True, append_images = images[1:], optimized = False, duration = 100)
    


def makeSelectionSortGif(height, width, pixels):
    print("Starting selection sort")
    images = [makeImage(height, width, pixels)]
    for i in range(len(pixels)):
        min_idx = i
        for j in range(i+1, len(pixels)):
            if pixels[min_idx][0] > pixels[j][0]:
                min_idx = j
        pixels[i], pixels[min_idx] = pixels[min_idx], pixels[i]
        images.append(makeImage(height, width, pixels))
    print("Selection sort finished with " + str(len(images)) + " images")
    images[0].save('sort_images/selection_sort.gif', save_all = True, append_images = images[1:], optimized = False, duration = 1)



def quickSortPartition(height, width, pixels, low, high, images):
    i = (low-1)
    pivot = pixels[high][0]
    for j in range(low, high):
        if pixels[j][0] <= pivot:
            i += 1
            pixels[i], pixels[j] = pixels[j], pixels[i]
            images.append(makeImage(height, width, pixels))
    pixels[i+1], pixels[high] = pixels[high], pixels[i+1]
    return (i+1)


def quickSort(height, width, pixels, low, high, images):
    if len(pixels) == 1:
        return pixels
    if low < high:
        pi = quickSortPartition(height, width, pixels, low, high, images)
        quickSort(height, width, pixels, low, pi-1, images)
        quickSort(height, width, pixels, pi+1, high, images)


def makeQuickSortGif(height, width, pixels, low, high):
    print("Starting quick sort")
    images = []
    quickSort(height, width, pixels, low, high, images)
    print("Quick sort finished with " + str(len(images)) + " images")
    images[0].save('sort_images/quick_sort.gif', save_all = True, append_images = images[1:], optimized = False, duration = 1)

def makeCountingSortGif(height, width, pixels):
    print (int(max(pixels)))

def makeImage(height, width, pixels):
    image = Image.new(mode = "RGB", size = (height, width), color = (0, 0, 0))
    draw = ImageDraw.Draw(image)
    index = 0
    for heightPixel in range(0, height):
        for widthPixel in range(0, width):
            draw.point((heightPixel, widthPixel), pixels[index][1])
            index += 1
    return image


def runscript(imageName):
    initialImage = Image.open(imageName)
    height, width = initialImage.size[0], initialImage.size[1]
    pixels = []
    count = 0
    for heightPixel in range(0, height):
        for widthPixel in range(0, width):
            color = initialImage.getpixel((heightPixel, widthPixel))
            pixels.append((count, color))
            count+= 1
    random.shuffle(pixels)
    #makeInsertionSortGif(height, width, pixels.copy())
    #makeBubbleSortGif(height, width, pixels.copy())
    #makeSelectionSortGif(height, width, pixels.copy())
    #makeQuickSortGif(height, width, pixels.copy(), 0, len(pixels)-1)
    makeCountingSortGif(height, width, pixels.copy())

quickSortImages = []
runscript("pikachu.jpg")

'''
Counting Sort
Radix Sort
Bucket Sort
Shell Sort
Heap Sort
'''

#images[0].save('blah.gif', save_all = True, append_images = images[1:], optimized = False, duration = 1, loop = 0)
