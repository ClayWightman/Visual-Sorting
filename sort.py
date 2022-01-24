from PIL import Image, ImageDraw
import random


def makeInsertionSortGif(height, width, pixels):
    print("Starting Insertion Sort")
    images = [makeImage(height, width, pixels)]
    count = 0
    for i in range(1, len(pixels)):
        key = pixels[i][0]
        valueHolder = pixels[i]
        j = i-1
        while j >= 0 and key < pixels[j][0]:
            pixels[j+1] = pixels[j]
            j -= 1
        pixels[j+1] = valueHolder
        count += 1
        images.append(makeImage(height, width, pixels))
    images.append(makeImage(height,width,pixels))
    print("Insertion sort finished with " + str(len(images)) + " images")
    images[0].save('sort_images/insertion_sort.gif', save_all = True, append_images = images[1:], optimized = False, duration = 1, loop = 0)
    

def makeBubbleSortGif(height, width, pixels):
    print("Starting bubble sort")
    images = [makeImage(height, width, pixels)]
    count = 0
    for i in range(len(pixels)-1):
        for j in range(0, len(pixels) -i -1):
            if pixels[j][0] > pixels[j+1][0]:
                if count%10000 == 0:
                    images.append(makeImage(height, width, pixels))
                pixels[j], pixels[j+1] = pixels[j+1], pixels[j]
                count += 1
    print("Bubble sort finished with " + str(len(images)) + " images")
    images[0].save('sort_images/bubble_sort.gif', save_all = True, append_images = images[1:], optimized = False, duration = 100, loop = 0)
    

def makeSelectionSortGif(height, width, pixels):
    print("Starting selection sort")
    images = [makeImage(height, width, pixels)]
    count = 0
    for i in range(len(pixels)):
        min_idx = i
        for j in range(i+1, len(pixels)):
            if pixels[min_idx][0] > pixels[j][0]:
                min_idx = j
        pixels[i], pixels[min_idx] = pixels[min_idx], pixels[i]
        count += 1
        images.append(makeImage(height, width, pixels))
    images.append(makeImage(height, width, pixels))
    print("Selection sort finished with " + str(len(images)) + " images")
    images[0].save('sort_images/selection_sort.gif', save_all = True, append_images = images[1:], optimized = False, duration = 1, loop = 0)


def quickSortPartition(height, width, pixels, low, high, images, count):
    i = (low-1)
    pivot = pixels[high][0]
    for j in range(low, high):
        if pixels[j][0] <= pivot:
            i += 1
            pixels[i], pixels[j] = pixels[j], pixels[i]
            count += 1
            if count % 10 == 0:
                images.append(makeImage(height, width, pixels))
    pixels[i+1], pixels[high] = pixels[high], pixels[i+1]
    return (i+1)


def quickSort(height, width, pixels, low, high, images, count):
    if len(pixels) == 1:
        return pixels
    if low < high:
        pi = quickSortPartition(height, width, pixels, low, high, images, count)
        quickSort(height, width, pixels, low, pi-1, images, count)
        quickSort(height, width, pixels, pi+1, high, images, count)


def makeQuickSortGif(height, width, pixels, low, high):
    print("Starting quick sort")
    images = [makeImage(height, width, pixels)]
    quickSort(height, width, pixels, low, high, images, 0)
    print("Quick sort finished with " + str(len(images)) + " images")
    images[0].save('sort_images/quick_sort.gif', save_all = True, append_images = images[1:], optimized = False, duration = 1, loop = 0)


def heapify(height, width, pixels, n, i, images, count):
    largest = i
    l = 2* i + 1
    r = 2 * i + 2
    if l < n and pixels[i][0] < pixels[l][0]:
        largest = l
    if r < n and pixels[largest][0] < pixels[r][0]:
        largest = r
    if largest != i:
        pixels[i], pixels[largest] = pixels[largest],pixels[i]
        heapify(height, width, pixels, n, largest, images, count)


def heapSort(height, width, pixels, images, count):
    n = len(pixels)
    for i in range (n // 2 - 1, -1, -1):
        heapify(height, width, pixels, n, i, images, count)
    for i in range(n-1, 0, -1):
        pixels[i], pixels[0] = pixels[0], pixels[i]
        count += 1
        images.append(makeImage(height, width, pixels))
        heapify(height, width, pixels, i, 0, images, count)


def makeHeapSortGif(height, width, pixels):
    print("Starting heap sort")
    images = [makeImage(height, width, pixels)]
    heapSort(height, width, pixels, images, 0)
    print("Heap sort finished with " + str(len(images)) + " images")
    images[0].save('sort_images/heap_sort.gif', save_all = True, append_images = images[1:], optimized = False, duration = 1, loop = 0)


def makeShellSortGif(height, width, pixels):
    images = [makeImage(height, width, pixels)]
    print("Starting shell sort")
    count = 0
    n = len(pixels)
    interval = n//2
    while interval > 0:
        for i in range(interval, n):
            tempNumber = pixels[i][0]
            tempValue = pixels[i]
            j = i
            while j >= interval and pixels[j-interval][0] > tempNumber:
                pixels[j] = pixels[j-interval]
                count += 1
                if count % 10 == 0:
                    images.append(makeImage(height, width, pixels))
                j-= interval
            pixels[j] = tempValue
        interval //=2
    print("Shell sort finished with " + str(len(images)) + " images")
    images[0].save('sort_images/shell_sort.gif', save_all = True, append_images = images[1:], optimized = False, duration = 1, loop = 0)


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
    makeInsertionSortGif(height, width, pixels.copy())
    makeBubbleSortGif(height, width, pixels.copy())
    makeSelectionSortGif(height, width, pixels.copy())
    makeQuickSortGif(height, width, pixels.copy(), 0, len(pixels)-1)
    makeHeapSortGif(height, width, pixels.copy())
    makeShellSortGif(height, width, pixels.copy())


runscript("pikachu.jpg")
