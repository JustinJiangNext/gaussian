import cv2
from multiprocessing import Process



def apply_gaussian_blur(input_image_path, output_image_path, kernel_size=(5, 5), sigma=0):
    # Load the image in color
    image = cv2.imread(input_image_path)
    
    # Check if the image was loaded properly
    if image is None:
        print(f"Error: Could not load image at {input_image_path}")
        return
    
    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(image, kernel_size, sigma)
    
    # Save the blurred image
    cv2.imwrite(output_image_path, blurred_image)
    print(f"Blurred image saved at {output_image_path}")


def convertFolder(inputPath, outputPath):
    os.mkdir(outputPath)
    for file in os.listdir(inputPath):
        apply_gaussian_blur(os.path.join(inputPath, file), os.path.join(outputPath, "blured_" +  file))

        print(file)
        
    print("""
    
    
    """ + inputPath + """
    
    
    
    """)


if __name__ == '__main__':
    print("Main start")
 
    converters = [
        Process(target=convertFolder, args=("loraDataSet1/SD21Airplane", "outputBlur")),
        Process(target=convertFolder, args=("loraDataSet1/SD21Automobile", "outputBlur")),
        Process(target=convertFolder, args=("loraDataSet1/SD21Bird", "outputBlur")),
    	Process(target=convertFolder, args=("loraDataSet1/SD21Cat", "outputBlur")),
    	Process(target=convertFolder, args=("loraDataSet1/SD21Deer", "outputBlur")),
    	Process(target=convertFolder, args=("loraDataSet1/SD21Dog", "outputBlur")),
    	Process(target=convertFolder, args=("loraDataSet1/SD21Frog", "outputBlur")),
    	Process(target=convertFolder, args=("loraDataSet1/SD21Horse", "outputBlur")),
    	Process(target=convertFolder, args=("loraDataSet1/SD21Ship", "outputBlur")),
    	Process(target=convertFolder, args=("loraDataSet1/SD21Truck", "outputBlur")),
    ]

    for worker in converters:
        worker.start()
    for worker in converters:
        worker.join()
    
